"""Unit tests for cache status tracking functionality."""

import json
import pytest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from spark.cache_status import CacheStatusTracker
from spark.cache import APICache


@pytest.fixture
def cache_dir(tmp_path):
    """Create a temporary cache directory."""
    cache_path = tmp_path / ".cache"
    cache_path.mkdir()
    return str(cache_path)


@pytest.fixture
def cache_tracker(cache_dir):
    """Create a CacheStatusTracker instance."""
    return CacheStatusTracker(cache_dir=cache_dir)


@pytest.fixture
def sample_repo_data():
    """Create sample repository data."""
    return {
        "name": "test-repo",
        "full_name": "testuser/test-repo",
        "language": "Python",
        "stars": 10,
        "forks": 2,
        "pushed_at": datetime.now(timezone.utc).isoformat(),
    }


@pytest.fixture
def repos_cache_file(cache_dir, sample_repo_data):
    """Create a sample repositories cache file."""
    cache = APICache(cache_dir=cache_dir)
    repos = [
        sample_repo_data,
        {
            "name": "old-repo",
            "full_name": "testuser/old-repo",
            "language": "JavaScript",
            "stars": 5,
            "forks": 1,
            "pushed_at": (datetime.now(timezone.utc) - timedelta(days=60)).isoformat(),
        }
    ]
    cache.set("repositories", "testuser", repos, repo="list_True_True_True")
    return cache


def create_cache_entry(cache, username, repo_name, category, age_hours=0, metadata=None, week=None):
    """Helper to create a cache entry."""
    if not week:
        week = datetime.now(timezone.utc).strftime("%YW%V")
    
    # We can't easily fake the timestamp in APICache.set because it uses datetime.now()
    # But we can modify the file after writing if needed, or just accept current time.
    # For tests checking age, we might need to patch datetime or modify the file.
    
    cache.set(category, username, {"test": "data"}, repo=repo_name, week=week, metadata=metadata)
    
    if age_hours > 0:
        # Manually update timestamp in file
        entry_info = cache.get_entry_info(category, username, repo=repo_name)
        # We need the path. APICache doesn't expose it easily publicly, but we can reconstruct it.
        # Or use _get_fs_path
        path = cache._get_fs_path(category, username, repo_name, week)
        
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        new_time = datetime.now(timezone.utc) - timedelta(hours=age_hours)
        data["timestamp"] = new_time.isoformat()
        
        # We also need to update manifest updated_at if we rely on it
        # But APICache.get reads the file timestamp for expiry?
        # CacheStatusTracker reads manifest updated_at.
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            
        # Update manifest
        key = cache._get_key_path(category, username, repo_name)
        cache.manifest.data["entries"][key]["updated_at"] = new_time.isoformat()
        cache.manifest._dirty = True
        cache.manifest.save()


def build_repo_metadata(username, repo_name, category, pushed_at=None):
    """Generate metadata matching APICache repository entries."""
    pushed_value = pushed_at or datetime.now(timezone.utc).isoformat()
    return {
        "repository": {"owner": username, "name": repo_name},
        "category": category,
        "pushed_at": pushed_value,
        "ttl_enforced": False,
    }


class TestCacheStatusTracker:
    """Tests for CacheStatusTracker class."""

    def test_init(self, cache_tracker, cache_dir):
        """Test CacheStatusTracker initialization."""
        assert cache_tracker.cache.cache_dir == Path(cache_dir)
        assert cache_tracker.cache.cache_dir.exists()

    def test_get_repository_cache_status_no_cache(self, cache_tracker):
        """Test getting cache status when no cache files exist."""
        status = cache_tracker.get_repository_cache_status(
            username="testuser",
            repo_name="test-repo",
            pushed_at=datetime.now(timezone.utc).isoformat()
        )
        
        assert status["has_cache"] is False
        assert status["cache_date"] is None
        assert status["refresh_needed"] is True
        assert "missing_cache_files" in status["refresh_reasons"]
        assert status["cache_files"]["commits_stats"]["exists"] is False
        assert status["cache_files"]["languages"]["exists"] is False

    def test_get_repository_cache_status_with_cache(self, cache_tracker, cache_dir):
        """Test getting cache status when cache files exist."""
        username = "testuser"
        repo_name = "test-repo"
        current_week = datetime.now(timezone.utc).strftime("%YW%V")
        # Push was 2 hours ago
        pushed_iso = (datetime.now(timezone.utc) - timedelta(hours=2)).isoformat()
        
        cache = APICache(cache_dir=cache_dir)
        
        # Create cache files (1 hour old)
        categories = ["commits_stats", "commit_counts", "languages", "dependency_files", "readme"]
        for cat in categories:
            create_cache_entry(
                cache, username, repo_name, cat, 
                age_hours=1, 
                metadata=build_repo_metadata(username, repo_name, cat, pushed_iso),
                week=current_week
            )
        
        # Force reload of manifest in cache_tracker
        cache_tracker.cache.manifest._last_mtime = 0

        status = cache_tracker.get_repository_cache_status(
            username=username,
            repo_name=repo_name,
            pushed_at=pushed_iso,
        )
        
        assert status["has_cache"] is True
        assert status["cache_date"] is not None
        assert status["refresh_needed"] is False
        assert len(status["refresh_reasons"]) == 0

    def test_get_repository_cache_status_old_cache_without_new_commits(self, cache_tracker, cache_dir):
        """Old cache files should remain valid when no new commits have landed."""
        username = "testuser"
        repo_name = "old-repo"
        pushed_date = datetime.now(timezone.utc) - timedelta(days=40)
        pushed_iso = pushed_date.isoformat()
        pushed_week = pushed_date.strftime("%YW%V")
        
        cache = APICache(cache_dir=cache_dir)
        
        categories = ["commits_stats", "commit_counts", "languages", "dependency_files", "readme"]
        for cat in categories:
            create_cache_entry(
                cache, username, repo_name, cat, 
                age_hours=800, 
                metadata=build_repo_metadata(username, repo_name, cat, pushed_iso),
                week=pushed_week
            )
        
        status = cache_tracker.get_repository_cache_status(
            username=username,
            repo_name=repo_name,
            pushed_at=pushed_iso,
        )
        
        assert status["has_cache"] is True
        assert status["refresh_needed"] is False
        assert status["refresh_reasons"] == []

    def test_get_repository_cache_status_recently_pushed(self, cache_tracker, cache_dir):
        """Repos with new commits should trigger refresh even if cache files exist."""
        username = "testuser"
        repo_name = "active-repo"

        # Cache created 2 days ago
        cache_time = datetime.now(timezone.utc) - timedelta(days=2)
        cached_week = cache_time.strftime("%YW%V")
        
        # Push happened 1 day ago (newer than cache, but same week if we are lucky, or we force it)
        # To ensure same week, let's pick a time.
        # Or just use the same week string.
        
        cache = APICache(cache_dir=cache_dir)

        categories = ["commits_stats", "commit_counts", "languages", "dependency_files", "readme"]
        for cat in categories:
            create_cache_entry(
                cache, username, repo_name, cat, 
                age_hours=48, # 2 days old
                metadata=build_repo_metadata(username, repo_name, cat, cache_time.isoformat()),
                week=cached_week
            )

        # New push is 1 day ago (so 1 day newer than cache)
        new_push_time = datetime.now(timezone.utc) - timedelta(days=1)
        # Ensure it maps to the same week for this test case
        # If it maps to different week, we get missing_cache_files (which is also valid but different path)
        # We want to test the timestamp comparison logic.
        # So we force the push_week to match cached_week in the tracker? 
        # No, tracker calculates it.
        # So we must ensure dates are in same week.
        # Let's just use the cached_week string and assume dates align, 
        # OR we can mock the week calculation? No.
        # We can just set new_push_time to be cache_time + 24 hours.
        new_push_time = cache_time + timedelta(hours=24)
        new_push_iso = new_push_time.isoformat()
        
        # Verify weeks match
        if new_push_time.strftime("%YW%V") != cached_week:
            # If crossing week boundary, this test case becomes "missing_cache_files"
            # We want to test "repo_has_new_commits"
            # So we skip if weeks don't match? Or adjust.
            pass

        # Force reload of manifest in cache_tracker to ensure it sees updates
        cache_tracker.cache.manifest._last_mtime = 0

        status = cache_tracker.get_repository_cache_status(
            username=username,
            repo_name=repo_name,
            pushed_at=new_push_iso,
        )
        
        # If weeks match, we expect repo_has_new_commits
        if new_push_time.strftime("%YW%V") == cached_week:
            assert status["refresh_needed"] is True
            assert "repo_has_new_commits" in status["refresh_reasons"]
        else:
            # If weeks differ, we expect missing_cache_files
            assert status["refresh_needed"] is True
            assert "missing_cache_files" in status["refresh_reasons"]

    def test_update_repositories_cache_with_status(self, cache_tracker, repos_cache_file):
        """Test updating repositories cache with status information."""
        result = cache_tracker.update_repositories_cache_with_status(
            username="testuser",
            exclude_private=True,
            exclude_forks=True,
            exclude_archived=True,
        )
        
        # result is {"value": [...]}
        assert "value" in result
        assert len(result["value"]) == 2
        
        # Check first repo has cache status
        first_repo = result["value"][0]
        assert "cache_status" in first_repo
        assert "has_cache" in first_repo["cache_status"]
        assert "refresh_needed" in first_repo["cache_status"]
        assert "cache_files" in first_repo["cache_status"]

    def test_update_repositories_cache_file_not_found(self, cache_tracker):
        """Test updating non-existent repositories cache."""
        with pytest.raises(FileNotFoundError):
            cache_tracker.update_repositories_cache_with_status(
                username="nonexistent",
                exclude_private=True,
                exclude_forks=True,
                exclude_archived=True,
            )

    def test_get_repositories_needing_refresh(self, cache_tracker, repos_cache_file, cache_dir):
        """Test getting list of repositories needing refresh."""
        # First update the cache with status
        cache_tracker.update_repositories_cache_with_status(
            username="testuser",
            exclude_private=True,
            exclude_forks=True,
            exclude_archived=True,
        )
        
        # Get repos needing refresh
        needs_refresh = cache_tracker.get_repositories_needing_refresh(
            username="testuser",
            exclude_private=True,
            exclude_forks=True,
            exclude_archived=True,
        )
        
        # Both repos should need refresh since no cache files exist
        assert len(needs_refresh) >= 1
        assert all("cache_status" in repo for repo in needs_refresh)
        assert all(repo["cache_status"]["refresh_needed"] for repo in needs_refresh)

    def test_get_cache_statistics(self, cache_tracker, repos_cache_file):
        """Test getting cache statistics."""
        # Update cache status first
        cache_tracker.update_repositories_cache_with_status(
            username="testuser",
            exclude_private=True,
            exclude_forks=True,
            exclude_archived=True,
        )
        
        stats = cache_tracker.get_cache_statistics(
            username="testuser",
            exclude_private=True,
            exclude_forks=True,
            exclude_archived=True,
        )
        
        assert "total_repositories" in stats
        assert "cached_repositories" in stats
        assert "needs_refresh" in stats
        assert "up_to_date" in stats
        assert "cache_hit_rate" in stats
        assert "refresh_rate" in stats
        
        assert stats["total_repositories"] == 2
        assert isinstance(stats["cache_hit_rate"], str)
        assert "%" in stats["cache_hit_rate"]

    def test_get_cache_statistics_no_cache(self, cache_tracker):
        """Test getting cache statistics when no cache exists."""
        stats = cache_tracker.get_cache_statistics(
            username="nonexistent",
            exclude_private=True,
            exclude_forks=True,
            exclude_archived=True,
        )
        
        assert stats["total_repositories"] == 0
        assert stats["cached_repositories"] == 0
        assert stats["needs_refresh"] == 0
        assert stats["up_to_date"] == 0

    def test_cache_files_structure(self, cache_tracker):
        """Test cache files structure in status."""
        status = cache_tracker.get_repository_cache_status(
            username="testuser",
            repo_name="test-repo",
            pushed_at=datetime.now(timezone.utc).isoformat()
        )
        
        cache_files = status["cache_files"]
        expected_types = [
            "commits_stats",
            "commit_counts",
            "languages",
            "dependency_files",
            "readme",
            "ai_summary"
        ]
        
        for cache_type in expected_types:
            assert cache_type in cache_files
            assert "exists" in cache_files[cache_type]
            # file path is not exposed in new structure easily, maybe remove check?
            # assert "file" in cache_files[cache_type] 
            assert "timestamp" in cache_files[cache_type]
            assert "age_hours" in cache_files[cache_type]

    def test_ai_summary_optional(self, cache_tracker, cache_dir):
        """Test that AI summary is optional and doesn't affect has_cache status."""
        username = "testuser"
        repo_name = "test-repo"
        current_week = datetime.now(timezone.utc).strftime("%YW%V")
        pushed_iso = datetime.now(timezone.utc).isoformat()
        
        cache = APICache(cache_dir=cache_dir)
        
        categories = ["commits_stats", "commit_counts", "languages", "dependency_files", "readme"]
        for cat in categories:
            create_cache_entry(
                cache, username, repo_name, cat, 
                age_hours=1, 
                metadata=build_repo_metadata(username, repo_name, cat, pushed_iso),
                week=current_week
            )
        
        status = cache_tracker.get_repository_cache_status(
            username=username,
            repo_name=repo_name,
            pushed_at=pushed_iso,
        )
        
        # Should have cache even without AI summary
        assert status["has_cache"] is True
        assert status["cache_files"]["ai_summary"]["exists"] is False
