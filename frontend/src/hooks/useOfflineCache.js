/**
 * useOfflineCache Hook
 * Custom hook for caching data with IndexedDB
 * Implements 7-day retention policy with automatic stale detection
 */

import { useState, useEffect, useCallback } from "react";
import { offlineStorage } from "../services/offlineStorage";
import { useOfflineCacheContext } from "../contexts/OfflineCacheContext";

/**
 * Hook for offline caching with automatic stale detection
 * @param {object} options
 * @param {string} options.key - Unique cache key
 * @param {number} [options.maxAge] - Max age in ms (default: 7 days)
 * @param {Function} [options.fetcher] - Function to fetch fresh data
 * @returns {object} Cache state and operations
 */
export function useOfflineCache({
  key,
  maxAge = 7 * 24 * 60 * 60 * 1000, // 7 days default
  fetcher = null,
}) {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isStale, setIsStale] = useState(false);
  const [error, setError] = useState(null);
  const [lastFetch, setLastFetch] = useState(null);

  const { isOnline, updateLastSync, refreshMetadata } =
    useOfflineCacheContext();

  // Load cached data on mount
  useEffect(() => {
    let mounted = true;

    async function loadCachedData() {
      try {
        setIsLoading(true);
        setError(null);

        const cachedData = await offlineStorage.get(key);

        if (mounted) {
          if (cachedData) {
            setData(cachedData);
            setLastFetch(Date.now());

            // Check if data is stale
            const entry = await offlineStorage.db.cache.get(key);
            if (entry) {
              const age = Date.now() - entry.timestamp;
              setIsStale(age > maxAge);
            }
          }
          setIsLoading(false);
        }
      } catch (err) {
        console.error("[useOfflineCache] Failed to load cached data:", err);
        if (mounted) {
          setError(err);
          setIsLoading(false);
        }
      }
    }

    loadCachedData();

    return () => {
      mounted = false;
    };
  }, [key, maxAge]);

  // Cache data
  const set = useCallback(
    async (newData, version = "1.0.0") => {
      try {
        await offlineStorage.set(key, newData, version);
        setData(newData);
        setLastFetch(Date.now());
        setIsStale(false);
        updateLastSync();
        await refreshMetadata();
      } catch (err) {
        console.error("[useOfflineCache] Failed to cache data:", err);
        setError(err);
        throw err;
      }
    },
    [key, updateLastSync, refreshMetadata],
  );

  // Fetch fresh data if fetcher provided
  const refresh = useCallback(async () => {
    if (!fetcher) {
      console.warn("[useOfflineCache] No fetcher provided, cannot refresh");
      return;
    }

    if (!isOnline) {
      console.log("[useOfflineCache] Offline, using cached data");
      return;
    }

    try {
      setIsLoading(true);
      setError(null);

      const freshData = await fetcher();
      await set(freshData);

      setIsLoading(false);
      return freshData;
    } catch (err) {
      console.error("[useOfflineCache] Failed to fetch fresh data:", err);
      setError(err);
      setIsLoading(false);
      throw err;
    }
  }, [fetcher, isOnline, set]);

  // Delete cached data
  const remove = useCallback(async () => {
    try {
      await offlineStorage.delete(key);
      setData(null);
      setLastFetch(null);
      setIsStale(false);
      await refreshMetadata();
    } catch (err) {
      console.error("[useOfflineCache] Failed to remove cached data:", err);
      setError(err);
      throw err;
    }
  }, [key, refreshMetadata]);

  // Get cache age in ms
  const getCacheAge = useCallback(async () => {
    try {
      const entry = await offlineStorage.db.cache.get(key);
      if (entry) {
        return Date.now() - entry.timestamp;
      }
      return null;
    } catch (err) {
      console.error("[useOfflineCache] Failed to get cache age:", err);
      return null;
    }
  }, [key]);

  return {
    data,
    isLoading,
    isStale,
    error,
    lastFetch,
    set,
    refresh,
    remove,
    getCacheAge,
  };
}

export default useOfflineCache;
