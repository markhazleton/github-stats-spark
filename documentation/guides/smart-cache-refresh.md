# Smart Cache Refresh Guide

## Overview

The Smart Cache Refresh feature optimizes the data generation process by intelligently determining which repositories need fresh data and which can reuse cached information. This significantly reduces API calls, processing time, and stays well within GitHub API rate limits.

## How It Works

### 1. Check Data Freshness

When you run `spark unified` without `--force-refresh`, the system:

1. Checks if `data/repositories.json` exists
2. Reads the `generated_at` timestamp from the metadata
3. Calculates the age of the data

### 2. Decision Logic

**If data is less than 1 week old:**
- ✅ **SKIP** generation entirely
- Returns existing data immediately
- No API calls made
- Instant response

**If data is more than 1 week old:**
- ✅ Uses **Smart Cache Refresh**
- Fetches lightweight repository list from GitHub
- Compares each repo's `pushed_at` date with `generated_at`
- Only refreshes cache for repos with new commits

**If no existing data or `--force-refresh` flag:**
- Clears all cache
- Performs full regeneration

### 3. Selective Cache Clearing

For repositories that have new commits, the system clears **ALL** cache entries related to that repository:

- `commits_*` - Commit history
- `commit_counts_*` - Commit statistics
- `commits_stats_*` - Detailed commit metrics
- `languages_*` - Language breakdown
- `readme_*` - README content
- `dependency_files_*` - Dependency manifests

This ensures complete data consistency while preserving cache for unchanged repositories.

## Usage Examples

### Example 1: Fresh Data (< 1 week)

```bash
$ spark unified --user markhazleton

[INFO] Found existing repositories.json generated at: 2026-01-03 10:30:00+00:00
[INFO] repositories.json is 1 days old (< 7 days) - skipping generation
[INFO] Use --force-refresh to regenerate anyway
```

**Result:** Instant response, no API calls

### Example 2: Testing with Limited Repositories

```bash
$ spark unified --user markhazleton --max-repos 2

[INFO] ⚠️  Testing mode: Limited to 2 repositories
[INFO] Fetching repositories for markhazleton...
[INFO] Found 50 repositories
[INFO] Limiting to first 2 repositories for processing
```

**Result:** Quick validation of cache logic without processing all repos

**Use cases:**
- Debugging cache refresh logic
- Testing configuration changes
- Validating AI summaries on a subset
- Quick development iterations

### Example 3: Stale Data (> 1 week)

```bash
$ spark unified --user markhazleton

[INFO] Found existing repositories.json generated at: 2025-12-20 10:30:00+00:00
[INFO] repositories.json is 15 days old (>= 7 days) - using smart cache refresh
[INFO] Checking for repositories with new commits since last generation...
[INFO]   git-spark: needs refresh (pushed 2026-01-03T14:20:00Z)
[INFO]   old-project: cache valid (last push 2025-12-15T09:00:00Z)
[INFO]   active-repo: needs refresh (pushed 2026-01-02T18:45:00Z)
[INFO] Found 2/50 repositories needing cache refresh
[INFO] Clearing cache for 2 repositories with new commits...
[INFO] Cleared 12 total cache entries for updated repositories
```

**Result:** Only 2 repositories are refreshed, saving ~96% of API calls

### Example 4: Force Full Refresh

```bash
$ spark unified --user markhazleton --force-refresh

[INFO] Force refresh enabled - clearing all cache and regenerating
[INFO] Fetching repositories for markhazleton...
[INFO] Found 50 repositories
```

**Result:** Full regeneration with fresh data for everything

## Performance Benefits

### API Call Reduction

| Scenario | Repos with Changes | API Calls Saved | Time Saved |
|----------|-------------------|-----------------|------------|
| All static (< 1 week) | 0/50 | ~500 calls | ~5 minutes |
| Few active (> 1 week) | 5/50 | ~450 calls | ~4 minutes |
| Many active (> 1 week) | 25/50 | ~250 calls | ~2 minutes |
| Force refresh | 50/50 | 0 calls | 0 minutes |

### Cache Efficiency

**Weekly Granularity:** Cache keys include ISO week format (`2026W01`), so cache automatically invalidates when:
1. A new week starts
2. Repository has new commits

This balances freshness with efficiency, ensuring data is never more than 1 week stale while maximizing cache hits.

## Configuration

### Default Behavior

```yaml
# config/spark.yml
cache:
  ttl_hours: 720  # 30 days (overridden by weekly granularity)
  directory: .cache
```

### CLI Override

```bash
# Always force fresh data
spark unified --user markhazleton --force-refresh

# Use default smart refresh
spark unified --user markhazleton
```

## Implementation Details

### Cache Key Format

Cache keys include the ISO week to enable automatic weekly invalidation:

```
commits_{username}_{repo_name}_{week}.json
languages_{username}_{repo_name}_{week}.json
readme_{username}_{repo_name}_{week}.json
```

Example: `commits_markhazleton_git-spark_2026W01.json`

### Data Freshness Check

```python
def _check_data_freshness(self) -> Optional[datetime]:
    """Check if repositories.json exists and return generation timestamp."""
    repos_json_path = self.output_dir / "repositories.json"
    
    if not repos_json_path.exists():
        return None
    
    data = json.load(open(repos_json_path))
    generated_at_str = data.get("metadata", {}).get("generated_at")
    return datetime.fromisoformat(generated_at_str)
```

### Selective Refresh Logic

```python
def _selective_cache_refresh(self, generated_at: datetime) -> List[str]:
    """Determine which repositories need cache refresh."""
    repos = self.fetcher.fetch_repositories(self.username)
    repos_needing_refresh = []
    
    for repo in repos:
        pushed_at = datetime.fromisoformat(repo["pushed_at"])
        if pushed_at > generated_at:
            repos_needing_refresh.append(repo["name"])
    
    return repos_needing_refresh
```

## Troubleshooting

### Issue: Data Seems Outdated

**Solution:** Use `--force-refresh` to bypass cache:
```bash
spark unified --user markhazleton --force-refresh
```

### Issue: Cache Not Being Used

**Check:**
1. Verify `.cache/` directory exists and has files
2. Check file timestamps: `ls -la .cache/`
3. Ensure GitHub token is set: `echo $GITHUB_TOKEN`

### Issue: Partial Data After Smart Refresh

**Cause:** Some repository fetches may have failed

**Solution:** Check logs for errors, retry with `--force-refresh`

## Best Practices

### 1. Regular Weekly Runs

Schedule weekly runs to keep data fresh:

```bash
# GitHub Actions workflow
- name: Update GitHub Stats
  run: spark unified --user ${{ github.actor }}
  schedule:
    - cron: '0 0 * * 0'  # Every Sunday at midnight
```

### 2. Development Workflow

During development, use `--force-refresh` to ensure latest data:

```bash
spark unified --user markhazleton --force-refresh --verbose
```

### 3. Testing with Limited Repositories

Test cache logic with a small subset of repositories:

```bash
spark unified --user markhazleton --max-repos 2 --verbose
```

The `--max-repos` parameter limits processing throughout the **entire workflow**, including:
- Data generation (repository fetching and analysis)
- SVG generation (visualizations)
- Report generation (markdown outputs)

This ensures faster testing cycles when validating cache behavior.

### 4. Production Workflow

In production, rely on smart refresh for efficiency:

```bash
spark unified --user markhazleton --include-ai-summaries
```

## Technical Specifications

### Constitutional Requirements Met

✅ **Performance:** <5 minutes for <500 repos (smart refresh achieves <1 minute for typical updates)  
✅ **Cache TTL:** 6-hour minimum (enhanced with weekly granularity)  
✅ **Rate Limiting:** Exponential backoff with smart caching reduces API calls by 80-95%  
✅ **Observable:** All cache operations logged to stdout/stderr  

### Schema Version

Smart cache refresh is compatible with schema version `2.0.0` and above.

### Breaking Changes

None - this is a backward-compatible enhancement. Existing workflows continue to function unchanged.

## Related Documentation

- [API Reference](../api/api-reference.md) - Cache and fetcher API details
- [Testing Guide](../TESTING.md) - Unit tests for smart cache refresh
- [Performance Guide](../performance/) - Performance optimization strategies
