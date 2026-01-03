# Tasks: Mobile-First Front-End Redesign

**Input**: Design documents from `C:\GitHub\MarkHazleton\github-stats-spark\docs\spec\001-mobile-first-redesign\`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Tests are OPTIONAL and NOT included in this task list (not explicitly requested in feature specification).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5, US6)
- Exact file paths included in all task descriptions

## Path Conventions

- **Frontend**: `C:\GitHub\MarkHazleton\github-stats-spark\frontend\`
- **Backend**: `C:\GitHub\MarkHazleton\github-stats-spark\src\` (UNCHANGED)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization, dependencies, and build configuration

- [X] T001 Update package.json to add new dependencies: @use-gesture/react@^10.3.1, react-modal-sheet@^5.2.1, dexie@^4.0.0, chart.js@^4.0.0 in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\package.json`
- [X] T002 Add dev dependencies: vite-plugin-pwa@latest, @lighthouse/cli@latest to `C:\GitHub\MarkHazleton\github-stats-spark\frontend\package.json`
- [X] T003 Run npm install to install all new dependencies in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\`
- [X] T004 Configure vite-plugin-pwa in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\vite.config.js` for service worker generation and offline support
- [X] T005 Add bundle size monitoring config with size limits (170KB JS gzipped, 50KB CSS gzipped) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\vite.config.js`
- [X] T006 Create .lighthouserc.json with performance budgets (FCP <2s, TTI <5s, Performance >90, Accessibility >95) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\.lighthouserc.json`
- [X] T007 [P] Create directory structure: `frontend\src\components\Mobile\`, `frontend\src\components\Layout\`, `frontend\src\hooks\`, `frontend\src\services\`, `frontend\src\styles\mobile\`
- [X] T008 [P] Create empty component directories: `frontend\src\components\Mobile\BottomSheet\`, `frontend\src\components\Mobile\TabBar\`, `frontend\src\components\Mobile\RepositoryCard\`, `frontend\src\components\Mobile\GestureHandler\`, `frontend\src\components\Mobile\EmptyState\`, `frontend\src\components\Mobile\TouchTarget\`
- [X] T009 [P] Create layout component directories: `frontend\src\components\Layout\Container\`, `frontend\src\components\Layout\Stack\`, `frontend\src\components\Layout\SafeArea\`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core mobile-first infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Mobile-First CSS Foundation

- [X] T010 [P] Create breakpoints.css with mobile-first breakpoint system (xs: 0-319px, sm: 320-767px, md: 768-1023px, lg: 1024-1279px, xl: 1280px+) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\styles\mobile\breakpoints.css`
- [X] T011 [P] Create touch.css with minimum 44x44px touch target styles, 8px spacing, and touch feedback states in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\styles\mobile\touch.css`
- [X] T012 [P] Create gestures.css with visual feedback for swipe, tap, long-press gestures (ripple effects, highlights) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\styles\mobile\gestures.css`
- [X] T013 [P] Create safe-area.css with CSS custom properties for safe area insets (iOS notch, Android home indicators) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\styles\mobile\safe-area.css`

### Core Layout Components

- [X] T014 Create Container component with mobile-first responsive padding and max-width in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Layout\Container\Container.jsx`
- [X] T015 Create Stack component for vertical/horizontal spacing with mobile-friendly gaps in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Layout\Stack\Stack.jsx`
- [X] T016 Create SafeArea component that applies safe area insets for notched devices in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Layout\SafeArea\SafeArea.jsx`

### Core Hooks and Context

- [X] T017 Create ViewportContext with current breakpoint, window dimensions, isMobile flag, orientation tracking in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\contexts\ViewportContext.jsx`
- [X] T018 Create useMediaQuery hook for responsive breakpoint detection (320px, 768px, 1024px, 1280px) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\useMediaQuery.js`
- [X] T019 Create useNetworkStatus hook wrapping Network Information API for connection quality detection in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\useNetworkStatus.js`

### Base Mobile Components

- [X] T020 Create TouchTarget wrapper component enforcing 44x44px minimum size with touch feedback in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\TouchTarget\TouchTarget.jsx`
- [X] T021 Create LoadingState component with skeleton screens for card, list, chart variants in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\LoadingState\LoadingState.jsx`

### App-Level Enhancements

- [X] T022 Update index.html to add viewport meta tag with width=device-width, initial-scale=1, and safe area inset support in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\index.html`
- [X] T023 Update index.html to inline critical CSS for mobile-first breakpoints and touch targets to prevent render-blocking in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\index.html`
- [X] T024 Update App.jsx to wrap application with ViewportContext provider in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Mobile Dashboard Browsing (Priority: P1) 🎯 MVP

**Goal**: Repository data in vertical card layout, 44x44px touch targets, no horizontal scroll on mobile viewports (320px-768px)

**Independent Test**: Load on 375px viewport, verify no horizontal scroll, confirm all touch targets are at least 44x44px

### Implementation for User Story 1

- [X] T025 [P] [US1] Create RepositoryCard component in collapsed state showing name, language badge, stars count, last commit date in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\RepositoryCard.jsx`
- [X] T026 [P] [US1] Create RepositoryCard.css with mobile-first card styles, vertical layout, proper spacing in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\RepositoryCard.css`
- [X] T027 [P] [US1] Create LanguageBadge component for primary language display in cards in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\LanguageBadge.jsx`
- [X] T028 [US1] Update RepositoryTable component to conditionally render as card list on mobile (<768px) and table on desktop in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`
- [X] T029 [US1] Add responsive grid layout that switches from single column (mobile) to multi-column (desktop) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`
- [X] T030 [US1] Ensure all interactive elements (cards, buttons, links) have 44x44px minimum touch targets in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`
- [X] T031 [US1] Add skeleton loading states for repository cards during data fetch in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`
- [X] T032 [US1] Prevent horizontal scrolling on viewports 320px-768px with overflow-x: hidden and max-width constraints in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.css`
- [X] T033 [US1] Position primary actions in bottom 1/3 of screen for thumb-reach zones (one-handed usage) in main dashboard view in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`
- [X] T034 [US1] Optimize critical rendering path to achieve <3s content load on 3G (1.6 Mbps) by lazy loading below-fold components in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`

**Checkpoint**: At this point, User Story 1 should be fully functional - mobile dashboard displays repository cards without horizontal scroll

---

## Phase 4: User Story 2 - Touch-Optimized Repository Comparison (Priority: P1)

**Goal**: Multi-select with checkboxes, swipe gestures, card expansion, comparison view optimized for mobile

**Independent Test**: Select 2-5 repos using checkboxes, verify swipe-to-delete works, test comparison view on 375px viewport

### Implementation for User Story 2

- [X] T035 [P] [US2] Create useGesture hook wrapping @use-gesture/react for swipe detection (left, right, up, down) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\useGesture.js`
- [X] T036 [P] [US2] Create GestureHandler component that wraps elements with swipe gesture detection in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\GestureHandler\GestureHandler.jsx`
- [X] T037 [US2] Add checkbox control (44x44px minimum) to RepositoryCard for multi-select in top-right corner in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\RepositoryCard.jsx`
- [X] T038 [US2] Add selection state management to RepositoryCard showing checkmark and highlighted border when selected in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\RepositoryCard.jsx`
- [X] T039 [US2] Add expanded state to RepositoryCard revealing commit history, full description, technology stack, detailed metrics in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\RepositoryCard.jsx`
- [X] T040 [US2] Implement tap-to-expand behavior on card body (not checkbox) with smooth animation in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\RepositoryCard.jsx`
- [X] T041 [US2] Add swipe-left gesture to reveal delete action for removing card from comparison list in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\RepositoryCard.jsx`
- [X] T042 [US2] Create CompareButton component that appears when 2-5 repositories are selected with selection count badge in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Comparison\CompareButton.jsx`
- [X] T043 [US2] Update Comparison component to display metrics in vertical stacked layout optimized for portrait orientation in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Comparison\Comparison.jsx`
- [X] T044 [US2] Add horizontal swipe navigation between different comparison metrics in comparison view in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Comparison\Comparison.jsx`
- [X] T045 [US2] Add haptic feedback (Vibration API) for swipe-to-delete and selection actions on supported devices in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\useGesture.js`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - users can select, compare, and interact with repositories using touch gestures

---

## Phase 5: User Story 3 - Progressive Chart Visualization (Priority: P2)

**Goal**: Mobile-optimized charts with touch interactions, migrate from Recharts to Chart.js for better mobile performance and smaller bundle size

**Independent Test**: Load charts on 375px viewport, verify touch tooltips work, test horizontal scroll within chart container

### Implementation for User Story 3

- [X] T046 [P] [US3] Remove Recharts dependency from package.json in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\package.json`
- [X] T047 [P] [US3] Create ChartWrapper component using Chart.js with canvas-based rendering in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Visualizations\ChartWrapper.jsx`
- [X] T048 [P] [US3] Create useChart hook for Chart.js initialization, configuration, and responsive behavior in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\useChart.js`
- [X] T049 [US3] Migrate bar charts from Recharts to Chart.js with vertical orientation and max 10 bars for mobile in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Visualizations\BarChart.jsx`
- [X] T050 [US3] Migrate line charts from Recharts to Chart.js with touch-optimized tooltips in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Visualizations\LineChart.jsx`
- [X] T051 [US3] Migrate pie/doughnut charts from Recharts to Chart.js with touch interactions in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Visualizations\PieChart.jsx`
- [X] T052 [US3] Add touch-and-hold tooltip display positioned to avoid finger occlusion in Chart.js config in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\useChart.js`
- [X] T053 [US3] Implement horizontal scroll within chart container when data exceeds viewport width (maintaining fixed axes) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Visualizations\ChartWrapper.jsx`
- [X] T054 [US3] Create ChartTypeSelector component with large touch-friendly buttons for switching chart types in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Visualizations\ChartTypeSelector.jsx`
- [X] T055 [US3] Optimize chart rendering performance for mobile devices with canvas debouncing and lazy loading in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\useChart.js`
- [X] T056 [US3] Add responsive chart sizing that adapts to viewport width (320px-768px) with appropriate aspect ratios in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Visualizations\ChartWrapper.jsx`

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently - charts render efficiently on mobile with touch interactions

---

## Phase 6: User Story 4 - Bottom Sheet Navigation Pattern (Priority: P2)

**Goal**: Bottom sheet UI pattern for filters, settings, and detailed views with swipe-to-dismiss and backdrop interaction

**Independent Test**: Trigger filter bottom sheet, verify swipe-down dismissal works, test backdrop click dismissal

### Implementation for User Story 4

- [X] T057 [P] [US4] Create useBottomSheet hook for managing bottom sheet state (open/close, snap points, current snap) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\useBottomSheet.js`
- [X] T058 [P] [US4] Create BottomSheet component using react-modal-sheet with snap points [0.4, 0.9] in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\BottomSheet\BottomSheet.jsx`
- [X] T059 [US4] Add swipe-down gesture detection for dismissing bottom sheet with smooth animation in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\BottomSheet\BottomSheet.jsx`
- [X] T060 [US4] Add dimmed backdrop with tap-to-dismiss functionality in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\BottomSheet\BottomSheet.jsx`
- [X] T061 [US4] Create FilterSheet component as bottom sheet containing filter options (language, stars, date range) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\FilterSheet.jsx`
- [X] T062 [US4] Create SortSheet component as bottom sheet with sort field options (name, stars, commits, last updated, language) and direction toggle in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\SortSheet.jsx`
- [X] T063 [US4] Add filter button in repository list header that opens FilterSheet bottom sheet in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`
- [X] T064 [US4] Add sort button in repository list header that opens SortSheet bottom sheet in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`
- [X] T065 [US4] Create DetailSheet component for full repository details accessed from expanded cards in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\DetailSheet.jsx`
- [X] T066 [US4] Add focus trap to bottom sheet for keyboard accessibility in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\BottomSheet\BottomSheet.jsx`
- [X] T067 [US4] Prevent browser pull-to-refresh when bottom sheet is active using touch event preventDefault in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\BottomSheet\BottomSheet.jsx`

**Checkpoint**: At this point, User Stories 1-4 should all work independently - bottom sheets provide mobile-native navigation patterns

---

## Phase 7: User Story 5 - Offline-First Data Access (Priority: P3)

**Goal**: IndexedDB cache with 7-day retention, offline indicators, automatic sync when connectivity returns

**Independent Test**: Load data, go offline (dev tools), verify cached data accessible, confirm offline indicator shows

### Implementation for User Story 5

- [ ] T068 [P] [US5] Create offlineStorage service using Dexie.js for IndexedDB wrapper with CRUD operations in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\services\offlineStorage.js`
- [ ] T069 [P] [US5] Create OfflineCacheContext for cache status (online/offline), last sync timestamp, pending sync operations in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\contexts\OfflineCacheContext.jsx`
- [ ] T070 [P] [US5] Create useOfflineCache hook for caching repository data with 7-day retention policy in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\useOfflineCache.js`
- [ ] T071 [US5] Define IndexedDB schema for repositories cache with timestamp, version, and size fields in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\services\offlineStorage.js`
- [ ] T072 [US5] Implement automatic cache cleanup on app load to remove entries older than 7 days in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\services\offlineStorage.js`
- [ ] T073 [US5] Update dataService to check offline cache before network requests in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\services\dataService.js`
- [ ] T074 [US5] Update dataService to store fetched data in IndexedDB cache with timestamp in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\services\dataService.js`
- [ ] T075 [US5] Create OfflineIndicator component showing offline status and cached data timestamp in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\OfflineIndicator\OfflineIndicator.jsx`
- [ ] T076 [US5] Add OfflineIndicator to App.jsx header that appears when navigator.onLine is false in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`
- [ ] T077 [US5] Create service worker for offline functionality and asset precaching in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\public\sw.js`
- [ ] T078 [US5] Add service worker registration in main.jsx with update notifications in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\main.jsx`
- [ ] T079 [US5] Implement background sync when connectivity returns to fetch fresh data in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\services\dataService.js`
- [ ] T080 [US5] Add toast notification when data is refreshed after coming back online in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\services\dataService.js`
- [ ] T081 [US5] Show friendly error message with manual retry button when offline refresh is attempted in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`

**Checkpoint**: At this point, User Stories 1-5 should all work independently - app works offline with cached data

---

## Phase 8: User Story 6 - Accessibility and Reduced Motion (Priority: P2)

**Goal**: ARIA labels, keyboard navigation, screen reader support, reduced motion preferences respected

**Independent Test**: Screen reader test (NVDA/JAWS), keyboard navigation only, verify prefers-reduced-motion CSS works

### Implementation for User Story 6

- [ ] T082 [P] [US6] Add ARIA labels to all interactive elements (buttons, links, checkboxes, cards) across all components in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\`
- [ ] T083 [P] [US6] Add ARIA live regions for dynamic content updates (repository count, filter changes, loading states) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`
- [ ] T084 [P] [US6] Implement logical focus order for keyboard navigation (tab bar -> cards -> filters -> actions) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`
- [ ] T085 [P] [US6] Add visible focus indicators with 4.5:1 contrast ratio to all interactive elements in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\styles\mobile\touch.css`
- [ ] T086 [US6] Create SkipLink component for bypassing repetitive navigation to main content in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Layout\SkipLink\SkipLink.jsx`
- [ ] T087 [US6] Add skip links to App.jsx header allowing keyboard users to jump to main content in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`
- [ ] T088 [US6] Create reduced-motion.css with prefers-reduced-motion media query replacing animations with instant transitions in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\styles\mobile\reduced-motion.css`
- [ ] T089 [US6] Replace card expansion animations with subtle fades when prefers-reduced-motion is enabled in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\RepositoryCard.jsx`
- [ ] T090 [US6] Replace bottom sheet slide animations with instant display when prefers-reduced-motion is enabled in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\BottomSheet\BottomSheet.jsx`
- [ ] T091 [US6] Replace gesture feedback animations with subtle visual changes when prefers-reduced-motion is enabled in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\styles\mobile\gestures.css`
- [ ] T092 [US6] Ensure all form controls have associated labels for screen readers in FilterSheet and SortSheet in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\`
- [ ] T093 [US6] Add semantic HTML (nav, main, section, article) throughout application for screen reader landmarks in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`
- [ ] T094 [US6] Test keyboard navigation flow and fix any keyboard traps or unreachable elements across all components

**Checkpoint**: At this point, all User Stories 1-6 should work independently - app is accessible and respects motion preferences

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final production readiness

### Tab Bar Navigation (Cross-Cutting)

- [ ] T095 [P] Create TabBar component with 3 tabs (Dashboard, Compare, Visualizations) fixed at bottom in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\TabBar\TabBar.jsx`
- [ ] T096 [P] Create TabBar.css with mobile-safe area insets and 44x44px touch targets per tab in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\TabBar\TabBar.css`
- [ ] T097 Add TabBar to App.jsx as fixed bottom navigation visible on all mobile viewports (<768px) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`
- [ ] T098 Add active tab state highlighting and badge counts (for comparison selection) in TabBar in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\TabBar\TabBar.jsx`

### Empty State (Cross-Cutting)

- [ ] T099 [P] Create EmptyState component with center-aligned icon, message, and action button in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\EmptyState\EmptyState.jsx`
- [ ] T100 Add EmptyState to RepositoryTable when filter results in zero items with "Clear filters" action in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`
- [ ] T101 Add EmptyState to Comparison view when no repositories selected with "Browse repositories" action in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Comparison\Comparison.jsx`

### Error Handling (Cross-Cutting)

- [ ] T102 [P] Create ErrorBoundary component for catastrophic React errors with friendly message and retry button in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\ErrorBoundary\ErrorBoundary.jsx`
- [ ] T103 Wrap App.jsx with ErrorBoundary to catch and display errors gracefully in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\main.jsx`
- [ ] T104 Add automatic retry after 30 seconds for network errors in dataService in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\services\dataService.js`
- [ ] T105 Add console error and warning logging for debugging (no silent failures) in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\services\dataService.js`

### Performance Optimization (Cross-Cutting)

- [ ] T106 [P] Implement lazy loading for Comparison route to reduce initial bundle size in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`
- [ ] T107 [P] Implement lazy loading for Visualizations route to reduce initial bundle size in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`
- [ ] T108 Add virtual scrolling to RepositoryTable for lists exceeding 50 items to maintain mobile performance in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`
- [ ] T109 Add responsive image loading with srcset for different viewport sizes in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\RepositoryCard\RepositoryCard.jsx`
- [ ] T110 Verify bundle size meets performance budget (<170KB JS gzipped, <50KB CSS gzipped) using Vite build analysis
- [ ] T111 Run Lighthouse CI audit to verify Performance >90, Accessibility >95, FCP <2s, TTI <5s on 3G

### Pull-to-Refresh (Cross-Cutting)

- [ ] T112 Create usePullToRefresh hook for detecting pull-down gesture on scroll containers in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\hooks\usePullToRefresh.js`
- [ ] T113 Add pull-to-refresh functionality to RepositoryTable for manual data updates on mobile in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\RepositoryTable\RepositoryTable.jsx`

### Toast Notifications (Cross-Cutting)

- [ ] T114 [P] Create Toast component for transient feedback positioned at bottom above TabBar in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\components\Mobile\Toast\Toast.jsx`
- [ ] T115 Add Toast notifications for data refresh success, offline mode warnings, and error states across application in `C:\GitHub\MarkHazleton\github-stats-spark\frontend\src\App.jsx`

### Documentation and Validation

- [ ] T116 Update README.md with mobile-first design documentation and getting started instructions in `C:\GitHub\MarkHazleton\github-stats-spark\README.md`
- [ ] T117 Validate implementation against quickstart.md patterns and examples in `C:\GitHub\MarkHazleton\github-stats-spark\docs\spec\001-mobile-first-redesign\quickstart.md`
- [ ] T118 Test all user stories independently on real mobile devices (iOS 13+, Android 8+) at 375px viewport

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-8)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
  - Recommended: US1 (P1) → US2 (P1) → US3 (P2) → US4 (P2) → US6 (P2) → US5 (P3)
- **Polish (Phase 9)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - MVP foundation for mobile cards
- **User Story 2 (P1)**: Can start after US1 - Builds on card component for selection/expansion
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Independent chart migration
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Adds bottom sheet pattern for filters
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - Offline enhancement
- **User Story 6 (P2)**: Can start after Foundational (Phase 2) - Cross-cutting accessibility improvements

### Within Each User Story

- Tasks marked [P] within a user story can run in parallel (different files)
- Non-parallel tasks must run sequentially within the story
- Complete all tasks in a user story before testing independently

### Parallel Opportunities

- All Setup tasks (T001-T009) can run in parallel
- All Foundational CSS tasks (T010-T013) can run in parallel
- All Foundational component tasks (T014-T016, T020-T021) can run in parallel
- All Foundational hooks (T017-T019) can run in parallel
- Within US1: T025-T027 can run in parallel
- Within US2: T035-T036 can run in parallel
- Within US3: T046-T048 can run in parallel
- Within US4: T057-T058 can run in parallel
- Within US5: T068-T070 can run in parallel
- Within US6: T082-T085 can run in parallel
- Within Polish: T095-T096, T099, T102, T106-T107, T114 can run in parallel

---

## Implementation Strategy

### MVP First (User Stories 1 + 2 - Both P1)

1. Complete Phase 1: Setup (T001-T009)
2. Complete Phase 2: Foundational (T010-T024) - CRITICAL
3. Complete Phase 3: User Story 1 (T025-T034)
4. **VALIDATE**: Test mobile dashboard independently on 375px viewport
5. Complete Phase 4: User Story 2 (T035-T045)
6. **VALIDATE**: Test repository comparison with touch gestures
7. Deploy/demo MVP with mobile dashboard and comparison

### Incremental Delivery (Recommended Order)

1. **Foundation**: Setup + Foundational → Base ready
2. **MVP**: US1 + US2 → Mobile dashboard + comparison → Deploy
3. **Enhancement 1**: US3 → Charts migration → Deploy
4. **Enhancement 2**: US4 → Bottom sheets → Deploy
5. **Enhancement 3**: US6 → Accessibility → Deploy
6. **Enhancement 4**: US5 → Offline support → Deploy
7. **Polish**: Phase 9 → Production ready → Final deploy

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T024)
2. Once Foundational is done:
   - Developer A: User Story 1 (T025-T034)
   - Developer B: User Story 3 (T046-T056) - Independent charts work
   - Developer C: User Story 4 (T057-T067) - Independent bottom sheets
3. After US1 complete:
   - Developer A: User Story 2 (T035-T045) - Builds on US1
4. Stories complete and integrate independently

---

## Notes

- **[P] tasks**: Different files, no dependencies - can run in parallel
- **[Story] label**: Maps task to specific user story (US1-US6) for traceability
- **File paths**: All paths are absolute starting from `C:\GitHub\MarkHazleton\github-stats-spark\`
- **Tests**: OPTIONAL - not included per feature specification requirements
- **Python backend**: `src/` directory is UNCHANGED - all changes in `frontend/` only
- **Bundle size**: Monitor closely - approaching 170KB limit with new dependencies
- **Chart.js migration**: Critical for bundle size savings (26-29KB reduction vs Recharts)
- **Each user story**: Should be independently completable and testable
- **Commit strategy**: Commit after each task or logical group for better git history
- **Stop at checkpoints**: Validate each user story independently before proceeding
- **Performance**: Run Lighthouse CI (T111) after completing user stories to catch regressions early
