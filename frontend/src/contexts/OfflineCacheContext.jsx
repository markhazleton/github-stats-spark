/**
 * Offline Cache Context
 * Manages offline cache state across the application
 * Tracks online/offline status, last sync, and pending operations
 */

import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  useCallback,
} from "react";
import { offlineStorage } from "../services/offlineStorage";

// Create context
const OfflineCacheContext = createContext(null);

/**
 * Offline Cache Provider Component
 * @param {object} props
 * @param {React.ReactNode} props.children
 */
export function OfflineCacheProvider({ children }) {
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const [lastSync, setLastSync] = useState(null);
  const [pendingSync, setPendingSync] = useState(false);
  const [cacheMetadata, setCacheMetadata] = useState({
    entryCount: 0,
    totalSize: 0,
    oldestTimestamp: null,
    newestTimestamp: null,
  });

  // Update online/offline status
  useEffect(() => {
    const handleOnline = () => {
      console.log("[OfflineCache] Network status: ONLINE");
      setIsOnline(true);
      setPendingSync(true); // Trigger sync when coming online
    };

    const handleOffline = () => {
      console.log("[OfflineCache] Network status: OFFLINE");
      setIsOnline(false);
    };

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);

    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, []);

  // Refresh cache metadata
  const refreshMetadata = useCallback(async () => {
    try {
      const metadata = await offlineStorage.getMetadata();
      setCacheMetadata(metadata);
    } catch (error) {
      console.error("[OfflineCache] Failed to refresh metadata:", error);
    }
  }, []);

  // Initialize offline storage
  useEffect(() => {
    let mounted = true;

    async function initStorage() {
      try {
        await offlineStorage.init();
        if (mounted) {
          await refreshMetadata();
        }
      } catch (error) {
        console.error("[OfflineCache] Failed to initialize storage:", error);
      }
    }

    initStorage();

    return () => {
      mounted = false;
    };
  }, [refreshMetadata]);

  // Update last sync timestamp
  const updateLastSync = useCallback(() => {
    const timestamp = Date.now();
    setLastSync(timestamp);
    setPendingSync(false);
    console.log(
      "[OfflineCache] Sync completed:",
      new Date(timestamp).toISOString(),
    );
  }, []);

  // Clear all cache
  const clearCache = useCallback(async () => {
    try {
      await offlineStorage.clear();
      await refreshMetadata();
      console.log("[OfflineCache] Cache cleared");
    } catch (error) {
      console.error("[OfflineCache] Failed to clear cache:", error);
      throw error;
    }
  }, [refreshMetadata]);

  // Cleanup old entries
  const cleanup = useCallback(async () => {
    try {
      const count = await offlineStorage.cleanup();
      await refreshMetadata();
      return count;
    } catch (error) {
      console.error("[OfflineCache] Cleanup failed:", error);
      return 0;
    }
  }, [refreshMetadata]);

  const value = {
    isOnline,
    lastSync,
    pendingSync,
    cacheMetadata,
    updateLastSync,
    clearCache,
    cleanup,
    refreshMetadata,
  };

  return (
    <OfflineCacheContext.Provider value={value}>
      {children}
    </OfflineCacheContext.Provider>
  );
}

/**
 * Custom hook to use offline cache context
 * @returns {object} Offline cache context value
 * @throws {Error} If used outside of OfflineCacheProvider
 */
export function useOfflineCacheContext() {
  const context = useContext(OfflineCacheContext);

  if (!context) {
    throw new Error(
      "useOfflineCacheContext must be used within OfflineCacheProvider",
    );
  }

  return context;
}

export default OfflineCacheContext;
