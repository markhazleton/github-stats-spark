# Tasks: Repository Comparison Dashboard

**Input**: Design documents from `/documentation/spec/001-repo-comparison-dashboard/`
**Prerequisites**: plan.md (required), spec.md (required), research.md (pending completion)

**Tests**: Testing tasks are included based on project constitution requirement for >80% coverage

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

- **Project Type**: Hybrid web (Python backend + JavaScript frontend)
- **Backend**: `src/spark/dashboard/` (new module extending existing Stats Spark)
- **Frontend**: `src/spark/dashboard/assets/` (CSS/JS) and `src/spark/dashboard/templates/` (Jinja2)
- **Tests**: `tests/dashboard/` (new directory)
- **Output**: `/docs/` (generated static files for GitHub Pages)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for dashboard module

- [ ] T001 Create dashboard module directory structure in src/spark/dashboard/ with __init__.py
- [ ] T002 [P] Create dashboard templates directory in src/spark/dashboard/templates/
- [ ] T003 [P] Create dashboard assets directory structure in src/spark/dashboard/assets/css/ and src/spark/dashboard/assets/js/
- [ ] T004 [P] Create dashboard tests directory in tests/dashboard/ with __init__.py
- [ ] T005 [P] Add dashboard configuration section to existing config/spark.yml
- [ ] T006 [P] Create test fixtures directory in tests/dashboard/fixtures/
- [ ] T007 [P] Create output directory structure for static files in /docs/
- [ ] T008 Install frontend dependencies (tabulator-tables, gsap) via package.json or CDN references
- [ ] T009 [P] Configure GitHub Pages settings in /docs/_config.yml

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T010 Implement DashboardConfig class in src/spark/config.py to handle dashboard-specific configuration
- [ ] T011 Create DataAggregator base class in src/spark/dashboard/aggregator.py for transforming Stats Spark outputs to dashboard data
- [ ] T012 [P] Create DashboardGenerator base class in src/spark/dashboard/generator.py for HTML/JSON generation
- [ ] T013 [P] Implement commit metrics calculator in src/spark/dashboard/metrics.py for commit size calculations (average, biggest, smallest)
- [ ] T014 Create base Jinja2 template layout in src/spark/dashboard/templates/base.html with common structure
- [ ] T015 [P] Implement repository data loader in src/spark/dashboard/aggregator.py to integrate with existing fetcher/calculator
- [ ] T016 Create CLI command structure for `spark dashboard` in src/cli.py
- [ ] T017 [P] Add dashboard generation to GitHub Actions workflow in .github/workflows/stats.yml
- [ ] T018 [P] Create utility functions for JSON schema validation in src/spark/dashboard/utils.py
- [ ] T019 Create base CSS framework setup in src/spark/dashboard/assets/css/base.css with theme variables

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View Repository Overview Table (Priority: P1) 🎯 MVP

**Goal**: Display all public repositories in a sortable, filterable table with key metrics (language, first commit, last commit, total commits, commit sizes)

**Independent Test**: Load the dashboard and verify all repositories appear with complete metrics in tabular format

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T020 [P] [US1] Unit test for repository data aggregation in tests/dashboard/test_aggregator.py
- [ ] T021 [P] [US1] Unit test for commit metrics calculations in tests/dashboard/test_metrics.py
- [ ] T022 [P] [US1] Integration test for table generation with sample data in tests/dashboard/test_table_generation.py
- [ ] T023 [P] [US1] Test fixture for sample repository data in tests/dashboard/fixtures/sample_repositories.json

### Implementation for User Story 1

- [ ] T024 [P] [US1] Extend DataAggregator to fetch all public repositories from existing Stats Spark in src/spark/dashboard/aggregator.py
- [ ] T025 [P] [US1] Implement commit size calculation (files changed + lines modified) in src/spark/dashboard/metrics.py
- [ ] T026 [US1] Create RepositoryTableData class in src/spark/dashboard/models.py for table data structure
- [ ] T027 [US1] Generate repositories.json with all table data in src/spark/dashboard/generator.py
- [ ] T028 [P] [US1] Create index.html Jinja2 template in src/spark/dashboard/templates/index.html
- [ ] T029 [P] [US1] Implement Tabulator.js table initialization in src/spark/dashboard/assets/js/table.js
- [ ] T030 [US1] Add column definitions for all metrics (language, commits, dates, sizes) in src/spark/dashboard/assets/js/table.js
- [ ] T031 [P] [US1] Create table styling in src/spark/dashboard/assets/css/table.css
- [ ] T032 [US1] Implement data loading from repositories.json in src/spark/dashboard/assets/js/app.js
- [ ] T033 [US1] Add empty state handling for users with no repositories in src/spark/dashboard/templates/index.html
- [ ] T034 [P] [US1] Add logging for repository data aggregation in src/spark/dashboard/aggregator.py

**Checkpoint**: At this point, User Story 1 should be fully functional - users can view all repositories in a table with complete metrics

---

## Phase 4: User Story 2 - Sort and Filter Repository Data (Priority: P2)

**Goal**: Enable interactive sorting by any column and filtering by programming language

**Independent Test**: Click column headers to sort and use filter controls to narrow repository list

### Tests for User Story 2

- [ ] T035 [P] [US2] Unit test for sort/filter logic in tests/dashboard/test_table_interactions.py
- [ ] T036 [P] [US2] Integration test for filter persistence in tests/dashboard/test_filtering.py

### Implementation for User Story 2

- [ ] T037 [P] [US2] Configure Tabulator.js sorting for all columns in src/spark/dashboard/assets/js/table.js
- [ ] T038 [P] [US2] Implement language filter dropdown in src/spark/dashboard/templates/components/filter.html
- [ ] T039 [US2] Add filter logic for language selection in src/spark/dashboard/assets/js/table.js
- [ ] T040 [US2] Implement filter clear functionality in src/spark/dashboard/assets/js/table.js
- [ ] T041 [P] [US2] Add filter UI styling in src/spark/dashboard/assets/css/filters.css
- [ ] T042 [US2] Add sort indicator icons to column headers in src/spark/dashboard/templates/index.html
- [ ] T043 [P] [US2] Implement performance optimization for sorting large datasets (virtual scrolling) in src/spark/dashboard/assets/js/table.js

**Checkpoint**: At this point, User Stories 1 AND 2 should both work - users can view, sort, and filter repositories

---

## Phase 5: User Story 5 - Drill Down into Repository Details (Priority: P2)

**Goal**: Click on any repository to see detailed analysis including AI summaries, SVG visualizations, and comprehensive statistics

**Independent Test**: Click repository rows to open detail modals showing all analysis content from weekly reports

### Tests for User Story 5

- [ ] T044 [P] [US5] Unit test for repository detail data generation in tests/dashboard/test_detail_generator.py
- [ ] T045 [P] [US5] Integration test for modal open/close behavior in tests/dashboard/test_modal.py

### Implementation for User Story 5

- [ ] T046 [P] [US5] Create repository detail JSON files in /docs/data/details/ for each repository
- [ ] T047 [P] [US5] Implement detail data aggregator to include AI summaries and Stats Spark analysis in src/spark/dashboard/aggregator.py
- [ ] T048 [US5] Create detail.html Jinja2 template for modal content in src/spark/dashboard/templates/detail.html
- [ ] T049 [P] [US5] Implement modal component in src/spark/dashboard/assets/js/modal.js
- [ ] T050 [US5] Add row click handler to open detail modal in src/spark/dashboard/assets/js/table.js
- [ ] T051 [P] [US5] Integrate existing SVG visualizations into detail view in src/spark/dashboard/assets/js/modal.js
- [ ] T052 [US5] Implement modal close on ESC key and close button in src/spark/dashboard/assets/js/modal.js
- [ ] T053 [P] [US5] Add next/previous navigation between repository details in src/spark/dashboard/assets/js/modal.js
- [ ] T054 [P] [US5] Style detail modal with CSS animations (slide-in transition) in src/spark/dashboard/assets/css/modal.css
- [ ] T055 [US5] Add links to GitHub repository and key commits in detail view template
- [ ] T056 [P] [US5] Implement lazy loading for detail data (only fetch when modal opens) in src/spark/dashboard/assets/js/modal.js

**Checkpoint**: At this point, users can view table, sort/filter, and drill into detailed repository analysis

---

## Phase 6: User Story 3 - Visualize Repository Metrics (Priority: P3)

**Goal**: Provide interactive charts (bar, line, scatter) showing repository metrics with tooltips

**Independent Test**: Select visualization types and verify charts display accurate data with interactive tooltips

### Tests for User Story 3

- [ ] T057 [P] [US3] Unit test for chart data formatting in tests/dashboard/test_chart_data.py
- [ ] T058 [P] [US3] Integration test for chart rendering in tests/dashboard/test_charts.py

### Implementation for User Story 3

- [ ] T059 [P] [US3] Add Chart.js library reference in src/spark/dashboard/templates/base.html
- [ ] T060 [P] [US3] Create chart container in index.html template for visualization display
- [ ] T061 [US3] Implement chart data formatter in src/spark/dashboard/assets/js/charts.js
- [ ] T062 [P] [US3] Create bar chart visualization for commit counts in src/spark/dashboard/assets/js/charts.js
- [ ] T063 [P] [US3] Create line graph for commit timeline (first vs last commit) in src/spark/dashboard/assets/js/charts.js
- [ ] T064 [P] [US3] Create scatter plot for repository activity patterns in src/spark/dashboard/assets/js/charts.js
- [ ] T065 [US3] Implement chart type selector UI in src/spark/dashboard/templates/components/chart-selector.html
- [ ] T066 [US3] Add metric selector for choosing which data to visualize in src/spark/dashboard/assets/js/charts.js
- [ ] T067 [P] [US3] Configure Chart.js tooltips with responsive display in src/spark/dashboard/assets/js/charts.js
- [ ] T068 [US3] Implement dynamic chart updates when filters are applied in src/spark/dashboard/assets/js/charts.js
- [ ] T069 [P] [US3] Style chart container and controls in src/spark/dashboard/assets/css/charts.css

**Checkpoint**: All visualization features complete - users can explore data through tables and charts

---

## Phase 7: User Story 4 - Compare Repositories Side-by-Side (Priority: P4)

**Goal**: Select multiple repositories and view comparison with highlighted differences

**Independent Test**: Select 2+ repositories and verify comparison view shows metrics side-by-side with clear diff indicators

### Tests for User Story 4

- [ ] T070 [P] [US4] Unit test for comparison data formatting in tests/dashboard/test_comparison.py
- [ ] T071 [P] [US4] Integration test for multi-select behavior in tests/dashboard/test_multi_select.py

### Implementation for User Story 4

- [ ] T072 [P] [US4] Add checkbox column to repository table in src/spark/dashboard/templates/index.html
- [ ] T073 [US4] Implement multi-select logic in src/spark/dashboard/assets/js/table.js
- [ ] T074 [P] [US4] Create comparison view template in src/spark/dashboard/templates/components/comparison.html
- [ ] T075 [US4] Implement comparison data aggregator in src/spark/dashboard/assets/js/comparison.js
- [ ] T076 [US4] Add comparison activation button (appears when 2+ selected) in src/spark/dashboard/assets/js/table.js
- [ ] T077 [P] [US4] Format comparison metrics with color-coded differences in src/spark/dashboard/assets/js/comparison.js
- [ ] T078 [P] [US4] Implement percentage difference calculator for metrics in src/spark/dashboard/assets/js/comparison.js
- [ ] T079 [US4] Add comparison view for commit timelines in src/spark/dashboard/assets/js/comparison.js
- [ ] T080 [US4] Implement deselect functionality to update comparison dynamically in src/spark/dashboard/assets/js/table.js
- [ ] T081 [P] [US4] Add warning for selecting more than 5 repositories in src/spark/dashboard/assets/js/table.js
- [ ] T082 [P] [US4] Style comparison view with side-by-side layout in src/spark/dashboard/assets/css/comparison.css

**Checkpoint**: Full feature set complete - users can view, filter, visualize, drill down, and compare repositories

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final deployment setup

- [ ] T083 [P] Implement CSS animations for view transitions (table ↔ charts ↔ comparison) in src/spark/dashboard/assets/css/animations.css
- [ ] T084 [P] Add GSAP library for complex animations (lazy-loaded) in src/spark/dashboard/assets/js/animations.js
- [ ] T085 [P] Implement 60fps animation optimization with CSS transforms in src/spark/dashboard/assets/css/animations.css
- [ ] T086 [P] Add responsive tooltip implementation with 200ms delay in src/spark/dashboard/assets/js/tooltips.js
- [ ] T087 Implement data export functionality (CSV, JSON) in src/spark/dashboard/assets/js/export.js
- [ ] T088 [P] Add export buttons to table toolbar in src/spark/dashboard/templates/index.html
- [ ] T089 [P] Implement theme inheritance from existing Stats Spark themes in src/spark/dashboard/generator.py
- [ ] T090 [P] Add WCAG AA accessibility compliance checks in src/spark/dashboard/assets/css/
- [ ] T091 Configure GitHub Pages deployment from /docs/ folder in repository settings
- [ ] T092 [P] Add error handling for missing data (display "N/A") across all components
- [ ] T093 [P] Implement API rate limit handling with user feedback in src/spark/dashboard/aggregator.py
- [ ] T094 [P] Add performance monitoring and logging in src/spark/dashboard/generator.py
- [ ] T095 Optimize JSON file sizes with compression for 200+ repositories
- [ ] T096 [P] Add quickstart.md validation - test all CLI commands
- [ ] T097 [P] Create README.md for dashboard feature in /docs/
- [ ] T098 Update main project README.md with dashboard section and link to demo
- [ ] T099 [P] Code cleanup and refactoring across all dashboard modules
- [ ] T100 Run full test suite and verify >80% coverage for dashboard module
- [ ] T101 Performance testing: Verify all success criteria (SC-001 through SC-013) are met
- [ ] T102 Deploy dashboard to GitHub Pages and verify URL pattern username.github.io/github-stats-spark

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User Story 1 (P1): No dependencies on other stories - MVP baseline
  - User Story 2 (P2): Depends on US1 (extends table functionality)
  - User Story 5 (P2): Depends on US1 (drill-down from table rows)
  - User Story 3 (P3): Depends on US1 (visualizes table data), can integrate with US2 filters
  - User Story 4 (P4): Depends on US1 (multi-select from table), can integrate with US2/US3
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - **MVP** - No dependencies on other stories
- **User Story 2 (P2)**: Can start after US1 completes - Extends table with sort/filter - Independently testable
- **User Story 5 (P2)**: Can start after US1 completes - Adds drill-down to table - Independently testable
- **User Story 3 (P3)**: Can start after US1 completes - Adds charts alongside table - Independently testable
- **User Story 4 (P4)**: Can start after US1 completes - Adds comparison to table - Independently testable

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models/data structures before services/logic
- Backend generation before frontend rendering
- Core implementation before integrations
- Story complete and tested before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes:
  - US1 tasks can proceed
  - After US1: US2, US3, US4, US5 can proceed in parallel (different files, independently testable)
- All tests for a user story marked [P] can run in parallel
- Polish tasks marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for repository data aggregation in tests/dashboard/test_aggregator.py"
Task: "Unit test for commit metrics calculations in tests/dashboard/test_metrics.py"
Task: "Integration test for table generation in tests/dashboard/test_table_generation.py"
Task: "Test fixture creation in tests/dashboard/fixtures/sample_repositories.json"

# Launch all parallel implementation tasks for User Story 1:
Task: "Extend DataAggregator in src/spark/dashboard/aggregator.py"
Task: "Implement commit size calculation in src/spark/dashboard/metrics.py"
Task: "Create index.html template in src/spark/dashboard/templates/index.html"
Task: "Create table styling in src/spark/dashboard/assets/css/table.css"
Task: "Add logging in src/spark/dashboard/aggregator.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T009)
2. Complete Phase 2: Foundational (T010-T019) - **CRITICAL CHECKPOINT**
3. Complete Phase 3: User Story 1 (T020-T034)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy to GitHub Pages and verify basic dashboard works
6. **MVP DELIVERED**: Users can view all repositories with metrics in a table

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → **Deploy/Demo (MVP!)**
3. Add User Story 2 → Test independently → Deploy/Demo (sortable/filterable table)
4. Add User Story 5 → Test independently → Deploy/Demo (drill-down details)
5. Add User Story 3 → Test independently → Deploy/Demo (visualizations)
6. Add User Story 4 → Test independently → Deploy/Demo (comparisons)
7. Add Polish → Final production-ready release
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (T020-T034) - **MVP focus**
3. After US1 completes:
   - Developer A: User Story 2 (T035-T043)
   - Developer B: User Story 5 (T044-T056)
   - Developer C: User Story 3 (T057-T069)
4. After US2, US3, US5 complete:
   - Developer A or B: User Story 4 (T070-T082)
5. All developers: Polish tasks (T083-T102)
6. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies - can run in parallel
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (TDD approach)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- **Technology Stack** (from plan.md):
  - Backend: Python 3.11+, Jinja2 templates
  - Frontend: Vanilla JavaScript, Tabulator.js, Chart.js, GSAP (selective)
  - Testing: pytest for Python, integration tests for frontend
  - Deployment: GitHub Pages from `/docs` folder
- **Performance Targets**:
  - Table load <5s for 50 repos
  - Sort/filter <1s for 100 repos
  - Visualizations <2s for 100 repos
  - Animations at 60fps
  - Drill-down <500ms
  - Tooltips <200ms
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Task Summary

- **Total Tasks**: 102
- **User Story 1 (P1 - MVP)**: 15 tasks (T020-T034)
- **User Story 2 (P2)**: 9 tasks (T035-T043)
- **User Story 5 (P2)**: 13 tasks (T044-T056)
- **User Story 3 (P3)**: 13 tasks (T057-T069)
- **User Story 4 (P4)**: 13 tasks (T070-T082)
- **Setup**: 9 tasks (T001-T009)
- **Foundational**: 10 tasks (T010-T019)
- **Polish**: 20 tasks (T083-T102)

**Parallel Opportunities**: 47 tasks marked [P] can run in parallel with other tasks in their phase
**MVP Scope**: Setup (9) + Foundational (10) + User Story 1 (15) = **34 tasks for MVP**
**Independent Test Criteria**: Each user story has clear acceptance scenarios from spec.md
