/**
 * Service Layer API Contracts
 * Mobile-First Front-End Redesign
 */

import { CacheEntry, CacheConfig, Repository } from './types';

// ============================================================================
// Offline Storage Service (IndexedDB)
// ============================================================================

export interface IOfflineStorageService {
  /**
   * Initialize the IndexedDB database
   * @returns Promise that resolves when database is ready
   */
  init(): Promise<void>;

  /**
   * Retrieve data from cache
   * @param key - Cache key
   * @returns Cached data or null if not found/expired
   */
  get<T>(key: string): Promise<T | null>;

  /**
   * Store data in cache
   * @param key - Cache key
   * @param data - Data to cache
   * @param version - Schema version (default: '1.0.0')
   * @returns Promise that resolves when data is stored
   */
  set<T>(key: string, data: T, version?: string): Promise<void>;

  /**
   * Delete specific cache entry
   * @param key - Cache key to delete
   * @returns Promise that resolves when entry is deleted
   */
  delete(key: string): Promise<void>;

  /**
   * Clear all cache entries
   * @returns Promise that resolves when cache is cleared
   */
  clear(): Promise<void>;

  /**
   * Remove expired entries (older than maxAge)
   * @returns Promise that resolves with number of entries removed
   */
  cleanup(): Promise<number>;

  /**
   * Get all cache keys
   * @returns Promise that resolves with array of cache keys
   */
  keys(): Promise<string[]>;

  /**
   * Get cache metadata (size, entry count, last cleanup)
   * @returns Promise that resolves with cache metadata
   */
  getMetadata(): Promise<CacheMetadata>;

  /**
   * Check if cache entry exists and is valid
   * @param key - Cache key to check
   * @returns Promise that resolves with boolean
   */
  has(key: string): Promise<boolean>;

  /**
   * Get cache entry with metadata
   * @param key - Cache key
   * @returns Promise that resolves with CacheEntry or null
   */
  getEntry<T>(key: string): Promise<CacheEntry<T> | null>;
}

export interface CacheMetadata {
  totalSize: number; // bytes
  entryCount: number;
  lastCleanup: number | null; // timestamp
  oldestEntry: number | null; // timestamp
  newestEntry: number | null; // timestamp
}

// ============================================================================
// Service Worker Service
// ============================================================================

export interface IServiceWorkerService {
  /**
   * Register service worker
   * @returns Promise that resolves with ServiceWorkerRegistration
   */
  register(): Promise<ServiceWorkerRegistration | null>;

  /**
   * Unregister service worker
   * @returns Promise that resolves with boolean (success)
   */
  unregister(): Promise<boolean>;

  /**
   * Check if service worker is supported
   * @returns Boolean indicating support
   */
  isSupported(): boolean;

  /**
   * Get current service worker registration
   * @returns Promise that resolves with registration or null
   */
  getRegistration(): Promise<ServiceWorkerRegistration | null>;

  /**
   * Update service worker
   * @returns Promise that resolves when update is complete
   */
  update(): Promise<void>;

  /**
   * Listen for service worker messages
   * @param callback - Message handler
   * @returns Cleanup function
   */
  onMessage(callback: (event: MessageEvent) => void): () => void;

  /**
   * Send message to service worker
   * @param message - Message to send
   * @returns Promise that resolves when message is sent
   */
  postMessage(message: any): Promise<void>;

  /**
   * Check if service worker is controlling the page
   * @returns Boolean indicating if SW is active
   */
  isControlling(): boolean;
}

export interface ServiceWorkerMessage {
  type: string;
  payload?: any;
  timestamp: number;
}

// ============================================================================
// Data Service (Repository Data Loading)
// ============================================================================

export interface IDataService {
  /**
   * Fetch all repositories
   * @param options - Fetch options
   * @returns Promise that resolves with repository array
   */
  getRepositories(options?: FetchOptions): Promise<Repository[]>;

  /**
   * Fetch single repository by ID
   * @param id - Repository ID
   * @returns Promise that resolves with repository or null
   */
  getRepository(id: string): Promise<Repository | null>;

  /**
   * Search repositories by query
   * @param query - Search query string
   * @returns Promise that resolves with matching repositories
   */
  searchRepositories(query: string): Promise<Repository[]>;

  /**
   * Filter repositories by criteria
   * @param filters - Filter criteria
   * @returns Promise that resolves with filtered repositories
   */
  filterRepositories(filters: RepositoryFilters): Promise<Repository[]>;

  /**
   * Sort repositories
   * @param repositories - Repositories to sort
   * @param field - Field to sort by
   * @param direction - Sort direction
   * @returns Sorted repository array
   */
  sortRepositories(
    repositories: Repository[],
    field: string,
    direction: 'asc' | 'desc'
  ): Repository[];

  /**
   * Refresh data from source
   * @returns Promise that resolves when data is refreshed
   */
  refresh(): Promise<void>;

  /**
   * Check if data is stale
   * @returns Boolean indicating staleness
   */
  isStale(): boolean;

  /**
   * Get data load timestamp
   * @returns Timestamp or null if not loaded
   */
  getLoadedAt(): number | null;
}

export interface FetchOptions {
  cache?: boolean; // Use cache if available
  forceRefresh?: boolean; // Bypass cache
}

export interface RepositoryFilters {
  language?: string[];
  minStars?: number;
  maxStars?: number;
  minCommits?: number;
  hasDescription?: boolean;
  technologies?: string[];
}

// ============================================================================
// Analytics Service
// ============================================================================

export interface IAnalyticsService {
  /**
   * Track page view
   * @param path - Page path
   * @param title - Page title
   */
  trackPageView(path: string, title?: string): void;

  /**
   * Track custom event
   * @param category - Event category
   * @param action - Event action
   * @param label - Event label (optional)
   * @param value - Event value (optional)
   */
  trackEvent(category: string, action: string, label?: string, value?: number): void;

  /**
   * Track user interaction (touch, swipe, etc.)
   * @param interaction - Interaction details
   */
  trackInteraction(interaction: InteractionEvent): void;

  /**
   * Track performance metric
   * @param metric - Metric name
   * @param value - Metric value
   * @param unit - Metric unit
   */
  trackPerformance(metric: string, value: number, unit: string): void;

  /**
   * Track error
   * @param error - Error object
   * @param context - Additional context
   */
  trackError(error: Error, context?: Record<string, any>): void;

  /**
   * Set user property
   * @param key - Property key
   * @param value - Property value
   */
  setUserProperty(key: string, value: any): void;
}

export interface InteractionEvent {
  type: 'touch' | 'swipe' | 'longpress' | 'scroll' | 'click';
  target: string;
  metadata?: Record<string, any>;
}

// ============================================================================
// Network Service
// ============================================================================

export interface INetworkService {
  /**
   * Check online status
   * @returns Boolean indicating connectivity
   */
  isOnline(): boolean;

  /**
   * Get network information (if available)
   * @returns Network info or null
   */
  getNetworkInfo(): NetworkInfo | null;

  /**
   * Listen for online status changes
   * @param callback - Status change handler
   * @returns Cleanup function
   */
  onStatusChange(callback: (isOnline: boolean) => void): () => void;

  /**
   * Estimate bandwidth
   * @returns Promise that resolves with estimated Mbps
   */
  estimateBandwidth(): Promise<number | null>;

  /**
   * Check if user prefers reduced data
   * @returns Boolean indicating data saver preference
   */
  prefersSaveData(): boolean;
}

export interface NetworkInfo {
  type: 'wifi' | 'cellular' | 'ethernet' | 'unknown';
  effectiveType: 'slow-2g' | '2g' | '3g' | '4g';
  downlink: number; // Mbps
  rtt: number; // Round-trip time in ms
  saveData: boolean;
}

// ============================================================================
// Haptic Feedback Service
// ============================================================================

export interface IHapticService {
  /**
   * Check if haptic feedback is supported
   * @returns Boolean indicating support
   */
  isSupported(): boolean;

  /**
   * Trigger haptic feedback
   * @param pattern - Vibration pattern (ms or array)
   * @returns Boolean indicating success
   */
  vibrate(pattern: number | number[]): boolean;

  /**
   * Stop ongoing vibration
   */
  cancel(): void;

  /**
   * Trigger light impact (10ms)
   */
  light(): boolean;

  /**
   * Trigger medium impact (20ms)
   */
  medium(): boolean;

  /**
   * Trigger heavy impact (30ms)
   */
  heavy(): boolean;

  /**
   * Trigger selection feedback (5ms)
   */
  selection(): boolean;

  /**
   * Trigger error feedback (pattern)
   */
  error(): boolean;

  /**
   * Trigger success feedback (pattern)
   */
  success(): boolean;
}

// ============================================================================
// Toast/Notification Service
// ============================================================================

export interface IToastService {
  /**
   * Show toast notification
   * @param message - Toast message
   * @param options - Toast options
   * @returns Toast ID for dismissal
   */
  show(message: string, options?: ToastOptions): string;

  /**
   * Dismiss toast by ID
   * @param id - Toast ID to dismiss
   */
  dismiss(id: string): void;

  /**
   * Dismiss all toasts
   */
  dismissAll(): void;

  /**
   * Show success toast
   * @param message - Success message
   * @returns Toast ID
   */
  success(message: string): string;

  /**
   * Show error toast
   * @param message - Error message
   * @returns Toast ID
   */
  error(message: string): string;

  /**
   * Show warning toast
   * @param message - Warning message
   * @returns Toast ID
   */
  warning(message: string): string;

  /**
   * Show info toast
   * @param message - Info message
   * @returns Toast ID
   */
  info(message: string): string;
}

export interface ToastOptions {
  duration?: number; // milliseconds
  position?: 'top' | 'bottom';
  variant?: 'success' | 'error' | 'warning' | 'info';
  icon?: React.ComponentType<{ size?: number }>;
  dismissible?: boolean;
  onDismiss?: () => void;
}

// ============================================================================
// Logger Service
// ============================================================================

export interface ILoggerService {
  /**
   * Log debug message
   * @param message - Log message
   * @param data - Additional data
   */
  debug(message: string, data?: any): void;

  /**
   * Log info message
   * @param message - Log message
   * @param data - Additional data
   */
  info(message: string, data?: any): void;

  /**
   * Log warning message
   * @param message - Log message
   * @param data - Additional data
   */
  warn(message: string, data?: any): void;

  /**
   * Log error message
   * @param message - Log message
   * @param error - Error object
   */
  error(message: string, error?: Error): void;

  /**
   * Set log level
   * @param level - Minimum level to log
   */
  setLevel(level: LogLevel): void;

  /**
   * Get current log level
   * @returns Current log level
   */
  getLevel(): LogLevel;
}

export type LogLevel = 'debug' | 'info' | 'warn' | 'error' | 'none';

// ============================================================================
// Performance Monitoring Service
// ============================================================================

export interface IPerformanceService {
  /**
   * Mark performance milestone
   * @param name - Mark name
   */
  mark(name: string): void;

  /**
   * Measure between two marks
   * @param name - Measure name
   * @param startMark - Start mark name
   * @param endMark - End mark name
   * @returns Duration in milliseconds
   */
  measure(name: string, startMark: string, endMark: string): number;

  /**
   * Get Web Vitals metrics
   * @returns Promise that resolves with metrics
   */
  getWebVitals(): Promise<WebVitalsMetrics>;

  /**
   * Report metric to analytics
   * @param metric - Metric to report
   */
  reportMetric(metric: PerformanceMetric): void;

  /**
   * Get navigation timing
   * @returns Navigation timing object
   */
  getNavigationTiming(): PerformanceNavigationTiming | null;
}

export interface WebVitalsMetrics {
  FCP: number; // First Contentful Paint
  LCP: number; // Largest Contentful Paint
  FID: number; // First Input Delay
  CLS: number; // Cumulative Layout Shift
  TTFB: number; // Time to First Byte
  TTI: number; // Time to Interactive
}

export interface PerformanceMetric {
  name: string;
  value: number;
  unit: string;
  rating?: 'good' | 'needs-improvement' | 'poor';
}
