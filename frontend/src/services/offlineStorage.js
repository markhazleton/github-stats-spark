/**
 * Offline Storage Service
 * IndexedDB wrapper using Dexie.js for offline data caching
 * Implements 7-day retention policy with automatic cleanup
 */

import Dexie from "dexie";

// Database name and version
const DB_NAME = "GitHubStatsDB";
const DB_VERSION = 1;

// Cache TTL: 7 days in milliseconds
const CACHE_TTL = 7 * 24 * 60 * 60 * 1000;

class OfflineStorageService {
  constructor() {
    this.db = null;
    this.initialized = false;
  }

  /**
   * Initialize the IndexedDB database
   * @returns {Promise<void>}
   */
  async init() {
    if (this.initialized) {
      return;
    }

    try {
      this.db = new Dexie(DB_NAME);

      // Define database schema
      this.db.version(DB_VERSION).stores({
        cache: "key, timestamp, version, size",
        repositories: "++id, name, timestamp, *tags",
      });

      // Add hooks for automatic timestamp tracking
      this.db.cache.hook("creating", (primKey, obj) => {
        obj.timestamp = Date.now();
        obj.version = obj.version || "1.0.0";
        obj.size = JSON.stringify(obj.data).length;
      });

      await this.db.open();
      this.initialized = true;

      // Run initial cleanup
      await this.cleanup();

      console.log("[OfflineStorage] Initialized successfully");
    } catch (error) {
      console.error("[OfflineStorage] Initialization failed:", error);
      throw new Error("Failed to initialize offline storage");
    }
  }

  /**
   * Ensure database is initialized before operations
   * @private
   */
  async ensureInitialized() {
    if (!this.initialized) {
      await this.init();
    }
  }

  /**
   * Store data in cache
   * @param {string} key - Cache key
   * @param {any} data - Data to cache
   * @param {string} version - Data schema version
   * @returns {Promise<void>}
   */
  async set(key, data, version = "1.0.0") {
    await this.ensureInitialized();

    try {
      await this.db.cache.put({
        key,
        data,
        version,
        timestamp: Date.now(),
        size: JSON.stringify(data).length,
      });

      console.log(`[OfflineStorage] Cached data for key: ${key}`);
    } catch (error) {
      console.error(
        `[OfflineStorage] Failed to cache data for key: ${key}`,
        error,
      );
      throw error;
    }
  }

  /**
   * Retrieve data from cache
   * @param {string} key - Cache key
   * @returns {Promise<any|null>} Cached data or null if not found/expired
   */
  async get(key) {
    await this.ensureInitialized();

    try {
      const entry = await this.db.cache.get(key);

      if (!entry) {
        console.log(`[OfflineStorage] Cache miss for key: ${key}`);
        return null;
      }

      // Check if entry is expired
      const age = Date.now() - entry.timestamp;
      if (age > CACHE_TTL) {
        console.log(`[OfflineStorage] Cache expired for key: ${key}`);
        await this.delete(key);
        return null;
      }

      console.log(`[OfflineStorage] Cache hit for key: ${key}`);
      return entry.data;
    } catch (error) {
      console.error(
        `[OfflineStorage] Failed to retrieve cache for key: ${key}`,
        error,
      );
      return null;
    }
  }

  /**
   * Delete specific cache entry
   * @param {string} key - Cache key
   * @returns {Promise<void>}
   */
  async delete(key) {
    await this.ensureInitialized();

    try {
      await this.db.cache.delete(key);
      console.log(`[OfflineStorage] Deleted cache for key: ${key}`);
    } catch (error) {
      console.error(
        `[OfflineStorage] Failed to delete cache for key: ${key}`,
        error,
      );
      throw error;
    }
  }

  /**
   * Clear all cache entries
   * @returns {Promise<void>}
   */
  async clear() {
    await this.ensureInitialized();

    try {
      await this.db.cache.clear();
      console.log("[OfflineStorage] Cleared all cache");
    } catch (error) {
      console.error("[OfflineStorage] Failed to clear cache", error);
      throw error;
    }
  }

  /**
   * Remove entries older than TTL (7 days)
   * Runs automatically on init and can be called manually
   * @returns {Promise<number>} Number of entries deleted
   */
  async cleanup() {
    await this.ensureInitialized();

    try {
      const cutoffTime = Date.now() - CACHE_TTL;
      const count = await this.db.cache
        .where("timestamp")
        .below(cutoffTime)
        .delete();

      if (count > 0) {
        console.log(`[OfflineStorage] Cleaned up ${count} expired entries`);
      }

      return count;
    } catch (error) {
      console.error("[OfflineStorage] Cleanup failed:", error);
      return 0;
    }
  }

  /**
   * Get cache metadata
   * @returns {Promise<object>} Cache statistics
   */
  async getMetadata() {
    await this.ensureInitialized();

    try {
      const entries = await this.db.cache.toArray();
      const totalSize = entries.reduce(
        (sum, entry) => sum + (entry.size || 0),
        0,
      );
      const oldestEntry = entries.reduce(
        (oldest, entry) =>
          !oldest || entry.timestamp < oldest ? entry.timestamp : oldest,
        null,
      );
      const newestEntry = entries.reduce(
        (newest, entry) =>
          !newest || entry.timestamp > newest ? entry.timestamp : newest,
        null,
      );

      return {
        entryCount: entries.length,
        totalSize,
        oldestTimestamp: oldestEntry,
        newestTimestamp: newestEntry,
        cacheTTL: CACHE_TTL,
      };
    } catch (error) {
      console.error("[OfflineStorage] Failed to get metadata", error);
      return {
        entryCount: 0,
        totalSize: 0,
        oldestTimestamp: null,
        newestTimestamp: null,
        cacheTTL: CACHE_TTL,
      };
    }
  }

  /**
   * Check if storage is available
   * @returns {boolean}
   */
  isAvailable() {
    return "indexedDB" in window;
  }

  /**
   * Close database connection
   * @returns {Promise<void>}
   */
  async close() {
    if (this.db) {
      await this.db.close();
      this.initialized = false;
      console.log("[OfflineStorage] Database closed");
    }
  }
}

// Export singleton instance
export const offlineStorage = new OfflineStorageService();

// Export class for testing
export default OfflineStorageService;
