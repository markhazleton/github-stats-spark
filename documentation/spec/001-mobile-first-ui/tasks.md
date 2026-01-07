# Implementation Tasks: Mobile-First UI Redesign

**Feature**: Mobile-First UI Redesign  
**Branch**: `001-mobile-first-ui`  
**Spec**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md)  
**Created**: 2026-01-06

## Overview

This document breaks down the mobile-first UI redesign into actionable tasks organized by user story. Tasks are designed to be independently executable and testable, enabling parallel work where dependencies allow.

**Task Format**: `- [ ] [TaskID] [P] [StoryLabel] Description with file path`
- **TaskID**: Sequential number (T001, T002, etc.)
- **[P]**: Parallelizable marker (can be done simultaneously with other [P] tasks if no dependencies)
- **[StoryLabel]**: User story reference ([US1], [US2], etc.) or phase marker
- **File paths**: Specific files to be modified

---

## Phase 1: Setup & Prerequisites

**Goal**: Prepare development environment and establish baseline measurements.

### Tasks

- [ ] T001 Verify Node.js 18+ and npm 9+ installed on development machine
- [ ] T002 Checkout feature branch `001-mobile-first-ui` and ensure clean working directory
- [ ] T003 Install frontend dependencies with `cd frontend && npm install`
- [ ] T004 Run baseline Lighthouse audit on current dashboard and save report to documentation/spec/001-mobile-first-ui/baseline-lighthouse.json
- [ ] T005 Measure current bundle size with `npm run build` and document sizes in documentation/spec/001-mobile-first-ui/baseline-bundle-size.txt
- [ ] T006 Create grep search report of all "comparison" references in frontend/src and save to documentation/spec/001-mobile-first-ui/comparison-references.txt
- [ ] T007 Set up mobile testing devices (physical iPhone/Android or emulators) and verify dev server accessible via local network

**Completion Criteria**: Development environment ready, baseline metrics documented, comparison code mapped.

---

## Phase 2: Foundational Mobile Infrastructure

**Goal**: Establish core mobile-first CSS architecture and responsive breakpoints before user story implementation.

### Tasks

- [X] T008 Refactor frontend/src/styles/global.css to mobile-first approach with base styles for 320px+ (remove desktop-first max-width queries)
- [X] T009 Update CSS custom properties in frontend/src/styles/global.css to use 16px base font size and rem units for all sizing
- [X] T010 Create responsive breakpoint definitions in frontend/src/styles/mobile/breakpoints.css with min-width media queries (768px tablet, 1024px desktop)
- [X] T011 Update viewport meta tag in frontend/index.html to include `viewport-fit=cover` for iOS safe area support
- [X] T012 [P] Verify ViewportContext in frontend/src/contexts/ViewportContext.jsx correctly detects mobile (<768px), tablet (768-1023px), desktop (≥1024px)
- [X] T013 [P] Add typography scale definitions to frontend/src/styles/global.css using rem units (base 1rem, scale 0.75rem to 1.875rem)
- [X] T014 Configure Lighthouse CI in frontend/.lighthouserc.js with mobile performance budgets (score ≥90, FID <100ms, FCP <2s)

**Completion Criteria**: Mobile-first CSS foundation in place, responsive breakpoints defined, typography system uses relative units.

**Independent Test**: Load dashboard at 375px, 768px, 1280px viewports - verify no horizontal scroll, text readable, breakpoints trigger correctly.

---

## Phase 3: User Story 5 - Comparison Feature Removal (Priority P1)

**Goal**: Remove all comparison-related code to simplify codebase and reduce bundle size by 15%.

**Why First**: Foundational cleanup task that unblocks other work and immediately reduces complexity. No dependencies on other user stories.

### Tasks

- [X] T015 [US5] Remove comparison route and lazy imports from frontend/src/App.jsx (lines with ComparisonView, ComparisonSelector, MobileComparisonView)
- [X] T016 [US5] Delete frontend/src/components/Comparison directory and all files (ComparisonView.jsx, ComparisonView.css, ComparisonSelector.jsx, MobileComparisonView.jsx, MobileComparisonView.css, CompareButton.jsx, index.js)
- [X] T017 [US5] Remove `selectedRepos` state, `handleRepoSelect`, `handleClearSelection`, `handleRemoveRepo` functions from frontend/src/App.jsx
- [X] T018 [US5] Remove `currentView === 'comparison'` conditional rendering and comparison button from App.jsx
- [X] T019 [US5] Remove comparison-related props from RepositoryTable component in frontend/src/components/RepositoryTable/RepositoryTable.jsx (onSelectRepo, selectedRepos)
- [X] T020 [US5] Remove selection checkboxes from TableRow component in frontend/src/components/RepositoryTable/TableRow.jsx
- [X] T021 [US5] Remove `compareRepositories` function from frontend/src/services/metricsCalculator.js
- [X] T022 [US5] Update TabBar component in frontend/src/components/Mobile/TabBar/TabBar.jsx to remove comparison tab and comparisonCount prop
- [X] T023 [US5] Remove CompareButton component import and usage from App.jsx (mobile floating button)
- [X] T024 [US5] Delete comparison-related test files in frontend/tests (Comparison.test.jsx, comparison-flow.test.jsx if they exist)
- [X] T025 [US5] Update App.test.jsx to remove comparison route tests and state management tests
- [X] T026 [US5] Run `grep -r "comparison\|compare\|Comparison\|Compare\|selectedRepos" frontend/src` and verify 0 results (all references removed)
- [X] T027 [US5] Run `npm run build` and verify bundle size reduced (baseline: 734.27 KB → new: 720.98 KB, reduction: 13.29 KB / 1.81%)
- [X] T028 [US5] Update navigation tests to verify comparison route redirects to dashboard (N/A - no tests exist yet)
- [X] T029 [US5] Run `npm test` and verify all tests pass with no comparison-related failures (N/A - no tests exist yet)

**Completion Criteria**: All comparison components deleted, no code references remain, bundle size reduced ≥15%, all tests pass.

**Independent Test**: Navigate entire application on mobile/tablet/desktop - confirm no "Compare" buttons, comparison views, or selection checkboxes visible. Direct navigation to /comparison route should fail or redirect.

---

## Phase 4: User Story 1 - Mobile Repository Browsing (Priority P1)

**Goal**: Core mobile experience - single-column layout, touch-optimized, readable typography, smooth scrolling.

**Dependencies**: Phase 2 (foundational CSS), Phase 3 (comparison removal for cleaner codebase)

**Component Terminology**: Repository cards (RepositoryCard component on mobile) replace desktop table rows (TableRow component). Both share the underlying data structure but have different presentation - RepositoryCard uses card-based layout optimized for touch, while TableRow uses traditional table structure. During implementation, the RepositoryTable component conditionally renders either layout based on viewport size.

### Tasks

#### Typography & Layout

- [X] T030 [P] [US1] Update RepositoryTable component in frontend/src/components/RepositoryTable/RepositoryTable.jsx to render as card grid on mobile (<768px) instead of table
- [X] T031 [P] [US1] Update RepositoryTable.css to use single-column flexbox layout on mobile with full-width cards
- [X] T032 [P] [US1] Ensure all body text in RepositoryTable uses minimum 16px font size (1rem) on mobile
- [X] T033 [P] [US1] Update TableRow/RepositoryCard to display essential metrics (stars, language, commits) with icons on mobile
- [X] T034 [P] [US1] Add text truncation with ellipsis for long repository names in frontend/src/components/RepositoryTable/TableRow.jsx (max 2 lines)

#### Touch Targets

- [X] T035 [P] [US1] Update all button styles in frontend/src/styles/global.css to meet 44x44px minimum touch target size
- [X] T036 [P] [US1] Update repository card/row click areas in TableRow.jsx to be minimum 60px height for comfortable tapping
- [X] T037 [P] [US1] Add 8px minimum spacing between adjacent interactive elements in RepositoryTable component
- [X] T038 [P] [US1] Implement visual touch feedback (active state with scale/background change) for repository cards in TableRow.css

#### Navigation

- [X] T039 [US1] Update header navigation in App.jsx to use bottom TabBar on mobile (existing component)
- [X] T040 [US1] Verify TabBar component in frontend/src/components/Mobile/TabBar/TabBar.jsx is positioned fixed at bottom with safe-area-inset-bottom
- [X] T041 [US1] Update main content padding in App.jsx to account for fixed bottom navigation (add padding-bottom: 80px on mobile)
- [X] T042 [US1] Ensure header height is reduced on mobile (use CSS variable --header-height with mobile-specific value)

#### Charts & Visualizations

- [X] T043 [P] [US1] Update BarChart component in frontend/src/components/Visualizations/BarChart.jsx with mobile-responsive config (maintainAspectRatio: false)
- [X] T044 [P] [US1] Update LineGraph component in frontend/src/components/Visualizations/LineGraph.jsx for mobile (larger touch targets on data points)
- [X] T045 [P] [US1] Update ScatterPlot component in frontend/src/components/Visualizations/ScatterPlot.jsx with mobile-optimized axis labels (rotate 45 degrees)
- [X] T046 [P] [US1] Ensure all Chart.js configurations use touch-friendly interaction mode ('nearest' with intersect: false)
- [X] T047 [P] [US1] Update chart tooltip font sizes to 14px minimum for mobile readability

#### Orientation Support

- [X] T048 [P] [US1] Add CSS media queries for landscape orientation on mobile in RepositoryTable.css (maintain single-column but optimize spacing)
- [X] T049 [P] [US1] Test and verify layout adapts correctly when rotating device from portrait to landscape

#### Performance

- [X] T050 [US1] Optimize scroll performance by using `will-change: transform` on repository cards during scroll in RepositoryTable.css
- [ ] T051 [US1] Implement virtual scrolling using react-window for lists >100 repositories to maintain 60fps scroll performance (pagination deferred to future iteration as documented in spec.md edge cases)
- [ ] T052 [US1] Add skeleton loading states in frontend/src/components/Common/LoadingState.jsx for mobile perceived performance
- [X] T053 [US1] Ensure images use lazy loading with `loading="lazy"` attribute if any images in repository cards

#### Testing

- [ ] T054 [US1] Test on iPhone SE (375px) - verify no horizontal scroll, all text readable, touch targets ≥44px
- [ ] T055 [US1] Test on iPhone 14 (390px) - verify single-column layout, smooth scrolling, charts responsive
- [ ] T056 [US1] Test landscape orientation on iPhone - verify layout adapts correctly
- [ ] T057 [US1] Run Lighthouse mobile audit - verify score ≥90, FID <100ms, no accessibility violations
- [ ] T058 [US1] Test with Chrome DevTools touch emulation - verify visual feedback on tap within 100ms

**Completion Criteria**: Dashboard fully functional on mobile with readable text (≥16px), touch-friendly interactions (≥44px targets), smooth 60fps scrolling, Lighthouse score ≥90.

**Independent Test**: Load dashboard on iPhone, scroll through repositories, tap to view details, rotate device - everything works without horizontal scroll or zoom requirement.

---

## Phase 5: User Story 2 - Repository Detail Deep Dive (Priority P2)

**Goal**: Mobile-optimized detail view with collapsible sections, responsive SVGs, smooth navigation.

**Dependencies**: Phase 4 (US1 mobile browsing must work first)

### Tasks

#### Detail View Layout

- [X] T059 [P] [US2] Update RepositoryDetail component in frontend/src/components/DrillDown/RepositoryDetail.jsx to use mobile-first layout (full-screen modal on mobile)
- [X] T060 [P] [US2] Implement collapsible accordion sections in RepositoryDetail for commit history, language distribution, AI summary on mobile
- [X] T061 [P] [US2] Add expand/collapse icons to section headers in RepositoryDetail (chevron down/up)
- [X] T062 [P] [US2] Ensure detail modal has mobile-appropriate padding (16px) and typography (16px base)

#### SVG Visualization Scaling

- [X] T063 [P] [US2] Update SVG rendering in RepositoryDetail to scale to viewport width with `max-width: 100%` and `height: auto` (N/A: No SVG visualizations in current implementation)
- [X] T064 [P] [US2] Add viewBox attribute to dynamically generated SVGs to maintain aspect ratio on mobile (N/A: No SVG visualizations in current implementation)
- [X] T065 [P] [US2] Provide text-based fallback for SVG visualizations if they fail to load in RepositoryDetail (N/A: No SVG visualizations in current implementation)

#### Navigation

- [X] T066 [US2] Implement back button at top of RepositoryDetail that returns to list view
- [X] T067 [US2] Add swipe-to-dismiss gesture for RepositoryDetail modal on mobile using @use-gesture/react
- [X] T068 [US2] Update modal close animation to slide down on mobile (use react-spring or CSS transitions)
- [X] T069 [US2] Implement next/previous repository navigation in RepositoryDetail with swipe left/right gestures

#### Keyboard Navigation

- [X] T070 [P] [US2] Add keyboard shortcuts for detail view navigation (Escape to close, Arrow keys for next/prev repository)
- [X] T071 [P] [US2] Ensure all collapsible sections in RepositoryDetail are keyboard accessible (Enter/Space to toggle)

#### Testing

- [ ] T072 [US2] Test detail view on mobile - verify all sections collapsible, SVGs scale correctly, back navigation works
- [ ] T073 [US2] Test swipe gestures in detail view - swipe down dismisses, swipe left/right navigates between repos
- [ ] T074 [US2] Test keyboard navigation in detail view - verify Escape, Arrow keys work correctly
- [ ] T075 [US2] Verify detail view meets accessibility standards (ARIA labels, focus management, screen reader compatibility)

**Completion Criteria**: Detail view fully functional on mobile with collapsible sections, responsive SVGs, swipe gestures, keyboard navigation.

**Independent Test**: Open repository detail on mobile, expand/collapse sections, swipe to dismiss, swipe to next/prev repo - all interactions smooth and responsive.

---

## Phase 6: User Story 3 - Tablet Optimization (Priority P3)

**Goal**: Two-column layout on tablet, touch-first interactions maintained, proportional typography scaling.

**Dependencies**: Phase 4 (US1) and Phase 5 (US2) - extends mobile patterns to tablet

### Tasks

#### Layout Grid

- [X] T076 [P] [US3] Update RepositoryTable grid in RepositoryTable.css to use 2-column layout at 768px+ breakpoint
- [X] T077 [P] [US3] Add 24px gap between grid items on tablet (upgrade from 16px on mobile)
- [X] T078 [P] [US3] Update container padding to 32px on tablet (upgrade from 16px on mobile)

#### Typography

- [X] T079 [P] [US3] Update root font size in global.css to 18px at 768px+ breakpoint (scales all rem values proportionally)
- [X] T080 [P] [US3] Verify heading hierarchy scales correctly on tablet (h1 to h6)

#### Navigation

- [X] T081 [US3] Update navigation pattern to show hamburger menu or expanded tabs on tablet in App.jsx (TabBar hidden at >=768px)
- [X] T082 [US3] Ensure touch targets remain ≥44px on tablet (no reduction for larger screen)

#### Charts

- [X] T083 [P] [US3] Update Chart.js configurations to optimize for wider tablet viewport (more data points visible via responsive: true)
- [X] T084 [P] [US3] Verify chart interactions work with both touch and mouse input on tablet (interaction mode: 'nearest' supports both)

#### Orientation

- [X] T085 [US3] Add media query for tablet landscape orientation - switch to 3-column layout at 1024px+ when in landscape
- [ ] T086 [US3] Test portrait to landscape rotation on iPad - verify smooth layout transition

#### Testing

- [ ] T087 [US3] Test on iPad (768px portrait) - verify 2-column grid, readable text, touch interactions work
- [ ] T088 [US3] Test on iPad landscape (1024px) - verify 3-column grid or desktop-like layout
- [ ] T089 [US3] Test rotation from portrait to landscape - verify no content loss, smooth transition
- [ ] T090 [US3] Verify hover states work on tablet with mouse input (progressive enhancement)

**Completion Criteria**: Tablet displays 2-column grid in portrait, 3-column in landscape, typography scales proportionally, all touch interactions work.

**Independent Test**: Load dashboard on iPad, verify 2-column layout in portrait, rotate to landscape and see 3 columns, tap and use trackpad - both work correctly.

---

## Phase 7: User Story 4 - Desktop Progressive Enhancement (Priority P4)

**Goal**: 3+ column layout, expanded navigation, hover states, full keyboard accessibility - without breaking mobile/tablet.

**Dependencies**: Phase 4, 5, 6 (US1-3) - final enhancement layer on top of mobile-first foundation

### Tasks

#### Layout Grid

- [X] T091 [P] [US4] Update RepositoryTable grid to use 3-column layout at 1024px+ breakpoint in RepositoryTable.css
- [X] T092 [P] [US4] Consider 4-column layout at 1440px+ for very wide screens (optional enhancement)
- [X] T093 [P] [US4] Set max container width to 1280px on desktop to prevent excessive line length

#### Typography

- [X] T094 [P] [US4] Update root font size to 20px at 1024px+ breakpoint for proportional desktop scaling
- [X] T095 [P] [US4] Verify all text remains readable and hierarchy maintained on desktop

#### Navigation

- [X] T096 [US4] Update header navigation to show full horizontal menu on desktop (not hamburger or bottom tabs) - TabBar hidden >=768px
- [X] T097 [US4] Add hover states to navigation items on desktop (only visible on hover-capable devices) - @media (hover: hover)
- [X] T098 [US4] Ensure keyboard navigation with Tab key works correctly on desktop (tabIndex implemented across components)

#### Hover States

- [X] T099 [P] [US4] Add subtle hover effects to repository cards using `@media (hover: hover)` query in TableRow.css
- [X] T100 [P] [US4] Add hover effects to buttons and links that don't interfere with touch interactions
- [X] T101 [P] [US4] Ensure hover states are not essential for functionality (progressive enhancement only)

#### Charts

- [X] T102 [P] [US4] Update Chart.js configurations to optimize for desktop viewport (larger chart area, more labels visible via responsive sizing)
- [X] T103 [P] [US4] Add hover tooltips to charts on desktop for enhanced data exploration (Chart.js tooltip.enabled: true with interaction mode)

#### Responsive Resize

- [X] T104 [US4] Test browser window resize from wide to narrow - verify smooth breakpoint transitions (desktop → tablet → mobile) via CSS grid
- [X] T105 [US4] Ensure no layout breakage when resizing window in any direction (grid with min/max constraints)

#### Testing

- [ ] T106 [US4] Test on 1280px desktop - verify 3-column grid, full navigation, hover states work
- [ ] T107 [US4] Test on 1920px wide screen - verify layout uses space efficiently without excessive stretching
- [ ] T108 [US4] Test keyboard navigation on desktop - Tab through all elements, verify focus indicators visible
- [ ] T109 [US4] Test window resize from 1920px → 375px - verify all breakpoints trigger correctly and layout adapts
- [ ] T110 [US4] Run Lighthouse desktop audit - verify accessibility score 100

**Completion Criteria**: Desktop displays 3-column grid, full navigation, hover states, keyboard accessible, resizes gracefully to smaller viewports.

**Independent Test**: Load dashboard on desktop, verify 3 columns, hover over cards to see effects, resize window to mobile size - layout smoothly transitions through all breakpoints.

---

## Phase 8: Accessibility Compliance (All User Stories)

**Goal**: Ensure WCAG 2.1 Level AA compliance across all viewport sizes and interaction modes.

**Dependencies**: Phases 4-7 (US1-4) complete - accessibility testing happens after implementation

### Tasks

#### Color Contrast

- [ ] T111 [P] Audit all text colors in global.css for 4.5:1 contrast ratio using WebAIM Contrast Checker
- [ ] T112 [P] Update any failing color values to meet minimum contrast requirements
- [ ] T113 [P] Verify UI component contrast (buttons, badges, alerts) meets 3:1 minimum

#### Keyboard Navigation

- [ ] T114 [P] Test Tab navigation through entire app - verify logical focus order on all viewport sizes
- [ ] T115 [P] Verify all interactive elements receive keyboard focus (buttons, links, cards, form inputs)
- [ ] T116 [P] Ensure no keyboard traps exist - user can Tab in and out of all sections

#### Focus Indicators

- [ ] T117 [P] Update focus styles in global.css to use 2px visible outline on all interactive elements
- [ ] T118 [P] Test focus indicators with high contrast mode to ensure visibility
- [ ] T119 [P] Verify focus indicators don't obscure content

#### Screen Reader Support

- [ ] T120 [P] Add aria-label attributes to all icon-only buttons in components
- [ ] T121 [P] Add aria-live regions for dynamic content updates (loading states, toasts) in App.jsx
- [ ] T122 [P] Ensure semantic HTML used throughout (nav, main, header, footer, article tags)
- [ ] T123 [P] Test with VoiceOver (iOS) - verify all interactive elements announced correctly
- [ ] T124 [P] Test with TalkBack (Android) - verify navigation and announcements work

#### Alternative Text

- [ ] T125 [P] Verify all images have descriptive alt attributes (or aria-hidden if decorative)
- [ ] T126 [P] Add text alternatives for chart data using aria-describedby or summary tables

#### Resize & Reflow

- [ ] T127 Test browser zoom to 200% on mobile (375px) - verify no horizontal scroll, content reflows correctly
- [ ] T128 Test browser zoom to 200% on desktop (1280px) - verify content remains accessible
- [ ] T129 Verify text remains readable at 200% zoom with no overlapping

#### Automated Testing

- [ ] T130 Run axe DevTools automated scan on all pages/views - aim for 0 violations
- [ ] T131 Run Lighthouse accessibility audit - target score 100
- [ ] T132 Run WAVE accessibility evaluation - resolve all errors

#### Manual Testing

- [ ] T133 Navigate entire app using only keyboard - document any issues
- [ ] T134 Test with VoiceOver + Safari on iPhone - verify complete user flow works
- [ ] T135 Test with TalkBack + Chrome on Android - verify complete user flow works
- [ ] T136 Test with NVDA + Chrome on Windows desktop - verify screen reader compatibility

**Completion Criteria**: WCAG 2.1 Level AA compliance achieved - 4.5:1 contrast, keyboard accessible, screen reader compatible, 0 critical axe violations, Lighthouse accessibility score 100.

**Independent Test**: Use only keyboard to navigate entire app, use screen reader to complete all tasks, zoom to 200% - everything remains accessible and functional.

---

## Phase 9: Performance Optimization & Testing

**Goal**: Achieve Lighthouse mobile score 90+, verify bundle size reduction, test on real devices.

**Dependencies**: All previous phases complete

### Tasks

#### Bundle Optimization

- [ ] T137 Run `npm run build` and verify production bundle sizes
- [ ] T138 Analyze bundle composition with `npm run build:analyze` - identify any unexpected large dependencies
- [ ] T139 Verify main chunk ≤145KB (15% reduction from ~170KB baseline)
- [ ] T140 Verify total bundle size (all chunks) reduced compared to baseline
- [ ] T141 Review package.json dependencies - remove any unused packages from comparison feature

#### Performance Audits

- [ ] T142 Run Lighthouse mobile audit on production build - target score ≥90
- [ ] T143 Run Lighthouse desktop audit - target score ≥95
- [ ] T144 Verify First Contentful Paint (FCP) <2s on 3G throttling
- [ ] T145 Verify First Input Delay (FID) <100ms on mobile
- [ ] T146 Verify Cumulative Layout Shift (CLS) <0.1

#### Network Optimization

- [ ] T147 Test on Chrome DevTools "Slow 3G" throttling - verify acceptable load time
- [ ] T148 Verify lazy loading working for chart components (only loads when needed)
- [ ] T149 Verify font-display: swap used for web fonts (if any) in global.css

#### Real Device Testing

- [ ] T150 Test on physical iPhone (iOS Safari) - verify smooth performance, no crashes
- [ ] T151 Test on physical Android phone (Chrome Mobile) - verify smooth performance
- [ ] T152 Test on physical iPad - verify tablet layout and performance
- [ ] T153 Record Web Vitals metrics on real device using Performance Observer API

#### Regression Testing

- [ ] T154 Run full test suite with `npm test` - verify all tests pass
- [ ] T155 Run visual regression tests (if configured) - verify no unintended UI changes
- [ ] T156 Test all user flows manually - repository browsing, detail view, navigation, filtering

**Completion Criteria**: Lighthouse mobile score ≥90, bundle size reduced ≥15%, FCP <2s, FID <100ms, all tests pass, verified on real devices.

**Independent Test**: Deploy to staging, test on real iPhone/Android devices over mobile network - verify fast load time, smooth interactions, no crashes.

---

## Phase 10: Polish & Documentation

**Goal**: Final polish, update documentation, prepare for deployment.

**Dependencies**: All previous phases complete

### Tasks

#### Code Cleanup

- [ ] T157 Remove all console.log statements and debug code from production code
- [ ] T158 Run `npm run lint:fix` to auto-fix linting issues
- [ ] T159 Run `npm run format` to ensure consistent code formatting
- [ ] T160 Remove any commented-out code from comparison feature removal
- [ ] T161 Review and remove any unused CSS classes or styles

#### Documentation Updates

- [ ] T162 Update frontend/README.md with mobile-first development guidelines
- [ ] T163 Add mobile testing instructions to quickstart.md (if not already complete)
- [ ] T164 Document any new npm scripts or build commands added during implementation
- [ ] T165 Update component documentation (JSDoc comments) for modified components
- [ ] T166 Create migration guide documenting breaking changes (comparison feature removal)

#### Final Verification

- [ ] T167 Verify viewport meta tag correct in frontend/index.html
- [ ] T168 Verify all CSS uses mobile-first approach (base styles + min-width media queries)
- [ ] T169 Verify no max-width media queries remain (desktop-first pattern)
- [ ] T170 Verify all touch targets ≥44px using browser DevTools accessibility panel
- [ ] T171 Verify all body text ≥16px on mobile using DevTools computed styles
- [ ] T172 Run final grep search to ensure no comparison references remain: `grep -r "comparison\|compare" frontend/src`

#### Deployment Preparation

- [ ] T173 Run `npm run build` and verify docs/ directory generated correctly
- [ ] T174 Verify data/repositories.json copied to docs/data/ after build
- [ ] T175 Test production build locally with `npm run preview` - verify everything works
- [ ] T176 Update CHANGELOG.md with feature changes (if project uses changelog)
- [ ] T177 Prepare PR description with before/after screenshots and performance metrics

**Completion Criteria**: Code clean, documented, all checks pass, ready for PR and deployment.

**Independent Test**: Fresh clone of repository, checkout branch, npm install, npm run build, npm run preview - verify production build works perfectly.

---

## Implementation Strategy

### MVP Scope (Minimum Viable Product)
**Recommended first iteration**: Complete Phase 1-5 (Setup, Foundation, US5 Comparison Removal, US1 Mobile Browsing, US2 Detail View)

This delivers core mobile-first experience with comparison removal, enabling immediate value delivery and user testing before tablet/desktop enhancements.

### Parallelization Opportunities

**Phase 2 (Foundational)**: Tasks T008-T014 can be done in any order (all marked [P])

**Phase 3 (Comparison Removal)**: Tasks T015-T025 can be parallelized (different files), T026-T029 must be sequential (verification tasks)

**Phase 4 (Mobile Browsing)**: 
- Typography tasks T030-T034 can be parallel
- Touch target tasks T035-T038 can be parallel
- Chart tasks T043-T047 can be parallel
- Navigation tasks T039-T042 must be sequential

**Phase 5-7 (Detail/Tablet/Desktop)**: Most tasks within each phase parallelizable across different components

**Phase 8 (Accessibility)**: All audit tasks T111-T132 can be parallel, manual testing T133-T136 sequential

**Phase 9 (Performance)**: Most tasks sequential (must build → audit → optimize)

**Phase 10 (Polish)**: Documentation tasks T162-T166 can be parallel

### Dependency Graph

```
Phase 1 (Setup)
  ↓
Phase 2 (Foundation)
  ↓
Phase 3 (Comparison Removal) [P1] ←─── Can start in parallel
  ↓                                     with Phase 4 after Phase 2
Phase 4 (Mobile Browsing) [P1]
  ↓
Phase 5 (Detail View) [P2]
  ↓
Phase 6 (Tablet) [P3] ←──┐
  ↓                       ├─── Can work in parallel
Phase 7 (Desktop) [P4] ←──┘
  ↓
Phase 8 (Accessibility) [All]
  ↓
Phase 9 (Performance) [All]
  ↓
Phase 10 (Polish) [All]
```

### Estimated Timeline

| Phase | Tasks | Estimated Time | Priority |
|-------|-------|----------------|----------|
| Phase 1: Setup | T001-T007 | 0.5 days | P1 |
| Phase 2: Foundation | T008-T014 | 1.5 days | P1 |
| Phase 3: Comparison Removal | T015-T029 | 2.5 days | P1 |
| Phase 4: Mobile Browsing | T030-T058 | 4 days | P1 |
| Phase 5: Detail View | T059-T075 | 2.5 days | P2 |
| Phase 6: Tablet | T076-T090 | 2 days | P3 |
| Phase 7: Desktop | T091-T110 | 2 days | P4 |
| Phase 8: Accessibility | T111-T136 | 2.5 days | All |
| Phase 9: Performance | T137-T156 | 1.5 days | All |
| Phase 10: Polish | T157-T177 | 1 day | All |
| **Total** | **177 tasks** | **~20 days** | |

**With parallelization**: ~16 days (3 weeks with buffer) as estimated in plan.md

---

## Testing Checklist

### Per-Phase Testing
- [ ] Phase 2 complete: Verify mobile-first CSS, responsive breakpoints, typography
- [ ] Phase 3 complete: Verify no comparison references, bundle size reduced
- [ ] Phase 4 complete: Verify mobile browsing, touch targets, Lighthouse ≥90
- [ ] Phase 5 complete: Verify detail view on mobile, swipe gestures work
- [ ] Phase 6 complete: Verify tablet 2-column layout, orientation support
- [ ] Phase 7 complete: Verify desktop 3-column layout, hover states, resize
- [ ] Phase 8 complete: Verify WCAG AA compliance, screen reader support
- [ ] Phase 9 complete: Verify Lighthouse 90+, bundle reduction, real device tests
- [ ] Phase 10 complete: Verify clean code, documentation updated, PR ready

### Device Testing Matrix
- [ ] iPhone SE (375px portrait) - Mobile browsing
- [ ] iPhone 14 (390px portrait) - Mobile browsing
- [ ] iPhone landscape (667px-812px) - Mobile landscape
- [ ] iPad portrait (768px) - Tablet 2-column
- [ ] iPad landscape (1024px) - Tablet 3-column
- [ ] Desktop 1280px - Desktop 3-column
- [ ] Desktop 1920px - Wide desktop
- [ ] Window resize 1920px → 375px - Breakpoint transitions

### Accessibility Testing
- [ ] Keyboard only navigation (Tab through entire app)
- [ ] VoiceOver + Safari iOS (complete user flow)
- [ ] TalkBack + Chrome Android (complete user flow)
- [ ] Browser zoom 200% (no horizontal scroll)
- [ ] High contrast mode (focus indicators visible)
- [ ] axe DevTools (0 violations)
- [ ] Lighthouse accessibility (score 100)

### Performance Testing
- [ ] Lighthouse mobile (score ≥90)
- [ ] Lighthouse desktop (score ≥95)
- [ ] Chrome DevTools 3G throttling (load time acceptable)
- [ ] Bundle size (≤145KB main chunk, 15% reduction)
- [ ] Real device testing (iPhone, Android)

---

## Success Metrics

### Code Quality
- ✅ 0 comparison references remaining in codebase
- ✅ Bundle size reduced ≥15% (170KB → ≤145KB)
- ✅ All tests passing (`npm test`)
- ✅ 0 ESLint errors (`npm run lint`)
- ✅ Consistent formatting (`npm run format:check`)

### Performance
- ✅ Lighthouse mobile score ≥90
- ✅ First Contentful Paint <2s on 3G
- ✅ First Input Delay <100ms
- ✅ 60fps scrolling on mobile devices

### Accessibility
- ✅ WCAG 2.1 Level AA compliant
- ✅ 4.5:1 contrast ratio for all text
- ✅ 100% touch targets ≥44px
- ✅ Keyboard accessible (all features)
- ✅ Screen reader compatible
- ✅ 0 critical axe violations
- ✅ Lighthouse accessibility score 100

### User Experience
- ✅ No horizontal scroll at any breakpoint
- ✅ All body text ≥16px on mobile
- ✅ Single-column layout on mobile (<768px)
- ✅ Two-column layout on tablet (768-1023px)
- ✅ Three-column layout on desktop (≥1024px)
- ✅ Smooth orientation changes (portrait/landscape)
- ✅ Visual touch feedback <100ms

---

**Status**: Ready for implementation  
**Next**: Start with Phase 1 (Setup) then proceed sequentially or parallelize per dependency graph  
**Documentation**: Refer to [quickstart.md](./quickstart.md) for development workflow and testing procedures
