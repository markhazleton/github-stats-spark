# Implementation Plan: Mobile-First Front-End Redesign

**Branch**: `001-mobile-first-redesign` | **Date**: 2026-01-03 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/docs/spec/001-mobile-first-redesign/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Transform the GitHub Stats Spark dashboard into a mobile-first web application using modern responsive design patterns, touch-optimized interactions, and progressive enhancement. The redesign will implement bottom sheet navigation, card-based layouts, swipe gestures, and offline caching while maintaining the existing React 19 + Vite architecture. Primary focus is on 320px-768px viewports with progressive enhancement for desktop, achieving <5s Time to Interactive on 3G connections and Lighthouse mobile scores of 90+ for Performance and 95+ for Accessibility.

## Technical Context

**Language/Version**: JavaScript (ES2022+), React 19.2.3
**Primary Dependencies**: React 19.2.3, React DOM 19.2.3, Recharts 3.6.0, Vite 7.3.0
**Storage**: IndexedDB for offline cache (7-day retention), LocalStorage for preferences
**Testing**: Vitest 4.0.16 (unit), Lighthouse CI (performance), manual device testing
**Target Platform**: Modern mobile browsers (iOS Safari 13+, Chrome for Android 90+, Samsung Internet 14+)
**Project Type**: Web application (frontend-only, SPA with static data files)
**Performance Goals**: First Contentful Paint <2s (3G), Time to Interactive <5s (3G), Lighthouse Performance >90, Lighthouse Accessibility >95
**Constraints**: Bundle size <170KB JS gzipped + <50KB CSS gzipped, CLS <0.1, 44x44px minimum touch targets, no horizontal scroll 320px-768px
**Scale/Scope**: Single-user dashboard, ~20 components, ~5 routes/views, progressive enhancement from mobile to desktop

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Alignment Assessment**:

- ✅ **Python-First (I)**: N/A - This is a frontend-only feature; Python backend unchanged
- ✅ **CLI Interface (II)**: N/A - Frontend changes don't affect CLI; `spark generate` continues to work
- ✅ **Data Privacy (III)**: PASS - No changes to data handling; all data remains public GitHub stats only
- ✅ **Testability (IV)**: PASS - Will add Vitest unit tests for mobile components, Lighthouse CI for performance
- ✅ **Observable (V)**: PASS - Console errors/warnings logging as specified; no silent failures
- ✅ **Performance Standards**: PASS - Performance budgets aligned with spec (170KB JS, 50KB CSS, <5s TTI)
- ✅ **Configuration**: N/A - Frontend doesn't use `config/spark.yml`; theme customization to be evaluated in research phase

**Gate Status**: ✅ PASS - No constitutional violations. Mobile-first redesign is frontend-only and doesn't affect Python core principles, data privacy, or CLI functionality.

## Project Structure

### Documentation (this feature)

```text
docs/spec/001-mobile-first-redesign/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
frontend/
├── src/
│   ├── components/
│   │   ├── Common/              # Existing: shared components
│   │   ├── Comparison/          # Existing: repository comparison
│   │   ├── DrillDown/           # Existing: detail views
│   │   ├── RepositoryTable/     # Existing: table component (to be refactored)
│   │   ├── Visualizations/      # Existing: charts
│   │   ├── Mobile/              # NEW: mobile-specific components
│   │   │   ├── BottomSheet/     # Bottom sheet pattern
│   │   │   ├── TabBar/          # Fixed bottom navigation
│   │   │   ├── RepositoryCard/  # Mobile card layout
│   │   │   ├── GestureHandler/  # Touch/swipe gestures
│   │   │   ├── EmptyState/      # Empty state component
│   │   │   └── TouchTarget/     # Touch-optimized button wrapper
│   │   └── Layout/              # NEW: responsive layout components
│   │       ├── Container/       # Mobile-first container
│   │       ├── Stack/           # Vertical/horizontal stack
│   │       └── SafeArea/        # Safe area insets handler
│   ├── hooks/
│   │   ├── useGesture.js        # NEW: gesture detection hook
│   │   ├── useBottomSheet.js    # NEW: bottom sheet state
│   │   ├── useOfflineCache.js   # NEW: IndexedDB offline cache
│   │   ├── useMediaQuery.js     # NEW: viewport breakpoint hook
│   │   └── useNetworkStatus.js  # NEW: Network Information API
│   ├── services/
│   │   ├── offlineStorage.js    # NEW: IndexedDB wrapper
│   │   ├── serviceWorker.js     # NEW: SW registration
│   │   └── dataService.js       # Existing: data loading (to be enhanced)
│   ├── styles/
│   │   ├── mobile/              # NEW: mobile-first styles
│   │   │   ├── breakpoints.css  # Viewport breakpoints
│   │   │   ├── touch.css        # Touch target styles
│   │   │   ├── gestures.css     # Gesture feedback
│   │   │   └── safe-area.css    # Safe area insets
│   │   └── themes/              # Existing: theme variables
│   ├── App.jsx                  # Existing: main app (to be enhanced)
│   └── main.jsx                 # Existing: entry point
├── tests/
│   ├── unit/
│   │   ├── components/
│   │   │   └── Mobile/          # NEW: mobile component tests
│   │   └── hooks/               # NEW: hook tests
│   └── setup.js                 # Existing: test setup
├── public/
│   └── sw.js                    # NEW: service worker file
├── index.html                   # Existing: HTML entry (to be enhanced)
├── vite.config.js               # Existing: Vite config (to be enhanced)
├── package.json                 # Existing: dependencies (to be updated)
└── .lighthouserc.json           # NEW: Lighthouse CI config

src/                             # Backend (Python) - UNCHANGED
└── spark/                       # Existing Python modules
```

**Structure Decision**: Web application structure (Option 2 equivalent). The repository has a clear frontend/backend separation with `frontend/` containing the React SPA and `src/` containing Python backend. This mobile-first redesign focuses exclusively on `frontend/` directory enhancements while leaving backend unchanged. New mobile-specific components will be organized under `frontend/src/components/Mobile/` and `frontend/src/components/Layout/` with supporting hooks and services.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations - this section intentionally left empty. Constitution check passed without issues.

---

## Post-Design Constitution Re-Check

**Date**: 2026-01-03 | **Phase**: After Phase 1 Design Completion

### Design Artifacts Review

**Generated Documents**:
- ✅ research.md - Technology decisions for 10 unknowns (bottom sheets, gestures, IndexedDB, service workers, charts, CSS features, APIs)
- ✅ data-model.md - 10 core entities with validation rules and state management architecture
- ✅ contracts/ - TypeScript interfaces for components, hooks, and services
- ✅ quickstart.md - Developer guide with patterns and examples

### Technology Stack Validation

**New Dependencies Added** (from research.md):
- `@use-gesture/react` (v10.3.1+) - 15-20KB - Touch gesture detection
- `react-modal-sheet` (v5.2.1+) - 30-40KB - Bottom sheet UI pattern
- `dexie.js` (v4.0+) - 26KB gzipped - IndexedDB wrapper for offline cache
- `chart.js` (v4.0+) - 11-14KB gzipped - Mobile-optimized charts (replaces Recharts, saves 26-29KB)
- `vite-plugin-pwa` (dev) - Service worker tooling
- `@lighthouse/cli` (dev) - Performance monitoring

**Total New Bundle Impact**: ~82-100KB (within 170KB budget, with 70-88KB remaining for app code)

### Constitution Compliance Re-Assessment

- ✅ **Python-First (I)**: PASS - Frontend changes don't affect Python backend modules (src/spark/ unchanged)
- ✅ **CLI Interface (II)**: PASS - `spark generate`, `spark preview`, `spark config` commands unaffected
- ✅ **Data Privacy (III)**: PASS - No changes to data handling; all data remains public GitHub stats from existing JSON files
- ✅ **Testability (IV)**: PASS - Vitest tests planned for mobile components, Lighthouse CI integrated for performance regression testing
- ✅ **Observable (V)**: PASS - Console errors/warnings only (FR-031), no silent failures, toast notifications for user feedback
- ✅ **Performance Standards**: PASS - Bundle budgets enforced (170KB JS, 50KB CSS), Lighthouse CI gates (<5s TTI, <2s FCP, 90+ Performance score)
- ✅ **Configuration**: PASS - Frontend doesn't modify `config/spark.yml`; uses LocalStorage for UI preferences only

### Dependency Justification

| Dependency | Why Needed | Simpler Alternative Rejected |
|------------|------------|------------------------------|
| `@use-gesture/react` | Industry-standard gesture library, 1.4M+ weekly downloads, modern React hooks API | Hammer.js (unmaintained since 2019), custom PointerEvent handlers (complex, error-prone) |
| `react-modal-sheet` | Accessible, performant bottom sheet with Framer Motion, mobile platform conventions | Custom implementation (2-3 weeks dev time, accessibility issues, iOS/Android quirks) |
| `dexie.js` | Advanced IndexedDB querying, efficient indexing, automatic 7-day cleanup | idb (too low-level, manual cleanup), localForage (limited querying, uses LocalStorage fallback) |
| `chart.js` | Canvas-based (faster on mobile), tree-shakeable, 26KB smaller than Recharts | Keep Recharts (40KB, slower SVG rendering on mobile, no touch optimization), Nivo (React-specific, larger bundle) |
| `vite-plugin-pwa` | Zero-config PWA, industry standard, automated precaching with Workbox | Custom service worker (weeks of dev time, cache strategy complexity, browser quirks) |

### Performance Budget Compliance

| Metric | Budget | Projected | Status |
|--------|--------|-----------|--------|
| JS Bundle (gzipped) | 170KB max | 82-100KB libraries + 70-88KB app code = 152-188KB | ⚠️ WARN - Monitor closely |
| CSS Bundle (gzipped) | 50KB max | ~35KB (mobile-first styles + themes) | ✅ PASS |
| First Contentful Paint | 2s max (3G) | 1.5s (critical CSS inline, Vite code-split) | ✅ PASS |
| Time to Interactive | 5s max (3G) | 4.2s (lazy loading, service worker precache) | ✅ PASS |
| Cumulative Layout Shift | 0.1 max | 0.06 (skeleton screens, reserved space) | ✅ PASS |

**Bundle Size Mitigation**:
- Chart.js tree-shaking saves 26-29KB vs Recharts
- Lazy load comparison and visualization routes (-30KB initial bundle)
- Service worker precache moves assets off critical path
- Monitor bundle size in CI with size-limit tool

### Architecture Decisions Alignment

**Mobile-First Approach**: ✅ Aligned
- CSS starts at 320px, progressively enhances to desktop
- Components designed for touch-first interaction
- Performance budgets target 3G connection speeds

**Progressive Enhancement**: ✅ Aligned
- Container queries with @supports fallback
- Network Information API with feature detection
- Vibration API (Android only, graceful iOS degradation)
- Service worker as enhancement (app works without offline)

**Accessibility**: ✅ Aligned
- WCAG 2.1 AA compliance (44px touch targets, 4.5:1 contrast)
- Screen reader support via ARIA labels
- Keyboard navigation
- Reduced motion support
- Focus trap for modals/bottom sheets

### Final Gate Status

**✅ PASS** - Mobile-first redesign design phase complete with no constitutional violations.

**Observations**:
1. Bundle size is approaching limit (projected 152-188KB vs 170KB budget) - requires monitoring during implementation
2. Migrating from Recharts to Chart.js provides 26-29KB savings critical for budget compliance
3. All new dependencies justify their inclusion with clear performance/DX benefits
4. Frontend-only changes maintain clean separation from Python backend
5. Performance budgets enforced via Lighthouse CI prevent regressions

**Recommendation**: Proceed to Phase 2 (task generation via `/speckit.tasks` command) with close monitoring of bundle size during implementation. Consider additional code-splitting if initial build exceeds 170KB JS budget.
