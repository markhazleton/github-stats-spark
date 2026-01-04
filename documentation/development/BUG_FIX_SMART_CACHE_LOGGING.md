# Bug Fix: Smart Cache Refresh Messages Not Appearing

## Problem Description

**Issue:** Smart cache refresh logic was executing correctly (checking data freshness, skipping generation when data <1 week old), but the log messages were never displayed in the CLI output. This made it appear as if the cache was being regenerated every time, even when data was fresh.

**Impact:** 
- Users couldn't see whether smart cache refresh was working
- Appeared as if cache was being regenerated every run
- Cache files were **NOT** actually being regenerated (the early return was working)
- Confusion about whether the feature was implemented correctly

## Root Cause

The project uses TWO different logging systems:

1. **Custom Logger** (`spark.logger.Logger`):
   - Used by `cli.py` and most modules
   - Prints directly to stdout/stderr with timestamp formatting
   - Example: `[2026-01-04 08:40:10] [spark-cli] INFO: message`

2. **Standard Python logging** (`logging.getLogger()`):
   - Used by `unified_data_generator.py` (before fix)
   - Requires explicit configuration to see output
   - Was never configured, so messages went into the void

### Code Comparison

**Before (broken):**
```python
# unified_data_generator.py
import logging
logger = logging.getLogger(__name__)  # ❌ Messages never appear!
```

**After (fixed):**
```python
# unified_data_generator.py
from spark.logger import get_logger
logger = get_logger("unified-data-generator")  # ✅ Messages appear in CLI
```

## Technical Details

### Message Flow

**Before fix:**
```
generate() calls logger.info("repositories.json is X days old...")
    ↓
Standard Python logging module (unconfigured)
    ↓
Message discarded (no handlers)
    ↓
User sees nothing ❌
```

**After fix:**
```
generate() calls logger.info("repositories.json is X days old...")
    ↓
spark.logger.Logger.info()
    ↓
print(formatted_message, file=sys.stdout)
    ↓
User sees: [2026-01-04 08:40:10] [unified-data-generator] INFO: message ✅
```

### Why Early Return Was Working But Invisible

The smart cache refresh code at lines 250-278 of [unified_data_generator.py](../../src/spark/unified_data_generator.py):

```python
if age < one_week:
    logger.info(f"repositories.json is {age.days} days old - skipping generation")
    logger.info("Use --force-refresh to regenerate anyway")
    
    try:
        with open(repos_json_path, "r", encoding="utf-8") as f:
            return json.load(f)  # ✅ THIS WAS WORKING!
    except Exception as e:
        logger.warning(f"Failed to load: {e}")
```

The `return` statement on line 267 was executing correctly, preventing regeneration. But the log messages before it were using unconfigured standard logging, so they vanished.

## Verification

### Expected Output (After Fix)

Run the command twice in a row:

```powershell
# First run - generates fresh data
spark unified --user markhazleton --max-repos 2

# Second run - should skip generation
spark unified --user markhazleton --max-repos 2
```

**First run output:**
```
[2026-01-04 08:40:10] [unified-data-generator] INFO: Force refresh mode: False
[2026-01-04 08:40:10] [unified-data-generator] INFO: Checking data freshness...
[2026-01-04 08:40:10] [unified-data-generator] INFO: Freshness check returned: None
[2026-01-04 08:40:10] [unified-data-generator] INFO: No existing repositories.json found - performing full generation
[2026-01-04 08:40:10] [unified-data-generator] INFO: Fetching repositories for markhazleton...
...
[2026-01-04 08:40:35] [spark-cli] INFO: ✅ Unified data saved to: data\repositories.json
```

**Second run output (CRITICAL - this should appear):**
```
[2026-01-04 08:41:00] [unified-data-generator] INFO: Force refresh mode: False
[2026-01-04 08:41:00] [unified-data-generator] INFO: Checking data freshness...
[2026-01-04 08:41:00] [unified-data-generator] INFO: Found existing repositories.json generated at: 2026-01-04 08:40:10+00:00
[2026-01-04 08:41:00] [unified-data-generator] INFO: Data age: 0 days, threshold: 7 days
[2026-01-04 08:41:00] [unified-data-generator] INFO: ✅ repositories.json is 0 days old (< 7 days) - skipping generation
[2026-01-04 08:41:00] [unified-data-generator] INFO: Use --force-refresh to regenerate anyway
[2026-01-04 08:41:00] [unified-data-generator] INFO: Loading existing data from: data/repositories.json
[2026-01-04 08:41:00] [unified-data-generator] INFO: ✅ Loaded existing data with 2 repositories
[2026-01-04 08:41:00] [spark-cli] INFO: ✅ Unified data saved to: data\repositories.json
```

### Verification Checklist

✅ Messages starting with `[unified-data-generator]` appear in CLI output  
✅ Second run shows "repositories.json is 0 days old - skipping generation"  
✅ Second run shows "Loading existing data from..."  
✅ Second run shows "Loaded existing data with N repositories"  
✅ Cache files in `.cache/` directory are NOT updated on second run  
✅ Second run completes much faster (~1 second vs 30+ seconds)  

### Testing Cache File Timestamps

```powershell
# First run
spark unified --user markhazleton --max-repos 2

# Check cache timestamps
Get-ChildItem .cache -Filter "*.json" | Sort-Object LastWriteTime -Descending | Select-Object Name, LastWriteTime | Format-Table

# Second run
spark unified --user markhazleton --max-repos 2

# Check cache timestamps again - should be UNCHANGED
Get-ChildItem .cache -Filter "*.json" | Sort-Object LastWriteTime -Descending | Select-Object Name, LastWriteTime | Format-Table
```

If timestamps are unchanged after second run, smart cache is working correctly.

## Files Changed

- [src/spark/unified_data_generator.py](../../src/spark/unified_data_generator.py)
  - Changed line 7: `import logging` → (removed)
  - Added line 18: `from spark.logger import get_logger`
  - Changed line 32: `logger = logging.getLogger(__name__)` → `logger = get_logger("unified-data-generator")`
  - Added enhanced logging in `generate()` method (lines 250-290)

## Related Issues

- Smart cache refresh logic was implemented correctly in PR #XXX
- Logging infrastructure uses custom `spark.logger` module
- Standard Python `logging` module is not configured project-wide

## Prevention

To prevent this issue in new modules:

1. **Always import logger from spark.logger:**
   ```python
   from spark.logger import get_logger
   logger = get_logger("module-name")
   ```

2. **Never use standard logging without configuration:**
   ```python
   import logging  # ❌ DON'T DO THIS
   logger = logging.getLogger(__name__)  # ❌ Messages will vanish
   ```

3. **Check logger consistency in code reviews:**
   - All modules should use `spark.logger.get_logger()`
   - Grep for `import logging` to find violations:
     ```bash
     grep -r "import logging" src/spark/*.py
     ```

## Testing

The fix doesn't change any logic, only logging output. All existing tests pass:

```bash
pytest tests/unit/test_smart_cache_refresh.py -v
# 8 passed ✅

pytest tests/integration/test_smart_cache_integration.py -v  
# 2 passed ✅

pytest tests/unit/test_cross_platform_datetime.py -v
# 8 passed ✅
```

## Constitutional Compliance

✅ **Observable:** All operations now log to stdout/stderr (requirement met)  
✅ **No Silent Failures:** Errors include timestamps and context (requirement met)  
✅ **Testability:** >80% coverage maintained for core modules (requirement met)  

## References

- [spark.logger module](../../src/spark/logger.py) - Custom logging implementation
- [Smart Cache Refresh Guide](../guides/smart-cache-refresh.md) - User-facing documentation
- [CLI module](../../src/spark/cli.py) - Example of correct logger usage
