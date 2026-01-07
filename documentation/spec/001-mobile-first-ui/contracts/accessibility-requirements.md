# Contract: Accessibility Requirements

**Feature**: Mobile-First UI Redesign  
**Purpose**: Define WCAG 2.1 Level AA compliance requirements for mobile-first implementation

## WCAG 2.1 Level AA Success Criteria

### Perceivable

#### 1.4.3 Contrast (Minimum) - Level AA

**Requirement**: Color contrast ratio of at least 4.5:1 for normal text and 3:1 for large text.

**Implementation**:
```css
/* All text must meet minimum contrast */
:root {
  --color-text: #24292e; /* On white background: 15.8:1 */
  --color-text-secondary: #586069; /* On white: 7.5:1 */
  --color-text-muted: #6a737d; /* On white: 5.7:1 */
  --color-background: #ffffff;
}

/* Large text (18px+ or 14px bold) requires 3:1 minimum */
.heading {
  color: var(--color-text); /* 15.8:1 - exceeds requirement */
  font-size: 1.5rem; /* 24px */
}

/* Interactive elements require 3:1 contrast */
.btn-primary {
  background: #0366d6; /* Against white: 4.6:1 */
  color: #ffffff; /* Against button: 8.6:1 */
}
```

**Testing**: Use WebAIM Contrast Checker or Chrome DevTools Accessibility panel.

**Validation**:
- [ ] All body text ≥4.5:1 contrast ratio
- [ ] All large text ≥3:1 contrast ratio  
- [ ] All UI components ≥3:1 contrast ratio
- [ ] Contrast maintained in all viewport sizes

---

#### 1.4.4 Resize Text - Level AA

**Requirement**: Text can be resized up to 200% without assistive technology and without loss of content or functionality.

**Implementation**:
```css
/* Use relative units (rem/em) throughout */
html {
  font-size: 16px; /* Base size */
}

body {
  font-size: 1rem; /* Scales with user preference */
  line-height: 1.5;
}

/* Avoid fixed pixel heights that prevent text growth */
.card {
  min-height: 5rem; /* Grows with text */
  padding: 1rem;
}

/* Container max-width in ch units (scales with font) */
.content {
  max-width: 75ch; /* Optimal reading width */
}
```

**Testing**: Browser zoom to 200% on all viewport sizes.

**Validation**:
- [ ] No horizontal scrolling at 200% zoom (mobile)
- [ ] All content remains visible and readable
- [ ] No overlapping text
- [ ] Interactive elements remain usable

---

#### 1.4.10 Reflow - Level AA

**Requirement**: Content can be presented without loss of information or functionality at 320 CSS pixels width without requiring horizontal scrolling.

**Implementation**:
```css
/* Mobile-first approach naturally satisfies this */
@media (max-width: 767px) {
  .container {
    width: 100%;
    padding: 1rem;
    /* No fixed widths that force horizontal scroll */
  }
  
  /* Images scale to container */
  img {
    max-width: 100%;
    height: auto;
  }
  
  /* Tables convert to card layouts */
  .table-responsive {
    display: block;
    /* Transform to vertical card layout on mobile */
  }
}
```

**Testing**: Chrome DevTools Device Mode at 320px width.

**Validation**:
- [ ] No horizontal scroll at 320px viewport
- [ ] All content visible without zooming
- [ ] Vertical scrolling only
- [ ] Two-dimensional scrolling not required

---

#### 1.3.4 Orientation - Level AA

**Requirement**: Content does not restrict its view and operation to a single display orientation (portrait or landscape) unless essential.

**Implementation**:
```css
/* Support both orientations */
@media (orientation: portrait) {
  .component {
    /* Portrait-optimized layout */
    flex-direction: column;
  }
}

@media (orientation: landscape) {
  .component {
    /* Landscape-optimized layout */
    flex-direction: row;
  }
}

/* Do NOT lock orientation */
/* ❌ FORBIDDEN:
@media (orientation: portrait) {
  body {
    transform: rotate(90deg); // Forces orientation
  }
}
*/
```

**Validation**:
- [ ] App works in portrait orientation
- [ ] App works in landscape orientation
- [ ] No orientation lock via CSS or JavaScript
- [ ] Content adapts fluidly to rotation

---

### Operable

#### 2.1.1 Keyboard - Level A (Required for AA)

**Requirement**: All functionality available via keyboard without requiring specific timings.

**Implementation**:
```jsx
// All interactive elements must be keyboard-accessible
function InteractiveCard({ onClick }) {
  return (
    <div
      role="button"
      tabIndex={0}
      onClick={onClick}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault()
          onClick()
        }
      }}
      aria-label="Open repository details"
    >
      {/* Card content */}
    </div>
  )
}

// Swipe gestures must have keyboard alternatives
function SwipeableList({ onNext, onPrevious }) {
  return (
    <div
      tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === 'ArrowLeft') onPrevious()
        if (e.key === 'ArrowRight') onNext()
      }}
      role="region"
      aria-label="Repository list. Use arrow keys to navigate."
    >
      {/* List content */}
    </div>
  )
}
```

**Validation**:
- [ ] All features accessible with keyboard only
- [ ] Tab order is logical
- [ ] No keyboard traps
- [ ] Skip links provided for main content

---

#### 2.4.7 Focus Visible - Level AA

**Requirement**: Keyboard focus indicator is visible.

**Implementation**:
```css
/* Clear focus indicators for all interactive elements */
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Remove focus for mouse clicks (still visible for keyboard) */
:focus:not(:focus-visible) {
  outline: none;
}

/* High contrast focus for buttons */
.btn:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  box-shadow: 0 0 0 4px rgba(3, 102, 214, 0.2);
}

/* Focus within containers */
.card:focus-within {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 2px rgba(3, 102, 214, 0.2);
}
```

**Validation**:
- [ ] Focus indicator visible on all interactive elements
- [ ] Minimum 2px outline width
- [ ] Sufficient color contrast (3:1 minimum)
- [ ] Focus indicator not obscured by other elements

---

#### 2.5.1 Pointer Gestures - Level A (Required for AA)

**Requirement**: All functionality using multipoint or path-based gestures can be operated with a single pointer without path-based gestures.

**Implementation**:
```javascript
// ✅ ALLOWED: Single tap/click
button.addEventListener('click', handleAction)

// ✅ ALLOWED: Single swipe with keyboard alternative
const bind = useGesture({
  onDrag: ({ direction: [dx] }) => {
    if (Math.abs(dx) > 100) {
      handleSwipe(dx > 0 ? 'right' : 'left')
    }
  }
})

// ❌ FORBIDDEN: Pinch zoom without alternative
// (unless browser-native zoom)

// ❌ FORBIDDEN: Two-finger rotate without alternative

// ✅ ALLOWED: Long press with keyboard alternative
const handleLongPress = () => {
  // Accessible via right-click or context menu key
}
```

**Validation**:
- [ ] No multi-finger gestures required
- [ ] No path-based gestures required
- [ ] All gestures have single-pointer alternatives
- [ ] Keyboard alternatives provided

---

#### 2.5.2 Pointer Cancellation - Level A (Required for AA)

**Requirement**: Functions triggered by single pointer can be cancelled before completion.

**Implementation**:
```javascript
// Execute action on pointer UP, not DOWN
// Allows user to drag finger away to cancel

// ✅ CORRECT
button.addEventListener('click', handleAction) // Fires on pointer up

// ❌ INCORRECT
button.addEventListener('mousedown', handleAction) // No cancellation

// Swipe with cancellation
const bind = useGesture({
  onDragEnd: ({ movement: [mx] }) => {
    // Only commits action when gesture ends
    if (Math.abs(mx) > threshold) {
      handleSwipe()
    }
    // User can cancel by reversing direction before release
  }
})
```

**Validation**:
- [ ] Actions trigger on pointer up, not down
- [ ] User can drag away to cancel
- [ ] Accidental activation prevented
- [ ] Essential exceptions documented

---

#### 2.5.5 Target Size - Level AAA (Recommended, but contract requires for mobile)

**Requirement**: Touch targets are at least 44x44 CSS pixels.

**Implementation**:
```css
/* All interactive elements minimum 44x44px */
.btn,
.link,
input,
select,
textarea,
.card-clickable {
  min-width: 44px;
  min-height: 44px;
}

/* Icon buttons with expanded hit area */
.icon-btn {
  width: 24px; /* Visual size */
  height: 24px;
  padding: 10px; /* Expands to 44x44px */
}

/* Spacing between targets */
.btn-group > * + * {
  margin-left: 8px; /* Minimum gap */
}
```

**Validation**:
- [ ] All touch targets ≥44x44px
- [ ] Minimum 8px spacing between adjacent targets
- [ ] Verified with touch event overlay tool
- [ ] Tested on physical touch devices

---

### Understandable

#### 3.2.4 Consistent Identification - Level AA

**Requirement**: Components with same functionality are identified consistently.

**Implementation**:
```jsx
// Consistent icon usage
const ICONS = {
  repository: '📦',
  star: '⭐',
  fork: '🔀',
  commit: '✓',
  language: '💻'
}

// Consistent button labels
const LABELS = {
  viewDetails: 'View Details',
  close: 'Close',
  back: 'Back to List'
}

// Use consistently across all components
<button aria-label={LABELS.viewDetails}>
  {ICONS.repository} {LABELS.viewDetails}
</button>
```

**Validation**:
- [ ] Same icons used for same actions
- [ ] Same labels used for same functions
- [ ] Consistent visual styling for similar elements
- [ ] Predictable behavior across components

---

#### 3.3.1 Error Identification - Level A (Required for AA)

**Requirement**: If an input error is detected, the item in error is identified and described to the user in text.

**Implementation**:
```jsx
function FormField({ value, onChange, error }) {
  return (
    <div>
      <label htmlFor="input">Repository Name</label>
      <input
        id="input"
        value={value}
        onChange={onChange}
        aria-invalid={!!error}
        aria-describedby={error ? 'input-error' : undefined}
      />
      {error && (
        <div id="input-error" role="alert">
          {error}
        </div>
      )}
    </div>
  )
}
```

**Validation**:
- [ ] Errors announced to screen readers
- [ ] Error messages in text, not just color
- [ ] `aria-invalid` attribute on error fields
- [ ] `aria-describedby` links to error message

---

### Robust

#### 4.1.3 Status Messages - Level AA

**Requirement**: Status messages can be programmatically determined through role or properties.

**Implementation**:
```jsx
// Success/error toasts with announcements
function Toast({ message, variant }) {
  return (
    <div
      role={variant === 'error' ? 'alert' : 'status'}
      aria-live={variant === 'error' ? 'assertive' : 'polite'}
      aria-atomic="true"
    >
      {message}
    </div>
  )
}

// Loading states
function LoadingState({ message }) {
  return (
    <div
      role="status"
      aria-live="polite"
      aria-busy="true"
    >
      <span className="sr-only">{message}</span>
      <Spinner />
    </div>
  )
}
```

**Validation**:
- [ ] Status messages use `role="status"` or `role="alert"`
- [ ] `aria-live` regions for dynamic updates
- [ ] Screen reader announces status changes
- [ ] Visual and auditory feedback provided

---

## Mobile-Specific Accessibility

### Touch Gestures Accessibility

```javascript
// All gestures must have keyboard + screen reader alternatives
function AccessibleGesture({ onSwipeLeft, onSwipeRight }) {
  return (
    <div
      {...useGesture({
        onDrag: ({ direction: [dx] }) => {
          if (dx > 100) onSwipeRight()
          if (dx < -100) onSwipeLeft()
        }
      })}
      onKeyDown={(e) => {
        if (e.key === 'ArrowLeft') onSwipeLeft()
        if (e.key === 'ArrowRight') onSwipeRight()
      }}
      role="region"
      aria-label="Swipeable content. Use left/right arrow keys to navigate."
      tabIndex={0}
    >
      {/* Content */}
    </div>
  )
}
```

### Screen Reader Mobile Optimization

```jsx
// Hide decorative elements from screen readers
<span aria-hidden="true">🎉</span>

// Provide text alternatives for icons
<button aria-label="Star repository">
  <span aria-hidden="true">⭐</span>
</button>

// Announce dynamic content changes
<div role="status" aria-live="polite">
  {loadingRepositories && 'Loading repositories...'}
  {repositoriesLoaded && `Loaded ${count} repositories`}
</div>
```

### Reduced Motion Preference

```css
/* Respect prefers-reduced-motion setting */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Testing Requirements

### Automated Testing

**Tools**:
- axe DevTools browser extension
- WAVE Web Accessibility Evaluation Tool
- Lighthouse Accessibility Audit

**Minimum Scores**:
- Lighthouse Accessibility: 100 (no critical violations)
- axe DevTools: 0 violations (critical/serious)
- WAVE: 0 errors

### Manual Testing

**Screen Readers**:
- VoiceOver (iOS Safari): Primary mobile screen reader
- TalkBack (Android Chrome): Primary Android screen reader
- NVDA (Windows): Desktop testing

**Keyboard Navigation**:
- Tab through all interactive elements
- Test all keyboard shortcuts
- Verify focus visibility
- Ensure no keyboard traps

**Touch Testing**:
- Test on physical iOS device (iPhone)
- Test on physical Android device
- Verify touch target sizes
- Test gesture alternatives

### Test Matrix

| Success Criterion | Test Method | Expected Result | Priority |
|-------------------|-------------|-----------------|----------|
| 1.4.3 Contrast | WebAIM Contrast Checker | All text ≥4.5:1 | P1 |
| 1.4.4 Resize Text | Browser zoom 200% | No loss of content | P1 |
| 1.4.10 Reflow | DevTools @ 320px | No horizontal scroll | P1 |
| 1.3.4 Orientation | Physical device rotation | Works both ways | P1 |
| 2.1.1 Keyboard | Keyboard only navigation | All features accessible | P1 |
| 2.4.7 Focus Visible | Tab navigation | Focus clearly visible | P1 |
| 2.5.5 Target Size | Touch overlay tool | All targets ≥44px | P1 |
| 4.1.3 Status Messages | Screen reader | Announcements heard | P2 |

## Validation Checklist

### Pre-Deployment Checks

- [ ] **Automated axe scan**: 0 critical violations
- [ ] **Lighthouse audit**: Accessibility score 100
- [ ] **Contrast check**: All text meets 4.5:1 (normal) or 3:1 (large)
- [ ] **Keyboard navigation**: Complete site traversable with keyboard
- [ ] **Focus indicators**: Visible on all interactive elements
- [ ] **Touch targets**: All ≥44x44px with 8px spacing
- [ ] **Screen reader**: VoiceOver + TalkBack testing complete
- [ ] **Orientation**: Portrait and landscape both functional
- [ ] **Zoom**: 200% zoom no content loss
- [ ] **Reflow**: 320px width no horizontal scroll
- [ ] **Reduced motion**: Respects prefers-reduced-motion
- [ ] **Status messages**: aria-live announcements working

## Error Handling

### Accessibility Failures

```javascript
// Log accessibility issues in development
if (process.env.NODE_ENV === 'development') {
  // Check for missing alt text
  document.querySelectorAll('img:not([alt])').forEach(img => {
    console.error('Missing alt text on image:', img.src)
  })
  
  // Check for interactive elements without labels
  document.querySelectorAll('button:not([aria-label]):not(:has(> *))').forEach(btn => {
    console.error('Button missing accessible label:', btn)
  })
}
```

### Graceful Degradation

```javascript
// Fallback for assistive technologies
if (!('IntersectionObserver' in window)) {
  // Load all content immediately instead of lazy loading
  loadAllContent()
}

// Fallback for reduced motion preference
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
if (prefersReducedMotion) {
  disableAnimations()
}
```

## Version Control

**Version**: 1.0.0  
**Last Updated**: 2026-01-06  
**Standard**: WCAG 2.1 Level AA  
**Breaking Changes**: None (initial version)

## References

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Apple Accessibility for Developers](https://developer.apple.com/accessibility/)
- [Google Web Accessibility Fundamentals](https://web.dev/accessibility/)
- [axe-core Rules Library](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md)
- [WebAIM: Designing for Screen Reader Compatibility](https://webaim.org/articles/screenreader_testing/)
