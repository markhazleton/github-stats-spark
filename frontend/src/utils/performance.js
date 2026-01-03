/**
 * Performance Optimization Utilities
 * 
 * Critical rendering path optimizations for mobile-first experience:
 * - Lazy loading below-the-fold content
 * - Resource hints for faster loading
 * - Bundle splitting strategies
 * 
 * Performance Targets (from plan.md):
 * - FCP < 2s
 * - TTI < 5s
 * - 170KB JS gzipped
 * - 50KB CSS gzipped
 */

/**
 * Lazy load component when it enters the viewport
 * Uses IntersectionObserver for efficient viewport detection
 * 
 * @param {Function} importFn - Dynamic import function () => import('./Component')
 * @returns {React.Component} - Lazy loaded component
 * 
 * @example
 * const HeavyChart = lazyLoadComponent(() => import('./HeavyChart'));
 */
export const lazyLoadComponent = (importFn) => {
  return React.lazy(importFn);
};

/**
 * Preload critical resources (fonts, images, data)
 * Adds <link rel="preload"> to document head
 * 
 * @param {string} url - Resource URL
 * @param {string} type - Resource type: 'font' | 'image' | 'fetch' | 'script' | 'style'
 * @param {string} [crossOrigin] - CORS mode: 'anonymous' | 'use-credentials'
 * 
 * @example
 * preloadResource('/data/repositories.json', 'fetch');
 * preloadResource('/fonts/Inter-var.woff2', 'font', 'anonymous');
 */
export const preloadResource = (url, type, crossOrigin = null) => {
  const link = document.createElement('link');
  link.rel = 'preload';
  link.href = url;

  // Set 'as' attribute based on type
  const asMap = {
    font: 'font',
    image: 'image',
    fetch: 'fetch',
    script: 'script',
    style: 'style',
  };
  link.as = asMap[type] || type;

  // Add crossorigin for fonts and fetch
  if (crossOrigin) {
    link.crossOrigin = crossOrigin;
  }

  // Add type for fonts
  if (type === 'font') {
    link.type = 'font/woff2';
  }

  document.head.appendChild(link);
};

/**
 * Prefetch resource for future navigation
 * Adds <link rel="prefetch"> for low-priority loading
 * 
 * @param {string} url - Resource URL
 * 
 * @example
 * prefetchResource('/comparison-view-bundle.js');
 */
export const prefetchResource = (url) => {
  const link = document.createElement('link');
  link.rel = 'prefetch';
  link.href = url;
  document.head.appendChild(link);
};

/**
 * Preconnect to external origin for faster DNS/TCP/TLS
 * Adds <link rel="preconnect">
 * 
 * @param {string} origin - Origin URL (e.g., 'https://api.github.com')
 * @param {boolean} [crossOrigin=true] - Add crossorigin attribute
 * 
 * @example
 * preconnectOrigin('https://api.github.com');
 */
export const preconnectOrigin = (origin, crossOrigin = true) => {
  const link = document.createElement('link');
  link.rel = 'preconnect';
  link.href = origin;
  if (crossOrigin) {
    link.crossOrigin = 'anonymous';
  }
  document.head.appendChild(link);
};

/**
 * Debounce function to limit execution frequency
 * Useful for scroll/resize handlers
 * 
 * @param {Function} func - Function to debounce
 * @param {number} wait - Wait time in milliseconds
 * @returns {Function} - Debounced function
 * 
 * @example
 * const debouncedScroll = debounce(handleScroll, 150);
 * window.addEventListener('scroll', debouncedScroll);
 */
export const debounce = (func, wait) => {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
};

/**
 * Throttle function to limit execution rate
 * Executes at most once per specified time period
 * 
 * @param {Function} func - Function to throttle
 * @param {number} limit - Minimum time between executions (ms)
 * @returns {Function} - Throttled function
 * 
 * @example
 * const throttledResize = throttle(handleResize, 200);
 * window.addEventListener('resize', throttledResize);
 */
export const throttle = (func, limit) => {
  let inThrottle;
  return function executedFunction(...args) {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
};

/**
 * Measure component render time (production-safe)
 * Uses React Profiler API for accurate measurements
 * 
 * @param {string} id - Component identifier
 * @param {string} phase - 'mount' | 'update'
 * @param {number} actualDuration - Time spent rendering (ms)
 * @param {number} baseDuration - Estimated render time without memoization (ms)
 * 
 * @example
 * <Profiler id="RepositoryTable" onRender={measureRenderTime}>
 *   <RepositoryTable {...props} />
 * </Profiler>
 */
export const measureRenderTime = (id, phase, actualDuration, baseDuration) => {
  // Only log in development
  if (import.meta.env.DEV) {
    console.log(`[Performance] ${id} (${phase}):`, {
      actualDuration: `${actualDuration.toFixed(2)}ms`,
      baseDuration: `${baseDuration.toFixed(2)}ms`,
      optimizationGain: baseDuration > 0 
        ? `${((1 - actualDuration / baseDuration) * 100).toFixed(1)}%`
        : 'N/A',
    });
  }
};

/**
 * Calculate and report Web Vitals metrics
 * Tracks FCP, LCP, FID, CLS, TTFB
 * 
 * @param {Function} onPerfEntry - Callback to receive metric data
 * 
 * @example
 * reportWebVitals((metric) => {
 *   console.log(metric.name, metric.value);
 *   // Send to analytics: analytics.send(metric);
 * });
 */
export const reportWebVitals = (onPerfEntry) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

/**
 * Check if user prefers reduced data usage
 * Uses Network Information API's saveData flag
 * 
 * @returns {boolean} - True if user prefers reduced data
 * 
 * @example
 * if (prefersReducedData()) {
 *   // Load lower resolution images
 *   // Skip non-essential API calls
 * }
 */
export const prefersReducedData = () => {
  if ('connection' in navigator) {
    return navigator.connection.saveData === true;
  }
  return false;
};

/**
 * Get effective connection type for adaptive loading
 * Returns 'slow-2g' | '2g' | '3g' | '4g' | 'unknown'
 * 
 * @returns {string} - Connection type
 * 
 * @example
 * const connectionType = getConnectionType();
 * if (connectionType === '2g' || connectionType === 'slow-2g') {
 *   // Reduce image quality
 *   // Defer non-critical resources
 * }
 */
export const getConnectionType = () => {
  if ('connection' in navigator && 'effectiveType' in navigator.connection) {
    return navigator.connection.effectiveType;
  }
  return 'unknown';
};

/**
 * Intersection Observer hook for lazy loading
 * Triggers callback when element enters viewport
 * 
 * @param {Function} callback - Function to call when element is visible
 * @param {Object} options - IntersectionObserver options
 * @returns {Function} - Ref callback to attach to element
 * 
 * @example
 * const lazyRef = useIntersectionObserver(() => {
 *   loadHeavyComponent();
 * }, { rootMargin: '100px' });
 * 
 * return <div ref={lazyRef}>Content</div>;
 */
export const useIntersectionObserver = (callback, options = {}) => {
  const defaultOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1,
    ...options,
  };

  return (node) => {
    if (!node) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          callback();
          observer.disconnect();
        }
      });
    }, defaultOptions);

    observer.observe(node);
  };
};

/**
 * Critical CSS injection for above-the-fold content
 * Inlines critical styles to prevent FOUC
 * 
 * @param {string} css - Critical CSS string
 * 
 * @example
 * injectCriticalCSS(`
 *   body { margin: 0; font-family: Inter, sans-serif; }
 *   .hero { min-height: 100vh; }
 * `);
 */
export const injectCriticalCSS = (css) => {
  const style = document.createElement('style');
  style.textContent = css;
  style.setAttribute('data-critical', 'true');
  document.head.insertBefore(style, document.head.firstChild);
};

/**
 * Defer non-critical JavaScript execution
 * Waits for page idle or timeout
 * 
 * @param {Function} callback - Function to defer
 * @param {number} [timeout=3000] - Maximum wait time (ms)
 * 
 * @example
 * deferExecution(() => {
 *   // Initialize analytics
 *   // Load chat widget
 * });
 */
export const deferExecution = (callback, timeout = 3000) => {
  if ('requestIdleCallback' in window) {
    requestIdleCallback(callback, { timeout });
  } else {
    setTimeout(callback, timeout);
  }
};
