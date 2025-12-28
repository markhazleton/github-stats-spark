"""Unit tests for APICache."""

import pytest
import tempfile
import shutil
from datetime import datetime, timedelta
from pathlib import Path

from spark.cache import APICache


class TestAPICache:
    """Test API caching functionality."""

    @pytest.fixture
    def temp_cache_dir(self):
        """Create a temporary cache directory."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    def test_cache_set_and_get(self, temp_cache_dir):
        """Test setting and getting cached values."""
        cache = APICache(cache_dir=temp_cache_dir)

        test_key = "test_key"
        test_value = {"data": "test_value", "count": 123}

        cache.set(test_key, test_value)
        result = cache.get(test_key)

        assert result == test_value

    def test_cache_miss(self, temp_cache_dir):
        """Test cache miss returns None."""
        cache = APICache(cache_dir=temp_cache_dir)

        result = cache.get("nonexistent_key")
        assert result is None

    def test_cache_expiration(self, temp_cache_dir):
        """Test cache expiration based on TTL."""
        # Create cache with very short TTL
        cache = APICache(cache_dir=temp_cache_dir, ttl_hours=0)

        test_key = "expiring_key"
        test_value = {"data": "expires"}

        cache.set(test_key, test_value)

        # Check expiration
        from datetime import datetime, timedelta
        old_timestamp = datetime.now() - timedelta(hours=1)
        assert cache.is_expired(old_timestamp) is True

        recent_timestamp = datetime.now()
        assert cache.is_expired(recent_timestamp) is False

    def test_cache_clear(self, temp_cache_dir):
        """Test clearing all cached values."""
        cache = APICache(cache_dir=temp_cache_dir)

        # Add multiple cache entries
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.set("key3", "value3")

        # Clear cache
        cache.clear()

        # Verify all entries are gone
        assert cache.get("key1") is None
        assert cache.get("key2") is None
        assert cache.get("key3") is None

    def test_cache_key_sanitization(self, temp_cache_dir):
        """Test that cache keys are sanitized for filesystem."""
        cache = APICache(cache_dir=temp_cache_dir)

        # Keys with special characters
        test_key = "user/repos:languages"
        test_value = {"data": "sanitized"}

        cache.set(test_key, test_value)
        result = cache.get(test_key)

        assert result == test_value
