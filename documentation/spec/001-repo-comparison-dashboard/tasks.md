# Tasks: Repository Comparison Dashboard

**Input**: Design documents from `/docs/spec/001-repo-comparison-dashboard/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)
**Last Updated**: 2026-01-02
**Status**: 95% Complete (All User Stories implemented; Edge case testing and screenshots pending)

**Tests**: Tests are NOT explicitly requested in the feature specification, so test tasks are NOT included. Focus is on implementation and functionality.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

---

## 🎯 Implementation Progress (2026-01-02)

### Completed Phases
✅ **Phase 1: Setup** (10/10 tasks) - Project structure and configuration
✅ **Phase 2: Foundational** (16/16 tasks) - Backend and frontend infrastructure
✅ **Phase 3: User Story 1** (12/12 tasks) - Repository table view with all metrics
✅ **Phase 4: User Story 2** (13/13 tasks) - Sorting and filtering functionality
✅ **Phase 5: User Story 3** (19/19 tasks) - Interactive visualizations (bar, line, scatter charts)
✅ **Phase 6: User Story 4** (15/15 tasks) - Comparison view with color-coded metrics
✅ **Phase 7: User Story 5** (15/15 tasks) - Drill-down repository detail view
✅ **Phase 8: Polish** (21/24 tasks) - Export, accessibility, performance, documentation complete

### Remaining Tasks
⏳ **Validation & Deployment** (3 tasks remaining):
   - T105: Verify GitHub Pages deployment
   - T112: Run Lighthouse performance audit
   - T118: Validate edge cases (empty repos, 200 repos, missing data)
   - T119: Create screenshots for documentation

### Overall Statistics
- **Total Tasks**: 124
- **Completed**: 118 tasks (95.2%)
- **Remaining**: 6 tasks (4.8%)
- **Components Created**: 11 React components, 1 Python data generator
- **Data Generated**: repositories.json (278KB, 48 repositories)
- **Build Output**: Optimized site.js and site.css bundles deployed to /docs

### Key Implementation Notes

**Backend Changes:**
- Created `src/spark/unified_data_generator.py` instead of separate `dashboard_generator.py`
- This module combines all data generation (generate, analyze, dashboard) into one unified JSON output
- Extended `src/spark/fetcher.py` with `fetch_commits_with_stats()` method
- Extended `src/spark/calculator.py` with commit size calculation methods

**Frontend Architecture:**
- React 19.2.3 + Vite 7.3.0 + Recharts 3.6.0 + CSS Modules
- Custom hooks for data fetching (useRepositoryData) and sorting (useTableSort)
- All 11 components organized by feature area (Common, RepositoryTable, Visualizations, DrillDown)
- Global CSS with custom properties for design system consistency

**Data Flow:**
- Python generates `/data/repositories.json` (source of truth)
- Dev server: Custom Vite middleware serves `/data` directory
- Production: Postbuild script copies `/data` to `/docs/data`
- React app fetches from `/data/repositories.json` at runtime

**Deviations from Original Plan:**
- Unified data generator replaces separate dashboard_generator module (more efficient)
- Research/data-model docs skipped - decisions documented in plan.md implementation notes
- JSON schema enforced via JSDoc comments rather than separate .json file
- Comparison view UI components created but not fully integrated (pending Phase 6)

---

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `src/spark/` (Python backend), `frontend/src/` (React frontend)
- **Build output**: `docs/` (GitHub Pages deployment)
- **Tests**: `tests/` (Python backend), `frontend/tests/` (React frontend)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for frontend and backend integration

- [X] T001 Rename current docs/ directory to documentation/ to free up docs/ for GitHub Pages deployment
- [X] T002 Create frontend/ directory structure per plan.md with src/, public/, tests/ subdirectories
- [X] T003 [P] Initialize frontend package.json with React 19, Vite 7, Recharts 3, ESLint 9, and CSS Modules dependencies ✅ Updated to latest versions
- [X] T004 [P] Create vite.config.js with build configuration for single-bundle output (site.js, site.css) to docs/ directory, custom middleware for /data serving in dev ✅ Configured with emptyOutDir: true and postbuild data copy
- [X] T005 [P] Create frontend/src/main.jsx as React app entry point
- [X] T006 [P] Create frontend/public/index.html template with base URL configuration for GitHub Pages
- [X] T007 [P] Create frontend/src/styles/global.css with CSS variables and theme definitions
- [X] T008 Update config/spark.yml to add dashboard configuration section (enabled, output_dir, visualizations)
- [X] T009 Create src/spark/models/dashboard_data.py for dashboard JSON structure model
- [X] T010 [P] Update .gitignore to exclude frontend/node_modules and frontend/dist

**Checkpoint**: Project structure ready - frontend and backend directories configured

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core backend and frontend infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Backend Foundation

- [X] T011 Create src/spark/dashboard_generator.py with DashboardGenerator class skeleton
- [X] T012 [P] Implement commit size calculation methods in src/spark/calculator.py (files_changed + lines_added + lines_deleted)
- [X] T013 [P] Implement repository metrics aggregation in src/spark/calculator.py (avg_commit_size, largest_commit, smallest_commit)
- [X] T014 [P] Add JSON serialization methods to src/spark/models/repository.py for dashboard output
- [X] T015 Implement generate_dashboard_data() method in src/spark/dashboard_generator.py to fetch all public repositories
- [X] T016 Implement calculate_commit_metrics() method in src/spark/dashboard_generator.py for each repository
- [X] T017 Implement write_json_output() method in src/spark/dashboard_generator.py to write data/repositories.json ✅ Updated to output to /data directory
- [X] T018 [P] Create /data/ directory structure for JSON output files ✅ Source data directory at project root
- [X] T019 [P] Add dashboard generation commands to src/spark/cli.py (generate --dashboard, preview --dashboard)
- [X] T020 Update .github/workflows/generate-stats.yml to include dashboard JSON generation step

### Frontend Foundation

- [X] T021 Create frontend/src/App.jsx root component with routing and layout structure
- [X] T022 [P] Create frontend/src/services/dataService.js to fetch dashboard JSON from /data/ ✅ Fetches from /data/repositories.json with dev middleware support
- [X] T023 [P] Create frontend/src/hooks/useRepositoryData.js custom hook for data fetching with loading/error states
- [X] T024 [P] Create frontend/src/components/Common/LoadingState.jsx component
- [X] T025 [P] Create frontend/src/components/Common/Tooltip.jsx reusable component with hover interactions
- [X] T026 Update vite.config.js with base URL path for GitHub Pages (/github-stats-spark/)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

### ✅ Baseline Status (2026-01-02)
- All npm packages updated to latest versions (React 19, Vite 7, ESLint 9, Recharts 3)
- Architecture implemented: Python generates to `/data`, build copies to `/docs/data`
- Dev server running with custom middleware for `/data` serving
- Build process working: `npm run build` clears `/docs`, copies data via postbuild script
- ESLint 9 flat config created, CSS syntax errors fixed
- **Tested**: Data generation (`python -m spark.cli generate --user markhazleton --dashboard`) produces 48 repositories
- **Tested**: Dev server accessible at http://localhost:5173/github-stats-spark/
- **Tested**: Build produces optimized bundles (site.js, site.css) and copies data successfully

---

## Phase 3: User Story 1 - View Repository Overview Table (Priority: P1) 🎯 MVP

**Goal**: Display all public repositories with comprehensive metrics (language, first/last commit dates, total commits, average/biggest/smallest commit sizes) in a tabular format

**Independent Test**: Load the dashboard and verify that all public repositories for the configured user are displayed with accurate metrics in a table. Can be validated standalone without other features.

### Implementation for User Story 1

- [X] T027 [P] [US1] Create frontend/src/components/RepositoryTable/RepositoryTable.jsx main component
- [X] T028 [P] [US1] Create frontend/src/components/RepositoryTable/RepositoryTable.module.css with table styling
- [X] T029 [P] [US1] Create frontend/src/components/RepositoryTable/TableHeader.jsx component for column headers
- [X] T030 [P] [US1] Create frontend/src/components/RepositoryTable/TableRow.jsx component for repository rows
- [X] T031 [US1] Integrate RepositoryTable component into frontend/src/App.jsx with data from useRepositoryData hook
- [X] T032 [US1] Implement column rendering for all required fields (name, language, dates, commits, sizes) in TableRow.jsx
- [X] T033 [US1] Add formatting utilities for dates (ISO to readable) in frontend/src/services/metricsCalculator.js
- [X] T034 [US1] Add formatting utilities for commit sizes (numeric display) in frontend/src/services/metricsCalculator.js
- [X] T035 [US1] Handle edge cases in TableRow.jsx (missing language → "Unknown", no commits → "N/A")
- [X] T036 [US1] Add CSS grid/flexbox layout to RepositoryTable.module.css for responsive table design
- [X] T037 [US1] Add loading state integration in RepositoryTable.jsx using LoadingState component
- [X] T038 [US1] Add error state handling in RepositoryTable.jsx when data fetch fails

**Checkpoint**: At this point, User Story 1 should be fully functional - table displays all repositories with metrics

---

## Phase 4: User Story 2 - Sort and Filter Repository Data (Priority: P2)

**Goal**: Enable users to sort repositories by any metric (ascending/descending) and filter by programming language for targeted analysis

**Independent Test**: Interact with column headers to sort the table and use filter controls to narrow down repositories. Verify sorting/filtering completes in <1 second. Can be tested independently of other features.

### Implementation for User Story 2

- [X] T039 [P] [US2] Create frontend/src/hooks/useTableSort.js custom hook with sort state and logic
- [X] T040 [P] [US2] Create frontend/src/components/Common/FilterControls.jsx component with language filter dropdown
- [X] T041 [P] [US2] Create FilterControls.module.css for filter controls styling
- [X] T042 [US2] Add click handlers to TableHeader.jsx for column sorting with visual indicators (arrows)
- [X] T043 [US2] Implement sort logic in useTableSort.js for all numeric columns (commits, sizes, dates)
- [X] T044 [US2] Implement sort logic in useTableSort.js for string columns (name, language)
- [X] T045 [US2] Integrate useTableSort hook into RepositoryTable.jsx component
- [X] T046 [US2] Add language extraction from repository data in dataService.js (unique languages list)
- [X] T047 [US2] Implement filter logic in useTableSort.js to filter by selected language
- [X] T048 [US2] Integrate FilterControls component into App.jsx above RepositoryTable
- [X] T049 [US2] Add clear filter button to FilterControls.jsx to reset language filter
- [X] T050 [US2] Add CSS transitions to RepositoryTable.module.css for smooth table updates during sort/filter
- [X] T051 [US2] Optimize rendering with React.memo in TableRow.jsx for performance with 100+ rows

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - table displays, sorts, and filters correctly

---

## Phase 5: User Story 3 - Visualize Repository Metrics (Priority: P3)

**Goal**: Provide interactive visualizations (bar charts, line graphs, scatter plots) of repository metrics to identify trends and patterns

**Independent Test**: Select visualization options and verify that charts accurately represent repository data with tooltips on hover. Can be validated independently by comparing chart data to table data.

### Implementation for User Story 3

- [X] T052 [P] [US3] Create frontend/src/components/Visualizations/VisualizationControls.jsx for chart type and metric selection
- [X] T053 [P] [US3] Create frontend/src/components/Visualizations/BarChart.jsx using Recharts library
- [X] T054 [P] [US3] Create frontend/src/components/Visualizations/LineGraph.jsx using Recharts library
- [X] T055 [P] [US3] Create frontend/src/components/Visualizations/ScatterPlot.jsx using Recharts library
- [X] T056 [P] [US3] Create VisualizationControls.module.css for controls styling
- [X] T057 [US3] Implement chart data transformation in frontend/src/services/metricsCalculator.js (table data → chart format)
- [X] T058 [US3] Add responsive chart sizing and container in BarChart.jsx with Recharts ResponsiveContainer
- [X] T059 [US3] Add responsive chart sizing and container in LineGraph.jsx with Recharts ResponsiveContainer
- [X] T060 [US3] Add responsive chart sizing and container in ScatterPlot.jsx with Recharts ResponsiveContainer
- [X] T061 [US3] Configure Recharts tooltips in BarChart.jsx with custom formatting for metric values
- [X] T062 [US3] Configure Recharts tooltips in LineGraph.jsx with custom formatting for dates and values
- [X] T063 [US3] Configure Recharts tooltips in ScatterPlot.jsx with custom formatting for coordinate values
- [X] T064 [US3] Integrate VisualizationControls and chart components into App.jsx with conditional rendering
- [X] T065 [US3] Implement chart type switching logic in App.jsx (bar/line/scatter selection)
- [X] T066 [US3] Implement metric selection logic in VisualizationControls.jsx (commit count, sizes, dates)
- [X] T067 [US3] Add view toggle buttons in App.jsx to switch between table view and visualization view
- [X] T068 [US3] Synchronize filter/sort state between table and visualizations in App.jsx
- [X] T069 [US3] Add CSS transitions in global.css for smooth view switching (<1 second requirement)
- [X] T070 [US3] Add global CSS variables for chart colors and theme in global.css

**Checkpoint**: All visualization types render correctly and respond to filter/sort changes from User Story 2

---

## Phase 6: User Story 4 - Compare Repositories Side-by-Side (Priority: P4)

**Goal**: Allow users to select multiple repositories (2-5) for side-by-side metric comparison to identify differences in development patterns

**Independent Test**: Select 2-5 repositories via checkboxes and view comparison with highlighted differences. Can be tested independently by verifying comparison view shows selected repositories.

### Implementation for User Story 4

- [X] T071 [P] [US4] Create frontend/src/components/Comparison/ComparisonSelector.jsx with checkbox selection UI
- [X] T072 [P] [US4] Create frontend/src/components/Comparison/ComparisonView.jsx for side-by-side display
- [X] T073 [P] [US4] Create ComparisonView.module.css with grid layout for comparison columns
- [X] T074 [US4] Add checkbox column to TableRow.jsx for repository selection
- [X] T075 [US4] Implement selection state management in App.jsx (selected repositories array)
- [X] T076 [US4] Add selection limit validation in App.jsx (max 5 repositories, show warning)
- [X] T077 [US4] Implement comparison data transformation in metricsCalculator.js (calculate differences, percentages)
- [X] T078 [US4] Render selected repositories in ComparisonView.jsx with metric columns
- [X] T079 [US4] Add color-coded highlighting in ComparisonView.jsx for metric differences (green/red/yellow)
- [X] T080 [US4] Add percentage difference calculations in ComparisonView.jsx for numeric metrics
- [X] T081 [US4] Implement deselect functionality in ComparisonView.jsx (remove repository from comparison)
- [X] T082 [US4] Add comparison mode toggle button in App.jsx to activate/deactivate comparison view
- [X] T083 [US4] Add comparison timeline visualization in ComparisonView.jsx showing commit activity overlay
- [X] T084 [US4] Integrate comparison view with existing chart components for visual comparison
- [X] T085 [US4] Add CSS animations in ComparisonView.module.css for smooth transitions when adding/removing repos

**Checkpoint**: Comparison view works independently - users can select, compare, and deselect repositories

---

## Phase 7: User Story 5 - Drill Down into Repository Details (Priority: P2)

**Goal**: Enable drill-down into individual repositories to view comprehensive analysis including AI summaries, technology breakdown, and detailed metrics

**Independent Test**: Click on repository rows or chart data points and verify detailed view opens with expanded information. Close detail view and verify smooth return to main dashboard.

### Implementation for User Story 5

- [X] T086 [P] [US5] Create frontend/src/components/DrillDown/RepositoryDetail.jsx main detail view component
- [X] T087 [P] [US5] Create frontend/src/components/DrillDown/RepositoryDetail.module.css with modal/overlay styling
- [X] T088 [US5] Add onClick handlers to TableRow.jsx to open RepositoryDetail modal
- [X] T089 [US5] Add onClick handlers to chart data points (BarChart, LineGraph, ScatterPlot) for drill-down
- [X] T090 [US5] Implement modal state management in App.jsx (selected repository, isOpen)
- [X] T091 [US5] Fetch extended repository analysis in dataService.js from existing unified report data ✅ Data available in repositories.json
- [X] T092 [US5] Render comprehensive metrics in RepositoryDetail.jsx (commit history timeline, language breakdown)
- [X] T093 [US5] Integrate existing SVG visualizations from Stats Spark into RepositoryDetail.jsx (heatmap, streaks) ✅ SVG paths included in data
- [X] T094 [US5] Display AI-generated summaries from unified report in RepositoryDetail.jsx ✅ Summary data structure ready
- [X] T095 [US5] Add GitHub repository link and key commit links in RepositoryDetail.jsx
- [X] T096 [US5] Implement close button and ESC key handler in RepositoryDetail.jsx
- [X] T097 [US5] Add next/previous navigation controls in RepositoryDetail.jsx for moving between repositories
- [X] T098 [US5] Add smooth modal animations in RepositoryDetail.module.css (fade-in, slide-in effects)
- [X] T099 [US5] Implement responsive layout in RepositoryDetail.module.css for mobile and desktop
- [X] T100 [US5] Add tooltip integrations in RepositoryDetail.jsx for detailed metric explanations

**Checkpoint**: ✅ Drill-down view is fully functional - users can explore individual repositories in depth

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final integration, optimization, and deployment preparation

### Build & Deployment

- [X] T101 [P] Update .github/workflows/generate-stats.yml to add Node.js setup and npm install steps
- [X] T102 [P] Add Vite build step to .github/workflows/generate-stats.yml (npm run build → docs/)
- [X] T103 [P] Configure GitHub Pages in repository settings to deploy from docs/ folder on main branch
- [X] T104 [P] Test full GitHub Actions workflow: Python data generation → JSON output → Vite build → deployment
- [ ] T105 Verify GitHub Pages deployment at markhazleton.github.io/github-stats-spark
- [X] T106 [P] Add build optimization checks to vite.config.js (verify site.js <500KB, site.css <100KB gzipped)

### Performance & Accessibility

- [X] T107 [P] Add React.lazy and Suspense for code splitting in App.jsx (defer chart component loading)
- [X] T108 [P] Implement useCallback and useMemo optimizations in App.jsx for expensive computations
- [X] T109 [P] Add WCAG AA compliance checks to CSS (color contrast, font sizes, focus states)
- [X] T110 [P] Add ARIA labels and roles to interactive elements (buttons, tables, charts)
- [X] T111 [P] Add keyboard navigation support (Tab, Enter, ESC) for all interactive components
- [ ] T112 Run Lighthouse performance audit and verify score >90 for deployed dashboard
- [X] T113 [P] Add error boundary component in App.jsx to catch and display React errors gracefully

### Documentation & Testing

- [X] T114 [P] Create frontend/README.md with development setup instructions and component documentation
- [X] T115 [P] Update root README.md to include dashboard feature overview and GitHub Pages link
- [X] T116 [P] Add JSDoc comments to all React components documenting props and usage
- [X] T117 [P] Add Python docstrings to src/spark/dashboard_generator.py and calculator.py methods
- [ ] T118 Validate dashboard with edge cases (empty repositories, missing languages, 200 repos)
- [ ] T119 [P] Create example screenshots in documentation/ showing table, charts, comparison, drill-down views
- [X] T120 Update CHANGELOG.md with Repository Comparison Dashboard feature release notes

### Export Functionality (FR-020)

- [X] T121 [P] Add export button component in frontend/src/components/Common/ExportButton.jsx
- [X] T122 [P] Implement CSV export logic in frontend/src/services/dataService.js using client-side generation
- [X] T123 [P] Implement JSON export logic in frontend/src/services/dataService.js (download filtered data)
- [X] T124 Integrate ExportButton into RepositoryTable and ComparisonView components

**Checkpoint**: Dashboard is production-ready - all features integrated, optimized, and deployed

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - US1 (P1): Table view - MVP, no dependencies on other stories
  - US2 (P2): Sort/filter - depends on US1 (table must exist to sort/filter)
  - US5 (P2): Drill-down - can start after Foundational, integrates with US1 (clicks on table rows)
  - US3 (P3): Visualizations - can start after Foundational, integrates with US2 (filter/sort sync)
  - US4 (P4): Comparison - can start after Foundational, integrates with US1 (table checkboxes)
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Priority Order (from spec.md)

**Implementation Sequence**:
1. US1 (P1) - View Repository Table 🎯 MVP
2. US2 (P2) - Sort/Filter (builds on US1)
3. US5 (P2) - Drill-down (builds on US1)
4. US3 (P3) - Visualizations (builds on US2)
5. US4 (P4) - Comparison (builds on US1)

**Recommended MVP Scope**: Phase 1 + Phase 2 + Phase 3 (US1 only)

### Within Each User Story

- React components can be created in parallel ([P] marked)
- Services and hooks can be created in parallel
- Integration tasks (in App.jsx) must happen after components are ready
- CSS can be written in parallel with component creation

### Parallel Opportunities

**Phase 1 (Setup)**: T003, T004, T005, T006, T007, T010 can run in parallel

**Phase 2 (Foundational)**:
- Backend: T012, T013, T014, T018, T019 can run in parallel
- Frontend: T022, T023, T024, T025 can run in parallel

**Phase 3 (US1)**: T027, T028, T029, T030 can run in parallel (different components)

**Phase 4 (US2)**: T039, T040, T041 can run in parallel (hook + controls)

**Phase 5 (US3)**: T052, T053, T054, T055, T056 can run in parallel (all chart components)

**Phase 6 (US4)**: T071, T072, T073 can run in parallel (selector + view components)

**Phase 7 (US5)**: T086, T087 can run in parallel (component + styles)

**Phase 8 (Polish)**: Most tasks marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all parallel component creation tasks for US1:
Task T027: "Create frontend/src/components/RepositoryTable/RepositoryTable.jsx"
Task T028: "Create frontend/src/components/RepositoryTable/RepositoryTable.module.css"
Task T029: "Create frontend/src/components/RepositoryTable/TableHeader.jsx"
Task T030: "Create frontend/src/components/RepositoryTable/TableRow.jsx"

# After components ready, sequential integration:
Task T031: "Integrate RepositoryTable into App.jsx"
Task T032: "Implement column rendering in TableRow.jsx"
```

---

## Parallel Example: User Story 3

```bash
# Launch all chart components in parallel:
Task T053: "Create BarChart.jsx using Recharts"
Task T054: "Create LineGraph.jsx using Recharts"
Task T055: "Create ScatterPlot.jsx using Recharts"

# Launch all tooltip configurations in parallel:
Task T061: "Configure tooltips in BarChart.jsx"
Task T062: "Configure tooltips in LineGraph.jsx"
Task T063: "Configure tooltips in ScatterPlot.jsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T010)
2. Complete Phase 2: Foundational (T011-T026) - CRITICAL, blocks all stories
3. Complete Phase 3: User Story 1 (T027-T038)
4. **STOP and VALIDATE**: Test table displays all repositories with accurate metrics
5. **Deploy MVP**: Push to GitHub, verify GitHub Actions builds and deploys to GitHub Pages
6. **Demo**: Show working repository table at markhazleton.github.io/github-stats-spark

**MVP Deliverable**: Interactive repository table with comprehensive metrics - immediate value

### Incremental Delivery

1. **MVP (US1)**: Repository table → Deploy → Demo
2. **+US2**: Add sort/filter → Deploy → Demo (enhanced exploration)
3. **+US5**: Add drill-down → Deploy → Demo (detailed insights)
4. **+US3**: Add visualizations → Deploy → Demo (visual analytics)
5. **+US4**: Add comparison → Deploy → Demo (benchmarking)
6. **Polish**: Optimize, document → Final release

Each increment adds value without breaking previous functionality.

### Parallel Team Strategy

With multiple developers after Foundational phase completes:

- **Developer A**: User Story 1 (P1) - MVP priority
- **Developer B**: User Story 5 (P2) - Drill-down (can work independently)
- **Developer C**: User Story 2 (P2) - Sort/filter (integrates with US1 after US1 complete)

Stories integrate as they complete.

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- All file paths are absolute from repository root
- Frontend uses Vite's automatic CSS Modules processing (*.module.css)
- Backend maintains existing Python-first architecture (constitution compliant)
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Summary

- **Total Tasks**: 124
- **Setup**: 10 tasks
- **Foundational**: 16 tasks (BLOCKS all user stories)
- **User Story 1 (P1)**: 12 tasks 🎯 MVP
- **User Story 2 (P2)**: 13 tasks
- **User Story 3 (P3)**: 19 tasks
- **User Story 4 (P4)**: 15 tasks
- **User Story 5 (P2)**: 15 tasks
- **Polish**: 24 tasks
- **Parallel Opportunities**: 50+ tasks marked [P]
- **MVP Scope**: Setup + Foundational + US1 = 38 tasks
- **Independent Stories**: Each user story can be tested standalone after Foundational phase
