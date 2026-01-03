/**
 * OfflineIndicator Component
 * Shows offline status and cached data timestamp
 * Appears when navigator.onLine is false
 */

import React from "react";
import { useOfflineCacheContext } from "@/contexts/OfflineCacheContext";
import "./OfflineIndicator.css";

export function OfflineIndicator() {
  const { isOnline, lastSync, cacheMetadata } = useOfflineCacheContext();

  // Don't show if online
  if (isOnline) {
    return null;
  }

  // Format last sync timestamp - use ref for current time to avoid impure function in render
  const formatLastSync = () => {
    if (!lastSync) {
      return "Never synced";
    }

    const now = new Date().getTime();
    const diff = now - lastSync;

    // Less than 1 minute
    if (diff < 60 * 1000) {
      return "Just now";
    }

    // Less than 1 hour
    if (diff < 60 * 60 * 1000) {
      const minutes = Math.floor(diff / (60 * 1000));
      return `${minutes}m ago`;
    }

    // Less than 1 day
    if (diff < 24 * 60 * 60 * 1000) {
      const hours = Math.floor(diff / (60 * 60 * 1000));
      return `${hours}h ago`;
    }

    // Days ago
    const days = Math.floor(diff / (24 * 60 * 60 * 1000));
    return `${days}d ago`;
  };

  return (
    <div className="offline-indicator" role="alert" aria-live="polite">
      <div className="offline-indicator__icon" aria-hidden="true">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path
            d="M8 1C4.13 1 1 4.13 1 8s3.13 7 7 7 7-3.13 7-7-3.13-7-7-7zm0 12.5c-3.03 0-5.5-2.47-5.5-5.5S4.97 2.5 8 2.5s5.5 2.47 5.5 5.5-2.47 5.5-5.5 5.5z"
            fill="currentColor"
          />
          <path
            d="M11.5 8h-7M8 4.5v7"
            stroke="currentColor"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
        </svg>
      </div>

      <div className="offline-indicator__content">
        <span className="offline-indicator__status">Offline Mode</span>
        <span className="offline-indicator__sync">
          Last synced: {formatLastSync()}
        </span>
      </div>

      {cacheMetadata.entryCount > 0 && (
        <div
          className="offline-indicator__badge"
          aria-label={`${cacheMetadata.entryCount} cached items`}
        >
          {cacheMetadata.entryCount}
        </div>
      )}
    </div>
  );
}

export default OfflineIndicator;
