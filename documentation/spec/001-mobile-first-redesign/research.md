# Mobile-First Redesign: Technical Research & Decisions

**Feature**: 001-mobile-first-redesign
**Date**: 2026-01-03
**Status**: Research Complete
**Target Performance Budget**: 170KB JS, 50KB CSS, <5s TTI on 3G

## Executive Summary

This document provides detailed research and technical decisions for 10 critical unknowns identified during the mobile-first redesign planning phase. Each section includes a clear decision, rationale, alternatives considered, and implementation notes aligned with React 19 best practices and 2026 browser support.

---

## 1. Bottom Sheet UI Pattern

### Decision
**Use `react-modal-sheet` (v5.2.1+)**

### Rationale
- **Modern Implementation**: Built with Framer Motion for buttery-smooth animations (60fps GPU-accelerated)
- **Accessibility-First**: Designed with WCAG compliance in mind, though it lets developers choose their own accessibility libraries to reduce bloat
- **Lightweight Philosophy**: Excludes built-in third-party libraries (focus trapping, screen reader utilities) allowing use of project-specific solutions
- **Active Maintenance**: v5.0 released recently with enhanced scroll control, dynamic snap points, and improved keyboard avoidance
- **Flexible Architecture**: Supports custom styling, dynamic `disableScroll` and `disableDrag` functions, and `disableDismiss` prop

### Alternatives Considered
1. **react-spring-bottom-sheet**
   - **Pros**: Built on react-spring and @use-gesture, excellent accessibility features out of the box, minimal rerenders
   - **Cons**: More opinionated about component structure (requires direct children), may include features we don't need
   - **Bundle Impact**: Similar to react-modal-sheet
   - **Rejected**: Less flexible for custom implementations

2. **Custom Implementation**
   - **Pros**: Full control, no external dependencies
   - **Cons**: Requires implementing gesture handling, scroll locking, focus management, spring animations (~2-3 weeks dev time)
   - **Rejected**: Not worth the development time given quality libraries available

### Implementation Notes
- **Structure Requirements**: Keep sheet components as direct children to ensure proper behavior (keyboard avoidance, scroll handling)
- **Accessibility**: Add custom focus trapping (use `focus-trap-react` if needed, ~2KB gzipped) and ARIA attributes
- **Snap Points**: Configure for mobile viewports (e.g., `[0.25, 0.5, 0.9]` of viewport height)
- **Performance**: Leverage Framer Motion's `layoutId` for shared element transitions between views
- **Gotcha**: Wrapping sheet parts with custom elements can break functionality - avoid unnecessary nesting

**Bundle Impact**: ~30-40KB minified, needs verification via Bundlephobia
**Browser Support**: All modern browsers (Chrome 90+, Safari 13+, Firefox 88+)

---

## 2. Touch Gesture Detection

### Decision
**Use `@use-gesture/react` (v10.3.1+)**

### Rationale
- **Modern React Integration**: Built specifically for React hooks pattern, works seamlessly with React 19
- **Active Development**: Actively maintained vs Hammer.js (appears unmaintained as of 2026)
- **Performance**: Designed for 60fps gesture handling, minimal overhead
- **Popularity**: 1.4M+ weekly downloads, 9.5K+ GitHub stars (growing ecosystem)
- **Integration**: Works standalone or pairs excellently with react-spring for gesture-driven animations
- **API**: Simple, declarative hook-based API requiring just a few lines of code

### Alternatives Considered
1. **Hammer.js + react-hammerjs**
   - **Pros**: 24K GitHub stars, 1.7M weekly downloads (legacy popularity), comprehensive gesture recognition
   - **Cons**: Repository no longer activated/maintained, not designed for React hooks, class-component wrapper pattern
   - **Rejected**: Unmaintained library is a risk for long-term project

2. **Custom PointerEvent Handlers**
   - **Pros**: Zero dependencies, full control, PointerEvent API is standardized
   - **Cons**: Complex to implement correctly (velocity tracking, momentum, multi-touch), ~1-2 weeks dev time
   - **Rejected**: Reinventing the wheel for well-solved problem

3. **React Native Gesture Handler**
   - **Pros**: Excellent for React Native
   - **Cons**: Not designed for web, unnecessary overhead
   - **Rejected**: Wrong platform

### Implementation Notes
- **Gestures Needed**: Drag (bottom sheet), swipe (navigation, dismiss), long-press (context menus)
- **Integration Pattern**:
  ```javascript
  import { useGesture } from '@use-gesture/react'
  import { useSpring, animated } from '@react-spring/web'

  const bind = useGesture({
    onDrag: ({ offset: [x, y] }) => api.start({ x, y }),
    onSwipe: ({ direction: [dx, dy] }) => handleSwipe(dx, dy)
  })
  ```
- **Performance**: Enable `passive` events where possible, use `transform` instead of `top/left` for 60fps
- **Touch Targets**: Ensure 44x44px minimum touch target size (accessibility)
- **Gotcha**: `@use-gesture` provides velocity data - use it for momentum scrolling/flinging

**Bundle Impact**: ~15-20KB minified (check Bundlephobia for exact size)
**Browser Support**: All modern browsers with PointerEvent support (Chrome 55+, Safari 13+, Firefox 59+)

---

## 3. IndexedDB Wrapper

### Decision
**Use `Dexie.js` (v4.0+)**

### Rationale
- **Feature-Rich**: Advanced querying, indexing, transactions, versioning, schema migrations
- **Performance**: Optimized for large datasets with efficient indexing system, supports bulk operations
- **Developer Experience**: Fluent, intuitive API that's significantly easier than raw IndexedDB
- **7-Day Cleanup**: Easily implement via schema hooks and versioning system
- **React Integration**: Works seamlessly with React hooks pattern
- **Popularity**: 8K+ GitHub stars, proven in production

### Alternatives Considered
1. **idb (by Google)**
   - **Pros**: Lightweight (~3-5KB minified), promise-based, close to native IndexedDB API
   - **Cons**: Minimal abstraction, no built-in querying/indexing features, manual cleanup implementation
   - **Bundle Impact**: ~3-5KB gzipped
   - **Rejected**: Too low-level, would require significant custom code for querying and auto-cleanup

2. **localForage**
   - **Pros**: Simple localStorage-like API, multi-backend fallback (IndexedDB → WebSQL → localStorage), 20K+ stars
   - **Cons**: No indexing (iterates all keys), slower queries, designed for simple key-value storage
   - **Bundle Impact**: ~8-10KB gzipped
   - **Rejected**: Not suitable for querying GitHub stats data efficiently

3. **Raw IndexedDB API**
   - **Pros**: Zero dependencies, full control
   - **Cons**: Complex callback-based API, verbose, error-prone, no built-in migration system
   - **Rejected**: Poor developer experience, high maintenance burden

### Implementation Notes
- **Schema Design**:
  ```javascript
  const db = new Dexie('GitHubStatsDB')
  db.version(1).stores({
    stats: '++id, username, timestamp, *repositories',
    cache: 'key, timestamp' // For 7-day cleanup
  })
  ```
- **7-Day Auto-Cleanup**:
  ```javascript
  // Add hook for automatic cleanup
  db.cache.hook('creating', (primKey, obj) => {
    obj.timestamp = Date.now()
  })

  // Periodic cleanup (run on app init)
  const sevenDaysAgo = Date.now() - (7 * 24 * 60 * 60 * 1000)
  await db.cache.where('timestamp').below(sevenDaysAgo).delete()
  ```
- **React Integration**: Use `useLiveQuery` hook for reactive queries
- **Versioning**: Implement schema migrations with `db.version()` for future changes
- **Error Handling**: Wrap in try-catch, provide fallback to in-memory storage if IndexedDB fails
- **Gotcha**: IndexedDB has storage quota limits (varies by browser) - implement quota monitoring

**Bundle Impact**: ~26KB gzipped (83KB minified)
**Browser Support**: All modern browsers (Chrome 24+, Safari 10+, Firefox 16+)
**Storage Limit**: ~50% of available disk space (varies by browser)

---

## 4. Service Worker Strategy

### Decision
**Use `vite-plugin-pwa` with Workbox `generateSW` strategy**

### Rationale
- **Zero-Config PWA**: Abstracts Workbox configuration, integrates seamlessly with Vite build process
- **Industry Standard**: Workbox is the de facto standard for service worker management in 2025-2026
- **Automated Precaching**: Generates precache manifest during Vite build, ensures app shell loads <100ms offline
- **Caching Strategies**: Built-in support for StaleWhileRevalidate, CacheFirst, NetworkFirst patterns
- **Lighthouse-Optimized**: Designed to pass PWA criteria out of the box
- **Active Maintenance**: Updated to Workbox 7.0+ (requires Node 16+)

### Alternatives Considered
1. **Custom Service Worker**
   - **Pros**: Full control, no dependencies, custom caching logic
   - **Cons**: Complex to maintain, manual precache manifest generation, easy to introduce bugs
   - **Rejected**: Workbox handles 90% of use cases correctly, not worth custom implementation

2. **vite-plugin-pwa with `injectManifest`**
   - **Pros**: Custom service worker logic while Workbox handles precache manifest injection
   - **Cons**: More complex setup, requires writing service worker code
   - **Use When**: Need custom SW logic beyond what generateSW provides
   - **Rejected for Now**: generateSW sufficient for current requirements, can migrate later if needed

3. **No Service Worker / Client-Side Only**
   - **Pros**: Simpler architecture, no offline complexity
   - **Cons**: No offline support, requirement violation, no PWA benefits
   - **Rejected**: Offline-first is a core requirement

### Implementation Notes
- **Vite Plugin Configuration**:
  ```javascript
  import { VitePWA } from 'vite-plugin-pwa'

  export default {
    plugins: [
      VitePWA({
        registerType: 'autoUpdate',
        workbox: {
          globPatterns: ['**/*.{js,css,html,ico,png,svg,woff2}'],
          runtimeCaching: [
            {
              urlPattern: /^https:\/\/api\.github\.com\/.*/i,
              handler: 'StaleWhileRevalidate',
              options: {
                cacheName: 'github-api-cache',
                expiration: {
                  maxEntries: 50,
                  maxAgeSeconds: 7 * 24 * 60 * 60 // 7 days
                }
              }
            }
          ]
        }
      })
    ]
  }
  ```
- **Caching Strategy**:
  - **App Shell**: CacheFirst (precached during install)
  - **GitHub API**: StaleWhileRevalidate (fast response, background update)
  - **Static Assets**: CacheFirst with 30-day expiration
- **Update Flow**: Use `registerType: 'autoUpdate'` for automatic SW updates
- **Testing**: Use Lighthouse PWA audit, Chrome DevTools Application tab
- **Gotcha**: Must serve over HTTPS (except localhost), SW scope is based on file location

**Bundle Impact**: Workbox runtime ~10-15KB gzipped (injected into SW, not main bundle)
**Browser Support**: All modern browsers with Service Worker support (Chrome 40+, Safari 11.1+, Firefox 44+)
**Performance**: App shell load <100ms offline (meets performance budget)

---

## 5. Mobile Chart Optimization

### Decision
**Use `Chart.js` (v4.0+) with Canvas rendering and tree-shaking**

### Rationale
- **Smallest Bundle**: 11KB gzipped (tree-shaken basic config) vs Recharts 40KB+ or Nivo 50KB+
- **Performance**: Canvas-based rendering (vs Recharts' SVG) - better for mobile, less DOM-heavy
- **Tree-Shakeable**: Modular design allows importing only needed chart types (bar, line, etc.)
- **Touch-Optimized**: Built-in touch event handling, responsive container support
- **React Integration**: `react-chartjs-2` wrapper provides hooks-based API
- **Meets Budget**: 11-14KB fits comfortably within 170KB JS budget

### Alternatives Considered
1. **Recharts**
   - **Pros**: React-first API, composable components, responsive by default, popular (50K+ weekly downloads)
   - **Cons**: ~40KB gzipped, SVG-based (DOM-heavy, slower on mobile), large datasets cause performance issues
   - **Bundle Impact**: ~40KB gzipped (114KB minified)
   - **Rejected**: Bundle size too large, SVG rendering doesn't scale well on mobile

2. **Nivo**
   - **Pros**: Multiple rendering options (SVG, Canvas, HTML), beautiful designs, highly customizable
   - **Cons**: ~50KB+ gzipped, complexity overkill for our use case
   - **Bundle Impact**: ~50KB+ gzipped
   - **Rejected**: Bundle size exceeds budget, unnecessary features

3. **Victory**
   - **Pros**: Composable, React-native compatible, performance-optimized
   - **Cons**: ~2.4s download time (large bundle), similar size to Recharts
   - **Rejected**: Bundle size too large

4. **Keep Recharts with Optimization**
   - **Pros**: Already in codebase, team familiarity
   - **Cons**: Even optimized, Recharts is 40KB+ (23% of 170KB budget for just charts)
   - **Rejected**: Doesn't meet performance budget

### Implementation Notes
- **Tree-Shaking Setup**:
  ```javascript
  import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    LineElement,
    PointElement,
    Title,
    Tooltip,
    Legend
  } from 'chart.js'
  import { Bar, Line } from 'react-chartjs-2'

  // Register only needed components
  ChartJS.register(CategoryScale, LinearScale, BarElement, LineElement, PointElement, Title, Tooltip, Legend)
  ```
- **Responsive Configuration**:
  ```javascript
  options={{
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      mode: 'index',
      intersect: false
    },
    plugins: {
      tooltip: {
        enabled: true,
        // Touch-optimized tooltip
        displayColors: false
      }
    }
  }}
  ```
- **Performance Optimizations**:
  - Use `decimation` plugin for large datasets (reduces points rendered)
  - Set `parsing: false` if data is pre-formatted
  - Use `animation: false` for initial render, enable for interactions
  - Lazy load chart components with React.lazy()
- **Touch Handling**: Chart.js has built-in touch support, no additional config needed
- **Accessibility**: Add `aria-label` to canvas, provide data table alternative for screen readers
- **Migration Path**: Create Chart.js components matching existing Recharts API to minimize component changes

**Bundle Impact**: ~11-14KB gzipped (tree-shaken) vs ~40KB for Recharts (26-29KB savings)
**Browser Support**: All modern browsers (Canvas support: Chrome 4+, Safari 3.1+, Firefox 3.6+)
**Performance**: Canvas rendering 2-3x faster than SVG for mobile devices

---

## 6. CSS Container Queries

### Decision
**Use CSS Container Queries with progressive enhancement**

### Rationale
- **Browser Support**: Baseline support since 2023, 82% compatibility score in 2026
- **Modern Standard**: Container size queries fully supported across modern browsers
- **Better Than Media Queries**: Component-based responsive design vs viewport-based
- **Performance**: Native CSS feature, zero JavaScript overhead
- **Maintainability**: Reusable components that adapt to container size, not viewport
- **Production-Ready**: Size queries stable, style queries partially supported (Firefox 2026)

### Alternatives Considered
1. **Media Queries Only**
   - **Pros**: Universal browser support, well-understood
   - **Cons**: Viewport-based (inflexible for component reuse), requires component duplication for different contexts
   - **Rejected**: Container queries provide better component modularity

2. **JavaScript-Based Resize Detection**
   - **Pros**: Works everywhere, can handle complex logic
   - **Cons**: Performance overhead, layout thrashing risk, requires ResizeObserver polyfill for old browsers
   - **Rejected**: Container queries are native and more performant

3. **Wait for Style Queries**
   - **Pros**: Full container query feature set
   - **Cons**: Style queries still partially supported in 2026
   - **Rejected**: Size queries meet current needs, can add style queries later

### Implementation Notes
- **Basic Pattern**:
  ```css
  .stats-card {
    container-type: inline-size;
    container-name: stats-card;
  }

  .stats-content {
    display: flex;
    flex-direction: column;
  }

  /* Switch to row layout when container is wide enough */
  @container stats-card (min-width: 400px) {
    .stats-content {
      flex-direction: row;
    }
  }
  ```
- **Container Query Units**:
  - `cqw`: 1% of container width
  - `cqh`: 1% of container height
  - `cqi`: 1% of container inline size
  - `cqb`: 1% of container block size
- **Progressive Enhancement**:
  - Mobile-first base styles (small screens default)
  - Container queries enhance for larger containers
  - Fallback to media queries for unsupported browsers (if needed)
- **Gotchas**:
  - Cannot query the container element itself (only children)
  - Style queries still partial support - use size queries for now
  - Container queries don't replace media queries - use both strategically
- **Use Cases**:
  - Repository cards (stack on mobile, horizontal on desktop)
  - Stat widgets (compact vs expanded layouts)
  - Chart legends (below vs side-by-side)

**Bundle Impact**: Zero (native CSS feature)
**Browser Support**: Chrome 105+, Safari 16+, Firefox 110+ (82% global support in 2026)
**Polyfill**: Optional for older browsers (~5KB), but acceptable to degrade to media queries

---

## 7. Network Information API

### Decision
**Implement Network Information API with progressive enhancement**

### Rationale
- **Progressive Enhancement**: Works in Chrome/Edge/Opera (Chromium-based), gracefully degrades in Safari/Firefox
- **Performance Benefits**: Adapt content delivery based on connection (reduce images on 2G, full experience on 4G+)
- **PWA Enhancement**: Excellent for offline-first apps, can defer non-critical API calls on slow connections
- **Zero Breaking**: API designed for progressive enhancement - non-supporting browsers simply ignore it
- **Future-Proof**: Support expected to expand, implementing now provides benefits for Chromium users (65% market share)

### Alternatives Considered
1. **Don't Use (Ignore Connection Speed)**
   - **Pros**: Simpler code, no API dependency
   - **Cons**: Miss opportunity to optimize for slow connections, poor 3G/2G experience
   - **Rejected**: Network-aware UX is valuable for mobile users

2. **Server-Side Detection (User-Agent)**
   - **Pros**: Works for all browsers
   - **Cons**: Unreliable, doesn't detect actual connection speed, spoofable
   - **Rejected**: Inaccurate, poor DX

3. **Custom Speed Test**
   - **Pros**: Works everywhere
   - **Cons**: Adds latency, requires hosting test assets, unreliable
   - **Rejected**: Overhead not worth it

### Implementation Notes
- **Detection Pattern**:
  ```javascript
  function getConnectionSpeed() {
    if ('connection' in navigator) {
      const connection = navigator.connection
      return {
        effectiveType: connection.effectiveType, // '4g', '3g', '2g', 'slow-2g'
        downlink: connection.downlink, // Mbps
        rtt: connection.rtt, // ms
        saveData: connection.saveData // boolean
      }
    }
    return null // Unsupported - use default behavior
  }
  ```
- **Adaptive Loading Strategy**:
  ```javascript
  const connection = getConnectionSpeed()

  if (connection?.effectiveType === 'slow-2g' || connection?.effectiveType === '2g') {
    // Reduce quality, defer non-critical
    useReducedData: true,
    imageSizes: 'small',
    deferCharts: true
  } else if (connection?.effectiveType === '3g') {
    // Medium quality
    useReducedData: false,
    imageSizes: 'medium',
    deferCharts: false
  } else {
    // Full experience (4g or unknown)
    useReducedData: false,
    imageSizes: 'large',
    deferCharts: false
  }
  ```
- **React Integration**:
  ```javascript
  function useNetworkStatus() {
    const [status, setStatus] = useState(getConnectionSpeed())

    useEffect(() => {
      if (!navigator.connection) return

      const updateStatus = () => setStatus(getConnectionSpeed())
      navigator.connection.addEventListener('change', updateStatus)
      return () => navigator.connection.removeEventListener('change', updateStatus)
    }, [])

    return status
  }
  ```
- **Use Cases**:
  - Reduce chart data points on slow connections
  - Defer non-critical GitHub API calls
  - Show "reduced data mode" indicator
  - Adapt image quality/sizes
- **Gotcha**: effectiveType is based on recent network conditions, can change mid-session

**Bundle Impact**: Zero (browser API)
**Browser Support**: Chrome 61+, Edge 79+, Opera 48+, Samsung Internet 8+ (Safari/Firefox: none)
**Fallback**: Safe to use - unsupported browsers get full experience

---

## 8. Haptic Feedback (Vibration API)

### Decision
**Implement Vibration API for Android with iOS graceful degradation**

### Rationale
- **Android Support**: Full support in Chrome 90+ (target audience)
- **Progressive Enhancement**: No iOS support, but feature-detect and degrade gracefully
- **UX Enhancement**: Haptic feedback improves native-like feel for actions (pull-to-refresh, swipe, long-press)
- **Zero Bundle**: Native browser API
- **iOS Workaround**: Limited haptic via `<input type="checkbox" switch>` (Safari 18+), but not standard

### Alternatives Considered
1. **Don't Implement Haptics**
   - **Pros**: Simpler, no platform differences
   - **Cons**: Misses opportunity for enhanced UX on Android
   - **Rejected**: Low effort, high impact for Android users

2. **iOS Polyfill/Workaround**
   - **Pros**: Could provide iOS support
   - **Cons**: Non-standard, hacky (checkbox switch method), unreliable
   - **Rejected**: Not worth complexity for edge case

3. **Wait for iOS Support**
   - **Cons**: Apple has not supported Vibration API for 10+ years, unlikely to change
   - **Rejected**: Indefinite wait

### Implementation Notes
- **Feature Detection**:
  ```javascript
  function vibrate(pattern) {
    if ('vibrate' in navigator) {
      navigator.vibrate(pattern)
    }
    // Silently fail on iOS - no error
  }
  ```
- **Usage Patterns**:
  ```javascript
  // Single vibration (200ms)
  vibrate(200)

  // Pattern: vibrate, pause, vibrate
  vibrate([200, 100, 200])

  // Stop vibration
  vibrate(0)
  ```
- **Use Cases**:
  - Pull-to-refresh trigger: `vibrate(50)` (light feedback)
  - Swipe navigation: `vibrate(30)` (subtle)
  - Long-press menu: `vibrate([50, 100, 50])` (pattern)
  - Error state: `vibrate([100, 50, 100, 50, 100])` (alert pattern)
- **Best Practices**:
  - Keep vibrations short (<200ms) to avoid annoyance
  - Respect user preferences (provide settings toggle)
  - Don't vibrate on every interaction (reserve for meaningful actions)
  - Test on real devices (emulator vibration doesn't match real feel)
- **iOS Workaround (Safari 18+)**:
  ```html
  <!-- Limited haptic via switch checkbox -->
  <input type="checkbox" switch id="haptic-trigger">
  <label for="haptic-trigger">Trigger Action</label>
  ```
  - **Note**: Not recommended for production, use only if critical
- **Gotcha**: Some users disable vibration globally in OS settings - API will fail silently

**Bundle Impact**: Zero (browser API)
**Browser Support**: Android Chrome 32+, Android Browser 4.4.3+ (iOS Safari: none)
**Fallback**: Feature-detect, gracefully degrade on iOS

---

## 9. Pull-to-Refresh

### Decision
**Use CSS `overscroll-behavior-y: contain` to prevent browser PTR, implement custom PTR**

### Rationale
- **Modern Standard**: `overscroll-behavior-y` is the CSS property designed specifically for this purpose
- **Non-Invasive**: Doesn't interfere with normal scrolling or desktop functionality
- **Browser Support**: Chrome, Firefox, Opera support; Safari limited but improving
- **Simple Implementation**: Single CSS line prevents conflict
- **Performance**: No JavaScript overhead for conflict prevention

### Alternatives Considered
1. **`touchmove` preventDefault()**
   - **Pros**: Works everywhere with touch events
   - **Cons**: Prevents ALL touch scrolling on affected element (too aggressive), complex to implement correctly
   - **Rejected**: Breaks normal scrolling, poor UX

2. **Third-Party Library** (e.g., web-pull-to-refresh, prevent-pull-refresh npm)
   - **Pros**: Handles edge cases
   - **Cons**: Additional bundle size, CSS solution is simpler
   - **Rejected**: CSS handles this natively

3. **Disable Pull-to-Refresh Entirely**
   - **Pros**: Simple - just use `overscroll-behavior-y: contain`
   - **Cons**: Loses native-like refresh UX
   - **Rejected**: Custom PTR is a feature requirement

### Implementation Notes
- **Prevent Browser PTR**:
  ```css
  body {
    overscroll-behavior-y: contain;
  }

  /* Or on specific scroll containers */
  .main-content {
    overscroll-behavior-y: contain;
  }
  ```
- **Custom Pull-to-Refresh Implementation**:
  ```javascript
  import { useGesture } from '@use-gesture/react'
  import { useSpring, animated } from '@react-spring/web'

  function usePullToRefresh(onRefresh) {
    const [{ y }, api] = useSpring(() => ({ y: 0 }))
    const [isRefreshing, setIsRefreshing] = useState(false)

    const bind = useGesture({
      onDrag: ({ movement: [, my], velocity: [, vy], direction: [, dy], last }) => {
        // Only allow pull down when scrolled to top
        if (window.scrollY > 0) return

        if (last) {
          if (my > 100 && dy > 0) {
            // Trigger refresh
            setIsRefreshing(true)
            vibrate(50) // Optional haptic
            onRefresh().finally(() => {
              setIsRefreshing(false)
              api.start({ y: 0 })
            })
          } else {
            api.start({ y: 0 })
          }
        } else {
          // Drag in progress (with rubber banding)
          api.start({ y: my > 0 ? my * 0.5 : 0, immediate: true })
        }
      }
    })

    return { bind, y, isRefreshing }
  }
  ```
- **Visual Indicator**:
  ```javascript
  <animated.div style={{ transform: y.to(y => `translateY(${y}px)`) }}>
    <RefreshIndicator visible={y > 50} spinning={isRefreshing} />
    {/* Main content */}
  </animated.div>
  ```
- **Gotchas**:
  - Check `window.scrollY === 0` before enabling PTR (don't conflict with scroll)
  - Use rubber-band effect (multiply drag distance by <1) for natural feel
  - Show spinner/indicator at threshold (e.g., 100px)
  - Prevent PTR during horizontal swipe gestures
- **Accessibility**: Provide a visible refresh button for keyboard/non-touch users

**Bundle Impact**: Zero for CSS, ~2-3KB for custom PTR logic (using existing @use-gesture)
**Browser Support**: overscroll-behavior-y - Chrome 63+, Firefox 59+, Opera 50+ (Safari partial)
**Fallback**: Safari may show browser PTR - acceptable degradation

---

## 10. Lighthouse CI Integration

### Decision
**Use Lighthouse CI with GitHub Actions and Vite via `vite preview` command**

### Rationale
- **Automated Regression Detection**: Catch performance degradation before production (LCP, TBT, CLS)
- **Official Tool**: Built by Google Chrome team, industry standard for CI/CD performance monitoring
- **GitHub Actions Integration**: Official action available, easy setup
- **Performance Budgets**: Configure thresholds (fail CI if LCP >2.5s, TBT >300ms, etc.)
- **Vite Compatibility**: Works with Vite's preview server after build
- **Historical Tracking**: Track metrics over time, visualize trends
- **Comprehensive**: Checks performance, accessibility, SEO, PWA, best practices

### Alternatives Considered
1. **Unlighthouse**
   - **Pros**: Specifically designed for Vite, nice UI, multi-page scanning
   - **Cons**: Less mature than Lighthouse CI, smaller community
   - **Rejected**: Lighthouse CI is more established, better GitHub Actions support

2. **Manual Lighthouse Audits**
   - **Pros**: Zero setup, use Chrome DevTools
   - **Cons**: Manual, not automated, no CI/CD integration, easy to forget
   - **Rejected**: Need automated checks in PR workflow

3. **WebPageTest API**
   - **Pros**: Real browser testing, multiple locations
   - **Cons**: More complex setup, requires API key, slower than Lighthouse
   - **Rejected**: Overkill for current needs

4. **Custom Performance Monitoring**
   - **Pros**: Full control, custom metrics
   - **Cons**: Significant dev effort, reinventing wheel
   - **Rejected**: Lighthouse CI handles 90% of needs

### Implementation Notes

#### GitHub Actions Workflow
```yaml
# .github/workflows/lighthouse-ci.yml
name: Lighthouse CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm install

      - name: Build project
        run: npm run build

      - name: Install Lighthouse CI
        run: npm install -g @lhci/cli@0.15.x

      - name: Run Lighthouse CI
        run: lhci autorun
        env:
          LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}
```

#### Lighthouse CI Configuration
```javascript
// lighthouserc.js
module.exports = {
  ci: {
    collect: {
      startServerCommand: 'npm run preview',
      startServerReadyPattern: 'Local',
      startServerReadyTimeout: 30000,
      url: [
        'http://localhost:4173/',
        'http://localhost:4173/dashboard',
        'http://localhost:4173/stats'
      ],
      numberOfRuns: 3
    },
    assert: {
      preset: 'lighthouse:recommended',
      assertions: {
        // Performance Budgets (aligned with spec)
        'first-contentful-paint': ['error', { maxNumericValue: 1800 }], // <1.8s
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }], // <2.5s
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }], // <0.1
        'total-blocking-time': ['error', { maxNumericValue: 300 }], // <300ms
        'speed-index': ['error', { maxNumericValue: 3400 }], // <3.4s
        'interactive': ['error', { maxNumericValue: 5000 }], // <5s (TTI)

        // Resource Budgets
        'resource-summary:script:size': ['error', { maxNumericValue: 174080 }], // 170KB
        'resource-summary:stylesheet:size': ['error', { maxNumericValue: 51200 }], // 50KB

        // PWA Requirements
        'installable-manifest': 'error',
        'service-worker': 'error',
        'offline-start-url': 'error',

        // Accessibility
        'categories:accessibility': ['error', { minScore: 0.9 }],

        // Best Practices
        'categories:best-practices': ['error', { minScore: 0.9 }]
      }
    },
    upload: {
      target: 'temporary-public-storage'
      // Alternative: Set up LHCI server for permanent storage
    }
  }
}
```

#### Vite Configuration
```javascript
// package.json
{
  "scripts": {
    "build": "vite build",
    "preview": "vite preview --port 4173 --host"
  }
}
```

- **Key Points**:
  - `startServerReadyPattern: 'Local'`: Detects when Vite preview server is ready (prints "Local: http://...")
  - `numberOfRuns: 3`: Run Lighthouse 3 times, take median (reduces variance)
  - Test multiple URLs (home, dashboard, stats pages)
  - Assertions aligned with performance budgets from spec
- **Performance Budgets**:
  - TTI: <5s on 3G (throttled)
  - LCP: <2.5s (Good)
  - CLS: <0.1 (Good)
  - TBT: <300ms (Good)
  - JS: <170KB (spec requirement)
  - CSS: <50KB (spec requirement)
- **CI Workflow**:
  1. Checkout code
  2. Install dependencies
  3. Build production bundle
  4. Start Vite preview server
  5. Run Lighthouse on specified URLs
  6. Assert against budgets
  7. Upload results
  8. Fail PR if any assertion fails
- **Gotchas**:
  - Ensure Vite preview port (4173) matches Lighthouse URLs
  - Use `--host` flag for Vite preview to allow Lighthouse connection
  - CI environment may have different performance than local (use median of 3 runs)
  - Set up `LHCI_GITHUB_APP_TOKEN` secret for PR comments (optional but recommended)

**Bundle Impact**: Zero (CI tool, not in production bundle)
**CI Time**: ~2-3 minutes per PR (build + 3 Lighthouse runs)
**Cost**: Free with GitHub Actions (public repos), uses included minutes (private repos)

---

## Performance Budget Compliance Summary

| Requirement | Budget | Recommended Approach | Estimated Impact |
|-------------|--------|---------------------|------------------|
| JavaScript Bundle | 170KB | Chart.js (11-14KB), Dexie (26KB), @use-gesture (15-20KB), react-modal-sheet (30-40KB) | ~82-100KB for libraries (leaves 70-88KB for app code) |
| CSS Bundle | 50KB | Container queries (0KB), custom PTR styles (~2KB) | ~2KB additional, ample room |
| TTI on 3G | <5s | Service Worker precaching (<100ms app shell), code splitting, lazy loading | Target: 3.5-4.5s |
| Offline Support | Required | vite-plugin-pwa + Workbox (10-15KB SW runtime, not in main bundle) | No main bundle impact |

**Total Library Overhead**: ~82-100KB (leaves 70-88KB for application code, framework, and dependencies)

---

## React 19 Performance Best Practices (2026)

### High-Impact Optimizations
1. **React Compiler**: Enable experimental compiler for automatic memoization (eliminates manual `useMemo`, `useCallback`)
2. **Code Splitting**: Lazy load routes and heavy components (`React.lazy()`, `Suspense`)
3. **Server Components**: Consider Next.js App Router for server-side rendering (reduces client JS)
4. **Automatic Batching**: React 19 batches state updates automatically (performance win out of the box)
5. **Resource Preloading**: Use React 19's built-in preload support for fonts, scripts, stylesheets

### Mobile-Specific Optimizations
- **Target Metrics**:
  - Lighthouse Score: 90+ Performance, 100 Accessibility, 90+ Best Practices
  - FCP: <1.8s
  - LCP: <2.5s
  - CLS: <0.1
  - FID: <100ms
  - Mobile performance within 30% of desktop
- **Techniques**:
  - Virtualize long lists (react-window, react-virtuoso)
  - Optimize images (WebP, lazy loading, responsive sizes)
  - Defer non-critical JavaScript
  - Use `loading="lazy"` for images
  - Minimize layout shifts (reserve space for dynamic content)

---

## Browser Support Matrix (2026)

| Feature | Chrome | Safari | Firefox | Edge | Notes |
|---------|--------|--------|---------|------|-------|
| Service Workers | 40+ | 11.1+ | 44+ | 17+ | Required for PWA |
| IndexedDB | 24+ | 10+ | 16+ | 12+ | All modern browsers |
| Container Queries | 105+ | 16+ | 110+ | 105+ | 82% global support |
| Network Info API | 61+ | No | No | 79+ | Progressive enhancement |
| Vibration API | 32+ | No | 16+ | 79+ | Android only |
| overscroll-behavior | 63+ | Partial | 59+ | 79+ | Safari improving |
| PointerEvents | 55+ | 13+ | 59+ | 12+ | Modern touch handling |

**Target Support**: Last 2 versions of major browsers, iOS Safari 13+, Android Chrome 90+

---

## Implementation Priority

### Phase 1: Foundation (Week 1-2)
1. **Service Worker**: Set up vite-plugin-pwa for offline support
2. **Lighthouse CI**: Configure GitHub Actions for automated monitoring
3. **Chart Migration**: Replace Recharts with Chart.js (26-29KB savings)

### Phase 2: Interactivity (Week 3-4)
4. **Gesture Detection**: Implement @use-gesture for touch handling
5. **Bottom Sheet**: Add react-modal-sheet for mobile navigation
6. **Pull-to-Refresh**: Custom PTR with overscroll-behavior-y

### Phase 3: Data & Polish (Week 5-6)
7. **IndexedDB**: Implement Dexie.js with 7-day cleanup
8. **Container Queries**: Refactor components for container-based responsiveness
9. **Network Awareness**: Add Network Information API for adaptive loading
10. **Haptic Feedback**: Implement Vibration API for Android

---

## Sources

### Bottom Sheet
- [$ npm i react-spring-bottom-sheet](https://react-spring.bottom-sheet.dev/)
- [react-modal-sheet - npm](https://www.npmjs.com/package/react-modal-sheet)
- [GitHub - Temzasse/react-modal-sheet](https://github.com/Temzasse/react-modal-sheet)
- [15 Best React UI Libraries for 2026](https://www.builder.io/blog/react-component-libraries-2026)

### Touch Gestures
- [use-gesture/react - npm](https://www.npmjs.com/package/@use-gesture/react)
- [GitHub - hammerjs/hammer.js](https://github.com/hammerjs/hammer.js)
- [@use-gesture/react vs hammerjs - npm trends](https://npmtrends.com/@use-gesture/react-vs-alloyfinger-vs-hammerjs-vs-interact.js-vs-rc-gesture-vs-react-use-gesture-vs-react-with-gesture)

### IndexedDB
- [idb vs localforage vs dexie - npm-compare](https://npm-compare.com/dexie,idb,localforage)
- [Dexie.js - Build Offline-First Apps](https://dexie.org/)
- [GitHub - dexie/Dexie.js](https://github.com/dexie/Dexie.js/)
- [Best library for IndexedDB](https://www.paultman.com/posts/best-library-for-indexeddb-localforage-idb-keyval-or-idb/)
- [Investigating IndexedDB Wrapper Libraries - Part Two](https://www.raymondcamden.com/2022/08/18/investigating-indexeddb-wrapper-libraries-part-two)

### Service Workers
- [Build a Blazing-Fast, Offline-First PWA with Vue 3 and Vite in 2025](https://medium.com/@Christopher_Tseng/build-a-blazing-fast-offline-first-pwa-with-vue-3-and-vite-in-2025-the-definitive-guide-5b4969bc7f96)
- [Using the VitePWA Plugin for an Offline Site - CSS-Tricks](https://css-tricks.com/vitepwa-plugin-offline-service-worker/)
- [Getting Started - Workbox - Vite PWA](https://vite-pwa-org.netlify.app/workbox/)
- [GitHub - vite-pwa/vite-plugin-pwa](https://github.com/vite-pwa/vite-plugin-pwa)

### Charts
- [Best React chart libraries (2025 update) - LogRocket](https://blog.logrocket.com/best-react-chart-libraries-2025/)
- [recharts vs chart.js vs victory vs nivo - npm-compare](https://npm-compare.com/recharts,chart.js,victory,nivo)
- [Top 7 React Chart Libraries for 2026 - DEV Community](https://dev.to/basecampxd/top-7-react-chart-libraries-for-2026-features-use-cases-and-benchmarks-412c)
- [Charting Libraries Performance Comparison](https://chart.pdfmunk.com/blog/charting-libraries-performance-comparison)
- [What's the best charts library with a small bundle size? - DEV](https://dev.to/ben/what-s-the-best-charts-library-with-a-small-bundle-size-fho)
- [recharts - Bundlephobia](https://bundlephobia.com/package/recharts)

### Container Queries
- [Container queries in 2026 - LogRocket](https://blog.logrocket.com/container-queries-2026)
- [CSS Container Queries - Can I use](https://caniuse.com/css-container-queries)
- [CSS Container Queries in 2025](https://caisy.io/blog/css-container-queries)
- [How to use container queries now - web.dev](https://web.dev/blog/how-to-use-container-queries-now)

### Network Information API
- [Network Information API - Can I use](https://caniuse.com/netinfo)
- [Connection-Aware Components - Max Böck](https://mxb.dev/blog/connection-aware-components/)
- [Network Information API - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Network_Information_API)
- [NetworkInformation API - PWA Demo](https://progressier.com/pwa-capabilities/network-information)

### Vibration API
- [Vibration API - PWA Demo](https://progressier.com/pwa-capabilities/vibration-api)
- [Vibration API - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API)
- [Haptic Feedback for Web Apps - OpenReplay](https://blog.openreplay.com/haptic-feedback-for-web-apps-with-the-vibration-api/)
- [Vibration API - Can I use](https://caniuse.com/vibration)

### Pull-to-Refresh
- [How to prevent pull-down-to-refresh - DEV Community](https://dev.to/khaled17/how-to-prevent-pull-down-to-refresh-of-mobile-browser-mjp)
- [How to disable pull to refresh - The Koi](https://www.the-koi.com/projects/how-to-disable-pull-to-refresh/)
- [GitHub - apeatling/web-pull-to-refresh](https://github.com/apeatling/web-pull-to-refresh)
- [Implement a pull to refresh component](https://www.fabrizioduroni.it/2019/11/16/pull-to-refresh-web/)

### Lighthouse CI
- [GitHub - GoogleChrome/lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci)
- [Lighthouse CI Action - GitHub Marketplace](https://github.com/marketplace/actions/lighthouse-ci-action)
- [Monitoring Performance with Lighthouse CI in GitHub Actions](https://softwarehouse.au/blog/monitoring-performance-with-lighthouse-ci-in-github-actions/)
- [Performance Audits with Lighthouse CI & GitHub Actions - DEV](https://dev.to/jacobandrewsky/performance-audits-with-lighthouse-ci-github-actions-3g0g)
- [Unlighthouse - Vite Integration](https://unlighthouse.dev/integrations/vite.md)

### React 19 Performance
- [React Performance Optimization: 15 Best Practices for 2025 - DEV](https://dev.to/alex_bobes/react-performance-optimization-15-best-practices-for-2025-17l9)
- [React 19.2: New Features & Performance Boosts](https://javascript-conference.com/blog/react-19-2-updates-performance-activity-component/)
- [React Performance Optimization 2025 - Growin](https://www.growin.com/blog/react-performance-optimization-2025/)
- [React 19 vs React 18: Performance Improvements - DEV](https://dev.to/manojspace/react-19-vs-react-18-performance-improvements-and-migration-guide-5h85)

### Bundle Sizes
- [@use-gesture/react - Bundlephobia](https://bundlephobia.com/package/@use-gesture/react)
- [react-modal-sheet - Bundlephobia](https://bundlephobia.com/package/react-modal-sheet)
- [dexie - Bundlephobia](https://bundlephobia.com/package/dexie)
- [Reduce bundle size · Issue #1585 - Dexie.js](https://github.com/dexie/Dexie.js/issues/1585)

---

**Document Version**: 1.0
**Last Updated**: 2026-01-03
**Next Review**: Before Phase 1 implementation kickoff
