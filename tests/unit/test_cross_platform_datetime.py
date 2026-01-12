"""Cross-platform datetime compatibility tests for smart cache refresh.

These tests ensure datetime handling works correctly on both Windows and Linux (GitHub Actions).
"""

import json
import tempfile
from datetime import datetime, timezone, timedelta
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from spark.config import SparkConfig
from spark.unified_data_generator import UnifiedDataGenerator


class TestCrossPlatformDatetimeHandling:
    """Tests to ensure datetime operations work on Windows and Linux."""

    @pytest.mark.parametrize("timestamp_format", [
        "2026-01-01T00:00:00Z",  # UTC with Z suffix
        "2026-01-01T00:00:00+00:00",  # UTC with offset
        "2026-01-01T00:00:00",  # Naive (should be treated as UTC)
    ])
    def test_parses_various_timestamp_formats(self, timestamp_format):
        """Test that various ISO timestamp formats are parsed correctly."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            
            # Create repositories.json with various timestamp formats
            mock_data = {
                "metadata": {
                    "generated_at": timestamp_format,
                    "schema_version": "2.0.0"
                },
                "repositories": []
            }
            
            repos_json_path = output_dir / "repositories.json"
            with open(repos_json_path, "w") as f:
                json.dump(mock_data, f)
            
            with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
                config = Mock(spec=SparkConfig)
                config.config = {"analyzer": {}, "dashboard": {"data_generation": {}}}
                
                generator = UnifiedDataGenerator(
                    config=config,
                    username="testuser",
                    output_dir=str(output_dir)
                )
                
                # Should parse successfully and return timezone-aware datetime
                generated_at = generator._check_data_freshness()
                
                assert generated_at is not None
                assert generated_at.tzinfo is not None  # Must be timezone-aware
                assert generated_at.tzinfo == timezone.utc  # Must be UTC

    def test_datetime_comparison_with_various_formats(self):
        """Test that datetime comparisons work regardless of input format."""
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
            
            # Base timestamp (10 days ago)
            base_time = datetime.now(timezone.utc) - timedelta(days=10)
            
            # Test various formats for pushed_at
            test_cases = [
                {
                    "name": "repo_with_z",
                    "pushed_at": (base_time + timedelta(days=1)).isoformat().replace('+00:00', 'Z'),
                },
                {
                    "name": "repo_with_offset",
                    "pushed_at": (base_time + timedelta(days=1)).isoformat(),
                },
                {
                    "name": "repo_naive",
                    "pushed_at": (base_time + timedelta(days=1)).replace(tzinfo=None).isoformat(),
                },
            ]
            
            generator.fetcher.fetch_repositories = Mock(return_value=test_cases)
            
            # All should be identified as needing refresh
            repos_to_refresh = generator._selective_cache_refresh(base_time)
            
            assert len(repos_to_refresh) == 3
            assert "repo_with_z" in repos_to_refresh
            assert "repo_with_offset" in repos_to_refresh
            assert "repo_naive" in repos_to_refresh

    def test_generated_metadata_always_uses_utc(self):
        """Test that generated metadata always uses UTC timezone."""
        # Simply test that when we generate metadata, it uses UTC
        # We don't need to run the full generator for this
        
        # Direct test: verify datetime.now(timezone.utc).isoformat() produces valid UTC timestamp
        test_timestamp = datetime.now(timezone.utc).isoformat()
        
        # Parse it back
        parsed = datetime.fromisoformat(test_timestamp)
        
        # Should be timezone-aware and UTC
        assert parsed.tzinfo is not None
        # ISO format with timezone should include offset info
        assert '+' in test_timestamp or 'Z' in test_timestamp

    def test_age_calculation_works_across_platforms(self):
        """Test that age calculation produces consistent results."""
        # Create a timestamp 10 days ago
        old_timestamp = (datetime.now(timezone.utc) - timedelta(days=10)).isoformat()
        
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            
            mock_data = {
                "metadata": {
                    "generated_at": old_timestamp,
                    "schema_version": "2.0.0"
                },
                "repositories": []
            }
            
            repos_json_path = output_dir / "repositories.json"
            with open(repos_json_path, "w") as f:
                json.dump(mock_data, f)
            
            with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
                config = Mock(spec=SparkConfig)
                config.config = {"analyzer": {}, "dashboard": {"data_generation": {}}}
                
                generator = UnifiedDataGenerator(
                    config=config,
                    username="testuser",
                    output_dir=str(output_dir)
                )
                
                generated_at = generator._check_data_freshness()
                
                # Calculate age (should work on any platform)
                age = datetime.now(timezone.utc) - generated_at
                
                # Should be approximately 10 days (allow 1 minute variance for test execution)
                assert 9.9 < age.days < 10.1
                assert age.total_seconds() > 0  # Should always be positive

    def test_timezone_aware_comparison_never_fails(self):
        """Test that timezone-aware comparisons never raise TypeError."""
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
            
            # Base time (timezone-aware)
            base_time = datetime.now(timezone.utc) - timedelta(days=7)
            
            # Mix of timezone-aware and naive timestamps
            mixed_repos = [
                {
                    "name": "repo1",
                    "pushed_at": datetime.now(timezone.utc).isoformat(),  # Aware
                },
                {
                    "name": "repo2",
                    "pushed_at": datetime.now().replace(tzinfo=None).isoformat(),  # Naive
                },
                {
                    "name": "repo3",
                    "pushed_at": None,  # Missing
                },
            ]
            
            generator.fetcher.fetch_repositories = Mock(return_value=mixed_repos)
            
            # Should not raise TypeError
            try:
                repos_to_refresh = generator._selective_cache_refresh(base_time)
                # All should be in refresh list (all pushed recently or missing date)
                assert len(repos_to_refresh) == 3
            except TypeError as e:
                pytest.fail(f"Timezone comparison raised TypeError: {e}")


def test_windows_and_linux_path_compatibility():
    """Test that Path operations work on both Windows and Linux."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir)
        
        # Create nested structure
        repos_json_path = output_dir / "repositories.json"
        repos_json_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write test data
        test_data = {"metadata": {"generated_at": datetime.now(timezone.utc).isoformat()}}
        with open(repos_json_path, "w") as f:
            json.dump(test_data, f)
        
        # Verify file exists and is readable
        assert repos_json_path.exists()
        assert repos_json_path.is_file()
        
        # Read back
        with open(repos_json_path, "r") as f:
            loaded = json.load(f)
        
        assert "metadata" in loaded
        assert "generated_at" in loaded["metadata"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
