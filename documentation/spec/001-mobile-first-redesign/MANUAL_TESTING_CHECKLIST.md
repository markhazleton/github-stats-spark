# Manual Testing Checklist

**Feature**: Mobile-First Redesign  
**Date**: 2026-01-03  
**Status**: Ready for Testing

---

## Pre-Testing Setup

- [ ] Run `cd frontend && npm run build`
- [ ] Verify build succeeds with no errors
- [ ] Check bundle sizes in output (should be <170KB JS, <50KB CSS)
- [ ] Run `npm run lighthouse` (Performance >90, Accessibility >95)

---

## Device Testing Matrix

### iOS Safari (iPhone 6S+, iOS 13+)
- [ ] iPhone 6S (375px) - Test at minimum supported size
- [ ] iPhone 12/13 (390px) - Test with notch/safe areas
- [ ] iPhone 14 Pro Max (430px) - Test at larger size
- [ ] iPad (768px+) - Test tablet breakpoint

### Android Chrome (Android 8+)
- [ ] Pixel 5 (393px) - Standard Android size
- [ ] Samsung Galaxy S21 (360px) - Common Android size
- [ ] OnePlus/Xiaomi (411px) - Large Android size

---

## User Story 1: Mobile Dashboard (P1)

### Viewport Testing
- [ ] Test at 320px - No horizontal scroll
- [ ] Test at 375px - No horizontal scroll
- [ ] Test at 414px - No horizontal scroll
- [ ] Test at 768px - Tablet layout works

### Touch Targets
- [ ] All buttons are 44x44px minimum
- [ ] Cards are tappable with adequate spacing
- [ ] Navigation elements are thumb-reachable

### Performance
- [ ] Page loads in <3 seconds on 3G
- [ ] Skeleton screens show during loading
- [ ] No layout shift when content loads

### Visual
- [ ] Repository cards display correctly
- [ ] Language badges visible and styled
- [ ] Star counts and dates formatted properly
- [ ] Spacing consistent across viewports

---

## User Story 2: Touch Gestures & Comparison (P1)

### Multi-Select
- [ ] Tap checkbox to select repository
- [ ] Checkbox is 44x44px minimum
- [ ] Visual feedback on selection (checkmark + border)
- [ ] Can select up to 5 repositories
- [ ] Warning shown when trying to select 6th
- [ ] Selection persists when switching views

### Card Expansion
- [ ] Tap card body (not checkbox) to expand
- [ ] Smooth animation on expansion
- [ ] Expanded view shows full details (commits, description, tech stack)
- [ ] Tap again to collapse
- [ ] No animation if prefers-reduced-motion enabled

### Swipe Gestures
- [ ] Swipe left on card reveals delete action
- [ ] Delete removes card from comparison
- [ ] Swipe right dismisses delete action
- [ ] Smooth gesture tracking with finger
- [ ] No conflicts with browser back gesture

### Comparison View
- [ ] Mobile: Vertical stacked layout
- [ ] Desktop: Side-by-side table layout
- [ ] Metrics display correctly
- [ ] Horizontal swipe between metric groups (mobile)
- [ ] Remove button works for each repo
- [ ] Empty state shows when <2 repos selected

### Haptic Feedback (Android only)
- [ ] Light vibration on select/deselect
- [ ] Vibration on swipe-to-delete
- [ ] No errors on iOS (silent fail expected)

---

## User Story 3: Charts & Visualizations (P2)

### Chart Rendering
- [ ] Bar chart displays correctly
- [ ] Line chart displays correctly
- [ ] Pie/doughnut chart displays correctly
- [ ] Charts responsive to viewport size

### Touch Interactions
- [ ] Touch-and-hold shows tooltip
- [ ] Tooltip positioned away from finger
- [ ] Tap data point opens drill-down
- [ ] Horizontal scroll works for wide charts
- [ ] Axes remain fixed during scroll

### Chart Type Selector
- [ ] Buttons are 44x44px minimum
- [ ] Active chart type highlighted
- [ ] Smooth transition between chart types
- [ ] Chart updates without flash

### Performance
- [ ] Charts render smoothly on mobile
- [ ] No lag when interacting
- [ ] Memory usage reasonable (check DevTools)

---

## User Story 4: Bottom Sheets (P2)

### Filter Bottom Sheet
- [ ] Tap filter button opens sheet
- [ ] Sheet slides up from bottom
- [ ] Snap point at 40% and 90% of viewport
- [ ] Drag to snap between positions
- [ ] Swipe down to dismiss
- [ ] Backdrop tap dismisses sheet
- [ ] Filters apply correctly
- [ ] Sheet closes smoothly

### Sort Bottom Sheet
- [ ] Tap sort button opens sheet
- [ ] Sort options displayed
- [ ] Active sort highlighted
- [ ] Sort applies immediately
- [ ] Sheet dismisses after selection

### Detail Sheet
- [ ] Tap "View Details" opens sheet
- [ ] Full repository info displayed
- [ ] Sheet scrollable if content exceeds height
- [ ] Close button works
- [ ] Swipe down to dismiss works

### Accessibility
- [ ] Focus trapped within sheet when open
- [ ] Keyboard ESC dismisses sheet
- [ ] Screen reader announces sheet opening
- [ ] ARIA attributes present

### iOS Specific
- [ ] Pull-to-refresh blocked when sheet open
- [ ] Safe area insets respected (notch)
- [ ] No conflicts with system gestures

---

## User Story 5: Offline Functionality (P3)

### Service Worker
- [ ] Service worker registers successfully (check DevTools Console)
- [ ] Assets precached on first visit
- [ ] Cached assets served on repeat visits

### Offline Indicator
- [ ] Indicator appears when going offline
- [ ] Shows last sync timestamp
- [ ] Shows cached item count
- [ ] Hides when back online

### Offline Cache
- [ ] Go offline (airplane mode)
- [ ] Reload page - data still loads from cache
- [ ] Navigate between views - all data available
- [ ] Cache older than 7 days is cleaned up

### Background Sync
- [ ] Go offline, then back online
- [ ] Toast notification shows "Data refreshed successfully"
- [ ] Fresh data loaded automatically
- [ ] Old cache replaced with new data

### Error Handling
- [ ] Offline error message is friendly
- [ ] "Retry" button works when back online
- [ ] Error distinguishes offline vs network error
- [ ] No silent failures (check console)

### IndexedDB
- [ ] Open DevTools → Application → IndexedDB
- [ ] Verify `github-stats-cache` database exists
- [ ] Check stored data is correct
- [ ] Verify timestamp is recent

---

## User Story 6: Accessibility (P2)

### Keyboard Navigation
- [ ] Tab through all interactive elements in logical order
- [ ] Skip links work ("Skip to main content", "Skip to navigation")
- [ ] Skip links visible on keyboard focus only
- [ ] Focus indicator visible (3px outline, 4.5:1 contrast)
- [ ] No keyboard traps
- [ ] Enter/Space activates buttons
- [ ] ESC closes modals/bottom sheets
- [ ] Arrow keys navigate within components (if applicable)

### Screen Reader (NVDA/JAWS on Windows, VoiceOver on Mac/iOS)
- [ ] All interactive elements have labels
- [ ] Images have alt text or aria-label
- [ ] Loading states announced
- [ ] Error messages announced
- [ ] Dynamic content updates announced (aria-live)
- [ ] Button states announced (aria-pressed)
- [ ] Selection count announced
- [ ] Landmarks detected (header, nav, main, section)
- [ ] Headings structure logical (h1 → h2 → h3)

### ARIA Attributes
- [ ] Buttons have `aria-label` or visible text
- [ ] Interactive elements have `role` if needed
- [ ] `aria-pressed` on toggle buttons
- [ ] `aria-live="polite"` on dynamic content
- [ ] `aria-hidden="true"` on decorative icons

### Focus Management
- [ ] Focus moves to opened modal/bottom sheet
- [ ] Focus returns to trigger on close
- [ ] Focus indicator never lost
- [ ] Focus order matches visual layout

### Reduced Motion
- [ ] Enable in OS settings (Windows: Settings → Ease of Access → Display → Simplify and personalize)
- [ ] Animations replaced with instant transitions
- [ ] Card expansion shows immediately
- [ ] Bottom sheet appears instantly
- [ ] Toast notifications fade instantly
- [ ] No nausea-inducing motion

### Color Contrast
- [ ] Text contrast ≥4.5:1 (normal text)
- [ ] UI component contrast ≥3:1 (buttons, borders)
- [ ] Focus indicators ≥4.5:1 contrast
- [ ] Error messages clearly visible

---

## Cross-Cutting Concerns

### Tab Bar Navigation
- [ ] Fixed at bottom on mobile (<768px)
- [ ] Hidden on desktop (≥768px)
- [ ] Active tab highlighted
- [ ] Badge count shows selected repos
- [ ] Touch targets 44x44px minimum
- [ ] Safe area insets applied (iOS)
- [ ] Doesn't overlap content

### Empty States
- [ ] Shows when no filter results
- [ ] Shows when no repos selected for comparison
- [ ] Icon, title, description displayed
- [ ] Action button works (if present)
- [ ] Friendly, helpful messaging

### Error Boundary
- [ ] Catches React errors gracefully
- [ ] Shows friendly error message
- [ ] Includes retry button
- [ ] Logs error to console
- [ ] No white screen of death

### Toast Notifications
- [ ] Appears above tab bar (mobile)
- [ ] Auto-dismisses after 3 seconds
- [ ] Manual close button works
- [ ] Multiple toasts stack properly
- [ ] Success/error/warning variants styled correctly
- [ ] Accessible to screen readers

### Loading States
- [ ] Skeleton screens shown during load
- [ ] Spinner for long operations
- [ ] Loading message descriptive
- [ ] No layout shift when content loads

---

## Performance Validation

### Bundle Size
- [ ] JS bundle <170KB gzipped (check Vite output)
- [ ] CSS bundle <50KB gzipped (check Vite output)
- [ ] Assets optimized (images, fonts)

### Lighthouse CI
- [ ] Performance score ≥90
- [ ] Accessibility score ≥95
- [ ] Best Practices score ≥90
- [ ] First Contentful Paint <2s
- [ ] Time to Interactive <5s
- [ ] Cumulative Layout Shift <0.1

### Network Conditions
- [ ] Test on Fast 3G (1.6 Mbps)
- [ ] Test on Slow 3G (0.4 Mbps)
- [ ] Test on 4G (10 Mbps)
- [ ] Test on WiFi (50+ Mbps)

### Memory Usage
- [ ] Check DevTools → Performance → Memory
- [ ] No memory leaks after navigation
- [ ] Garbage collection working
- [ ] <50MB heap size for dashboard

---

## Browser Compatibility

### Chrome/Edge (Desktop & Mobile)
- [ ] All features work
- [ ] Network Info API works (adaptive loading)
- [ ] Service worker works

### Safari (Desktop & iOS)
- [ ] All features work
- [ ] Network Info API degrades gracefully
- [ ] Service worker works
- [ ] Safe area insets respected (iOS)

### Firefox (Desktop & Mobile)
- [ ] All features work
- [ ] Network Info API degrades gracefully
- [ ] Service worker works

---

## Edge Cases

### Device Rotation
- [ ] Rotate portrait → landscape
- [ ] Layout adapts correctly
- [ ] No content cut off
- [ ] Bottom sheets reposition properly

### Very Small Screens (320px)
- [ ] No horizontal scroll
- [ ] Content readable
- [ ] Touch targets still 44x44px
- [ ] Images scale correctly

### Very Large Screens (2560px+)
- [ ] Content centered or max-width applied
- [ ] No excessive whitespace
- [ ] Cards/content properly sized

### Slow Network (2G)
- [ ] Skeleton screens shown
- [ ] Timeout warnings shown
- [ ] Retry options available
- [ ] Offline cache used if available

### No JavaScript
- [ ] Fallback message shown
- [ ] Service worker fails gracefully
- [ ] Basic HTML content accessible

### High Contrast Mode (Windows)
- [ ] Focus indicators visible
- [ ] Borders visible
- [ ] Text readable
- [ ] Icons visible

---

## Final Checks

- [ ] All console errors resolved
- [ ] No console warnings (except 3rd party)
- [ ] No 404 errors in Network tab
- [ ] Service worker active and running
- [ ] IndexedDB populated correctly
- [ ] LocalStorage within quota
- [ ] Cookies (if any) necessary and compliant

---

## Sign-Off

- [ ] iOS Testing Complete - Tester: _____________ Date: _______
- [ ] Android Testing Complete - Tester: _____________ Date: _______
- [ ] Accessibility Testing Complete - Tester: _____________ Date: _______
- [ ] Performance Testing Complete - Tester: _____________ Date: _______
- [ ] Cross-Browser Testing Complete - Tester: _____________ Date: _______
- [ ] **APPROVED FOR PRODUCTION** - Approver: _____________ Date: _______

---

## Issues Found

| # | Issue Description | Severity | Device/Browser | Status |
|---|------------------|----------|----------------|--------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Severity Levels**: Critical (blocks release), High (should fix), Medium (can defer), Low (nice to have)

---

**Testing Guidance**: Test systematically, user story by user story. Log all issues immediately. Take screenshots/videos for visual bugs. Use real devices, not just emulators, for final validation.
