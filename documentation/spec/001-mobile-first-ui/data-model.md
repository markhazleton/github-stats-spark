# Data Model: Mobile-First UI Components

**Date**: 2026-01-06  
**Feature**: [spec.md](./spec.md)  
**Purpose**: Define component state models and data structures for mobile-first redesign

## Overview

This document defines the logical data models (entities) required for the mobile-first UI implementation. These models represent component state, configuration objects, and interaction patterns - NOT database schemas or API contracts (data/repositories.json remains unchanged).

---

## 1. Viewport Configuration

**Purpose**: Represents responsive breakpoint definitions and current viewport state.

### Attributes

| Attribute | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `currentBreakpoint` | enum | Active breakpoint name | 'mobile', 'tablet', 'desktop' |
| `width` | number | Current viewport width in pixels | 375, 768, 1920 |
| `height` | number | Current viewport height in pixels | 667, 1024, 1080 |
| `isMobile` | boolean | Derived: width < 768px | true, false |
| `isTablet` | boolean | Derived: 768px ≤ width < 1024px | true, false |
| `isDesktop` | boolean | Derived: width ≥ 1024px | true, false |
| `orientation` | enum | Device orientation | 'portrait', 'landscape' |
| `isTouchDevice` | boolean | Supports touch events | true, false |
| `isRetina` | boolean | High DPI display (window.devicePixelRatio > 1) | true, false |

### Breakpoint Definitions

```javascript
const BREAKPOINTS = {
  mobile: { min: 320, max: 767 },
  tablet: { min: 768, max: 1023 },
  desktop: { min: 1024, max: Infinity }
}
```

### State Management
- **Provider**: `ViewportContext.jsx` (already exists)
- **Consumer Hook**: `useMediaQuery()` hook
- **Update Trigger**: `window.resize` event listener with debouncing

### Relationships
- Consumed by: All layout components, responsive components
- Affects: Navigation pattern, grid column count, typography scale

---

## 2. Touch Target

**Purpose**: Represents interactive UI elements with mobile-optimized sizing and hit areas.

### Attributes

| Attribute | Type | Description | Constraints |
|-----------|------|-------------|-------------|
| `visualWidth` | number | Visible width in pixels | Any positive number |
| `visualHeight` | number | Visible height in pixels | Any positive number |
| `hitAreaWidth` | number | Touch-interactive width | ≥44px (WCAG 2.1 requirement) |
| `hitAreaHeight` | number | Touch-interactive height | ≥44px (WCAG 2.1 requirement) |
| `padding` | object | Additional touch padding | `{ top, right, bottom, left }` |
| `hasVisibleFocus` | boolean | Focus indicator enabled | Required for accessibility |
| `isDisabled` | boolean | Interaction disabled state | Reduces opacity, no events |

### Sizing Rules

```javascript
// Minimum touch target calculation
const effectiveTouchArea = {
  width: Math.max(visualWidth + padding.left + padding.right, 44),
  height: Math.max(visualHeight + padding.top + padding.bottom, 44)
}
```

### Examples

**Standard Button**:
```javascript
{
  visualWidth: 120,
  visualHeight: 40,
  hitAreaWidth: 120,
  hitAreaHeight: 44, // Padded to minimum
  padding: { top: 2, right: 0, bottom: 2, left: 0 },
  hasVisibleFocus: true,
  isDisabled: false
}
```

**Icon Button**:
```javascript
{
  visualWidth: 24, // Small icon
  visualHeight: 24,
  hitAreaWidth: 44, // Expanded via padding
  hitAreaHeight: 44,
  padding: { top: 10, right: 10, bottom: 10, left: 10 },
  hasVisibleFocus: true,
  isDisabled: false
}
```

---

## 3. Responsive Layout Grid

**Purpose**: Represents the adaptive column system for repository cards and content layout.

### Attributes

| Attribute | Type | Description | Values |
|-----------|------|-------------|--------|
| `columns` | number | Number of columns at current breakpoint | 1 (mobile), 2 (tablet), 3+ (desktop) |
| `gap` | number | Spacing between grid items in pixels | 16px (mobile), 24px (tablet/desktop) |
| `containerPadding` | number | Horizontal padding on container | 16px (mobile), 32px (tablet/desktop) |
| `maxWidth` | number | Maximum container width | 1280px (desktop) |
| `flow` | enum | Grid flow direction | 'row' (default), 'column' |

### Breakpoint-Specific Configurations

```javascript
const GRID_CONFIG = {
  mobile: {
    columns: 1,
    gap: 16,
    containerPadding: 16,
    maxWidth: null // Full width
  },
  tablet: {
    columns: 2,
    gap: 24,
    containerPadding: 32,
    maxWidth: null
  },
  desktop: {
    columns: 3,
    gap: 24,
    containerPadding: 32,
    maxWidth: 1280
  }
}
```

### Derived Values

```javascript
// Column width calculation
const itemWidth = (
  (containerWidth - containerPadding * 2 - gap * (columns - 1)) / columns
)
```

### State Transitions
- Mobile → Tablet: 1 column → 2 columns
- Tablet → Desktop: 2 columns → 3 columns
- Orientation change: May adjust column count (landscape tablet = 3 columns)

---

## 4. Typography Scale

**Purpose**: Font sizing hierarchy that scales proportionally across viewports.

### Attributes

| Attribute | Type | Description | Mobile (16px base) | Tablet (18px base) | Desktop (20px base) |
|-----------|------|-------------|--------------------|--------------------|---------------------|
| `baseSize` | number | Root font size (px) | 16 | 18 | 20 |
| `scale` | object | Size multipliers in rem | See table below | | |

### Size Scale (rem units)

| Element | rem Value | Mobile (px) | Tablet (px) | Desktop (px) |
|---------|-----------|-------------|-------------|--------------|
| `xs` | 0.75rem | 12 | 13.5 | 15 |
| `sm` | 0.875rem | 14 | 15.75 | 17.5 |
| `base` | 1rem | 16 | 18 | 20 |
| `lg` | 1.125rem | 18 | 20.25 | 22.5 |
| `xl` | 1.25rem | 20 | 22.5 | 25 |
| `2xl` | 1.5rem | 24 | 27 | 30 |
| `3xl` | 1.875rem | 30 | 33.75 | 37.5 |

### Line Height Ratios

| Type | Ratio | Purpose |
|------|-------|---------|
| Body text | 1.5 | Optimal readability |
| Headings | 1.25 | Tighter spacing for hierarchy |
| Small text | 1.4 | Compensates for smaller size |

### Implementation

```css
:root {
  font-size: 16px; /* Mobile base */
}

body {
  font-size: 1rem; /* Inherits from :root */
  line-height: 1.5;
}

@media (min-width: 768px) {
  :root { font-size: 18px; } /* All rem values scale automatically */
}

@media (min-width: 1024px) {
  :root { font-size: 20px; }
}
```

---

## 5. Navigation State

**Purpose**: Represents current navigation pattern based on viewport and user interaction.

### Attributes

| Attribute | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `pattern` | enum | Navigation UI pattern | 'bottom-tab', 'hamburger', 'full-nav' |
| `isOpen` | boolean | Mobile menu open state | true, false |
| `activeTab` | string | Currently active view/tab | 'table', 'visualizations' |
| `position` | enum | Navigation placement | 'bottom', 'top', 'left' |
| `hasBackButton` | boolean | Shows back navigation | true (detail view), false (main view) |

### Pattern Rules (Viewport-Dependent)

```javascript
const getNavigationPattern = (viewport) => {
  if (viewport.isMobile) {
    return {
      pattern: 'bottom-tab',
      position: 'bottom',
      isOpen: false, // Always visible as tab bar
      hasBackButton: false
    }
  }
  
  if (viewport.isTablet) {
    return {
      pattern: 'hamburger',
      position: 'top',
      isOpen: false, // Collapsible
      hasBackButton: false
    }
  }
  
  return {
    pattern: 'full-nav',
    position: 'top',
    isOpen: true, // Always expanded
    hasBackButton: false
  }
}
```

### State Transitions

| Trigger | Mobile | Tablet | Desktop |
|---------|--------|--------|---------|
| Initial load | Bottom tab visible | Hamburger collapsed | Full nav expanded |
| User tap menu | N/A | Toggle hamburger | N/A |
| Navigate to detail | Back button appears | Back button appears | Back button appears |
| Viewport resize | Switch pattern | Switch pattern | Switch pattern |

### Components Affected
- **Mobile**: `TabBar` component (bottom tabs)
- **Tablet**: `HeaderNav` component with hamburger icon
- **Desktop**: `HeaderNav` component with full horizontal menu

---

## 6. Repository Card

**Purpose**: Represents a single repository's display unit with adaptive presentation density.

### Attributes

| Attribute | Type | Description | Required |
|-----------|------|-------------|----------|
| `repository` | object | Full repository data from data/repositories.json | Yes |
| `displayDensity` | enum | Content density level | 'compact', 'comfortable', 'spacious' |
| `isExpanded` | boolean | Shows full description/details | No (default: false) |
| `isClickable` | boolean | Card is interactive | Yes |
| `showActions` | boolean | Display action buttons | Yes (mobile: false) |
| `highlightedMetrics` | array | Key metrics to emphasize | ['stars', 'language', 'commits'] |

### Display Density Rules

```javascript
const DENSITY_CONFIG = {
  compact: {
    viewports: ['mobile'],
    padding: 12,
    fontSize: 14,
    showDescription: false,
    maxMetrics: 3,
    layout: 'vertical'
  },
  comfortable: {
    viewports: ['tablet'],
    padding: 16,
    fontSize: 16,
    showDescription: 'truncated', // 2 lines
    maxMetrics: 5,
    layout: 'vertical'
  },
  spacious: {
    viewports: ['desktop'],
    padding: 24,
    fontSize: 16,
    showDescription: 'full',
    maxMetrics: 8,
    layout: 'horizontal'
  }
}
```

### Responsive Behavior

**Mobile (<768px)**:
```
┌─────────────────────────────┐
│ 📦 Repository Name          │
│ ⭐ 123  🔀 45  ✓ Python     │
│ [Tap to view details]       │
└─────────────────────────────┘
```

**Tablet (768-1023px)**:
```
┌────────────────────┬────────────────────┐
│ 📦 Repository Name │ 📦 Repository Name │
│ Short description  │ Short description  │
│ ⭐ 123  🔀 45      │ ⭐ 89  🔀 12       │
│ ✓ Python           │ ✓ JavaScript       │
└────────────────────┴────────────────────┘
```

**Desktop (1024px+)**:
```
┌─────────────────────────────────────────────────────────┐
│ 📦 Repository Name                         ⭐ 123  🔀 45 │
│ Full description text explaining the repository purpose │
│ ✓ Python  📊 1,234 commits  📅 Active  ⏰ Updated 2d ago│
│ [View Details] [Visit GitHub] [Download]                │
└─────────────────────────────────────────────────────────┘
```

### State Management
- Parent manages `isExpanded` state for each card
- Click handler in parent triggers detail view modal
- Cards are pure presentational components (no internal state)

---

## 7. Touch Gesture State

**Purpose**: Tracks active gesture interactions for swipe, drag, and tap actions.

### Attributes

| Attribute | Type | Description | Values |
|-----------|------|-------------|--------|
| `isActive` | boolean | Gesture in progress | true, false |
| `gestureType` | enum | Type of gesture | 'swipe', 'tap', 'drag', 'long-press' |
| `startPosition` | object | Initial touch coordinates | `{ x, y }` |
| `currentPosition` | object | Current touch coordinates | `{ x, y }` |
| `velocity` | object | Swipe velocity | `{ x, y }` in px/ms |
| `direction` | enum | Swipe direction | 'left', 'right', 'up', 'down' |
| `threshold` | number | Distance to trigger action | 100px (default) |

### Gesture Detection Logic

```javascript
const detectGesture = (start, current, velocity) => {
  const deltaX = current.x - start.x
  const deltaY = current.y - start.y
  const distance = Math.sqrt(deltaX ** 2 + deltaY ** 2)
  
  if (distance < 10) return 'tap'
  if (Math.abs(deltaX) > Math.abs(deltaY)) {
    return deltaX > threshold ? 'swipe-right' : 'swipe-left'
  }
  return deltaY > threshold ? 'swipe-down' : 'swipe-up'
}
```

### Use Cases
- **Swipe left/right on card**: Dismiss, reveal actions
- **Swipe left/right on modal**: Navigate between repositories
- **Tap**: Select, open detail
- **Long press**: Show context menu (future feature)

---

## Entity Relationships

```
ViewportConfiguration
  ↓ (determines)
NavigationState
  ↓ (affects)
ResponsiveLayoutGrid
  ↓ (contains)
RepositoryCard[]
  ↓ (each has)
TouchTarget (for interactive areas)

TypographyScale
  ↓ (applied to)
RepositoryCard, NavigationState, All UI Components

TouchGestureState
  ↓ (modifies)
RepositoryCard.isExpanded, NavigationState.activeTab
```

## Data Flow

1. **Viewport Detection**: `ViewportContext` detects screen size on mount/resize
2. **Layout Adaptation**: Components query viewport state via `useMediaQuery()` hook
3. **Grid Configuration**: `ResponsiveLayoutGrid` selects column count based on viewport
4. **Card Rendering**: `RepositoryCard` adjusts density based on viewport
5. **Navigation Update**: `NavigationState` switches pattern (tab bar vs hamburger vs full)
6. **Typography Scaling**: CSS `rem` values automatically scale with viewport-based `:root` font-size
7. **Touch Interaction**: `TouchGestureState` tracks user interactions, triggers state updates

## Validation Rules

### Touch Target Validation
```javascript
const validateTouchTarget = (target) => {
  const errors = []
  if (target.hitAreaWidth < 44) {
    errors.push('Touch target width must be ≥44px (WCAG 2.1 violation)')
  }
  if (target.hitAreaHeight < 44) {
    errors.push('Touch target height must be ≥44px (WCAG 2.1 violation)')
  }
  return errors
}
```

### Typography Validation
```javascript
const validateTypography = (element, viewport) => {
  const minSize = viewport.isMobile ? 16 : 14 // Mobile requires 16px minimum
  if (element.fontSize < minSize) {
    throw new Error(`Font size ${element.fontSize}px violates mobile minimum (${minSize}px)`)
  }
}
```

### Viewport Configuration Validation
```javascript
const validateViewport = (config) => {
  if (config.width < 320) {
    console.warn('Viewport width below minimum support threshold (320px)')
  }
  if (!['mobile', 'tablet', 'desktop'].includes(config.currentBreakpoint)) {
    throw new Error('Invalid breakpoint value')
  }
}
```

---

## Summary

These data models represent the core state structures required for mobile-first implementation:

| Model | Purpose | Key Attributes | Consumers |
|-------|---------|----------------|-----------|
| **Viewport Configuration** | Responsive breakpoint detection | width, isMobile, isTablet, isDesktop | All layout components |
| **Touch Target** | Mobile-optimized interaction areas | hitAreaWidth, hitAreaHeight ≥44px | All buttons, links, cards |
| **Responsive Layout Grid** | Adaptive column system | columns (1/2/3), gap, padding | Repository list, card grids |
| **Typography Scale** | Scalable font hierarchy | baseSize (16/18/20px), rem units | All text content |
| **Navigation State** | Adaptive navigation patterns | pattern (tab/hamburger/full) | Header, TabBar components |
| **Repository Card** | Adaptive content density | displayDensity, isExpanded | Repository list rendering |
| **Touch Gesture State** | User interaction tracking | gestureType, velocity, direction | Swipeable cards, modals |

**Next**: Create contracts for component interfaces and accessibility requirements.
