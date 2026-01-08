# Clean Architecture Refactor Plan

## Current Problem
- Cache write operations scattered throughout fetcher methods
- Side effects during data reading make it impossible to run commands twice without API churn
- Unclear when caches get updated vs read
- AI summaries being regenerated unnecessarily

## New Clean Architecture

### Phase 1: Fetch Repository List
**File**: `unified_data_generator.py` → `_fetch_repository_list()`
- GET current list of public repos from GitHub (1 API call)
- Returns: List[Dict] with `name`, `pushed_at`, `stars`, etc.
- **No cache writes**

### Phase 2: Validate & Refresh Caches  
**File**: `cache_manager.py` (NEW)
- `CacheManager.refresh_user_data(username, repo_list, force_refresh)`
- For each repo: compare `pushed_at` with cached `pushed_at`
- If different: fetch & write new cache entries
- If same: skip (zero API calls)
- Returns: `RefreshSummary(repos_refreshed, repos_unchanged, api_calls)`
- **Only writes to cache, never reads during generation**

### Phase 3: Assemble Data from Cache
**File**: `unified_data_generator.py` → `_assemble_data()`
- READ all cached data for repositories
- Calculate AI summaries for repos that need them
- Calculate rankings, metrics, aggregations
- Returns: `UnifiedData` object ready for output
- **Only reads from cache, zero API calls, zero cache writes**

### Phase 4: Generate Outputs
**Files**: `unified_report_workflow.py`, `visualizer.py`
- Generate SVG visualizations from UnifiedData
- Generate markdown reports from UnifiedData
- Generate JSON export from UnifiedData
- **Pure functions - take data, produce outputs**
- **Zero cache operations, zero API calls**

## Implementation Steps

### Step 1: Create CacheManager ✅ DONE
- [x] Created `src/spark/cache_manager.py`
- [x] Implements `refresh_commit_counts()`, `refresh_languages()`
- [x] Main entry point: `refresh_user_data()`

### Step 2: Update Fetcher (Make Read-Only)
**File**: `src/spark/fetcher.py`
- [ ] Remove ALL `cache.set()` calls
- [ ] Keep only `cache.get()` calls
- [ ] Methods become pure read operations
- [ ] If cache miss → return None (don't fetch)

### Step 3: Update UnifiedDataGenerator
**File**: `src/spark/unified_data_generator.py`
- [ ] Phase 1: Call `fetcher.fetch_repositories()` (read from cache or fetch once)
- [ ] Phase 2: Call `cache_manager.refresh_user_data()` with repo list
- [ ] Phase 3: Assemble data by reading from cache
- [ ] Phase 4: Write JSON output

### Step 4: Update UnifiedReportWorkflow
**File**: `src/spark/unified_report_workflow.py`
- [ ] Remove all cache refresh logic
- [ ] Only READ from cache to generate reports
- [ ] Assume cache is already populated by Phase 2

### Step 5: Update CLI
**File**: `src/spark/cli.py`
- [ ] Update `handle_unified()` to use new flow
- [ ] Log refresh summary clearly
- [ ] Show "0 API calls" when running twice

## Expected Benefits

1. **Zero API Churn**: Running command twice = 0 API calls (all from cache)
2. **Clear Separation**: Refresh phase separate from read phase
3. **Predictable**: Know exactly when caches get updated
4. **Testable**: Each phase can be tested independently
5. **Fast**: Skip refresh phase entirely if data is fresh

## Testing Plan

1. **Test 1: Fresh Run**
   - Clear cache
   - Run `spark unified --user X`
   - Expect: All repos refreshed, N API calls

2. **Test 2: Second Run (No Changes)**
   - Run again immediately
   - Expect: 0 repos refreshed, 0 API calls, instant completion

3. **Test 3: Partial Refresh**
   - Push to one repo
   - Run again
   - Expect: Only 1 repo refreshed, minimal API calls

4. **Test 4: Force Refresh**
   - Run with `--force-refresh`
   - Expect: All repos refreshed regardless of cache

## Migration Notes

- Old code in `fetcher.py` that writes cache will be removed
- Cache operations centralized in `cache_manager.py`
- Backwards compatible - cache format unchanged
- Can be rolled out incrementally (one module at a time)
