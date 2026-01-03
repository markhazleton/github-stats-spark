import { useState, useEffect } from 'react';

/**
 * useNetworkStatus Hook
 * Wraps Network Information API for connection quality detection
 * 
 * @returns {Object} Network status information
 * 
 * @example
 * const { isOnline, effectiveType, downlink, rtt, saveData } = useNetworkStatus();
 */
export function useNetworkStatus() {
  const [status, setStatus] = useState(() => getNetworkStatus());

  useEffect(() => {
    const handleOnline = () => {
      setStatus(prev => ({ ...prev, isOnline: true }));
    };

    const handleOffline = () => {
      setStatus(prev => ({ ...prev, isOnline: false }));
    };

    const handleConnectionChange = () => {
      setStatus(getNetworkStatus());
    };

    // Listen for online/offline events
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    // Listen for connection changes (if supported)
    if (navigator.connection) {
      navigator.connection.addEventListener('change', handleConnectionChange);
    }

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
      if (navigator.connection) {
        navigator.connection.removeEventListener('change', handleConnectionChange);
      }
    };
  }, []);

  return status;
}

/**
 * Get current network status
 */
function getNetworkStatus() {
  const isOnline = navigator.onLine;
  
  // Network Information API (Chromium only)
  if ('connection' in navigator) {
    const conn = navigator.connection;
    return {
      isOnline,
      effectiveType: conn.effectiveType || '4g', // 'slow-2g', '2g', '3g', '4g'
      downlink: conn.downlink || null, // Mbps
      rtt: conn.rtt || null, // ms
      saveData: conn.saveData || false
    };
  }

  // Fallback for browsers without Network Information API
  return {
    isOnline,
    effectiveType: '4g', // Assume good connection
    downlink: null,
    rtt: null,
    saveData: false
  };
}

export default useNetworkStatus;
