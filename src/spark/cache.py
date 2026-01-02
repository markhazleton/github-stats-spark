"""API response caching with 30-day TTL."""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional


class APICache:
    """Manages cached API responses with 30-day TTL."""

    def __init__(self, cache_dir: str = ".cache", ttl_hours: int = 720):
        """Initialize the cache.

        Args:
            cache_dir: Directory to store cache files
            ttl_hours: Time-to-live in hours (default: 720 = 30 days)
        """
        self.cache_dir = Path(cache_dir)
        self.ttl = timedelta(hours=ttl_hours)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_path(self, key: str) -> Path:
        """Get the file path for a cache key.

        Args:
            key: Cache key

        Returns:
            Path to cache file
        """
        # Sanitize key for filesystem
        safe_key = key.replace("/", "_").replace(":", "_")
        return self.cache_dir / f"{safe_key}.json"

    def get(self, key: str) -> Optional[Any]:
        """Retrieve a cached value if not expired.

        Args:
            key: Cache key

        Returns:
            Cached value or None if not found/expired
        """
        cache_path = self._get_cache_path(key)

        if not cache_path.exists():
            return None

        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            timestamp = datetime.fromisoformat(data["timestamp"])
            if self.is_expired(timestamp):
                # Remove expired cache
                cache_path.unlink()
                return None

            return data["value"]
        except (json.JSONDecodeError, KeyError, ValueError):
            # Invalid cache file, remove it
            cache_path.unlink()
            return None

    def set(self, key: str, value: Any) -> None:
        """Store a value in the cache.

        Args:
            key: Cache key
            value: Value to cache (must be JSON serializable)
        """
        cache_path = self._get_cache_path(key)

        data = {
            "timestamp": datetime.now().isoformat(),
            "value": value,
        }

        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def is_expired(self, timestamp: datetime) -> bool:
        """Check if a timestamp is expired based on TTL.

        Args:
            timestamp: Timestamp to check

        Returns:
            True if expired, False otherwise
        """
        return datetime.now() - timestamp > self.ttl

    def clear(self) -> None:
        """Clear all cached values."""
        for cache_file in self.cache_dir.glob("*.json"):
            cache_file.unlink()
