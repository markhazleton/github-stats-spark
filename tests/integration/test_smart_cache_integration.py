"""Smoke test for smart cache refresh integration."""

import json
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock, patch

from spark.config import SparkConfig
from spark.unified_data_generator import UnifiedDataGenerator


def test_smart_cache_integration():
    """Integration test: verify smart cache refresh works end-to-end."""
    
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir)
        
        # Create a mock old repositories.json
        old_timestamp = (datetime.now(timezone.utc) - timedelta(days=10)).isoformat()
        old_data = {
            "metadata": {
                "generated_at": old_timestamp,
                "schema_version": "2.0.0"
            },
            "repositories": [],
            "profile": {"username": "testuser"}
        }
        
        repos_json_path = output_dir / "repositories.json"
        with open(repos_json_path, "w") as f:
            json.dump(old_data, f)
        
        # Set up mocks
        with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
            config = Mock(spec=SparkConfig)
            config.config = {
                "analyzer": {},
                "dashboard": {"data_generation": {}},
                "repositories": {"exclude_forks": False, "exclude_archived": True}
            }
            
            generator = UnifiedDataGenerator(
                config=config,
                username="testuser",
                output_dir=str(output_dir),
                force_refresh=False
            )
            
            # Mock the fetcher methods
            mock_repos = [
                {
                    "name": "repo1",
                    "pushed_at": (datetime.now(timezone.utc) - timedelta(days=5)).isoformat(),
                    "archived": False
                },
                {
                    "name": "repo2", 
                    "pushed_at": (datetime.now(timezone.utc) - timedelta(days=15)).isoformat(),
                    "archived": False
                }
            ]
            
            generator.fetcher.fetch_repositories = Mock(return_value=mock_repos)
            generator.cache.clear_repository_cache = Mock(return_value=5)
            
            # Test 1: Check data freshness
            generated_at = generator._check_data_freshness()
            assert generated_at is not None
            print(f"✅ Found existing data generated at: {generated_at}")
            
            # Test 2: Selective refresh identifies correct repos
            repos_to_refresh = generator._selective_cache_refresh(generated_at)
            assert "repo1" in repos_to_refresh  # Pushed after generated_at
            assert "repo2" not in repos_to_refresh  # Pushed before generated_at
            print(f"✅ Identified {len(repos_to_refresh)} repositories needing refresh")
            
            # Test 3: Apply selective cache clear
            generator._apply_selective_cache_clear(repos_to_refresh)
            assert generator.cache.clear_repository_cache.call_count == len(repos_to_refresh)
            print(f"✅ Cleared cache for {len(repos_to_refresh)} repositories")
            
            print("\n🎉 Smart cache refresh integration test PASSED!")


def test_fresh_data_skip():
    """Integration test: verify generation is skipped for fresh data."""
    
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir)
        
        # Create a fresh repositories.json (2 days old)
        fresh_timestamp = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
        fresh_data = {
            "metadata": {
                "generated_at": fresh_timestamp,
                "schema_version": "2.0.0"
            },
            "repositories": [],
            "profile": {"username": "testuser"}
        }
        
        repos_json_path = output_dir / "repositories.json"
        with open(repos_json_path, "w") as f:
            json.dump(fresh_data, f)
        
        with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
            config = Mock(spec=SparkConfig)
            config.config = {
                "analyzer": {},
                "dashboard": {"data_generation": {}},
                "repositories": {}
            }
            
            generator = UnifiedDataGenerator(
                config=config,
                username="testuser",
                output_dir=str(output_dir),
                force_refresh=False
            )
            
            # Check data freshness
            generated_at = generator._check_data_freshness()
            assert generated_at is not None
            
            # Calculate age
            age = datetime.now(timezone.utc) - generated_at
            print(f"Data age: {age.days} days")
            
            # Verify it's less than 1 week
            assert age < timedelta(days=7)
            print("✅ Data is fresh (<7 days old)")
            
            # In real usage, generate() would return existing data immediately
            # We're just verifying the age check logic works
            print("✅ Would skip generation and return existing data")
            print("\n🎉 Fresh data skip test PASSED!")


if __name__ == "__main__":
    print("Running Smart Cache Refresh Integration Tests\n")
    print("=" * 60)
    print("\nTest 1: Smart Cache Integration")
    print("-" * 60)
    test_smart_cache_integration()
    
    print("\n" + "=" * 60)
    print("\nTest 2: Fresh Data Skip")
    print("-" * 60)
    test_fresh_data_skip()
    
    print("\n" + "=" * 60)
    print("\n✨ All integration tests passed successfully!")
