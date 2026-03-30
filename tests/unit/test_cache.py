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


class TestAPICacheHasEntry:
    """Test has_entry() method."""

    @pytest.fixture
    def temp_cache_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    def test_has_entry_true(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        cache.set("cat", "owner", "val", repo="repo", week="2026W01")
        assert cache.has_entry("cat", "owner", repo="repo", week="2026W01") is True

    def test_has_entry_false(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        assert cache.has_entry("cat", "owner", repo="nope") is False

    def test_has_entry_without_week(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        cache.set("cat", "owner", "val", repo="repo", week="2026W01")
        assert cache.has_entry("cat", "owner", repo="repo") is True


class TestAPICacheGetEntryInfo:
    """Test get_entry_info() method."""

    @pytest.fixture
    def temp_cache_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    def test_nonexistent_entry(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        assert cache.get_entry_info("cat", "owner", repo="nope") is None

    def test_existing_entry_has_fields(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        cache.set("cat", "owner", "val", repo="repo", week="2026W01")
        info = cache.get_entry_info("cat", "owner", repo="repo")
        assert info is not None
        assert "weeks" in info
        assert "latest_week" in info

    def test_multiple_weeks(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        cache.set("cat", "owner", "v1", repo="repo", week="2026W01")
        cache.set("cat", "owner", "v2", repo="repo", week="2026W02")
        info = cache.get_entry_info("cat", "owner", repo="repo")
        assert len(info["weeks"]) == 2
        assert info["latest_week"] == "2026W02"


class TestAPICacheClearRepository:
    """Test clear_repository_cache() method."""

    @pytest.fixture
    def temp_cache_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    def test_clears_all_categories(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        cache.set("commits", "user", "data1", repo="my-repo", week="2026W01")
        cache.set("readme", "user", "data2", repo="my-repo", week="2026W01")
        cache.set("languages", "user", "data3", repo="my-repo", week="2026W01")

        deleted = cache.clear_repository_cache("user", "my-repo")
        assert deleted >= 3

        assert cache.get("commits", "user", repo="my-repo", week="2026W01") is None
        assert cache.get("readme", "user", repo="my-repo", week="2026W01") is None

    def test_does_not_affect_other_repos(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        cache.set("cat", "user", "keep", repo="other-repo", week="2026W01")
        cache.set("cat", "user", "delete", repo="target-repo", week="2026W01")

        cache.clear_repository_cache("user", "target-repo")

        assert cache.get("cat", "user", repo="other-repo", week="2026W01") == "keep"


class TestAPICacheLatestWeek:
    """Test that get() returns latest week when no week specified."""

    @pytest.fixture
    def temp_cache_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    def test_get_returns_latest(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        cache.set("cat", "owner", "old", repo="repo", week="2026W01")
        cache.set("cat", "owner", "new", repo="repo", week="2026W02")
        result = cache.get("cat", "owner", repo="repo")
        assert result == "new"


class TestAPICacheManifestPersistence:
    """Test that manifest survives cache reloads."""

    @pytest.fixture
    def temp_cache_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    def test_reload_preserves_entries(self, temp_cache_dir):
        cache1 = APICache(cache_dir=temp_cache_dir)
        cache1.set("cat", "owner", "val", repo="repo", week="2026W01")

        # Create a new instance (simulates process restart)
        cache2 = APICache(cache_dir=temp_cache_dir)
        result = cache2.get("cat", "owner", repo="repo", week="2026W01")
        assert result == "val"

    def test_reload_preserves_manifest_info(self, temp_cache_dir):
        cache1 = APICache(cache_dir=temp_cache_dir)
        cache1.set("cat", "owner", "val", repo="repo", week="2026W01")

        cache2 = APICache(cache_dir=temp_cache_dir)
        info = cache2.get_entry_info("cat", "owner", repo="repo")
        assert info is not None
        assert "2026W01" in info["weeks"]


class TestAPICacheOwnerOnly:
    """Test cache operations at owner level (no repo)."""

    @pytest.fixture
    def temp_cache_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    def test_set_and_get_owner_level(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        cache.set("profile", "owner", {"username": "testuser"})
        result = cache.get("profile", "owner")
        assert result == {"username": "testuser"}

    def test_prune_empty_cache(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        # Should not raise
        cache.prune(keep_weeks=2)

    def test_clear_empty_cache(self, temp_cache_dir):
        cache = APICache(cache_dir=temp_cache_dir)
        # Should not raise
        cache.clear()
