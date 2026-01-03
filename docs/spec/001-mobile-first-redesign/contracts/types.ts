/**
 * Shared Type Definitions
 * Mobile-First Front-End Redesign
 */

// ============================================================================
// Viewport & Breakpoints
// ============================================================================

export type BreakpointName = 'xs' | 'sm' | 'md' | 'lg' | 'xl';

export type Orientation = 'portrait' | 'landscape';

export interface Breakpoint {
  name: BreakpointName;
  minWidth: number;
  maxWidth: number | null;
  isMobile: boolean;
  columns: number;
}

export interface ViewportDimensions {
  width: number;
  height: number;
  orientation: Orientation;
}

// ============================================================================
// Touch & Gestures
// ============================================================================

export type GestureType =
  | 'swipe-left'
  | 'swipe-right'
  | 'swipe-up'
  | 'swipe-down'
  | 'long-press'
  | 'drag'
  | 'pinch';

export type SwipeDirection = 'left' | 'right' | 'up' | 'down';

export interface GestureEvent {
  type: GestureType;
  target: HTMLElement;
  direction?: SwipeDirection;
  distance?: number;
  duration?: number;
  velocity?: number;
  pointerPosition: { x: number; y: number };
  originalEvent: PointerEvent | TouchEvent;
}

export interface TouchFeedback {
  visual: boolean;
  haptic: boolean;
  duration: number;
  color: string;
}

export interface TouchTargetConfig {
  minWidth: number;
  minHeight: number;
  spacing: number;
  feedback: TouchFeedback;
}

// ============================================================================
// Navigation
// ============================================================================

export type TabPosition = 'bottom' | 'top';

export interface TabItem {
  id: string;
  label: string;
  icon: React.ComponentType<{ size?: number; color?: string }>;
  route: string;
  badge?: number;
  ariaLabel: string;
}

// ============================================================================
// Repository Data
// ============================================================================

export interface Repository {
  id: string;
  name: string;
  description: string | null;
  language: string;
  stars: number;
  forks: number;
  lastCommitDate: string;
  commits: number;
  contributors: number;
  technologies: string[];
  url: string;
  // Optional extended fields
  issues?: number;
  pullRequests?: number;
  license?: string;
}

export type RepositoryCardVariant = 'collapsed' | 'expanded';

export type SortField = 'name' | 'stars' | 'commits' | 'lastUpdated' | 'language';

export type SortDirection = 'asc' | 'desc';

export interface SortConfig {
  field: SortField;
  direction: SortDirection;
}

// ============================================================================
// Loading & Empty States
// ============================================================================

export type LoadingType = 'card' | 'table' | 'chart' | 'text' | 'list';

export type LoadingVariant = 'skeleton' | 'spinner' | 'progressive';

export interface SkeletonDimensions {
  titleWidth: string;
  badgeWidth: string;
  metaWidth: string;
  height: string;
}

export interface EmptyStateAction {
  label: string;
  onClick: () => void;
  variant: 'primary' | 'secondary';
  icon?: React.ComponentType<{ size?: number }>;
}

// ============================================================================
// Bottom Sheet
// ============================================================================

export type BottomSheetSnapPoint = number; // 0.0 - 1.0 (percentage of viewport height)

export interface BottomSheetConfig {
  id: string;
  snapPoints: BottomSheetSnapPoint[];
  dismissible: boolean;
  backdrop: boolean;
  closeOnBackdropClick: boolean;
}

// ============================================================================
// Offline Cache
// ============================================================================

export interface CacheEntry<T = any> {
  key: string;
  data: T;
  timestamp: number;
  version: string;
  size: number;
}

export type CacheStatus = 'online' | 'offline' | 'syncing';

export interface CacheConfig {
  storeName: string;
  maxAge: number; // milliseconds
  maxSize?: number; // bytes
}

// ============================================================================
// Performance
// ============================================================================

export type BudgetStatus = 'pass' | 'warn' | 'fail';

export interface BudgetMetric {
  target: number;
  limit: number;
  current: number;
  unit: string;
  status: BudgetStatus;
}

export interface PerformanceBudget {
  jsBundle: BudgetMetric;
  cssBundle: BudgetMetric;
  timeToInteractive: BudgetMetric;
  firstContentfulPaint: BudgetMetric;
  cumulativeLayoutShift: BudgetMetric;
}

// ============================================================================
// Theme & Styling
// ============================================================================

export type ThemeMode = 'light' | 'dark' | 'system';

export interface SafeAreaInsets {
  top: number;
  right: number;
  bottom: number;
  left: number;
}

export interface ThemeConfig {
  mode: ThemeMode;
  safeAreaInsets: SafeAreaInsets;
  reducedMotion: boolean;
}

// ============================================================================
// Network
// ============================================================================

export type ConnectionType = '4g' | '3g' | '2g' | 'slow-2g' | 'unknown';

export type EffectiveConnectionType = 'slow-2g' | '2g' | '3g' | '4g';

export interface NetworkInfo {
  type: ConnectionType;
  effectiveType: EffectiveConnectionType;
  downlink: number; // Mbps
  rtt: number; // Round-trip time in ms
  saveData: boolean;
}

// ============================================================================
// Error Handling
// ============================================================================

export type ErrorSeverity = 'info' | 'warning' | 'error' | 'critical';

export interface AppError {
  message: string;
  severity: ErrorSeverity;
  timestamp: number;
  code?: string;
  details?: Record<string, any>;
  stack?: string;
}

export interface RetryConfig {
  maxAttempts: number;
  delayMs: number;
  backoff: 'linear' | 'exponential';
}

// ============================================================================
// Accessibility
// ============================================================================

export interface A11yConfig {
  announceToScreenReader: (message: string) => void;
  focusElement: (element: HTMLElement) => void;
  skipLinkTarget?: string;
}

export type AriaRole =
  | 'button'
  | 'link'
  | 'navigation'
  | 'dialog'
  | 'menu'
  | 'menuitem'
  | 'tab'
  | 'tabpanel';

// ============================================================================
// Chart/Visualization
// ============================================================================

export type ChartType = 'bar' | 'line' | 'pie' | 'doughnut' | 'radar';

export type ChartOrientation = 'vertical' | 'horizontal';

export interface ChartConfig {
  type: ChartType;
  orientation: ChartOrientation;
  touchOptimized: boolean;
  maxDataPoints: number;
  responsive: boolean;
}

export interface TooltipPosition {
  x: number;
  y: number;
  anchor: 'top' | 'bottom' | 'left' | 'right';
}
