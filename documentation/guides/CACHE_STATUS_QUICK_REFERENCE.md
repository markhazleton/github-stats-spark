# Cache Status Quick Reference

## 🚀 Quick Start

```bash
# Update cache status
spark cache --update-status --user USERNAME

# Check cache health
spark cache --status --user USERNAME

# See what needs refresh
spark cache --list-refresh-needed --user USERNAME
```

## 📊 CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `--status` | Show cache statistics | `spark cache --status --user markhazleton` |
| `--update-status` | Update cache metadata | `spark cache --update-status --user markhazleton` |
| `--list-refresh-needed` | List repos needing refresh | `spark cache --list-refresh-needed --user markhazleton` |
| `--info` | Show cache directory info | `spark cache --info` |
| `--clear` | Clear all cache | `spark cache --clear` |

## 🎯 Cache Status Fields

| Field | Type | Description |
|-------|------|-------------|
| `has_cache` | boolean | All essential cache files exist |
| `cache_date` | ISO timestamp | Most recent cache file date |
| `cache_age_hours` | float | Cache age in hours |
| `refresh_needed` | boolean | True if refresh required |
| `refresh_reasons` | array | Why refresh is needed |
| `cache_files` | object | Per-file cache status |

## 🔄 Refresh Triggers

1. **Missing Cache** - Essential cache files don't exist
2. **Expired Cache** - Cache older than 30 days (720 hours)
3. **Recent Update** - Repo pushed within last 7 days

## 📈 Performance Gains

- **API Calls**: 80-90% reduction
- **Generation Time**: ~80% faster
- **Rate Limits**: Better protection
- **Cache Hit Rate**: 90%+ after initial run

## 🎨 Output Examples

### Cache Statistics
```
Total repositories: 48
Cached repositories: 45 (93.8%)
Needs refresh: 3 (6.2%)
Up to date: 45 (93.8%)
Cache hit rate: 93.8%
Refresh rate: 6.2%
```

### Refresh List
```
⚠️  3 repositories need refresh:
  • repo1: missing_cache_files
  • repo2: cache_expired (age: 750.2 hours)
  • repo3: repo_updated_recently (pushed 2 days ago)
```

## 🔧 Programmatic Usage

### Check Single Repo
```python
from spark.cache_status import CacheStatusTracker

tracker = CacheStatusTracker()
status = tracker.get_repository_cache_status(
    username="markhazleton",
    repo_name="github-stats-spark",
    pushed_at="2026-01-04T12:00:00+00:00"
)
```

### Get Refresh List
```python
repos = tracker.get_repositories_needing_refresh(
    username="markhazleton"
)
print(f"{len(repos)} need refresh")
```

## ⚙️ Configuration

### Enable/Disable
```python
# Enabled (default)
fetcher = GitHubFetcher(use_cache_status=True)

# Disabled (legacy)
fetcher = GitHubFetcher(use_cache_status=False)
```

### Force Refresh
```bash
spark unified --user USERNAME --force-refresh
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| All repos need refresh | Run `spark cache --update-status --user USERNAME` |
| No repositories found | Check username and run initial generation |
| Cache not updating | Use `--force-refresh` flag |
| Wrong statistics | Verify `.cache/repositories_USERNAME_True_False.json` exists |

## 📚 Documentation

- **Full Guide**: [CACHE_STATUS_GUIDE.md](CACHE_STATUS_GUIDE.md)
- **Implementation**: [CACHE_STATUS_IMPLEMENTATION.md](CACHE_STATUS_IMPLEMENTATION.md)
- **Tests**: `tests/unit/test_cache_status.py`

## ✅ Testing

```bash
# Unit tests
pytest tests/unit/test_cache_status.py -v

# Integration test
.\test-cache-status.ps1    # Windows
./test-cache-status.sh     # Unix/macOS
```

## 🎓 Best Practices

1. **Update status after initial generation**
   ```bash
   spark unified --user USERNAME
   spark cache --update-status --user USERNAME
   ```

2. **Check health regularly**
   ```bash
   spark cache --status --user USERNAME
   ```

3. **Force refresh when needed**
   ```bash
   spark unified --user USERNAME --force-refresh
   ```

4. **Monitor refresh rate**
   - Good: <10% refresh rate
   - Normal: 10-30% refresh rate
   - High: >30% refresh rate (may need cache tuning)

## 🚦 Status Indicators

- ✅ `refresh_needed: false` - Cache valid, will skip
- ⚠️ `refresh_needed: true` - Will fetch fresh data
- 📅 `cache_age_hours` - Cache freshness indicator
- 🔄 `push_week` vs `current_week` - Update detection

## 💡 Pro Tips

1. Run `--update-status` after each generation
2. Use `--list-refresh-needed` before long runs
3. Check `--info` to monitor cache size
4. Use `--force-refresh` sparingly (wastes API calls)
5. Cache expires after 30 days (automatic cleanup)
