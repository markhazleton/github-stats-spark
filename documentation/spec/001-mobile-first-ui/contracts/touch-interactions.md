# Contract: Touch Interactions

**Feature**: Mobile-First UI Redesign  
**Purpose**: Define touch interaction standards, gesture patterns, and accessibility requirements

## Touch Target Size Contract

### Minimum Size Requirements (WCAG 2.1 Level AA)

**Success Criterion 2.5.5: Target Size**
- **Minimum dimensions**: 44x44 CSS pixels for all interactive elements
- **Exceptions**: Inline text links, targets in sentences (but should still be generously sized)
- **Spacing**: Minimum 8px between adjacent touch targets

### Size Categories

| Element Type | Minimum Width | Minimum Height | Recommended |
|--------------|---------------|----------------|-------------|
| Primary button | 120px | 44px | 140px × 48px |
| Icon button | 44px | 44px | 48px × 48px |
| Text link | (varies) | 44px | Generous padding |
| Form input | 100% | 44px | Full width × 48px |
| Checkbox/Radio | 44px | 44px | 48px × 48px (includes label) |
| Card/List item | 100% | 60px | Full width × 72px+ |
| Navigation tab | 60px | 56px | Equal width × 60px |

### Implementation Pattern

```css
/* Minimum touch target sizing */
.btn, .link-button, .card-clickable {
  min-width: 44px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* Expand hit area for small visual elements */
.icon-button {
  width: 24px; /* Visual icon size */
  height: 24px;
  padding: 10px; /* Expands to 44x44px hit area */
}

/* Spacing between touch targets */
.button-group > * + * {
  margin-left: 8px; /* Minimum gap */
}
```

## Gesture Patterns Contract

### Supported Gestures

| Gesture | Usage | Implementation | Cancel Condition |
|---------|-------|----------------|------------------|
| **Tap** | Select, activate, navigate | Touch down + up within 10px, <300ms | Move >10px, hold >300ms |
| **Swipe** | Navigate, dismiss, reveal actions | Horizontal/vertical drag >100px | Opposite direction drag |
| **Long Press** | Context menu (future) | Touch hold >500ms without movement | Move >10px |
| **Pull to Refresh** | Reload data (future) | Downward drag at scroll top | Release before threshold |

### Tap Gesture Contract

```typescript
interface TapGesture {
  startTime: number
  startPosition: { x: number, y: number }
  endPosition: { x: number, y: number }
  duration: number // milliseconds
  
  // Valid tap criteria
  maxDuration: 300 // ms
  maxMovement: 10 // pixels
}

function isTap(gesture: TapGesture): boolean {
  const distance = Math.sqrt(
    Math.pow(gesture.endPosition.x - gesture.startPosition.x, 2) +
    Math.pow(gesture.endPosition.y - gesture.startPosition.y, 2)
  )
  
  return gesture.duration < 300 && distance < 10
}
```

### Swipe Gesture Contract

```typescript
interface SwipeGesture {
  direction: 'left' | 'right' | 'up' | 'down'
  distance: number // pixels
  velocity: number // pixels per millisecond
  threshold: number // minimum distance to trigger
  
  // Default thresholds
  minDistance: 100 // pixels
  minVelocity: 0.3 // px/ms (300px/s)
}

function detectSwipe(start, end, duration): SwipeGesture | null {
  const deltaX = end.x - start.x
  const deltaY = end.y - start.y
  const distance = Math.sqrt(deltaX ** 2 + deltaY ** 2)
  const velocity = distance / duration
  
  if (distance < 100 || velocity < 0.3) return null
  
  // Determine primary direction
  if (Math.abs(deltaX) > Math.abs(deltaY)) {
    return {
      direction: deltaX > 0 ? 'right' : 'left',
      distance,
      velocity,
      threshold: 100
    }
  } else {
    return {
      direction: deltaY > 0 ? 'down' : 'up',
      distance,
      velocity,
      threshold: 100
    }
  }
}
```

## Touch Feedback Contract

### Visual Feedback Requirements

**Immediate feedback (<100ms)**: All touch interactions must provide visual confirmation within 100ms.

```css
/* Touch active state (replaces hover on touch devices) */
.btn:active,
.card-clickable:active {
  background-color: var(--color-primary-light);
  transform: scale(0.98);
  transition: all 50ms ease-out;
}

/* Ripple effect (Material Design pattern) */
.btn::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
  opacity: 0;
  pointer-events: none;
}

.btn:active::after {
  opacity: 1;
  animation: ripple 0.6s ease-out;
}

@keyframes ripple {
  from {
    transform: scale(0);
    opacity: 1;
  }
  to {
    transform: scale(2);
    opacity: 0;
  }
}
```

### Haptic Feedback (Optional Enhancement)

```javascript
// Vibration API for touch confirmation (if supported)
function provideTouchFeedback() {
  if ('vibrate' in navigator) {
    navigator.vibrate(10) // 10ms gentle vibration
  }
}

// Use sparingly - only for important actions
button.addEventListener('click', () => {
  provideTouchFeedback()
  handleAction()
})
```

## Scroll Behavior Contract

### Mobile Scroll Optimization

```css
/* Smooth scroll on mobile */
html {
  scroll-behavior: smooth;
  /* iOS momentum scrolling */
  -webkit-overflow-scrolling: touch;
}

/* Prevent overscroll bounce on body (but allow on scrollable containers) */
body {
  overscroll-behavior-y: contain;
}

/* Scrollable container */
.scrollable-list {
  overflow-y: auto;
  -webkit-overflow-scrolling: touch; /* iOS momentum */
  overscroll-behavior-y: contain; /* Prevent parent scroll chaining */
}
```

### Scroll Performance
- **Target**: 60fps scrolling on mobile devices
- **Technique**: Use `will-change: transform` for animated elements during scroll
- **Avoid**: Heavy JavaScript calculations during scroll events (use `requestAnimationFrame`)

```javascript
// Optimized scroll handler
let ticking = false

function onScroll() {
  if (!ticking) {
    window.requestAnimationFrame(() => {
      updateScrollPosition()
      ticking = false
    })
    ticking = true
  }
}

window.addEventListener('scroll', onScroll, { passive: true })
```

## Touch vs Mouse Detection

### Device Capability Detection

```javascript
// Detect touch support
const isTouchDevice = (
  'ontouchstart' in window ||
  navigator.maxTouchPoints > 0 ||
  navigator.msMaxTouchPoints > 0
)

// Detect fine pointer (mouse)
const hasFinePointer = window.matchMedia('(pointer: fine)').matches

// Detect coarse pointer (touch)
const hasCoarsePointer = window.matchMedia('(pointer: coarse)').matches
```

### Interaction Mode Switching

```css
/* Hide hover effects on touch devices */
@media (hover: none) {
  .card:hover {
    /* Disable hover state */
    box-shadow: none;
  }
}

/* Show hover effects only on hover-capable devices */
@media (hover: hover) {
  .card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transform: translateY(-2px);
  }
}
```

## Accessibility Requirements

### Keyboard Navigation Equivalents

**Requirement**: All touch gestures MUST have keyboard equivalents.

| Touch Gesture | Keyboard Equivalent | Implementation |
|---------------|---------------------|----------------|
| Tap | Enter or Space | `onClick` handles both |
| Swipe left/right | Arrow keys | `onKeyDown` with ArrowLeft/Right |
| Long press | Context menu key | `onContextMenu` event |
| Scroll | Arrow keys, Page Up/Down | Native browser behavior |

```javascript
// Implement keyboard navigation for swipeable content
function SwipeableCard({ onNext, onPrevious }) {
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
      aria-label="Swipeable card. Use arrow keys to navigate."
    >
      {/* Content */}
    </div>
  )
}
```

### Focus Management

```css
/* Visible focus indicator for keyboard navigation */
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Hide focus for mouse clicks (still shows for keyboard) */
:focus:not(:focus-visible) {
  outline: none;
}
```

### Screen Reader Announcements

```jsx
// Announce gesture results to screen readers
function DismissibleCard({ onDismiss }) {
  const [dismissed, setDismissed] = useState(false)
  
  const handleDismiss = () => {
    setDismissed(true)
    onDismiss()
  }
  
  return (
    <>
      <div
        role="article"
        aria-live="polite"
        aria-atomic="true"
      >
        {dismissed && (
          <span className="sr-only">Card dismissed</span>
        )}
        {/* Card content */}
      </div>
    </>
  )
}
```

## Performance Contract

### Touch Event Performance

```javascript
// Use passive event listeners for scroll performance
element.addEventListener('touchstart', handleTouch, { passive: true })
element.addEventListener('touchmove', handleMove, { passive: true })

// Only use non-passive when preventing default is necessary
element.addEventListener('touchstart', (e) => {
  if (shouldPreventDefault) {
    e.preventDefault()
  }
  handleTouch(e)
}, { passive: false })
```

### Debouncing Touch Events

```javascript
// Debounce rapid touch events (e.g., double-tap prevention)
let lastTouchTime = 0
const TOUCH_DEBOUNCE = 300 // ms

function handleTouch(e) {
  const now = Date.now()
  if (now - lastTouchTime < TOUCH_DEBOUNCE) {
    return // Ignore rapid successive touches
  }
  lastTouchTime = now
  
  // Process touch
}
```

## Testing Requirements

### Touch Interaction Testing Matrix

| Test Case | Method | Expected Result |
|-----------|--------|-----------------|
| Tap accuracy | Tap center of 44x44px target | Action triggers |
| Tap edge accuracy | Tap edge of 44x44px target | Action triggers |
| Adjacent tap prevention | Tap between two targets 8px apart | No accidental activation |
| Swipe gesture | Swipe 100px+ at 300px/s | Direction detected correctly |
| Scroll performance | Scroll rapidly on mobile device | Smooth 60fps, no jank |
| Orientation change | Rotate device | Touch targets remain 44x44px |
| Keyboard alternative | Navigate with keyboard only | All actions accessible |

### Required Test Tools
- **Physical touch devices**: iPhone, Android phone, tablet
- **Chrome DevTools**: Touch event emulation + mobile viewport
- **Touch event visualizer**: Browser extension to show touch/click locations

### Validation Checklist
- [ ] All interactive elements ≥44x44px
- [ ] 8px minimum spacing between adjacent targets
- [ ] Visual feedback within 100ms of touch
- [ ] Swipe gestures work with 100px threshold
- [ ] Keyboard equivalents for all gestures
- [ ] Focus indicators visible on all interactive elements
- [ ] Screen reader announces gesture results
- [ ] 60fps scroll performance maintained

## Error Handling

### Touch Event Failures

```javascript
// Graceful fallback if touch events fail
function setupTouchHandlers(element) {
  if ('ontouchstart' in window) {
    element.addEventListener('touchstart', handleTouchStart)
    element.addEventListener('touchend', handleTouchEnd)
  } else {
    // Fallback to mouse events
    element.addEventListener('mousedown', handleTouchStart)
    element.addEventListener('mouseup', handleTouchEnd)
  }
}
```

### Gesture Recognition Failures

```javascript
// Log gesture failures for debugging
function detectGesture(start, end, duration) {
  const gesture = attemptGestureDetection(start, end, duration)
  
  if (!gesture) {
    console.warn('Gesture detection failed:', {
      start, end, duration,
      distance: calculateDistance(start, end),
      velocity: calculateVelocity(start, end, duration)
    })
    return null
  }
  
  return gesture
}
```

## Version Control

**Version**: 1.0.0  
**Last Updated**: 2026-01-06  
**Breaking Changes**: None (initial version)

## References

- WCAG 2.1 Success Criterion 2.5.5 (Target Size)
- WCAG 2.1 Success Criterion 2.5.1 (Pointer Gestures)
- Apple Human Interface Guidelines: Gestures
- Google Material Design: Touch Targets
- MDN: Touch Events API
