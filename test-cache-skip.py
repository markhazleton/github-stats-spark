"""Quick test to verify cache skip functionality."""

from spark.cache_status import CacheStatusTracker
from spark.fetcher import GitHubFetcher
import os

# Check cache statistics
tracker = CacheStatusTracker()
stats = tracker.get_cache_statistics('markhazleton')

print("=" * 60)
print("Cache Statistics")
print("=" * 60)
print(f"Total repositories: {stats['total_repositories']}")
print(f"Cached repositories: {stats['cached_repositories']}")
print(f"Needs refresh: {stats['needs_refresh']}")
print(f"Up to date: {stats['up_to_date']}")
print(f"Cache hit rate: {stats['cache_hit_rate']}")
print(f"Refresh rate: {stats['refresh_rate']}")
print()
print(f"✅ Fetcher will SKIP {stats['up_to_date']} repositories with valid cache")
print(f"⚠️  Fetcher will REFRESH {stats['needs_refresh']} repositories")
print("=" * 60)

# Show which repos will be skipped
repos_needing_refresh = tracker.get_repositories_needing_refresh('markhazleton')
print(f"\n{len(repos_needing_refresh)} repositories need refresh:")
for repo in repos_needing_refresh[:10]:
    reasons = repo.get('cache_status', {}).get('refresh_reasons', [])
    print(f"  • {repo['name']}: {', '.join(reasons) if reasons else 'unknown'}")

if len(repos_needing_refresh) > 10:
    print(f"  ... and {len(repos_needing_refresh) - 10} more")

print("\n" + "=" * 60)
print("Test complete!")
print("=" * 60)
