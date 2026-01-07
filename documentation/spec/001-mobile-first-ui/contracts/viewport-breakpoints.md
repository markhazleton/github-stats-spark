# Contract: Viewport Breakpoints

**Feature**: Mobile-First UI Redesign  
**Purpose**: Define responsive breakpoint standards and viewport detection requirements

## Breakpoint Definitions

### Mobile Breakpoint
- **Range**: 320px - 767px
- **Target Devices**: Smartphones (iPhone SE 375px to Pro Max 428px, Android phones)
- **Layout**: Single column, bottom tab navigation, touch-optimized
- **Base Font Size**: 16px (prevents iOS zoom)
- **Touch Target Minimum**: 44x44px

### Tablet Breakpoint
- **Range**: 768px - 1023px  
- **Target Devices**: iPad (768px portrait), iPad Pro (1024px portrait), Android tablets
- **Layout**: 2 column grid, hamburger menu or expanded navigation
- **Base Font Size**: 18px
- **Touch Target Minimum**: 44x44px (still touch-first)

### Desktop Breakpoint
- **Range**: 1024px and above
- **Target Devices**: Laptops, desktops, large tablets in landscape
- **Layout**: 3+ column grid, full horizontal navigation, enhanced hover states
- **Base Font Size**: 20px
- **Touch Target Minimum**: 44x44px (progressive enhancement, maintains touch capability)

## Media Query Contract

### Standard Format (min-width, mobile-first)

```css
/* Mobile styles (default, no media query) */
.component {
  /* Styles for 320px+ */
}

/* Tablet styles */
@media (min-width: 768px) {
  .component {
    /* Override/enhance for tablet */
  }
}

/* Desktop styles */
@media (min-width: 1024px) {
  .component {
    /* Override/enhance for desktop */
  }
}
```

### JavaScript Breakpoint Detection

```javascript
const BREAKPOINTS = {
  mobile: { min: 320, max: 767 },
  tablet: { min: 768, max: 1023 },
  desktop: { min: 1024, max: Infinity }
}

// matchMedia API usage
const isMobile = window.matchMedia('(max-width: 767px)').matches
const isTablet = window.matchMedia('(min-width: 768px) and (max-width: 1023px)').matches
const isDesktop = window.matchMedia('(min-width: 1024px)').matches
```

## Viewport Context API Contract

### Provider Interface

```typescript
interface ViewportContextValue {
  // Current viewport dimensions
  width: number
  height: number
  
  // Breakpoint state
  currentBreakpoint: 'mobile' | 'tablet' | 'desktop'
  isMobile: boolean
  isTablet: boolean
  isDesktop: boolean
  
  // Device capabilities
  orientation: 'portrait' | 'landscape'
  isTouchDevice: boolean
  isRetina: boolean
  
  // Safe area (iOS notch/home indicator)
  safeArea: {
    top: number
    right: number
    bottom: number
    left: number
  }
}
```

### Consumer Hook Interface

```typescript
// Usage in components
function MyComponent() {
  const { isMobile, isTablet, isDesktop } = useViewport()
  
  // Or more specific hook
  const isMobile = useMediaQuery('(max-width: 767px)')
  
  return isMobile ? <MobileView /> : <DesktopView />
}
```

## Orientation Contract

### Supported Orientations
- **Portrait**: Primary orientation for mobile (width < height)
- **Landscape**: Supported on all devices (width > height)
- **No orientation locking**: Content must adapt to both orientations

### Orientation-Specific Styles

```css
/* Mobile landscape optimization */
@media (max-width: 767px) and (orientation: landscape) {
  .component {
    /* Optimize for wide, short viewport */
    height: 100vh; /* Use full height */
    flex-direction: row; /* Horizontal layout */
  }
}

/* Tablet landscape (treat more like desktop) */
@media (min-width: 768px) and (orientation: landscape) {
  .component {
    columns: 3; /* More columns available */
  }
}
```

## Viewport Meta Tag Contract

### Required Configuration

```html
<meta 
  name="viewport" 
  content="width=device-width, initial-scale=1.0, viewport-fit=cover"
/>
```

**Explanation**:
- `width=device-width`: Use device's natural width, not scaled desktop view
- `initial-scale=1.0`: Start at 1:1 pixel ratio (no zoom)
- `viewport-fit=cover`: iOS - extend content into safe areas (notch, home indicator)

### Forbidden Attributes
❌ `user-scalable=no` - Violates WCAG 2.1 (prevents accessibility zoom)
❌ `maximum-scale=1` - Same violation
✅ Allow user to pinch-zoom for accessibility

## Testing Requirements

### Viewport Testing Matrix

| Device Class | Test Widths | Orientation | Priority |
|--------------|-------------|-------------|----------|
| Mobile Small | 320px, 375px | Portrait | P1 |
| Mobile Large | 414px, 428px | Portrait | P1 |
| Mobile Landscape | 667px, 812px | Landscape | P2 |
| Tablet Portrait | 768px, 834px | Portrait | P2 |
| Tablet Landscape | 1024px, 1180px | Landscape | P3 |
| Desktop | 1280px, 1920px | Landscape | P3 |

### Required Test Tools
- **Chrome DevTools Device Mode**: Test all responsive breakpoints
- **Real Device Testing**: At least 1 iOS phone, 1 Android phone, 1 tablet
- **BrowserStack/Sauce Labs**: Cross-browser viewport testing (optional but recommended)

### Validation Criteria
✅ No horizontal scroll at any breakpoint  
✅ All content visible and readable without zooming  
✅ Layout doesn't break during viewport resize  
✅ Orientation changes handled gracefully (no content cutoff)  
✅ Touch targets remain ≥44px at all breakpoints  

## Performance Contract

### Breakpoint Detection Performance
- **Initial detection**: <10ms on mount
- **Resize debouncing**: 150ms delay (balance between responsiveness and performance)
- **No layout thrashing**: Use `ResizeObserver` or debounced `window.resize` listener

```javascript
// Debounced resize handler
const handleResize = debounce(() => {
  updateViewportState(window.innerWidth, window.innerHeight)
}, 150)

window.addEventListener('resize', handleResize)
```

### CSS Performance
- **Single stylesheet**: No separate mobile/tablet/desktop CSS files (increases HTTP requests)
- **Critical CSS inlining**: Inline mobile-first base styles in `<head>` for faster first paint
- **Media query consolidation**: Group breakpoint styles together to reduce rule duplication

## Error Handling

### Unsupported Viewport Scenarios

```javascript
// Warn for very small viewports (<320px)
if (window.innerWidth < 320) {
  console.warn(
    'Viewport width below minimum support threshold (320px). ' +
    'Layout may not render correctly.'
  )
}

// Warn for very large viewports (>2560px)
if (window.innerWidth > 2560) {
  console.warn(
    'Viewport width exceeds tested range (2560px). ' +
    'Layout may not utilize screen space optimally.'
  )
}
```

### Fallback Strategy
- If viewport detection fails, default to **mobile layout** (safest assumption)
- Log error to console with instructions for reporting issue
- Graceful degradation: app remains functional even if viewport detection broken

## Accessibility Contract

### WCAG 2.1 Success Criteria

**1.4.4 Resize Text (Level AA)**:
- Text must be resizable up to 200% without loss of content or functionality
- Use relative units (rem/em) to respect user font size preferences

**1.4.10 Reflow (Level AA)**:
- Content must reflow at 320 CSS pixels width without horizontal scrolling
- No two-dimensional scrolling required for reading order

**1.3.4 Orientation (Level AA)**:
- Content must not be restricted to a single orientation (portrait or landscape)
- Exception: If specific orientation is essential to the functionality

### Implementation Requirements
- Use `prefers-reduced-motion` media query for users with motion sensitivity
- Ensure focus indicators visible at all breakpoints
- Test with browser zoom at 200% on all breakpoints

## Version Control

**Version**: 1.0.0  
**Last Updated**: 2026-01-06  
**Breaking Changes**: None (initial version)

## References

- WCAG 2.1 Success Criterion 1.4.4 (Resize Text)
- WCAG 2.1 Success Criterion 1.4.10 (Reflow)
- WCAG 2.1 Success Criterion 1.3.4 (Orientation)
- MDN: Responsive Design
- CSS-Tricks: A Complete Guide to CSS Media Queries
