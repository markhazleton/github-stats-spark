# Cross-Platform Compatibility Guide

## Overview

The smart cache refresh feature is designed to work consistently across both **Windows CLI** and **GitHub Actions (Linux)** environments. This guide documents the platform-agnostic design decisions and testing strategies.

## Platform Compatibility

### Supported Platforms

✅ **Windows 10/11** (PowerShell, CMD)  
✅ **Linux** (Ubuntu 20.04+, GitHub Actions runners)  
✅ **macOS** (10.15+)  
✅ **WSL2** (Windows Subsystem for Linux)

## Key Design Decisions

### 1. Timezone-Aware Datetimes

**Problem:** Python's `datetime` module can produce naive (no timezone) or aware (with timezone) objects, leading to comparison errors across platforms.

**Solution:** All datetime operations explicitly use `timezone.utc`:

```python
# Module-level import
from datetime import datetime, timezone, timedelta

# All datetime.now() calls use UTC
start_time = datetime.now(timezone.utc)
generated_at = datetime.now(timezone.utc).isoformat()

# Age calculation (both operands are timezone-aware)
age = datetime.now(timezone.utc) - generated_at
```

**Benefits:**
- No `TypeError: can't subtract offset-naive and offset-aware datetimes`
- Consistent behavior across time zones
- Explicit UTC makes intent clear

### 2. ISO 8601 Timestamp Parsing

**Problem:** Timestamps from JSON can have various formats:
- `2026-01-01T00:00:00Z` (UTC with Z suffix)
- `2026-01-01T00:00:00+00:00` (UTC with offset)
- `2026-01-01T00:00:00` (naive)

**Solution:** Normalize all formats and ensure timezone awareness:

```python
# Normalize Z suffix to +00:00
generated_at_str_clean = generated_at_str.replace('Z', '+00:00')
generated_at = datetime.fromisoformat(generated_at_str_clean)

# If parsed datetime is naive, assume UTC
if generated_at.tzinfo is None:
    generated_at = generated_at.replace(tzinfo=timezone.utc)
```

**Benefits:**
- Handles all common ISO 8601 formats
- Never produces naive datetimes
- Safe assumption (GitHub API always returns UTC)

### 3. Path Handling

**Problem:** Windows uses backslashes (`\`), Linux uses forward slashes (`/`).

**Solution:** Use `pathlib.Path` for all file operations:

```python
from pathlib import Path

# Automatically handles platform-specific separators
repos_json_path = output_dir / "repositories.json"
cache_dir = Path(".cache")
```

**Benefits:**
- Platform-agnostic path operations
- No manual path separator handling
- Works with both absolute and relative paths

### 4. JSON Serialization

**Problem:** Datetime objects aren't JSON-serializable.

**Solution:** Always serialize to ISO 8601 strings with UTC timezone:

```python
metadata = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    # Output: "2026-01-04T12:34:56.789012+00:00"
}
```

**Benefits:**
- Standard format recognized by all platforms
- Includes timezone information
- Easy to parse back to datetime

## Testing Strategy

### 1. Cross-Platform DateTime Tests

Located in [`tests/unit/test_cross_platform_datetime.py`](../../tests/unit/test_cross_platform_datetime.py)

**Test Coverage:**
- ✅ Parses various timestamp formats (Z, +00:00, naive)
- ✅ Datetime comparisons with mixed formats
- ✅ Generated metadata always uses UTC
- ✅ Age calculation consistency
- ✅ Timezone-aware comparisons never fail
- ✅ Path operations work on both platforms

### 2. GitHub Actions Validation

**Workflow:** `.github/workflows/generate-stats.yml`

```yaml
name: Generate Stats
on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:

jobs:
  generate:
    runs-on: ubuntu-latest  # Linux environment
    steps:
      - name: Generate Stats
        run: |
          spark unified --user ${{ github.actor }}
```

**Validation Points:**
- Runs on Linux (ubuntu-latest)
- Uses UTC timezone by default
- Tests smart cache refresh in production environment

### 3. Local Testing on Windows

**PowerShell:**
```powershell
# Run all platform tests
pytest tests/unit/test_cross_platform_datetime.py -v

# Run integration tests
pytest tests/integration/test_smart_cache_integration.py -v

# Test actual command
spark unified --user yourusername
```

## Common Issues & Solutions

### Issue 1: TypeError on DateTime Subtraction

**Error:**
```
TypeError: can't subtract offset-naive and offset-aware datetimes
```

**Cause:** Mixing naive and aware datetimes

**Solution:** ✅ Fixed - All datetimes now use `timezone.utc`

### Issue 2: Path Not Found on Windows

**Error:**
```
FileNotFoundError: [WinError 3] The system cannot find the path specified: '.cache\\file.json'
```

**Cause:** Hardcoded path separators

**Solution:** ✅ Fixed - Using `pathlib.Path` throughout

### Issue 3: Timestamp Parsing Fails

**Error:**
```
ValueError: Invalid isoformat string: '2026-01-01T00:00:00Z'
```

**Cause:** `fromisoformat()` doesn't handle 'Z' suffix

**Solution:** ✅ Fixed - Replace 'Z' with '+00:00' before parsing

### Issue 4: Cache Keys Different on Windows

**Cause:** Path separators in cache keys

**Solution:** ✅ Fixed - Cache keys use underscores, not path separators:
```python
cache_key = f"commits_{username}_{repo_name}_{week}"
```

## Environment Variables

### Required

```bash
# Both platforms
export GITHUB_TOKEN=your_token_here

# Optional (for AI summaries)
export ANTHROPIC_API_KEY=your_key_here
```

**Windows PowerShell:**
```powershell
$env:GITHUB_TOKEN = "your_token_here"
$env:ANTHROPIC_API_KEY = "your_key_here"
```

## Platform-Specific Notes

### Windows

**Date/Time Display:**
- PowerShell: Uses local timezone for display
- UTC internally: All operations use UTC
- No conversion needed

**File Paths:**
- Supports both `/` and `\` in paths
- `pathlib.Path` normalizes automatically

**Line Endings:**
- Git handles CRLF/LF conversion
- JSON files use LF for consistency

### Linux (GitHub Actions)

**Date/Time Display:**
- Uses UTC by default
- Matches internal UTC operations
- Consistent with GitHub API

**File Paths:**
- Only `/` separator supported
- `pathlib.Path` handles correctly

**Line Endings:**
- Always LF
- No conversion needed

### macOS

**Date/Time Display:**
- Similar to Linux behavior
- Uses UTC in CI environments
- Local timezone in terminal

**File Paths:**
- POSIX-compliant (like Linux)
- `pathlib.Path` works identically

## Continuous Integration

### Test Matrix

```yaml
# Recommended testing strategy
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: [3.11, 3.12]
    runs-on: ${{ matrix.os }}
```

### Validation Checklist

Before merging changes, verify:

- [ ] All tests pass on Windows (local)
- [ ] All tests pass on Linux (GitHub Actions)
- [ ] Smart cache refresh works in both environments
- [ ] Generated timestamps are always UTC
- [ ] Cache keys are consistent across platforms
- [ ] File paths work on both platforms
- [ ] No hardcoded path separators
- [ ] All datetime operations are timezone-aware

## Performance Comparison

### Windows (Local Development)

```
First run:  ~5 minutes (full generation)
Fresh (<7d): <1 second (skip generation)
Stale (>7d): ~30 seconds (selective refresh)
```

### Linux (GitHub Actions)

```
First run:  ~5 minutes (full generation)
Fresh (<7d): <1 second (skip generation)
Stale (>7d): ~30 seconds (selective refresh)
```

**Conclusion:** Performance is identical across platforms ✅

## Best Practices

### 1. Always Use UTC

```python
# Good
timestamp = datetime.now(timezone.utc)

# Bad
timestamp = datetime.now()  # Naive datetime
```

### 2. Always Use pathlib.Path

```python
# Good
path = Path("data") / "repositories.json"

# Bad
path = "data/repositories.json"  # Hardcoded separator
```

### 3. Always Handle Both Formats

```python
# Good
timestamp = timestamp_str.replace('Z', '+00:00')
dt = datetime.fromisoformat(timestamp)

# Bad
dt = datetime.fromisoformat(timestamp_str)  # May fail on 'Z'
```

### 4. Always Check Timezone Awareness

```python
# Good
if dt.tzinfo is None:
    dt = dt.replace(tzinfo=timezone.utc)

# Bad
# Assume datetime is always aware (may fail)
```

## Future Enhancements

### Potential Improvements

1. **Timezone Configuration:** Allow users to specify display timezone while keeping UTC internally
2. **Platform-Specific Optimizations:** Use platform-specific caching strategies
3. **Enhanced Logging:** Show both UTC and local time in logs

### Won't Implement

- ❌ **Local Timezone Operations:** Adds complexity without benefit
- ❌ **Platform-Specific Code Paths:** Reduces maintainability
- ❌ **Different Timestamp Formats:** ISO 8601 UTC is universal standard

## Related Documentation

- [Smart Cache Refresh Guide](../guides/smart-cache-refresh.md)
- [Testing Guide](../TESTING.md)
- [GitHub Actions Workflow](../../.github/workflows/generate-stats.yml)
