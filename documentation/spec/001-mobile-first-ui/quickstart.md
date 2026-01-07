# Quickstart Guide: Mobile-First UI Development

**Feature**: Mobile-First UI Redesign  
**Branch**: `001-mobile-first-ui`  
**Target Audience**: Developers implementing and testing the mobile-first redesign

## Prerequisites

### Required Software
- **Node.js**: 18.0.0 or higher
- **npm**: 9.0.0 or higher
- **Git**: For version control
- **Modern browser**: Chrome/Edge (for DevTools), Firefox, Safari

### Required Browser DevTools
- **Chrome DevTools**: Device emulation, accessibility auditing
- **axe DevTools extension**: Accessibility scanning
- **React DevTools extension**: Component debugging

### Physical Devices (Recommended)
- **iPhone** (any model): iOS Safari testing
- **Android phone**: Chrome Mobile testing
- **Tablet** (optional): iPad or Android tablet

---

## Quick Start (5 Minutes)

### 1. Clone and Setup

```bash
# Navigate to project
cd github-stats-spark

# Checkout feature branch
git checkout 001-mobile-first-ui

# Install frontend dependencies
cd frontend
npm install

# Start development server
npm run dev
```

### 2. Open Mobile DevTools

1. Open http://localhost:5173 in Chrome
2. Press `F12` to open DevTools
3. Click device icon or press `Ctrl+Shift+M` (Windows) / `Cmd+Shift+M` (Mac)
4. Select "iPhone 12 Pro" from device dropdown
5. Refresh page to apply mobile viewport

### 3. Verify Mobile-First Baseline

**✅ Checklist**:
- [ ] Page loads without horizontal scroll
- [ ] Text is readable (no tiny fonts)
- [ ] Buttons are tappable (not too small)
- [ ] Navigation appears as bottom tabs
- [ ] No "Comparison" tab visible (removed feature)

---

## Development Workflow

### Mobile-First CSS Development

**Rule**: Always write mobile styles first, then enhance for larger screens.

```css
/* Step 1: Write mobile base styles (320px+) */
.repository-card {
  padding: 16px;
  font-size: 16px;
  display: flex;
  flex-direction: column;
}

/* Step 2: Enhance for tablet (768px+) */
@media (min-width: 768px) {
  .repository-card {
    padding: 24px;
    font-size: 18px;
    /* Keep column layout or switch to row if space allows */
  }
}

/* Step 3: Enhance for desktop (1024px+) */
@media (min-width: 1024px) {
  .repository-card {
    padding: 32px;
    flex-direction: row; /* Horizontal layout on desktop */
    justify-content: space-between;
  }
}
```

### Testing Breakpoints Quickly

Use Chrome DevTools responsive mode presets:

| Device | Width | Breakpoint | Test Focus |
|--------|-------|------------|------------|
| iPhone SE | 375px | Mobile | Smallest common mobile |
| iPhone 12 Pro | 390px | Mobile | Modern mobile standard |
| iPad Mini | 768px | Tablet | Tablet portrait |
| iPad Pro | 1024px | Desktop | Tablet landscape / small desktop |
| Desktop | 1280px+ | Desktop | Full desktop experience |

**Keyboard Shortcut**: `Ctrl+Shift+M` (Windows) / `Cmd+Shift+M` (Mac) toggles device mode

---

## Component Development Checklist

When creating or modifying a component:

### Visual Design
- [ ] Looks good on mobile (375px width)
- [ ] Looks good on tablet (768px width)
- [ ] Looks good on desktop (1280px+ width)
- [ ] No horizontal scroll at any breakpoint
- [ ] Text is readable without zooming

### Typography
- [ ] Body text minimum 16px on mobile
- [ ] All text uses rem/em units, not px
- [ ] Line height 1.5 for body text
- [ ] Heading line height 1.25

### Touch Targets
- [ ] All interactive elements ≥44x44px
- [ ] Minimum 8px spacing between adjacent targets
- [ ] Visual feedback on tap (<100ms)
- [ ] No accidental activation on adjacent elements

### Accessibility
- [ ] Keyboard navigation works (Tab, Enter, Space, Arrows)
- [ ] Focus indicators visible (2px outline)
- [ ] Screen reader labels present (aria-label)
- [ ] Color contrast ≥4.5:1 for text
- [ ] Works with browser zoom at 200%

### Performance
- [ ] Component renders in <100ms
- [ ] No layout thrashing on scroll
- [ ] Lazy loading for heavy content
- [ ] No console errors or warnings

---

## Testing Mobile-First Implementation

### Quick Visual Test (2 Minutes)

```bash
# Start dev server
npm run dev

# Open in Chrome
# Press F12 → Toggle device mode (Ctrl+Shift+M)
# Select "iPhone 12 Pro"
# Navigate through app:
#   - Repository list
#   - Repository detail view
#   - Visualizations
#   - (No comparison view - should be removed)
# Rotate device (landscape/portrait)
# Check: No horizontal scroll, all content visible
```

### Touch Target Test (5 Minutes)

```javascript
// Add to global.css temporarily for visual debugging
* {
  outline: 1px solid rgba(255, 0, 0, 0.2) !important;
}

button, a, [role="button"], .clickable {
  outline: 2px solid rgba(0, 255, 0, 0.8) !important;
  min-width: 44px;
  min-height: 44px;
}
```

Visually scan for green outlines <44px - these violate touch target requirements.

### Accessibility Audit (5 Minutes)

```bash
# Run Lighthouse in CLI
npm run lighthouse

# Or in Chrome DevTools:
# F12 → Lighthouse tab → 
# Select: Mobile, Accessibility
# Click "Analyze page load"

# Target: Accessibility score 100, 0 violations
```

### Screen Reader Test (10 Minutes)

**iOS (VoiceOver)**:
1. Settings → Accessibility → VoiceOver → On
2. Open Safari, navigate to localhost (use Mac + iPhone on same network)
3. Swipe right to navigate between elements
4. Double-tap to activate
5. Verify all interactive elements have labels

**Android (TalkBack)**:
1. Settings → Accessibility → TalkBack → On  
2. Open Chrome, navigate to your local IP (e.g., 192.168.1.100:5173)
3. Swipe right to navigate
4. Verify labels and functionality

### Performance Test (3 Minutes)

```bash
# Build production bundle
npm run build

# Check bundle sizes
ls -lh ../docs/assets/

# Target: Main chunk <170KB, vendor chunks <200KB combined
# Verify: 15% reduction from baseline after comparison removal
```

---

## Common Development Tasks

### Add a New Mobile-Optimized Component

```jsx
import React from 'react'
import { useViewport } from '@/contexts/ViewportContext'
import './MyComponent.css'

export default function MyComponent() {
  const { isMobile, isTablet, isDesktop } = useViewport()
  
  return (
    <div className="my-component">
      <h2>Component Title</h2>
      
      {/* Render different layouts based on viewport */}
      {isMobile && <MobileLayout />}
      {isTablet && <TabletLayout />}
      {isDesktop && <DesktopLayout />}
    </div>
  )
}
```

```css
/* MyComponent.css - Mobile-first */
.my-component {
  padding: 1rem;
  font-size: 1rem;
}

@media (min-width: 768px) {
  .my-component {
    padding: 1.5rem;
  }
}

@media (min-width: 1024px) {
  .my-component {
    padding: 2rem;
  }
}
```

### Implement Touch Gestures

```jsx
import { useGesture } from '@use-gesture/react'
import { animated, useSpring } from '@react-spring/web'

export default function SwipeableCard({ onDismiss }) {
  const [{ x }, api] = useSpring(() => ({ x: 0 }))
  
  const bind = useGesture({
    onDrag: ({ down, movement: [mx] }) => {
      api.start({ x: down ? mx : 0, immediate: down })
    },
    onDragEnd: ({ movement: [mx] }) => {
      if (Math.abs(mx) > 100) {
        onDismiss() // Swipe threshold reached
      }
    }
  })
  
  return (
    <animated.div 
      {...bind()} 
      style={{ x }}
      className="swipeable-card"
    >
      {/* Card content */}
    </animated.div>
  )
}
```

### Add Keyboard Navigation for Gestures

```jsx
export default function AccessibleSwipe({ onNext, onPrevious }) {
  const handleKeyDown = (e) => {
    if (e.key === 'ArrowLeft') {
      e.preventDefault()
      onPrevious()
    } else if (e.key === 'ArrowRight') {
      e.preventDefault()
      onNext()
    }
  }
  
  return (
    <div
      tabIndex={0}
      onKeyDown={handleKeyDown}
      role="region"
      aria-label="Swipeable content. Use left/right arrows to navigate."
    >
      {/* Content with gesture handlers */}
    </div>
  )
}
```

---

## Debugging Mobile Issues

### Responsive Layout Debugging

```css
/* Add to global.css temporarily */
body::before {
  content: 'Mobile';
  position: fixed;
  top: 0;
  right: 0;
  background: red;
  color: white;
  padding: 4px 8px;
  z-index: 9999;
  font-size: 12px;
}

@media (min-width: 768px) {
  body::before {
    content: 'Tablet';
    background: orange;
  }
}

@media (min-width: 1024px) {
  body::before {
    content: 'Desktop';
    background: green;
  }
}
```

This displays current breakpoint in top-right corner.

### Touch Event Debugging

```javascript
// Log touch events in console
document.addEventListener('touchstart', (e) => {
  console.log('Touch start:', {
    x: e.touches[0].clientX,
    y: e.touches[0].clientY,
    target: e.target
  })
}, { passive: true })

document.addEventListener('touchend', (e) => {
  console.log('Touch end')
}, { passive: true })
```

### Performance Profiling

```bash
# Chrome DevTools Performance tab
# 1. Open DevTools (F12)
# 2. Switch to Performance tab
# 3. Click Record (or Ctrl+E)
# 4. Interact with app (scroll, tap, navigate)
# 5. Stop recording
# 6. Analyze:
#    - Look for long tasks (>50ms)
#    - Check for layout thrashing
#    - Verify 60fps (green line)
```

---

## Code Review Checklist

Before submitting PR, verify:

### Mobile-First CSS
- [ ] Mobile styles written first (no media query)
- [ ] Tablet styles in `@media (min-width: 768px)`
- [ ] Desktop styles in `@media (min-width: 1024px)`
- [ ] No max-width media queries (desktop-first pattern)
- [ ] No fixed pixel widths that break mobile

### Typography
- [ ] All font sizes use rem/em units
- [ ] Body text ≥16px on mobile (1rem with 16px base)
- [ ] Line height 1.5 for body, 1.25 for headings

### Touch Targets
- [ ] All interactive elements ≥44x44px
- [ ] Visual touch feedback implemented (<100ms)
- [ ] Spacing between adjacent targets ≥8px

### Accessibility
- [ ] All images have alt text
- [ ] All buttons/links have accessible labels
- [ ] Focus indicators visible (2px outline)
- [ ] Keyboard navigation works
- [ ] Color contrast ≥4.5:1 verified
- [ ] aria-live regions for dynamic content

### Performance
- [ ] No console errors/warnings
- [ ] Lighthouse mobile score ≥90
- [ ] Bundle size within budget (<170KB main chunk)
- [ ] Lazy loading for heavy components

### Comparison Removal
- [ ] No references to "Comparison" in code
- [ ] ComparisonView components deleted
- [ ] selectedRepos state removed
- [ ] Routes updated (no /comparison)
- [ ] Navigation tabs updated

---

## Useful Commands

```bash
# Development
npm run dev              # Start dev server (localhost:5173)
npm run build            # Build for production
npm run preview          # Preview production build locally

# Testing
npm test                 # Run unit tests
npm run test:ui          # Run tests with UI
npm run test:coverage    # Coverage report
npm run lighthouse       # Performance audit

# Code Quality
npm run lint             # ESLint check
npm run lint:fix         # Auto-fix lint issues
npm run format           # Prettier format
npm run format:check     # Check formatting

# Cleanup
npm run clean            # Remove build artifacts
```

---

## Troubleshooting

### "Horizontal scroll on mobile"
- Check for fixed pixel widths in CSS
- Verify images have `max-width: 100%`
- Inspect tables - convert to card layout on mobile
- Use Chrome DevTools: Inspect → Computed → Check for overflow

### "Touch targets too small"
- Add this to component CSS:
  ```css
  min-width: 44px;
  min-height: 44px;
  ```
- Verify with axe DevTools or Lighthouse audit

### "Text too small on mobile"
- Check base font size: `:root { font-size: 16px; }`
- Use rem units: `font-size: 1rem` (not `14px`)
- Verify in DevTools: Inspect → Computed → font-size

### "Lighthouse score low"
- Run `npm run build` first (dev server is slower)
- Check bundle sizes in `docs/assets/`
- Lazy load chart components
- Optimize images (use WebP, compress)

### "Screen reader not announcing"
- Add `aria-label` to interactive elements
- Use `role="status"` or `role="alert"` for updates
- Add `aria-live="polite"` for dynamic content
- Test with actual screen reader (VoiceOver/TalkBack)

---

## Resources

### Documentation
- [Research findings](./research.md) - Mobile-first best practices
- [Data model](./data-model.md) - Component state structures
- [Contracts](./contracts/) - Interface definitions

### External Resources
- [MDN: Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)
- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Chrome DevTools Mobile Emulation](https://developer.chrome.com/docs/devtools/device-mode/)

### Tools
- **axe DevTools**: https://www.deque.com/axe/devtools/
- **Lighthouse**: Built into Chrome DevTools
- **React DevTools**: https://react.dev/learn/react-developer-tools
- **BrowserStack**: https://www.browserstack.com/ (optional)

---

## Getting Help

### Questions?
- Check [research.md](./research.md) for design decisions
- Review [data-model.md](./data-model.md) for component structures
- Consult [contracts/](./contracts/) for requirements

### Found a Bug?
1. Verify it reproduces on mobile device (not just DevTools)
2. Check console for errors
3. Document steps to reproduce
4. Include viewport size and device info

### Need to Test on Real Device?
1. Get your local IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Ensure phone on same WiFi network
3. Navigate to `http://YOUR_IP:5173` on phone
4. iOS: May need to allow insecure connections in Settings

---

**Next Steps**: After quickstart, proceed to [tasks.md](./tasks.md) for implementation task breakdown (generated via `/speckit.tasks` command).
