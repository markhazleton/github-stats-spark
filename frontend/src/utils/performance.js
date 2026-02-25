/**
 * Performance Optimization Utilities
 *
 * Performance Targets:
 * - FCP < 2s
 * - TTI < 5s
 * - 170KB JS gzipped
 * - 50KB CSS gzipped
 */

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
 * Get effective connection type for adaptive loading
 * Returns 'slow-2g' | '2g' | '3g' | '4g' | 'unknown'
 *
 * @returns {string} - Connection type
 *
 * @example
 * const connectionType = getConnectionType();
 * if (connectionType === '2g' || connectionType === 'slow-2g') {
 *   // Defer non-critical resources
 * }
 */
export const getConnectionType = () => {
  if ("connection" in navigator && "effectiveType" in navigator.connection) {
    return navigator.connection.effectiveType;
  }
  return "unknown";
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
 * });
 */
export const deferExecution = (callback, timeout = 3000) => {
  if ("requestIdleCallback" in window) {
    requestIdleCallback(callback, { timeout });
  } else {
    setTimeout(callback, timeout);
  }
};
