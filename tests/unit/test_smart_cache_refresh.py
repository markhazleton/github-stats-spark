"""Unit tests for smart cache refresh logic."""

import json
import pytest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock, patch, mock_open

from spark.cache import APICache
from spark.unified_data_generator import UnifiedDataGenerator
from spark.config import SparkConfig


class TestAPICacheClearRepository:
    """Tests for selective repository cache clearing."""

    def test_clear_repository_cache_removes_matching_files(self, tmp_path):
        """Test that clear_repository_cache removes all files for a repository."""
        cache = APICache(cache_dir=str(tmp_path))
        
        # Create mock cache files
        username = "testuser"
        repo_name = "testrepo"
        
        cache_files = [
            f"commits_{username}_{repo_name}_2026W01.json",
            f"languages_{username}_{repo_name}_2026W01.json",
            f"readme_{username}_{repo_name}_2026W01.json",
            f"commit_counts_{username}_{repo_name}_2026W01.json",
            f"commits_stats_{username}_{repo_name}_200_2026W01.json",
            f"dependency_files_{username}_{repo_name}_2026W01.json",
        ]
        
        for filename in cache_files:
            (tmp_path / filename).write_text('{"test": "data"}')
        
        # Also create cache files for another repository (should NOT be deleted)
        other_repo_files = [
            f"commits_{username}_otherrepo_2026W01.json",
            f"languages_{username}_otherrepo_2026W01.json",
        ]
        for filename in other_repo_files:
            (tmp_path / filename).write_text('{"test": "data"}')
        
        # Clear cache for specific repository
        cleared_count = cache.clear_repository_cache(username, repo_name)
        
        # Verify correct number of files cleared
        assert cleared_count == len(cache_files)
        
        # Verify the correct files were removed
        for filename in cache_files:
            assert not (tmp_path / filename).exists()
        
        # Verify other repository files still exist
        for filename in other_repo_files:
            assert (tmp_path / filename).exists()

    def test_clear_repository_cache_handles_no_matches(self, tmp_path):
        """Test that clear_repository_cache handles case with no matching files."""
        cache = APICache(cache_dir=str(tmp_path))
        
        cleared_count = cache.clear_repository_cache("testuser", "nonexistent")
        assert cleared_count == 0


class TestDataFreshnessCheck:
    """Tests for checking repositories.json freshness."""

    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_check_data_freshness_returns_none_when_file_missing(
        self, mock_exists, mock_file
    ):
        """Test that _check_data_freshness returns None when file doesn't exist."""
        mock_exists.return_value = False
        
        with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
            config = Mock(spec=SparkConfig)
            config.config = {"analyzer": {}, "dashboard": {"data_generation": {}}}
            
            generator = UnifiedDataGenerator(
                config=config,
                username="testuser",
                output_dir="data"
            )
            
            result = generator._check_data_freshness()
            assert result is None

    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_check_data_freshness_parses_timestamp(self, mock_exists, mock_file):
        """Test that _check_data_freshness correctly parses generation timestamp."""
        mock_exists.return_value = True
        
        # Mock repositories.json with metadata
        test_timestamp = "2026-01-01T00:00:00Z"
        mock_data = {
            "metadata": {
                "generated_at": test_timestamp,
                "schema_version": "2.0.0"
            },
            "repositories": []
        }
        mock_file.return_value.read.return_value = json.dumps(mock_data)
        
        with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
            config = Mock(spec=SparkConfig)
            config.config = {"analyzer": {}, "dashboard": {"data_generation": {}}}
            
            generator = UnifiedDataGenerator(
                config=config,
                username="testuser",
                output_dir="data"
            )
            
            # Mock the file read
            with patch("json.load", return_value=mock_data):
                result = generator._check_data_freshness()
                
                assert result is not None
                assert isinstance(result, datetime)


class TestSelectiveCacheRefresh:
    """Tests for selective cache refresh logic."""

    def test_selective_cache_refresh_identifies_updated_repos(self):
        """Test that repos with new commits are identified for refresh."""
        with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
            config = Mock(spec=SparkConfig)
            config.config = {
                "analyzer": {},
                "dashboard": {"data_generation": {}},
                "repositories": {"exclude_forks": True, "exclude_archived": True}
            }
            
            generator = UnifiedDataGenerator(
                config=config,
                username="testuser",
                output_dir="data"
            )
            
            # Mock generated_at timestamp (7 days ago)
            generated_at = datetime.now(timezone.utc) - timedelta(days=7)
            
            # Mock repository data
            old_repo_pushed = (generated_at - timedelta(days=1)).isoformat()
            new_repo_pushed = (generated_at + timedelta(days=1)).isoformat()
            
            mock_repos = [
                {"name": "old-repo", "pushed_at": old_repo_pushed},
                {"name": "new-repo", "pushed_at": new_repo_pushed},
                {"name": "no-push-date", "pushed_at": None},
            ]
            
            # Mock the fetcher
            generator.fetcher.fetch_repositories = Mock(return_value=mock_repos)
            
            # Call selective cache refresh
            repos_to_refresh = generator._selective_cache_refresh(generated_at)
            
            # Verify results
            assert "new-repo" in repos_to_refresh  # Has new commits
            assert "no-push-date" in repos_to_refresh  # No push date (assume needs refresh)
            assert "old-repo" not in repos_to_refresh  # No new commits

    def test_apply_selective_cache_clear_calls_cache_clear(self):
        """Test that cache clearing is called for each repository."""
        with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
            config = Mock(spec=SparkConfig)
            config.config = {"analyzer": {}, "dashboard": {"data_generation": {}}}
            
            generator = UnifiedDataGenerator(
                config=config,
                username="testuser",
                output_dir="data"
            )
            
            # Mock the cache
            generator.cache.clear_repository_cache = Mock(return_value=5)
            
            repos_to_refresh = ["repo1", "repo2", "repo3"]
            generator._apply_selective_cache_clear(repos_to_refresh)
            
            # Verify cache clearing was called for each repo
            assert generator.cache.clear_repository_cache.call_count == 3
            generator.cache.clear_repository_cache.assert_any_call("testuser", "repo1")
            generator.cache.clear_repository_cache.assert_any_call("testuser", "repo2")
            generator.cache.clear_repository_cache.assert_any_call("testuser", "repo3")


class TestGenerateWithSmartRefresh:
    """Tests for the complete generate() workflow with smart refresh."""

    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    @patch("json.load")
    def test_generate_skips_when_data_is_fresh(
        self, mock_json_load, mock_exists, mock_file
    ):
        """Test that generate() returns existing data when less than 1 week old."""
        mock_exists.return_value = True
        
        # Mock recent timestamp (2 days ago)
        recent_timestamp = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
        mock_data = {
            "metadata": {
                "generated_at": recent_timestamp,
                "schema_version": "2.0.0"
            },
            "repositories": []
        }
        mock_json_load.return_value = mock_data
        
        with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
            config = Mock(spec=SparkConfig)
            config.config = {"analyzer": {}, "dashboard": {"data_generation": {}}}
            
            generator = UnifiedDataGenerator(
                config=config,
                username="testuser",
                output_dir="data",
                force_refresh=False
            )
            
            # Call generate - should return existing data without regenerating
            result = generator.generate()
            
            assert result == mock_data

    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_generate_uses_selective_refresh_when_data_is_old(
        self, mock_exists, mock_file
    ):
        """Test that generate() uses selective cache refresh when data is old."""
        mock_exists.return_value = True
        
        # Mock old timestamp (10 days ago)
        old_timestamp = (datetime.now(timezone.utc) - timedelta(days=10)).isoformat()
        mock_data = {
            "metadata": {
                "generated_at": old_timestamp,
                "schema_version": "2.0.0"
            },
            "repositories": []
        }
        
        with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
            config = Mock(spec=SparkConfig)
            config.config = {
                "analyzer": {},
                "dashboard": {"data_generation": {}},
                "repositories": {"exclude_forks": True, "exclude_archived": True}
            }
            
            generator = UnifiedDataGenerator(
                config=config,
                username="testuser",
                output_dir="data",
                force_refresh=False
            )
            
            # Mock methods
            with patch("json.load", return_value=mock_data):
                generator._selective_cache_refresh = Mock(return_value=["repo1", "repo2"])
                generator._apply_selective_cache_clear = Mock()
                generator.fetcher.fetch_repositories = Mock(return_value=[])
                generator.fetcher.fetch_user_profile = Mock(return_value={
                    "login": "testuser",
                    "username": "testuser"
                })
                
                # This will attempt full generation but we're testing the cache refresh logic
                try:
                    generator.generate()
                except Exception:
                    pass  # Expected to fail since we're not mocking everything
                
                # Verify selective refresh was called
                generator._selective_cache_refresh.assert_called_once()
                generator._apply_selective_cache_clear.assert_called_once()
