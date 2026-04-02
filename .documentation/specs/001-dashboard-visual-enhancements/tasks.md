# Tasks: Dashboard Visual Enhancements

**Input**: Design documents from `/.documentation/specs/001-dashboard-visual-enhancements/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Constitution requires >80% coverage for core modules. T034 adds unit tests for the new `calculate_bus_factor()` method in `calculator.py`. Additional test tasks for frontend components should be added during implementation as needed.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup

**Purpose**: No new project scaffolding needed — this feature extends existing backend and frontend. Only schema version bump required.

- [ ] T001 Bump schema version from `"2.2.0"` to `"2.3.0"` and add new feature flags in `src/spark/unified_data_generator.py`

---

## Phase 2: Foundational (Backend Data Pipeline)

**Purpose**: Persist `commits_by_day` (already computed) and add new GitHub API calls for contributor stats and code frequency. These data changes MUST be complete before any frontend user story can consume the new fields.

**CRITICAL**: No frontend user story work should begin until Phase 2 is complete and `data/repositories.json` contains the new fields.

- [ ] T002 Persist `activity_calendar` (the existing `commits_by_day` dict) into profile-level output in `src/spark/unified_data_generator.py`
- [ ] T003 Derive `weekly_activity` array from `activity_calendar` data and persist in profile-level output in `src/spark/unified_data_generator.py`
- [ ] T004 [P] Add `fetch_contributor_stats()` method to `src/spark/fetcher.py` — calls `repo.get_stats_contributors()`, handles 202/retry and `RateLimitExceededException` with graceful `None` fallback, returns list of contributor dicts with login/commits/additions/deletions
- [ ] T005 [P] Add `fetch_code_frequency()` method to `src/spark/fetcher.py` — calls `repo.get_stats_code_frequency()`, handles 202/retry and `RateLimitExceededException` with graceful `None` fallback, returns total additions and total deletions
- [ ] T006 Add `calculate_bus_factor()` static method to `src/spark/calculator.py` — takes contributor commit counts, returns minimum contributors for 50% of total commits plus health classification
- [ ] T007 Integrate new fetcher methods into cache refresh pipeline in `src/spark/unified_data_generator.py` — cache contributor stats and code frequency per-repo using existing pushed_at invalidation
- [ ] T008 Add per-repository `total_additions`, `total_deletions`, `code_churn`, `bus_factor`, `bus_factor_health`, and `contributor_stats` fields to the repo_dict assembly in `src/spark/unified_data_generator.py`
- [ ] T009 Run `spark unified --user markhazleton --verbose` and verify new fields appear in `data/repositories.json` with correct values

**Checkpoint**: `data/repositories.json` now has schema v2.3.0 with `activity_calendar`, `weekly_activity`, and per-repo commit volume + bus factor fields.

---

## Phase 3: User Story 1 — Interactive Contribution Heatmap Calendar (Priority: P1) MVP

**Goal**: Display a GitHub-style 52-week calendar heatmap of daily commit counts in the dashboard profile section.

**Independent Test**: Load dashboard with generated `repositories.json` containing `activity_calendar`. Verify heatmap renders with colored cells, tooltips on hover, and empty-day handling.

- [ ] T010 [P] [US1] Add `computeHeatmapData()` function to `frontend/src/services/metricsCalculator.js` — converts `activity_calendar` dict to array of `{date, count, intensity}` objects for trailing 365 days, calculating intensity levels 0-4 by quartile distribution
- [ ] T011 [US1] Create `ContributionHeatmap.jsx` component in `frontend/src/components/Visualizations/ContributionHeatmap.jsx` — renders 7-row × 53-column CSS Grid of colored cells, uses existing `Tooltip` component for hover, handles empty/missing `activity_calendar` with empty state message
- [ ] T012 [P] [US1] Create `ContributionHeatmap.module.css` in `frontend/src/components/Visualizations/ContributionHeatmap.module.css` — grid layout, 5 intensity levels using CSS custom properties (theme-aware), day/month labels, responsive scaling
- [ ] T013 [US1] Integrate `ContributionHeatmap` into the dashboard profile section in `frontend/src/App.jsx` — pass `activity_calendar` data from loaded JSON, position above or below existing profile stats

**Checkpoint**: Heatmap is visible and interactive with real data. US1 is independently testable.

---

## Phase 4: User Story 2 — Multi-Series Activity Timeline (Priority: P1)

**Goal**: Display an interactive line chart showing weekly commits and active repositories over 52 weeks, with toggleable series.

**Independent Test**: Load dashboard with `weekly_activity` data. Verify two series render, legend toggles work, and tooltips show correct per-week values.

- [ ] T014 [P] [US2] Add `computeTimelineData()` function to `frontend/src/services/metricsCalculator.js` — converts `weekly_activity` array to Chart.js-compatible dataset with labels and two series (commits, activeRepos)
- [ ] T015 [US2] Create `ActivityTimeline.jsx` component in `frontend/src/components/Visualizations/ActivityTimeline.jsx` — uses `react-chartjs-2` `Line` chart with two datasets, interactive legend toggle, tooltips, responsive container
- [ ] T016 [P] [US2] Create `ActivityTimeline.module.css` in `frontend/src/components/Visualizations/ActivityTimeline.module.css` — container sizing, responsive width, theme-aware colors via CSS custom properties
- [ ] T017 [US2] Integrate `ActivityTimeline` into the visualizations section in `frontend/src/App.jsx` — pass `weekly_activity` data, position within existing chart area, handle missing data gracefully

**Checkpoint**: Timeline chart renders with two toggleable series. US2 is independently testable.

---

## Phase 5: User Story 3 — Dark Mode Toggle (Priority: P2)

**Goal**: Add a manual light/dark/system theme toggle that persists via localStorage and integrates with existing OS-preference dark mode CSS.

**Independent Test**: Click toggle to cycle through light → dark → system. Verify all dashboard elements change theme, preference persists across reload, and system mode follows OS preference.

- [ ] T018 [US3] Create `ThemeContext.jsx` in `frontend/src/contexts/ThemeContext.jsx` — React context providing `theme` (light/dark/system), `resolvedTheme` (light/dark), and `toggleTheme()`. Reads localStorage on mount, falls back to OS `prefers-color-scheme`. Sets `data-theme` attribute on `<html>`.
- [ ] T019 [US3] Refactor `@media (prefers-color-scheme: dark)` blocks to `[data-theme="dark"]` selectors in `frontend/src/styles/global.css` — preserve all existing color values, just change the trigger mechanism
- [ ] T020 [P] [US3] Refactor `@media (prefers-color-scheme: dark)` blocks to `[data-theme="dark"]` selectors in component CSS files: `frontend/src/components/ErrorBoundary/ErrorBoundary.css`, `frontend/src/components/Mobile/*.css`, `frontend/src/components/RepositoryTable/FilterSheet.css`, `frontend/src/components/RepositoryTable/SortSheet.css`, and any other component CSS with dark mode media queries
- [ ] T021 [P] [US3] Create `ThemeToggle.jsx` component in `frontend/src/components/Common/ThemeToggle.jsx` — renders sun/moon/system icon button, consumes ThemeContext, accessible label and keyboard support
- [ ] T022 [P] [US3] Create `ThemeToggle.module.css` in `frontend/src/components/Common/ThemeToggle.module.css` — button styling, icon transitions, WCAG AA contrast in both themes
- [ ] T023 [US3] Wrap `App.jsx` with `ThemeProvider` and add `ThemeToggle` to the header/nav area in `frontend/src/App.jsx`
- [ ] T024 [US3] Verify WCAG AA contrast (4.5:1) for all text elements in both themes — spot-check key components (heatmap labels, timeline legend, table headers, stat cards)

**Checkpoint**: Theme toggle works across all components. Dark mode is persistent and accessible. US3 is independently testable.

---

## Phase 6: User Story 4 — Export Enhancement (Priority: P2)

**Goal**: Update the existing ExportButton to include new fields (commit volume, bus factor) in CSV/JSON exports.

**Independent Test**: Export CSV and JSON; verify new columns (total_additions, total_deletions, code_churn, bus_factor) appear and contain correct values.

- [ ] T025 [US4] Add new export column definitions for `total_additions`, `total_deletions`, `code_churn`, `bus_factor`, and `bus_factor_health` to `frontend/src/components/Common/ExportButton.jsx` — place new columns logically alongside existing commit metrics in the column order

**Checkpoint**: Export includes new fields. US4 is independently testable. (Note: Core export functionality already exists — this is enhancement only.)

---

## Phase 7: User Story 5 — Commit Size & Volume Metrics Display (Priority: P3)

**Goal**: Display per-repository and aggregate commit volume metrics (lines added/deleted/churn) in the dashboard.

**Independent Test**: View a repository detail panel; verify additions, deletions, and churn display. View profile overview; verify aggregate churn is shown. Verify "Stats not available" for repos without data.

- [ ] T026 [US5] Add commit volume display (total_additions, total_deletions, code_churn) to the profile summary stats section in `frontend/src/components/Visualizations/StatCards.jsx` or equivalent aggregate stats area
- [ ] T027 [US5] Add commit volume display to per-repository detail view in `frontend/src/components/DrillDown/RepositoryDetail.jsx` — show lines added, lines deleted, net change with appropriate formatting (e.g., "+15.4K / -8.2K"). Handle null values with "Stats not available" message.

**Checkpoint**: Commit volume metrics visible in both aggregate and detail views. US5 is independently testable.

---

## Phase 8: User Story 6 — Bus Factor Indicator (Priority: P3)

**Goal**: Display bus factor metric with color-coded health badge per repository.

**Independent Test**: View repository detail for a single-contributor repo; verify bus factor shows "1" with critical/red badge. View a multi-contributor repo; verify appropriate health color.

- [ ] T028 [US6] Add bus factor display to per-repository detail view in `frontend/src/components/DrillDown/RepositoryDetail.jsx` — show integer value with color-coded badge (red for critical/1, orange for warning/2, green for healthy/3+). Handle null with "N/A".
- [ ] T029 [P] [US6] Add bus factor column to the repository table in `frontend/src/components/RepositoryTable/RepositoryTable.jsx` — sortable column showing bus factor value with inline color indicator

**Checkpoint**: Bus factor visible in detail view and table. US6 is independently testable.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final integration, backward compatibility, and regression verification.

- [ ] T030 [P] Verify backward compatibility — load a pre-2.3.0 `repositories.json` file in the dashboard and confirm no errors, empty states render gracefully for missing fields
- [ ] T031 [P] Verify SVG regression — run `spark unified --user markhazleton` before and after changes, diff the `output/` SVG files to confirm they are unchanged
- [ ] T032 Verify performance — run `spark unified --user markhazleton --verbose` and confirm execution time is within 10% of baseline (SC-010)
- [ ] T033 [P] Verify responsive rendering — spot-check all new visualizations (heatmap, timeline, stat cards, bus factor badges) at viewport widths 768px, 1280px, and 2560px to confirm no overflow, truncation, or layout breakage (SC-007)
- [ ] T034 Add unit tests for `calculate_bus_factor()` in `tests/unit/test_calculator.py` — test single contributor (bus_factor=1, critical), even split (healthy), empty input (None), to maintain >80% core module coverage per constitution
- [ ] T035 Run `cd frontend && npm test` and `pytest tests/` to confirm no regressions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 — BLOCKS all frontend user stories
- **Phase 3 (US1 Heatmap)**: Depends on Phase 2 (needs `activity_calendar` in JSON)
- **Phase 4 (US2 Timeline)**: Depends on Phase 2 (needs `weekly_activity` in JSON)
- **Phase 5 (US3 Dark Mode)**: No backend dependency — can start after Phase 1, but benefits from running after Phase 3/4 to verify theme on new components
- **Phase 6 (US4 Export)**: Depends on Phase 2 (needs new fields to export)
- **Phase 7 (US5 Commit Volume)**: Depends on Phase 2 (needs `total_additions`/`total_deletions`)
- **Phase 8 (US6 Bus Factor)**: Depends on Phase 2 (needs `bus_factor` fields)
- **Phase 9 (Polish)**: Depends on all desired user stories being complete

### User Story Independence

- **US1 (Heatmap)** and **US2 (Timeline)**: Can run in parallel after Phase 2 (different components, different data fields)
- **US3 (Dark Mode)**: Can run in parallel with US1/US2 (CSS changes, independent component)
- **US4 (Export Enhancement)**: Can run in parallel with US3/US5/US6 (single file edit)
- **US5 (Commit Volume)** and **US6 (Bus Factor)**: Can run in parallel (different data, different display areas)

### Within Each User Story

1. Metrics calculator function first (data transformation)
2. Component creation (JSX + CSS in parallel)
3. Integration into App.jsx last

### Parallel Opportunities Per Story

```text
Phase 2 (Backend):
  T004 ──┐
  T005 ──┼── all [P] can run in parallel
  T006 ──┘
  T002 → T003 (sequential: weekly_activity depends on activity_calendar)
  T007 → T008 → T009 (sequential: integration pipeline)

Phase 3 (US1):
  T010 ──┐
  T012 ──┼── parallel (different files)
  T011 ──┘ (depends on T010 + T012 for data + styles)
  T013     (depends on T011)

Phase 5 (US3):
  T018 → T019 (sequential: context before CSS refactor)
  T020 ──┐
  T021 ──┼── parallel (different files)
  T022 ──┘
  T023     (depends on T018 + T021)
  T024     (depends on T023)
```

---

## Implementation Strategy

### MVP Scope

**US1 (Heatmap)** alone is a viable MVP — it's the single most visually impactful change, requires only persisting already-computed data (Phase 2: T001-T003), and delivers immediate value with no new API calls.

### Recommended Delivery Order

1. **Phase 1 + Phase 2** (T001-T009): Backend data pipeline — unlocks all frontend work
2. **Phase 3 (US1)** + **Phase 4 (US2)** in parallel: Highest-impact visualizations
3. **Phase 5 (US3)**: Dark mode — enhances all existing + new components
4. **Phase 6 + 7 + 8** in parallel: Export, commit volume, bus factor
5. **Phase 9**: Polish and verification

### Incremental Delivery

Each phase produces a deployable increment:
- After Phase 2: Backend generates richer data (no visible frontend change yet)
- After Phase 3: Heatmap visible on dashboard — can deploy
- After Phase 4: Timeline visible — can deploy
- After Phase 5: Dark mode toggle — can deploy
- After Phase 6-8: Enhanced detail views — can deploy
- After Phase 9: Fully verified release
