# Research: Mobile-First UI Redesign Best Practices

**Date**: 2026-01-06  
**Feature**: [spec.md](./spec.md)  
**Purpose**: Research findings to resolve unknowns and guide Phase 1 design decisions

## 1. Mobile-First CSS Architecture

### Decision
Structure CSS using mobile-first approach with min-width media queries starting from 320px base, scaling through breakpoints: mobile (320-767px), tablet (768-1023px), desktop (1024px+).

### Rationale
- **Mobile-first is content-first**: Forces prioritization of essential content, naturally creates better UX
- **Performance advantage**: Mobile styles loaded by default, larger viewport styles only when needed (reduces CSS parse time on mobile)
- **Industry standard breakpoints** (based on StatCounter Global Stats 2025):
  - Mobile: <768px (covers 90%+ of smartphones including iPhone SE 375px to Pro Max 428px)
  - Tablet: 768-1023px (iPad 768px, iPad Pro 1024px)
  - Desktop: ≥1024px (covers all desktop/laptop resolutions)
- **Bootstrap 5 and Tailwind** use similar breakpoint values, ensuring familiarity for developers

### Alternatives Considered
- **Desktop-first with max-width queries**: Rejected - requires more CSS overrides for mobile, increases bundle size, slower mobile performance
- **Container queries**: Rejected for now - limited browser support in older iOS Safari versions (target is iOS 14+)

### Implementation Guidance
```css
/* Base mobile styles (320px+) - no media query needed */
.repository-card {
  padding: 16px;
  font-size: 16px; /* Prevents iOS zoom on focus */
}

/* Tablet (768px+) */
@media (min-width: 768px) {
  .repository-card {
    padding: 24px;
    font-size: 18px;
  }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .repository-card {
    padding: 32px;
  }
}
```

**Sources**: 
- MDN Web Docs: Responsive Design Basics
- Google Web Fundamentals: Mobile First Design
- WCAG 2.1 Guidelines Section 1.4.4 (Resize Text)

---

## 2. Touch Target Sizing Standards

### Decision
Implement 44x44px minimum touch target size for all interactive elements (buttons, links, form inputs, cards) per WCAG 2.1 Level AA Success Criterion 2.5.5.

### Rationale
- **WCAG 2.1 Level AA requirement**: Minimum 44x44 CSS pixels for all targets except inline text links
- **Apple Human Interface Guidelines**: 44pt (≈44px) minimum tap target size
- **Google Material Design**: 48dp (≈48px) recommended touch target
- **Biological basis**: Average adult finger pad is 10-14mm wide (≈45-57 CSS pixels at typical mobile DPI)
- **Accessibility**: Benefits users with motor impairments, tremors, or larger fingers

### Alternatives Considered
- **36x36px targets**: Rejected - fails WCAG 2.1 AA, too small for comfortable tapping
- **48x48px minimum**: Considered optimal but rejected for space constraints on small screens (44px is standards-compliant minimum)

### Implementation Guidance
```css
/* Touch target minimum sizing */
.btn, .link, .card-clickable {
  min-height: 44px;
  min-width: 44px;
  /* If visual size must be smaller, expand hit area with padding or pseudo-elements */
}

/* Expand hit area for small icons */
.icon-button {
  width: 24px; /* Visual size */
  height: 24px;
  padding: 10px; /* Expands to 44x44px total hit area */
}

/* Spacing between adjacent touch targets */
.button-group > * + * {
  margin-left: 8px; /* Minimum 8px gap prevents accidental taps */
}
```

**Testing**: Use Chrome DevTools mobile emulation + touch event overlay to visualize hit areas.

**Sources**:
- WCAG 2.1 Success Criterion 2.5.5 (Target Size)
- Apple HIG: Layout - iOS
- Google Material Design: Touch Targets

---

## 3. Mobile Typography Strategy

### Decision
Use 16px base font size on mobile with relative units (rem/em) for all typography, scaling proportionally across breakpoints. Line height 1.5 for body text, 1.25 for headings.

### Rationale
- **16px mobile minimum prevents browser zoom**: iOS Safari auto-zooms if input fields use <16px text, breaking layout
- **Relative units (rem) enable user scaling**: Respects user font size preferences, critical for accessibility
- **1rem = 16px at default**: Simplifies mental math (1.5rem = 24px, 0.875rem = 14px)
- **Line height 1.5 recommended by WCAG 2.1 AA**: Improves readability, especially on small screens where text wraps more frequently
- **Heading line height 1.25**: Tighter spacing acceptable for larger text, improves visual hierarchy

### Alternatives Considered
- **14px base**: Rejected - triggers iOS zoom, poor readability on mobile
- **Pixel units throughout**: Rejected - doesn't respect user font size settings, fails accessibility
- **Viewport units (vw/vh)**: Rejected - unpredictable sizing across devices, accessibility issues

### Implementation Guidance
```css
:root {
  font-size: 16px; /* Base size for 1rem */
}

body {
  font-size: 1rem; /* 16px on mobile */
  line-height: 1.5; /* 24px */
}

h1 { 
  font-size: 1.875rem; /* 30px */
  line-height: 1.25; 
}

small, .text-sm {
  font-size: 0.875rem; /* 14px - still readable on mobile */
}

/* Scale up for larger viewports */
@media (min-width: 768px) {
  :root {
    font-size: 18px; /* 1rem now equals 18px */
  }
}

@media (min-width: 1024px) {
  :root {
    font-size: 20px; /* 1rem now equals 20px */
  }
}
```

**Sources**:
- WCAG 2.1 Success Criterion 1.4.4 (Resize Text)
- iOS Safari Viewport and User Scaling Behavior
- MDN: CSS Values and Units

---

## 4. Mobile Performance Optimization for React SPAs

### Decision
Target Lighthouse mobile score 90+ through: code splitting, lazy loading, optimized bundles (<170KB chunks), responsive images, and 3G network simulation testing.

### Rationale
- **Lighthouse 90+ = Good user experience**: Correlates with <2s initial paint, <100ms FID, stable CLS
- **3G as baseline**: 40% of global mobile connections are 3G or slower (Ericsson Mobility Report 2025)
- **170KB chunk size**: Loads in ~2s on 3G (750Kbps effective throughput), psychological threshold for user engagement
- **Bundle splitting reduces parse time**: JS execution is CPU-intensive on mobile devices (slower processors than desktop)
- **Lazy loading defers non-critical code**: Initial bundle only needs homepage + critical path components

### Alternatives Considered
- **4G as baseline**: Rejected - excludes 40% of users in emerging markets and rural areas
- **Single bundle**: Rejected - increases initial load time, poor Time to Interactive metric
- **Aggressive code splitting (10+ chunks)**: Rejected - HTTP/2 mitigates but still creates overhead, diminishing returns

### Implementation Guidance
```javascript
// Vite code splitting via dynamic imports
const ChartComponent = lazy(() => import('./components/Chart'))
const DetailView = lazy(() => import('./components/DetailView'))

// Manual chunk naming in vite.config.js
export default {
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'vendor-react': ['react', 'react-dom'],
          'vendor-charts': ['chart.js', 'react-chartjs-2']
        }
      }
    }
  }
}

// Preload critical resources
<link rel="preload" as="script" href="/assets/vendor-react.js" />
```

**Testing Process**:
1. `npm run build` to generate production bundles
2. `npm run lighthouse` to audit performance
3. Chrome DevTools Network throttling: "Slow 3G" preset
4. Monitor Web Vitals: LCP <2.5s, FID <100ms, CLS <0.1

**Sources**:
- Google Lighthouse Scoring Guide
- Ericsson Mobility Report 2025
- Vite Build Optimizations Documentation

---

## 5. Touch Gesture Implementation in React

### Decision
Use @use-gesture/react (already in dependencies) for touch gesture handling. Implement swipe (list navigation, modal dismiss), tap (selection, detail view), and drag (reorder) interactions.

### Rationale
- **@use-gesture/react is battle-tested**: Used by major React apps (Vercel, Linear), actively maintained
- **Unified API for touch and mouse**: Single codebase handles desktop drag and mobile swipe
- **Performance optimized**: Uses requestAnimationFrame, prevents layout thrashing, cancels default browser behaviors appropriately
- **Small bundle size**: ~8KB gzipped, tree-shakeable
- **Existing dependency**: Already installed in package.json, no new dependency needed

### Alternatives Considered
- **React DnD**: Rejected - focused on desktop drag-and-drop, poor mobile support
- **Custom touch event handlers**: Rejected - complex to handle touch vs mouse, edge cases, browser inconsistencies
- **Hammer.js**: Rejected - not React-specific, larger bundle, less maintained

### Implementation Guidance
```javascript
import { useGesture } from '@use-gesture/react'

function SwipeableCard({ onRemove }) {
  const [{ x }, api] = useSpring(() => ({ x: 0 }))
  
  const bind = useGesture({
    onDrag: ({ down, movement: [mx] }) => {
      api.start({ x: down ? mx : 0, immediate: down })
    },
    onDragEnd: ({ movement: [mx] }) => {
      if (Math.abs(mx) > 100) {
        onRemove() // Swipe threshold reached
      }
    }
  })
  
  return <animated.div {...bind()} style={{ x }} />
}
```

**Gesture Patterns**:
- **Swipe left/right**: Navigate between items, dismiss cards
- **Tap**: Select, open detail view
- **Long press**: Show context menu (use onPointerDown with timer)
- **Pull to refresh**: Downward drag at top of scroll container

**Sources**:
- @use-gesture/react Documentation
- iOS Human Interface Guidelines: Gestures
- Android Material Design: Gestures

---

## 6. Responsive Visualizations (Chart.js)

### Decision
Make Chart.js responsive using `maintainAspectRatio: false` with container-based sizing, `responsive: true`, and viewport-specific configurations.

### Rationale
- **Chart.js responsive option**: Automatically resizes charts on viewport changes
- **Container-based sizing**: More reliable than viewport units, works with CSS Grid/Flexbox
- **Aspect ratio control**: Disable maintainAspectRatio for mobile to prevent excessive vertical space
- **Touch optimization**: Enable interaction modes for touch events
- **SVG over Canvas**: For static visualizations, use SVG (better accessibility, scalable)

### Alternatives Considered
- **Recharts library**: Considered - more React-native, but Chart.js already integrated and performant
- **Fixed aspect ratios**: Rejected - wastes vertical space on mobile portrait orientation
- **Separate mobile charts**: Rejected - code duplication, maintenance burden

### Implementation Guidance
```javascript
const mobileChartOptions = {
  responsive: true,
  maintainAspectRatio: false, // Allow container to control height
  interaction: {
    mode: 'nearest', // Better for touch - larger hit area
    intersect: false
  },
  plugins: {
    legend: {
      display: false, // Hide legend on mobile, show in separate list
      position: 'bottom' // If shown, bottom is more mobile-friendly
    },
    tooltip: {
      enabled: true,
      bodyFont: { size: 14 }, // Larger tooltip text on mobile
      padding: 12 // Larger touch-friendly tooltip
    }
  },
  scales: {
    x: {
      ticks: {
        maxRotation: 45, // Angle labels to fit mobile width
        minRotation: 45,
        font: { size: 12 }
      }
    }
  }
}

// Responsive container
<div style={{ height: '300px', width: '100%' }}>
  <Chart options={mobileChartOptions} />
</div>
```

**SVG Optimization**:
```css
svg {
  max-width: 100%;
  height: auto; /* Maintain aspect ratio */
}
```

**Sources**:
- Chart.js Responsive Charts Documentation
- MDN: Responsive Images
- WCAG 2.1 Success Criterion 1.4.10 (Reflow)

---

## 7. Mobile Accessibility (WCAG 2.1 Level AA)

### Decision
Implement full WCAG 2.1 Level AA compliance with focus on mobile-specific criteria: touch target sizing (2.5.5), orientation adaptability (1.3.4), contrast ratios (1.4.3), and keyboard equivalents for all touch gestures.

### Rationale
- **WCAG 2.1 adds mobile-specific criteria**: Version 2.1 (2018) introduced mobile accessibility requirements
- **4.5:1 contrast ratio for normal text**: Ensures readability in bright outdoor mobile conditions
- **Keyboard navigation must work**: Not all mobile users use touch (switch control, voice control, assistive devices)
- **Orientation agnostic**: Content must work in both portrait and landscape
- **Screen reader optimization**: Mobile screen readers (VoiceOver, TalkBack) have different interaction models than desktop

### Alternatives Considered
- **WCAG 2.0 only**: Rejected - lacks mobile-specific criteria (orientation, touch targets)
- **AAA compliance**: Rejected - not required for this project, 7:1 contrast ratio too restrictive for design

### Implementation Guidance

**Touch Targets (2.5.5)**:
```css
/* All interactive elements */
button, a, input, .clickable {
  min-width: 44px;
  min-height: 44px;
}
```

**Keyboard Navigation**:
```javascript
// All touch gestures MUST have keyboard equivalents
function SwipeableList({ onNext, onPrev }) {
  return (
    <div 
      onKeyDown={(e) => {
        if (e.key === 'ArrowLeft') onPrev()
        if (e.key === 'ArrowRight') onNext()
      }}
      tabIndex={0} // Make focusable
      role="region"
      aria-label="Swipeable list"
    >
      {/* Touch gesture UI */}
    </div>
  )
}
```

**Focus Indicators**:
```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

**Contrast Ratios**:
- Normal text (16px+): 4.5:1 minimum
- Large text (24px+ or 19px bold): 3:1 minimum
- UI components: 3:1 minimum

**Screen Reader Support**:
```jsx
<button 
  aria-label="Open repository details for ProjectX"
  aria-describedby="repo-stats"
>
  <span aria-hidden="true">📊</span> {/* Decorative emoji */}
  Details
</button>
```

**Orientation Support**:
```css
/* Don't lock orientation via CSS or JS */
/* Ensure content reflows in both portrait and landscape */
@media (orientation: landscape) and (max-width: 900px) {
  /* Optimize for mobile landscape */
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

**Testing Tools**:
- **axe DevTools**: Automated accessibility scanning (catches 57% of issues)
- **VoiceOver (iOS)**: Manual screen reader testing
- **TalkBack (Android)**: Manual screen reader testing
- **Keyboard only**: Navigate entire app without mouse/touch
- **Color contrast analyzer**: Verify all text meets 4.5:1 ratio

**Sources**:
- WCAG 2.1 Guidelines (W3C)
- Apple Accessibility: VoiceOver
- Google Accessibility: TalkBack
- axe-core Rules Library

---

## 8. Safe Feature Removal Strategy (Comparison Functionality)

### Decision
Use multi-step removal process: 1) Identify all references via code search, 2) Remove UI components, 3) Remove routes, 4) Clean state management, 5) Prune unused dependencies, 6) Update tests, 7) Verify bundle size reduction.

### Rationale
- **Gradual removal prevents breakage**: Removing incrementally allows testing between steps
- **Code search catches hidden references**: Grep for "comparison", "compare", "selected repos" catches all usage
- **State cleanup prevents memory leaks**: Remove unused React state prevents unnecessary re-renders
- **Dependency pruning reduces bundle size**: Unused npm packages increase build time and bundle size
- **Test updates maintain coverage**: Removing code without updating tests creates false positives

### Alternatives Considered
- **Comment out code first**: Rejected - leaves dead code, doesn't achieve bundle reduction goals
- **Delete all at once**: Rejected - high risk of breaking unrelated features
- **Keep code but hide UI**: Rejected - doesn't achieve performance/simplification goals

### Implementation Guidance

**Step 1: Identify References**
```bash
# Search entire codebase
grep -r "comparison\|compare\|Comparison\|Compare" frontend/src --include="*.jsx" --include="*.js"

# Specific searches
grep -r "selectedRepos" frontend/src
grep -r "ComparisonView" frontend/src
grep -r "handleRepoSelect" frontend/src
```

**Step 2: Remove Components**
```
frontend/src/components/Comparison/
├── ComparisonView.jsx          ❌ Delete
├── ComparisonView.css          ❌ Delete
├── ComparisonSelector.jsx      ❌ Delete
├── MobileComparisonView.jsx    ❌ Delete
├── CompareButton.jsx           ❌ Delete
└── index.js                    ❌ Delete
```

**Step 3: Remove Routes and State**
```javascript
// In App.jsx - REMOVE these sections:
const [selectedRepos, setSelectedRepos] = useState([])
const handleRepoSelect = (repoName) => { /* ... */ }

// Remove from view state
const [currentView, setCurrentView] = useState('table') 
// Remove 'comparison' option

// Remove lazy imports
// const ComparisonView = lazy(() => import('./components/Comparison'))
```

**Step 4: Clean Service Functions**
```javascript
// In metricsCalculator.js - REMOVE:
export function compareRepositories(repo1, repo2) { /* ... */ }
```

**Step 5: Prune Dependencies**
```bash
# Check if any packages were only used for comparison
npm run build:analyze # View bundle composition
# If no other usage, remove from package.json
```

**Step 6: Update Tests**
```bash
# Remove comparison-specific test files
rm frontend/tests/unit/Comparison.test.jsx
rm frontend/tests/integration/comparison-flow.test.jsx

# Update App.test.jsx to remove comparison route tests
```

**Step 7: Verify Bundle Reduction**
```bash
npm run build
# Check output size vs baseline
# Expected: 15% reduction (~170KB → ~145KB)

npm run lighthouse
# Verify performance score maintained/improved
```

**Git Workflow**:
```bash
git checkout 001-mobile-first-ui
git add frontend/src/components/Comparison # Stage deletions
git commit -m "feat: remove comparison functionality"
git diff --stat # Verify files removed
```

**Verification Checklist**:
- [ ] All comparison components removed
- [ ] No references to "comparison" in active code (grep returns 0 results)
- [ ] App builds without errors (`npm run build`)
- [ ] App runs without console errors (`npm run dev`)
- [ ] Bundle size reduced by ≥15%
- [ ] All tests pass (`npm test`)
- [ ] Lighthouse score maintained/improved

**Sources**:
- Refactoring: Improving the Design of Existing Code (Martin Fowler)
- React Documentation: Removing Features Safely
- npm-check-unused Documentation

---

## Summary of Research Decisions

| Area | Decision | Key Metric |
|------|----------|------------|
| **CSS Architecture** | Mobile-first with min-width queries | Breakpoints: <768px, 768-1023px, 1024px+ |
| **Touch Targets** | 44x44px minimum per WCAG 2.1 AA | 44x44 CSS pixels |
| **Typography** | 16px mobile base with rem units | 1.5 line-height, scale at 768px/1024px |
| **Performance** | Code splitting + lazy loading | Lighthouse 90+, <170KB chunks, 3G baseline |
| **Gestures** | @use-gesture/react library | Swipe, tap, drag patterns |
| **Charts** | Chart.js responsive mode | maintainAspectRatio: false, touch interactions |
| **Accessibility** | WCAG 2.1 Level AA full compliance | 4.5:1 contrast, keyboard navigation |
| **Code Removal** | Multi-step safe removal process | 15% bundle reduction target |

## Next Steps

Proceed to **Phase 1 Design** to generate:
1. **data-model.md**: Component state models (viewport config, touch target, navigation state)
2. **contracts/**: Interface definitions for responsive breakpoints, touch interactions, accessibility
3. **quickstart.md**: Developer guide for testing mobile-first implementation

All unknowns have been resolved with industry-standard decisions backed by WCAG, HIG, Material Design, and performance research.
