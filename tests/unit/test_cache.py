"""Unit tests for APICache."""

import pytest
import tempfile
import shutil
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

        cache.set("test_cat", "owner", {"data": "test_value"})
        result = cache.get("test_cat", "owner")

        assert result == {"data": "test_value"}

    def test_cache_miss(self, temp_cache_dir):
        """Test cache miss returns None."""
        cache = APICache(cache_dir=temp_cache_dir)

        result = cache.get("nonexistent", "owner")
        assert result is None

    def test_cache_clear(self, temp_cache_dir):
        """Test clearing all cached values."""
        cache = APICache(cache_dir=temp_cache_dir)

        # Add multiple cache entries
        cache.set("cat1", "owner", "value1")
        cache.set("cat2", "owner", "value2")

        # Clear cache
        cache.clear()

        # Verify all entries are gone
        assert cache.get("cat1", "owner") is None
        assert cache.get("cat2", "owner") is None

    def test_hierarchical_storage(self, temp_cache_dir):
        """Test that cache uses hierarchical storage."""
        cache = APICache(cache_dir=temp_cache_dir)
        
        cache.set("category", "owner", "value", repo="repo", week="2026W01")
        
        expected_path = Path(temp_cache_dir) / "owner" / "repo" / "category" / "2026W01.json"
        assert expected_path.exists()

    def test_manifest_update(self, temp_cache_dir):
        """Test that manifest is updated."""
        cache = APICache(cache_dir=temp_cache_dir)
        
        cache.set("category", "owner", "value", repo="repo", week="2026W01")
        
        entry = cache.get_entry_info("category", "owner", repo="repo")
        assert entry is not None
        assert "2026W01" in entry["weeks"]
        assert entry["latest_week"] == "2026W01"

    def test_prune(self, temp_cache_dir):
        """Test pruning old entries."""
        cache = APICache(cache_dir=temp_cache_dir)
        
        # Add 3 weeks
        cache.set("cat", "owner", "v1", repo="repo", week="2026W01")
        cache.set("cat", "owner", "v2", repo="repo", week="2026W02")
        cache.set("cat", "owner", "v3", repo="repo", week="2026W03")
        
        # Prune to keep 2
        cache.prune(keep_weeks=2)
        
        assert cache.get("cat", "owner", repo="repo", week="2026W03") == "v3"
        assert cache.get("cat", "owner", repo="repo", week="2026W02") == "v2"
        assert cache.get("cat", "owner", repo="repo", week="2026W01") is None
        
        entry = cache.get_entry_info("cat", "owner", repo="repo")
        assert "2026W01" not in entry["weeks"]
