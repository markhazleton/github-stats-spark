---
gate: analyze
status: pass
blocking: false
severity: info
summary: "10 findings identified and remediated (0 critical, 1 high, 4 medium, 5 low). All resolved. No constitution violations. Ready for /devspark.implement."
generated: 2026-04-24
remediated: 2026-04-24
feature: 004-portfolio-intelligence
---

# Specification Analysis Report: Portfolio Intelligence System

**Artifacts analyzed**: spec.md, plan.md, tasks.md, research.md, data-model.md, contracts/portfolio-json-schema.md, constitution.md

---

## Findings

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| C1 | Inconsistency | HIGH | spec.md US4 acceptance scenario line 73, data-model.md, tasks.md | `signalScore` (camelCase) in spec User Story 4 acceptance criteria conflicts with `signal_score` (snake_case) used in data-model.md, contracts/, and all tasks. Breaks acceptance test design. | Normalize to `signal_score` (snake_case) in spec.md US4 acceptance criteria to match data-model.md and contracts. |
| C2 | Coverage Gap | MEDIUM | spec.md FR-001a; tasks.md | FR-001a (store AI `portfolio_role` alongside rule-based `classification`) has no task. The summarizer changes from the current session partially implement this, but no task verifies the coexistence of both fields in `data/repositories.json`. | Add a verification sub-task to T011 or T026: "Verify `portfolio_role` (AI) and `classification` (rule-based) both present in `data/repositories.json`." |
| C3 | Coverage Gap | MEDIUM | spec.md SC-007; tasks.md | SC-007 (≤5 minutes for 100 repos) has no corresponding task. Classification is expected to be fast (pure computation on cached data), but there is no validation task. | Add a timing assertion to T029 (end-to-end pipeline run): log elapsed time and assert <5 minutes for the test run. |
| C4 | Inconsistency | MEDIUM | tasks.md Phase 3 (T013/T014) vs spec.md FR-008/FR-009 | FR-008 (portfolio breakdown visualization) and FR-009 (signal distribution) are split across two phases: React frontend components (T013/T014, Phase 3/US1) and SVG generators (T019/T020, Phase 5/US3). Tasks.md does not document this distinction, which could cause an implementer to think the requirements are already satisfied by T013/T014 and skip T019/T020. | Add a comment in tasks.md Phase 3 clarifying "T013/T014 = frontend React components; T019/T020 = CLI SVG output — both required for FR-008/FR-009." |
| C5 | Underspecification | MEDIUM | tasks.md T013, data-model.md PortfolioBreakdown | `PortfolioBreakdown` is a spec-defined entity with aggregated counts/percentages. T013 (frontend component) consumes `classification` field per repo but no task explicitly covers how the aggregate (count, percentage) is produced. Client-side aggregation from repo list is valid per data-model.md, but this should be stated in the task. | Update T013 description to include: "compute Core/Supporting/Archive counts client-side from repo list `classification` field per data-model.md." |
| D1 | Duplication | LOW | spec.md FR-011, FR-013; tasks.md | FR-011 (no private repos) and FR-013 (filter forks) have no tasks because they're handled by pre-existing `exclude_private: true` / `exclude_forks: true` in config. This is correct behavior, but the gap looks like missing coverage without an explanation. | Add a note in tasks.md Phase 2 Foundational section: "FR-011 and FR-013 are satisfied by pre-existing `config/spark.yml` filters; no new tasks required." |
| A1 | Ambiguity | LOW | research.md signal score section | Volume score ceiling (30 commits = 100) is documented only in research.md, not in spec.md FR-004 or data-model.md. An implementer reading only spec.md would not know the ceiling value. | Mirror the volume ceiling (`min(100, commits_90d / 30 * 100)`) into data-model.md Signal Score Formula section (already present) and confirm it matches research.md. |
| A2 | Ambiguity | LOW | tasks.md T001 | "four documented example overrides" in T001 is vague — no specific repos named. The spec's classification config example (devspark, TailwindSpark, PromptSpark.Chat, DocSpecSpark) can be used directly. | Update T001 to reference the example repos from spec.md Classification Engine config section. |
| A3 | Ambiguity | LOW | tasks.md T019/T020 | Color mapping for SVG visualizations is described only as "WCAG AA compliant" without specific colors defined. An implementer will have to choose colors without guidance. | Specify colors in T019/T020 referencing the existing theme system (e.g., "use `theme.accent` for Core, `theme.secondary` for Supporting, `theme.muted` for Archive per `config/themes.yml`"). |
| A4 | Underspecification | LOW | tasks.md T021 | T021 checks `visualizer.py` LOC *after* T019 and T020. This is listed as a separate sequential task, but T019 and T020 are not marked [P] — meaning they must run sequentially. The ordering is correct but the inter-task dependency is not stated. | Add "(depends on T019 and T020)" to T021 description. |

---

## Coverage Summary

| Requirement | Has Task? | Task IDs | Notes |
|-------------|-----------|----------|-------|
| FR-001 (classify repos) | ✓ | T005, T010, T011 | Full coverage |
| FR-001a (store AI role alongside) | Partial | — | Pre-implemented in summarizer; needs verification task (see C2) |
| FR-002 (read config/portfolio.yml) | ✓ | T001, T002, T005 | |
| FR-003 (wildcard support) | ✓ | T009, T018 | |
| FR-004 (signal score formula) | ✓ | T006, T009 | |
| FR-005 (relevance derived from tier) | ✓ | T005, T011 | |
| FR-006 (notes field) | ✓ | T007, T011 | |
| FR-007 (enriched JSON export) | ✓ | T011, T025 | |
| FR-008 (portfolio breakdown viz) | ✓ | T013, T019, T022 | Frontend + SVG both covered |
| FR-009 (signal distribution viz) | ✓ | T014, T020, T022 | Frontend + SVG both covered |
| FR-010 (narrative section) | ✓ | T023 | |
| FR-011 (no private repos) | Pre-existing | — | config/spark.yml `exclude_private: true` (see D1) |
| FR-012 (warn on missing config) | ✓ | T002, T017 | |
| FR-013 (filter forks) | Pre-existing | — | config/spark.yml `exclude_forks: true` (see D1) |
| FR-014 (README update) | ✓ | T027 | |
| SC-001 (visitor understands at glance) | Partial | T013, T015, T023 | No explicit validation task |
| SC-002 (30-second description) | Partial | T023 | Qualitative — validated by manual review |
| SC-003 (100% repos classified) | ✓ | T025 | |
| SC-004 (JSON consumable without transform) | ✓ | T024, T026 | |
| SC-005 (overrides in one run) | ✓ | T018 | |
| SC-006 (breakdown visible without scroll) | ✓ | T023 | Viewport check included in task |
| SC-007 (≤5 min for 100 repos) | ✗ | — | No task (see C3) |

---

## Constitution Alignment

No constitution violations detected.

| Principle | Check | Status |
|-----------|-------|--------|
| I — Single Responsibility (<500 LOC) | `classifier.py` (new, <300 LOC target). `models/repository.py` crosses 500 → SIZE JUSTIFICATION planned in T008. `unified_data_generator.py` reaches ~835 → pre-existing justification updated in T012. | Pass (with planned mitigations) |
| II — Data Privacy | Classification only on public, non-forked repos. No private data path introduced. | Pass |
| III — Fail Fast | Missing/malformed config logs warning + proceeds. Error paths in classifier produce actionable messages. | Pass |
| IV — Change-Driven Caching | Classification runs on cached data; no new API calls. Cache invalidation unchanged. | Pass |
| V — Accessibility | SVG generators use theme system with WCAG AA enforcement. | Pass (T019/T020 must reference theme) |
| VI — Generated Artifact Boundary | No new output directories. `data/repositories.json` is existing. T028 verifies `scan.exclude_paths`. | Pass |

---

## Unmapped Tasks

All 29 tasks map to at least one requirement or story. No orphaned tasks detected.

---

## Metrics

| Metric | Value |
|--------|-------|
| Total Functional Requirements | 14 (FR-001 through FR-014) |
| Total Success Criteria | 7 (SC-001 through SC-007) |
| Total Tasks | 29 |
| Requirements Coverage (≥1 task) | 17/21 = **81%** (4 pre-existing or partial) |
| Effective Coverage (excl. pre-existing) | 19/21 = **90%** |
| Critical Issues | 0 |
| High Issues | 1 |
| Medium Issues | 4 |
| Low Issues | 5 |
| Constitution Violations | 0 |

---

## Next Actions

**No blocking issues.** The artifact set is coherent and constitution-clean. Recommended fixes before `/devspark.implement`:

1. **Fix C1 (HIGH)** — Edit spec.md US4 acceptance scenario: change `signalScore` → `signal_score` (one-line fix)
2. **Fix C2 (MEDIUM)** — Add verification note to T011 or T026 for FR-001a AI field coexistence
3. **Fix C3 (MEDIUM)** — Add timing assertion to T029
4. **Fix C4 (MEDIUM)** — Add clarifying comment to tasks.md Phase 3 about FR-008/FR-009 split
5. **Fix C5 (MEDIUM)** — Expand T013 description to specify client-side aggregation

Low-severity items (D1, A1-A4) are advisory — can be addressed during implementation without replanning.

**Suggested next command**: `/devspark.implement` (after applying fixes C1–C5)

---

## Resolution Contract

```yaml
findings:
  - finding_id: analyze-C1
    severity: high
    description: "`signalScore` (camelCase) in spec.md US4 acceptance criteria conflicts with `signal_score` (snake_case) used in data-model.md, contracts/, and all task descriptions. Creates ambiguity in acceptance test design."
    recommended_action: "Edit spec.md US4 acceptance scenario to replace `signalScore` with `signal_score`"
    execution_mode: auto
    status: resolved
    outcome: "applied"
  - finding_id: analyze-C2
    severity: medium
    description: "FR-001a has no verification task. The AI `portfolio_role` field was pre-implemented but no task confirms coexistence with `classification` in output JSON."
    recommended_action: "Add verification step to T011 or T026: confirm both fields present in repositories.json"
    execution_mode: selective
    status: resolved
    outcome: "applied"
  - finding_id: analyze-C3
    severity: medium
    description: "SC-007 (≤5 minutes for 100 repos) has no corresponding validation task."
    recommended_action: "Add timing assertion to T029 end-to-end pipeline run"
    execution_mode: selective
    status: resolved
    outcome: "applied"
  - finding_id: analyze-C4
    severity: medium
    description: "FR-008/FR-009 are split across two phases (React frontend in Phase 3, SVG CLI in Phase 5) without documentation. An implementer reading tasks.md may assume FR-008/FR-009 are satisfied by T013/T014 alone."
    recommended_action: "Add cross-reference comment in tasks.md Phase 3 header"
    execution_mode: auto
    status: resolved
    outcome: "applied"
  - finding_id: analyze-C5
    severity: medium
    description: "`PortfolioBreakdown` is a spec entity requiring aggregated count/percentage data. T013 does not specify how the aggregate is produced (client-side vs. pre-computed)."
    recommended_action: "Update T013 description to state 'compute Core/Supporting/Archive counts client-side from classification field per data-model.md'"
    execution_mode: auto
    status: resolved
    outcome: "applied"
  - finding_id: analyze-D1
    severity: low
    description: "FR-011 and FR-013 have zero tasks due to pre-existing filters. Without a note, this looks like missing coverage."
    recommended_action: "Add explanatory comment in tasks.md Foundational phase"
    execution_mode: auto
    status: resolved
    outcome: "applied"
  - finding_id: analyze-A1
    severity: low
    description: "Volume score ceiling (30 commits = 100) is in research.md but not in spec.md FR-004. Spec FR-004 only states 'equal-weight contributions' without the normalization details."
    recommended_action: "Confirm data-model.md Signal Score formula is complete (it is); no spec change needed"
    execution_mode: manual
    status: resolved
    outcome: "no-change-needed: data-model.md already contains the complete formula including volume ceiling"
  - finding_id: analyze-A2
    severity: low
    description: "T001 says 'four documented example overrides' without naming them. The spec's config example names specific repos."
    recommended_action: "Update T001 to reference spec.md classification config example repos"
    execution_mode: auto
    status: resolved
    outcome: "applied"
  - finding_id: analyze-A3
    severity: low
    description: "SVG color mapping in T019/T020 is described as 'WCAG AA compliant' without specific theme variable references."
    recommended_action: "Update T019/T020 to reference theme variables (theme.accent/secondary/muted) from config/themes.yml"
    execution_mode: auto
    status: resolved
    outcome: "applied"
  - finding_id: analyze-A4
    severity: low
    description: "T021 dependency on T019 and T020 is not stated in the task description."
    recommended_action: "Append '(depends on T019 and T020)' to T021 description"
    execution_mode: auto
    status: resolved
    outcome: "applied"
```
