# Tasks: Portfolio Intelligence System

**Input**: Design documents from `.documentation/specs/004-portfolio-intelligence/`
**Branch**: `004-portfolio-intelligence`
**Spec frontmatter**: `classification: full-spec` | `risk_level: medium` | `required_gates: checklist, analyze, critic`

**Gate check**: `checklists/requirements.md` — all items passed at spec time. Proceeding without blocking findings.

**Organization**: Tasks grouped by user story. Each phase is independently testable.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel with other [P] tasks in the same phase
- **[Story]**: User story this task belongs to (US1–US4)

---

## Phase 1: Setup (Configuration Layer)

**Purpose**: Create `config/portfolio.yml` and wire it into the config system. No other phase can use classification overrides until this is complete.

- [ ] T001 Create `config/portfolio.yml` with default wildcard (`"*": archive`) and four documented example overrides using the repos named in the spec: `devspark: core`, `TailwindSpark: core`, `PromptSpark.Chat: core`, `BootstrapSpark: supporting`
- [ ] T002 Add `get_portfolio_config()` method to `SparkConfig` in `src/spark/config.py` — returns override dict; logs warning and returns `{}` on missing/malformed file
- [ ] T003 Register `"portfolio"` as a valid stats category in `SparkConfig.VALID_STATS_CATEGORIES` in `src/spark/config.py`

---

## Phase 2: Foundational (Classification Engine)

**Purpose**: Implement `RepositoryClassifier` — the deterministic core. Every user story depends on this phase.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

> **FR-011 & FR-013 note**: Private repo exclusion (FR-011) and fork filtering (FR-013) are satisfied by pre-existing `exclude_private: true` / `exclude_forks: true` in `config/spark.yml`. No new tasks required for these requirements.

- [ ] T004 Create `src/spark/classifier.py` — define `ClassificationResult` dataclass (fields: classification, signal_score, relevance, notes) and `RepositoryClassifier` class shell with `__init__(self, overrides: dict)` signature
- [ ] T005 [P] Implement `RepositoryClassifier.classify(repo_dict, commits_90d, days_since_push, has_tests, has_ci_cd) -> ClassificationResult` using three-factor priority-ordered rules from spec FR-001 in `src/spark/classifier.py`
- [ ] T006 [P] Implement `RepositoryClassifier.compute_signal_score(days_since_push, commits_90d, classification) -> int` using equal-weight formula (recency 33%, volume 33%, tier 34%) from spec FR-004 in `src/spark/classifier.py`
- [ ] T007 [P] Implement `RepositoryClassifier.generate_notes(classification, commits_90d, override_notes) -> str` using tier-based phrase templates from data-model.md in `src/spark/classifier.py`
- [ ] T008 [P] Add SIZE JUSTIFICATION comment to `src/spark/models/repository.py` (will cross 500 LOC after Phase 3 additions — document this proactively)
- [ ] T009 Write unit tests in `tests/unit/test_classifier.py`: Core threshold boundary (pushed=89d, commits=5, has_ci_cd=True), Supporting boundary (pushed=364d, commits=0), Archive fallback, config override priority over rules, wildcard `"*"` default, signal score formula with known inputs, notes phrase for each tier

**Checkpoint**: `RepositoryClassifier` is fully tested and deterministic. Integration into the data pipeline can begin.

---

## Phase 3: User Story 1 – Signal Profile in Dashboard (Priority: P1) 🎯 MVP

**Goal**: Every non-forked public repo has `classification`, `signal_score`, `relevance`, `notes` in `data/repositories.json`; frontend groups repos by tier.

> **FR-008/FR-009 split**: T013/T014 here cover the **React frontend components** (dashboard). The **CLI SVG outputs** for the same requirements are covered by T019/T020 in Phase 5. Both are required — FR-008/FR-009 are not fully satisfied until Phase 5 is complete.

**Independent Test**: Load generated `data/repositories.json` — verify every non-forked public repo entry contains all four classification fields. Load dashboard — verify repos are grouped under Core, Supporting, Archive headers with visible signal scores.

- [ ] T010 [US1] Extend `unified_data_generator.py` assembly phase: instantiate `RepositoryClassifier` with `SparkConfig.get_portfolio_config()` overrides; call `classifier.classify()` for each repo in the assembly loop
- [ ] T011 [US1] Inject `classification`, `signal_score`, `relevance`, `notes` into each `repo_dict` in `unified_data_generator.py` (alongside existing `portfolio_role` AI fields); assert both `classification` (rule-based) and `portfolio_role` (AI, may be null) are present in a sample output entry to satisfy FR-001a
- [ ] T012 [US1] Update SIZE JUSTIFICATION comment in `unified_data_generator.py` to reflect the additional ~30 LOC from T010–T011
- [ ] T013 [P] [US1] Create `frontend/src/components/PortfolioBreakdown/` — Chart.js doughnut/bar showing Core/Supporting/Archive counts; compute counts client-side by grouping on the `classification` field per data-model.md `PortfolioBreakdown` shape (`{ core: { count, percentage }, supporting: { count, percentage }, archive: { count, percentage } }`)
- [ ] T014 [P] [US1] Create `frontend/src/components/SignalDistribution/` — Chart.js horizontal bar chart ordered by `signal_score` descending; consumes `signal_score` and `classification` fields
- [ ] T015 [US1] Add `PortfolioBreakdown` and `SignalDistribution` to `frontend/src/components/DashboardView/DashboardView.jsx`

**Checkpoint**: User Story 1 fully functional — every repo classified, dashboard shows tier groups and signal scores.

---

## Phase 4: User Story 2 – Manual Override Config (Priority: P2)

**Goal**: Engineer edits `config/portfolio.yml`, regenerates data, and sees overrides reflected in output. Missing/malformed file degrades gracefully with a logged warning.

**Independent Test**: Edit `config/portfolio.yml` to set one repo as `core`, one as `archive`. Regenerate data. Verify `classification` fields match config regardless of automated rule result.

- [ ] T016 [US2] Annotate `config/portfolio.yml` with inline YAML comments documenting all valid tier values (`core`, `supporting`, `archive`), wildcard `"*"` usage, and case-insensitivity note
- [ ] T017 [US2] Verify the malformed-config warning path in `src/spark/classifier.py` and `src/spark/config.py` emits a message including the file path `config/portfolio.yml` (grep for the warning log call; add path if missing)
- [ ] T018 [US2] Add acceptance scenario to `tests/unit/test_classifier.py`: given override `{"devspark": "core"}` + repo that would otherwise be Archive, assert `classification == "core"` and `relevance == "high"`

**Checkpoint**: User Story 2 complete — config overrides are respected and the graceful-degradation path is exercised.

---

## Phase 5: User Story 3 – Visitor-Facing Narrative & Visualizations (Priority: P3)

**Goal**: Portfolio breakdown chart visible without scrolling; signal vs noise narrative in first visible section.

**Independent Test**: Open generated dashboard without prior context — verify narrative section appears above the fold, PortfolioBreakdown chart is visible without scrolling, and a Core repo shows a notes field explaining its significance.

- [ ] T019 [US3] Add `portfolio_breakdown_svg(repos, theme)` method to `src/spark/visualizer.py` — bar/pie chart of Core/Supporting/Archive counts; use `theme["colors"]["accent"]` for Core, `theme["colors"]["secondary"]` for Supporting, `theme["colors"]["muted"]` for Archive (all from `config/themes.yml`; verify each passes WCAG AA 4.5:1 against the theme background)
- [ ] T020 [US3] Add `signal_distribution_svg(repos, theme, top_n=20)` method to `src/spark/visualizer.py` — horizontal bar chart of top repos sorted by `signal_score` descending; apply the same `theme["colors"]` tier mapping from T019 for bar colors
- [ ] T021 [US3] Check `visualizer.py` LOC after T019–T020 (depends on T019 and T020); if >500, add SIZE JUSTIFICATION comment explaining the single-class dispatch pattern
- [ ] T022 [US3] Wire both SVG methods to generation pipeline in `src/spark/cli_handlers.py` under the `portfolio` stats category (follow existing `overview`/`heatmap` dispatch pattern)
- [ ] T023 [US3] Add narrative section to dashboard frontend (hardcoded content per FR-010): "Most GitHub profiles accumulate over time…" positioning statement visible in first viewport section in `frontend/src/`

**Checkpoint**: User Story 3 complete — visitor can understand portfolio positioning at a glance without scrolling.

---

## Phase 6: User Story 4 – JSON Integration Contract (Priority: P4)

**Goal**: `data/repositories.json` exposes all four classification fields in a stable, documented schema for markhazleton.com consumption.

**Independent Test**: Read `data/repositories.json` directly — every repo entry has `classification` (string), `signal_score` (integer 0–100), `relevance` (string), `notes` (non-empty string). No transformation needed to render a classification summary.

- [ ] T024 [P] [US4] Update `frontend/src/services/dataService.js` to surface `classification`, `signal_score`, `relevance`, `notes` fields alongside existing repo data
- [ ] T025 [P] [US4] Add schema validation helper or assertion in the generation pipeline to verify 100% of non-forked public repos have all four classification fields (SC-003)
- [ ] T026 [US4] Update `contracts/portfolio-json-schema.md` with final observed field types and any deviation from draft schema

**Checkpoint**: User Story 4 complete — JSON output is consumable without transformation.

---

## Phase 7: Polish & Cross-Cutting Concerns

- [ ] T027 [P] Rewrite `README.md` per FR-014: sections = What This Is, Why It Exists, Core Idea, How It Works, Output, Relationship to DevSpark Ecosystem
- [ ] T028 Verify `config/spark.yml` `scan.exclude_paths` covers all new generated output paths; update if any new directories were introduced
- [ ] T029 [P] Run full generation pipeline end-to-end with `markhazleton` as test user; validate `data/repositories.json` contains classification fields for all repos; log and assert total elapsed time is under 5 minutes to satisfy SC-007

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 — BLOCKS all user story phases
- **Phase 3 (US1)**: Depends on Phase 2 — MVP delivery target
- **Phase 4 (US2)**: Depends on Phase 2 (classifier must exist before testing overrides)
- **Phase 5 (US3)**: Depends on Phase 3 (needs classification data in output JSON)
- **Phase 6 (US4)**: Depends on Phase 3 (needs enriched JSON output)
- **Phase 7 (Polish)**: Depends on all desired user stories being complete

### User Story Dependencies

- **US1 (P1)**: Depends on Foundational (Phase 2) only — no dependency on other stories
- **US2 (P2)**: Depends on Foundational (Phase 2) — override logic is in classifier; can develop in parallel with US1
- **US3 (P3)**: Depends on US1 (needs `classification` and `signal_score` in output) — not on US2
- **US4 (P4)**: Depends on US1 (needs enriched JSON) — not on US2 or US3

### Parallel Opportunities

- T005, T006, T007, T008 — all Phase 2, different methods/files
- T013, T014 — different frontend components
- T019, T020 — different SVG methods in the same file (coordinate to avoid conflicts)
- T024, T025 — different files
- T027, T028, T029 — all polish tasks, no dependencies on each other

---

## Parallel Example: Phase 2 (Foundational)

```
# These four tasks can start simultaneously after T004:
Task T005: implement classify() method
Task T006: implement compute_signal_score() method
Task T007: implement generate_notes() method
Task T008: add SIZE JUSTIFICATION to models/repository.py
```

---

## Implementation Strategy

### MVP (User Stories 1 only)

1. Complete Phase 1: Setup (T001–T003)
2. Complete Phase 2: Foundational (T004–T009)
3. Complete Phase 3: US1 (T010–T015)
4. **STOP and VALIDATE**: Every repo classified, dashboard shows tiers
5. All 14 functional requirements gated by US1 are satisfied at this point

### Full Delivery

Phase 4 → Phase 5 → Phase 6 → Phase 7, each validated independently

### Total Tasks: 29

| Phase | Tasks | Story |
|-------|-------|-------|
| 1 Setup | T001–T003 | — |
| 2 Foundational | T004–T009 | — |
| 3 US1 MVP | T010–T015 | P1 |
| 4 US2 | T016–T018 | P2 |
| 5 US3 | T019–T023 | P3 |
| 6 US4 | T024–T026 | P4 |
| 7 Polish | T027–T029 | — |
