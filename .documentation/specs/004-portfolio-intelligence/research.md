# Research: Portfolio Intelligence System

**Feature**: `004-portfolio-intelligence` | **Date**: 2026-04-24

## Decision Log

### 1. Classification Engine Location

**Decision**: New standalone module `src/spark/classifier.py`

**Rationale**: `ranker.py` (315 LOC) already handles composite scoring for display ranking — a separate module avoids coupling ranking concerns with portfolio classification. The classifier is independently testable and does not depend on `RepositoryRanker`. Constitution I LOC target (<500) is achievable in a new file.

**Alternatives considered**:
- Extend `ranker.py` → rejected: conflates display ranking with portfolio positioning; also risks pushing `ranker.py` past 500 LOC
- Extend `calculator.py` → rejected: already at 938 LOC with SIZE JUSTIFICATION; adding more defers the planned split further

---

### 2. Config File Loading Strategy

**Decision**: Extend `SparkConfig` with `get_portfolio_config()` — loads `config/portfolio.yml` using existing `yaml.safe_load` pattern

**Rationale**: `SparkConfig` already handles all YAML loading in the project; adding one method keeps all config I/O in one place. The new method returns an empty dict (not an error) when `config/portfolio.yml` is missing — satisfying FR-012.

**Alternatives considered**:
- Classifier loads config directly → rejected: scatters config I/O; harder to mock in tests
- Add `portfolio:` section to `spark.yml` → rejected: pollutes the main config file; makes it harder to open-source the classification config separately

---

### 3. Signal Score Normalization

**Decision**: Three sub-scores each normalized to 0–100, then averaged with equal weight (33/33/34)

Sub-score formulas:
- **Recency score**: `max(0, 100 - (days_since_push / 365 * 100))` → 0 at ≥365 days, 100 at day 0
- **Volume score**: `min(100, commits_90d / 30 * 100)` → 100 at ≥30 commits in 90 days (aligns with "active" threshold)
- **Tier score**: Core=100, Supporting=60, Archive=20 (fixed values from spec)

Final: `signal_score = round((recency + volume + tier) / 3)`

**Rationale**: Anchoring volume to 30 commits/90d as the "full score" ceiling matches the existing ranking system's RECENCY_FAIR=90 day threshold and is consistent with what "actively maintained" means in this codebase.

**Alternatives considered**:
- Cap volume at 5 commits → too easy to reach 100; doesn't differentiate active vs very-active repos
- Cap volume at 100 commits → too hard to reach 100 for legitimate Core repos with small commit cadence

---

### 4. Auto-Generated Notes Phrases

**Decision**: Tier-based phrase templates with activity context injected

| Classification | Commits 90d | Generated Note |
|----------------|-------------|----------------|
| Core | ≥10 | "Actively maintained core system with {n} commits in the last 90 days" |
| Core | <10 | "Core system in the portfolio; maintained with focused recent activity" |
| Supporting | ≥1 | "Supporting project with recent updates" |
| Supporting | 0 | "Supporting project; periodically maintained" |
| Archive | any | "Historical project; no longer actively maintained" |

**Rationale**: Satisfies User Story 3 acceptance scenario 3 (Core repos must have notes that "briefly explain why significant") even without manual overrides. Phrases use only data already available in the repo_dict.

**Alternatives considered**:
- Use GitHub description field → rejected (clarification Q2 answer B): descriptions are often absent, generic, or developer-focused rather than portfolio-focused
- Always empty unless overridden → rejected (clarification Q2 answer C): breaks acceptance scenario 3

---

### 5. Visualization Pipeline Integration

**Decision**: Add new SVG generators directly to `visualizer.py`; wire via a new `portfolio` stats category

**Rationale**: `visualizer.py` already contains all SVG generation logic and is wired to `cli_handlers.py` via category dispatch. Adding a new category follows the exact same pattern as `overview`, `heatmap`, etc. — minimal coupling change.

**Alternatives considered**:
- New `portfolio_visualizer.py` file → rejected: the existing `visualizer.py` pattern uses a single class with category methods; splitting would require significant refactoring of the dispatch logic. The planned CAP-2026-003 split is the right time to do that.

Current `visualizer.py` LOC: check required during Phase D before adding to ensure size gate is not violated.

---

### 6. Frontend Component Strategy

**Decision**: Two new standalone React components (`PortfolioBreakdown`, `SignalDistribution`) added to `DashboardView`

**Rationale**: Follows existing component isolation pattern (each visualization is a separate directory under `frontend/src/components/`). Uses existing Chart.js 4 + react-chartjs-2 already in the dependency tree — no new frontend dependencies required.

**Alternatives considered**:
- Embed charts inline in DashboardView → rejected: violates Single Responsibility; DashboardView already manages enough complexity
- Use a new charting library → rejected: unnecessary dependency for chart types already supported by Chart.js 4

---

### 7. Backward Compatibility

**Decision**: All new `repo_dict` fields are additive; existing consumers (frontend, report generators) continue working unchanged

**Rationale**: `classification`, `signal_score`, `relevance`, `notes` are new top-level keys. Nothing removes or renames existing keys. The `portfolio_role` (AI) and `classification` (rule-based) coexist in the output with clearly different names.

**Risk**: Consumers that iterate all keys may surface the new fields unexpectedly. Mitigation: frontend `dataService.js` already destructures specific fields, so it is unaffected until explicitly updated in Phase E.
