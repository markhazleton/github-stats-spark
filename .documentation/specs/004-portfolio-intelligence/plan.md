# Implementation Plan: Portfolio Intelligence System

**Branch**: `004-portfolio-intelligence` | **Date**: 2026-04-24 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `.documentation/specs/004-portfolio-intelligence/spec.md`

## Summary

Reposition github-stats-spark as a Portfolio Intelligence System by introducing a deterministic classification engine that assigns each public, non-forked repository to a Core/Supporting/Archive tier using rule-based thresholds (commit activity + recency + quality indicators). The engine reads manual overrides from `config/portfolio.yml`, computes a 0–100 signal score with equal-weight inputs (recency 33%, 90-day commit volume 33%, tier score 34%), and enriches the JSON output with `classification`, `signal_score`, `relevance`, and `notes` fields. Two new SVG visualizations (Portfolio Breakdown, Signal Distribution) and a README refactor complete the repositioning.

## Technical Context

**Language/Version**: Python 3.11 (backend), React 19 / TypeScript (frontend)
**Primary Dependencies**: PyGithub, anthropic, PyYAML (already used for spark.yml), pytest
**Storage**: File-based cache (`.cache/`), JSON output (`data/repositories.json`), SVG output (`output/`)
**Testing**: pytest (backend), Vitest (frontend)
**Target Platform**: GitHub Actions + GitHub Pages (static site)
**Project Type**: CLI tool + static site generator
**Performance Goals**: Full classification of 100 repos within the existing ≤5-minute budget (SC-007)
**Constraints**: No new GitHub API calls for classification; classification uses only cached data already in `repo_dict`; new modules MUST be <500 LOC (Constitution I)
**Scale/Scope**: Up to 100 repos initial scope (SC-007), up to 500 per constitution boundary

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| # | Question | Answer | Action if No/Yes |
|---|----------|--------|------------------|
| 1 | **Privacy**: Does this feature touch private repository data? | No | Config enforces `exclude_private: true`; classifier only receives public repos |
| 2 | **Testability**: Can new logic be unit-tested without external services? | Yes | `classifier.py` operates on cached `repo_dict` data — no API calls |
| 3 | **Observability**: Do failure paths produce actionable error messages? | Yes | Missing/malformed `config/portfolio.yml` logs a warning with path; classification proceeds |
| 4 | **Efficiency**: Does this avoid unnecessary API calls? | Yes | Classification reads from already-cached commit histories and repo metadata |
| 5 | **Accessibility**: Does any visual output meet WCAG AA (4.5:1 contrast)? | Yes | New SVGs follow existing theme system; theme validation enforced at generation time |
| 6 | **Size** *(Principle I)*: Will any modified module exceed 800 LOC after this change? | Partial | `unified_data_generator.py` (805 LOC pre-existing, +~30 LOC). SIZE JUSTIFICATION comment must be updated. `models/repository.py` (486 LOC) will cross 500 → requires new SIZE JUSTIFICATION comment. Both remain under 800 LOC. |
| 7 | **Generated Output** *(Principle VI)*: Does this add a new generated output directory? | No | Classification data added to existing `data/repositories.json`; new SVGs go into existing `output/` tree |

## Project Structure

### Documentation (this feature)

```text
.documentation/specs/004-portfolio-intelligence/
├── plan.md              ← this file
├── research.md          ← Phase 0 output
├── data-model.md        ← Phase 1 output
├── contracts/
│   └── portfolio-json-schema.md
├── checklists/
│   └── requirements.md
└── tasks.md             ← created by /devspark.tasks
```

### Source Code (key paths)

```text
config/
├── spark.yml                       # EXTEND — update SIZE JUSTIFICATION; add portfolio section ref
└── portfolio.yml                   # NEW — classification overrides (FR-002)

src/spark/
├── classifier.py                   # NEW — RepositoryClassifier (FR-001, FR-004–FR-006)
├── config.py                       # EXTEND — add get_portfolio_config() method
├── models/
│   └── repository.py               # EXTEND — SIZE JUSTIFICATION update (will cross 500 LOC)
├── unified_data_generator.py       # EXTEND — call classifier in assembly phase
└── visualizer.py                   # EXTEND — portfolio_breakdown + signal_distribution SVGs

tests/
├── unit/
│   └── test_classifier.py          # NEW — classifier unit tests

frontend/src/
├── components/
│   ├── PortfolioBreakdown/         # NEW — tier distribution visualization
│   └── SignalDistribution/         # NEW — ranked signal weight chart
└── services/
    └── dataService.js              # EXTEND — surface new classification fields

README.md                           # REWRITE — per FR-014 section structure
```

## Implementation Phases

### Phase A — Configuration Layer (½ day)
1. Create `config/portfolio.yml` with documented defaults and annotated example overrides
2. Add `get_portfolio_config()` to `SparkConfig` — loads `config/portfolio.yml`, returns empty dict when file is absent (FR-012)
3. Gate: validate config values are one of `core|supporting|archive`; log warning and skip invalid entries

### Phase B — Classification Engine (1 day)
1. Create `src/spark/classifier.py` (`RepositoryClassifier` class, target <300 LOC)
2. Implement `classify(repo_dict, commit_history, overrides) -> ClassificationResult` using three-factor priority-ordered thresholds (FR-001)
3. Implement `compute_signal_score(repo_dict, commit_history, classification) -> int` using equal-weight formula (FR-004)
4. Implement `generate_notes(classification, commits_90d, override_notes) -> str` using tier-based phrase templates (FR-006)
5. Add unit tests in `tests/unit/test_classifier.py`: threshold boundaries, wildcard override, missing config fallback, signal score formula, notes generation

### Phase C — Data Model & Output Enrichment (½ day)
1. Add SIZE JUSTIFICATION comment to `models/repository.py`
2. Extend `unified_data_generator.py` assembly phase to call `RepositoryClassifier.classify_all()` and inject `classification`, `signal_score`, `relevance`, `notes` into each `repo_dict`
3. Update SIZE JUSTIFICATION comment in `unified_data_generator.py`
4. Verify AI `portfolio_role` and rule-based `classification` both appear in output JSON with distinct keys

### Phase D — Visualizations (1–1½ days)
1. Add `portfolio_breakdown_svg(repos)` to `visualizer.py`: bar chart of Core/Supporting/Archive counts with WCAG AA color mapping
2. Add `signal_distribution_svg(repos)` to `visualizer.py`: horizontal bar chart, repos ordered by signal score descending
3. Register `portfolio` as a valid stats category in `SparkConfig.VALID_STATS_CATEGORIES`
4. Wire both SVGs to generation pipeline in `cli_handlers.py` under the `portfolio` category
5. Verify LOC of `visualizer.py` before and after; add SIZE JUSTIFICATION if >500

### Phase E — Frontend Components (1 day)
1. Create `PortfolioBreakdown` component using Chart.js doughnut/bar chart; consume `classification` field from repo data
2. Create `SignalDistribution` component using Chart.js horizontal bar; consume `signal_score` field
3. Add narrative section to dashboard home explaining signal vs noise (FR-010)
4. Update `DashboardView` to render both components; verify visible without scrolling on 1280px viewport (SC-006)
5. Update `dataService.js` to surface `classification`, `signal_score`, `relevance`, `notes` fields

### Phase F — README Refactor (½ day)
1. Rewrite `README.md` with sections: What This Is, Why It Exists, Core Idea, How It Works, Output, Relationship to DevSpark Ecosystem (FR-014)

### Phase G — Scan Exclusions (15 min)
1. Verify no new output directories were created; if added, update `scan.exclude_paths` in `config/spark.yml`

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|--------------------------------------|
| `unified_data_generator.py` will reach ~835 LOC | Classification call must share the 4-phase pipeline's cache-read boundary (Constitution IV) | Splitting would require threading portfolio config across phase boundaries, violating the zero-API-call guarantee. Pre-existing CAP-2026-003 tracks planned split. |
| `models/repository.py` will cross 500 LOC (~510) | Classification output fields belong in the shared schema contract so backend + frontend JSON stay in sync | A separate schema file scatters the output contract and requires dual maintenance |
