/**
 * Custom Hooks API Contracts
 * Mobile-First Front-End Redesign
 */

import {
  BreakpointName,
  ViewportDimensions,
  Orientation,
  GestureType,
  GestureEvent,
  CacheEntry,
  CacheStatus,
  NetworkInfo,
  ThemeMode,
  SafeAreaInsets,
  BottomSheetSnapPoint,
} from './types';

// ============================================================================
// Viewport & Responsive Hooks
// ============================================================================

export interface UseMediaQueryReturn {
  matches: boolean;
}

/**
 * Hook: useMediaQuery(query: string)
 *
 * @example
 * const isMobile = useMediaQuery('(max-width: 767px)');
 */
export type UseMediaQuery = (query: string) => UseMediaQueryReturn['matches'];

export interface UseBreakpointReturn {
  current: BreakpointName;
  isMobile: boolean;
  isTablet: boolean;
  isDesktop: boolean;
  width: number;
  height: number;
}

/**
 * Hook: useBreakpoint()
 *
 * @example
 * const { current, isMobile } = useBreakpoint();
 */
export type UseBreakpoint = () => UseBreakpointReturn;

export interface UseViewportReturn {
  dimensions: ViewportDimensions;
  orientation: Orientation;
  isMobile: boolean;
}

/**
 * Hook: useViewport()
 *
 * @example
 * const { dimensions, orientation } = useViewport();
 */
export type UseViewport = () => UseViewportReturn;

export interface UseSafeAreaReturn {
  insets: SafeAreaInsets;
  applyInsets: (edges: Array<'top' | 'right' | 'bottom' | 'left'>) => React.CSSProperties;
}

/**
 * Hook: useSafeArea()
 *
 * @example
 * const { insets, applyInsets } = useSafeArea();
 * const style = applyInsets(['bottom']);
 */
export type UseSafeArea = () => UseSafeAreaReturn;

// ============================================================================
// Gesture & Touch Hooks
// ============================================================================

export interface UseGestureConfig {
  threshold?: number;
  enabled?: boolean;
}

export interface UseGestureReturn {
  bind: () => Record<string, any>; // Event handlers from @use-gesture/react
  handlers: {
    onSwipeLeft?: (event: GestureEvent) => void;
    onSwipeRight?: (event: GestureEvent) => void;
    onSwipeUp?: (event: GestureEvent) => void;
    onSwipeDown?: (event: GestureEvent) => void;
    onLongPress?: (event: GestureEvent) => void;
    onDrag?: (event: GestureEvent) => void;
  };
}

/**
 * Hook: useGesture(handlers, config)
 *
 * @example
 * const { bind } = useGesture({
 *   onSwipeLeft: (e) => handleDelete(e.target.dataset.id)
 * }, { threshold: 50 });
 *
 * <div {...bind()}>Swipe me</div>
 */
export type UseGesture = (
  handlers: UseGestureReturn['handlers'],
  config?: UseGestureConfig
) => Pick<UseGestureReturn, 'bind'>;

export interface UseLongPressConfig {
  threshold?: number; // milliseconds
  onStart?: () => void;
  onCancel?: () => void;
}

export interface UseLongPressReturn {
  onTouchStart: (event: React.TouchEvent) => void;
  onTouchEnd: (event: React.TouchEvent) => void;
  onTouchMove: (event: React.TouchEvent) => void;
  isPressed: boolean;
}

/**
 * Hook: useLongPress(callback, config)
 *
 * @example
 * const longPressHandlers = useLongPress(() => {
 *   console.log('Long pressed!');
 * }, { threshold: 500 });
 *
 * <button {...longPressHandlers}>Long press me</button>
 */
export type UseLongPress = (
  callback: () => void,
  config?: UseLongPressConfig
) => UseLongPressReturn;

export interface UseHapticReturn {
  vibrate: (pattern?: number | number[]) => void;
  supported: boolean;
}

/**
 * Hook: useHaptic()
 *
 * @example
 * const { vibrate, supported } = useHaptic();
 * if (supported) vibrate(10); // 10ms vibration
 */
export type UseHaptic = () => UseHapticReturn;

// ============================================================================
// Bottom Sheet Hook
// ============================================================================

export interface UseBottomSheetConfig {
  snapPoints?: BottomSheetSnapPoint[];
  initialSnap?: number;
  dismissible?: boolean;
}

export interface UseBottomSheetReturn {
  isOpen: boolean;
  currentSnap: number;
  open: (snapIndex?: number) => void;
  close: () => void;
  toggle: () => void;
  snapTo: (index: number) => void;
  sheetRef: React.RefObject<HTMLDivElement>;
}

/**
 * Hook: useBottomSheet(config)
 *
 * @example
 * const { isOpen, open, close, sheetRef } = useBottomSheet({
 *   snapPoints: [0.5, 0.9],
 *   dismissible: true
 * });
 */
export type UseBottomSheet = (config?: UseBottomSheetConfig) => UseBottomSheetReturn;

// ============================================================================
// Offline Cache Hooks
// ============================================================================

export interface UseOfflineCacheConfig {
  key: string;
  maxAge?: number; // milliseconds
}

export interface UseOfflineCacheReturn<T> {
  data: T | null;
  isLoading: boolean;
  isStale: boolean;
  error: Error | null;
  set: (data: T) => Promise<void>;
  clear: () => Promise<void>;
  refresh: () => Promise<void>;
  lastUpdated: number | null;
}

/**
 * Hook: useOfflineCache<T>(config)
 *
 * @example
 * const { data, isLoading, set } = useOfflineCache<Repository[]>({
 *   key: 'repositories-list',
 *   maxAge: 7 * 24 * 60 * 60 * 1000 // 7 days
 * });
 */
export type UseOfflineCache = <T>(
  config: UseOfflineCacheConfig
) => UseOfflineCacheReturn<T>;

export interface UseNetworkStatusReturn {
  isOnline: boolean;
  status: CacheStatus;
  networkInfo: NetworkInfo | null;
  effectiveType: NetworkInfo['effectiveType'];
  saveData: boolean;
}

/**
 * Hook: useNetworkStatus()
 *
 * @example
 * const { isOnline, effectiveType, saveData } = useNetworkStatus();
 */
export type UseNetworkStatus = () => UseNetworkStatusReturn;

// ============================================================================
// Data Loading Hooks
// ============================================================================

export interface UseRepositoriesConfig {
  sortField?: string;
  sortDirection?: 'asc' | 'desc';
  filters?: Record<string, any>;
}

export interface UseRepositoriesReturn {
  repositories: any[];
  isLoading: boolean;
  error: Error | null;
  refetch: () => Promise<void>;
  totalCount: number;
}

/**
 * Hook: useRepositories(config)
 *
 * @example
 * const { repositories, isLoading, refetch } = useRepositories({
 *   sortField: 'stars',
 *   sortDirection: 'desc'
 * });
 */
export type UseRepositories = (config?: UseRepositoriesConfig) => UseRepositoriesReturn;

// ============================================================================
// Selection & Multi-Select Hooks
// ============================================================================

export interface UseSelectionReturn<T = string> {
  selectedIds: T[];
  isSelected: (id: T) => boolean;
  toggle: (id: T) => void;
  select: (id: T) => void;
  deselect: (id: T) => void;
  selectAll: (ids: T[]) => void;
  clear: () => void;
  count: number;
}

/**
 * Hook: useSelection<T>(initialIds?)
 *
 * @example
 * const selection = useSelection<string>([]);
 * selection.toggle('repo-1');
 * console.log(selection.selectedIds); // ['repo-1']
 */
export type UseSelection = <T = string>(initialIds?: T[]) => UseSelectionReturn<T>;

// ============================================================================
// Toggle & State Hooks
// ============================================================================

export interface UseToggleReturn {
  value: boolean;
  toggle: () => void;
  setTrue: () => void;
  setFalse: () => void;
  setValue: (value: boolean) => void;
}

/**
 * Hook: useToggle(initialValue)
 *
 * @example
 * const { value, toggle, setTrue } = useToggle(false);
 */
export type UseToggle = (initialValue?: boolean) => UseToggleReturn;

export interface UseLocalStorageReturn<T> {
  value: T;
  setValue: (value: T | ((prev: T) => T)) => void;
  remove: () => void;
}

/**
 * Hook: useLocalStorage<T>(key, initialValue)
 *
 * @example
 * const [theme, setTheme] = useLocalStorage('theme', 'light');
 */
export type UseLocalStorage = <T>(
  key: string,
  initialValue: T
) => [T, (value: T | ((prev: T) => T)) => void];

// ============================================================================
// Theme & Appearance Hooks
// ============================================================================

export interface UseThemeReturn {
  mode: ThemeMode;
  setMode: (mode: ThemeMode) => void;
  isDark: boolean;
  isLight: boolean;
  toggle: () => void;
  systemPreference: 'light' | 'dark';
}

/**
 * Hook: useTheme()
 *
 * @example
 * const { mode, setMode, isDark, toggle } = useTheme();
 */
export type UseTheme = () => UseThemeReturn;

export interface UseReducedMotionReturn {
  prefersReducedMotion: boolean;
}

/**
 * Hook: useReducedMotion()
 *
 * @example
 * const { prefersReducedMotion } = useReducedMotion();
 */
export type UseReducedMotion = () => UseReducedMotionReturn['prefersReducedMotion'];

// ============================================================================
// Scroll & Pull-to-Refresh Hooks
// ============================================================================

export interface UseScrollReturn {
  scrollY: number;
  scrollX: number;
  scrollDirection: 'up' | 'down' | null;
  isScrolling: boolean;
  isAtTop: boolean;
  isAtBottom: boolean;
}

/**
 * Hook: useScroll(ref?)
 *
 * @example
 * const { scrollY, isAtBottom } = useScroll(containerRef);
 */
export type UseScroll = (ref?: React.RefObject<HTMLElement>) => UseScrollReturn;

export interface UsePullToRefreshConfig {
  threshold?: number; // pixels
  onRefresh: () => Promise<void>;
  disabled?: boolean;
}

export interface UsePullToRefreshReturn {
  pullDistance: number;
  isRefreshing: boolean;
  isPulling: boolean;
  bind: () => Record<string, any>;
}

/**
 * Hook: usePullToRefresh(config)
 *
 * @example
 * const { bind, isRefreshing } = usePullToRefresh({
 *   threshold: 80,
 *   onRefresh: async () => { await fetchData(); }
 * });
 *
 * <div {...bind()}>Pull to refresh content</div>
 */
export type UsePullToRefresh = (config: UsePullToRefreshConfig) => UsePullToRefreshReturn;

// ============================================================================
// Performance & Optimization Hooks
// ============================================================================

export interface UseIntersectionObserverConfig {
  threshold?: number | number[];
  root?: Element | null;
  rootMargin?: string;
}

export interface UseIntersectionObserverReturn {
  ref: React.RefObject<HTMLElement>;
  isIntersecting: boolean;
  entry: IntersectionObserverEntry | null;
}

/**
 * Hook: useIntersectionObserver(config)
 *
 * @example
 * const { ref, isIntersecting } = useIntersectionObserver({
 *   threshold: 0.5
 * });
 *
 * <div ref={ref}>{isIntersecting ? 'Visible' : 'Hidden'}</div>
 */
export type UseIntersectionObserver = (
  config?: UseIntersectionObserverConfig
) => UseIntersectionObserverReturn;

export interface UseDebounceReturn<T> {
  debouncedValue: T;
  isPending: boolean;
}

/**
 * Hook: useDebounce<T>(value, delay)
 *
 * @example
 * const debouncedSearch = useDebounce(searchTerm, 300);
 */
export type UseDebounce = <T>(value: T, delay: number) => T;

export interface UseThrottleReturn<T> {
  throttledValue: T;
}

/**
 * Hook: useThrottle<T>(value, interval)
 *
 * @example
 * const throttledScroll = useThrottle(scrollY, 100);
 */
export type UseThrottle = <T>(value: T, interval: number) => T;

// ============================================================================
// Focus & Accessibility Hooks
// ============================================================================

export interface UseFocusTrapReturn {
  focusTrapRef: React.RefObject<HTMLElement>;
  activate: () => void;
  deactivate: () => void;
}

/**
 * Hook: useFocusTrap(active)
 *
 * @example
 * const { focusTrapRef } = useFocusTrap(modalIsOpen);
 * <div ref={focusTrapRef}>Modal content</div>
 */
export type UseFocusTrap = (active: boolean) => UseFocusTrapReturn;

export interface UseScreenReaderReturn {
  announce: (message: string, priority?: 'polite' | 'assertive') => void;
}

/**
 * Hook: useScreenReader()
 *
 * @example
 * const { announce } = useScreenReader();
 * announce('Form submitted successfully', 'polite');
 */
export type UseScreenReader = () => UseScreenReaderReturn;
