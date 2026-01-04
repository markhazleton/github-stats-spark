# Verify Smart Cache Refresh Is Working
# This script runs spark unified twice and checks that cache isn't regenerated on second run

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Smart Cache Refresh Verification" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$user = "markhazleton"
$maxRepos = 2

# Clean start
Write-Host "Step 1: Clearing existing data..." -ForegroundColor Yellow
if (Test-Path "data\repositories.json") {
    Remove-Item "data\repositories.json" -Force
    Write-Host "  ✓ Removed existing repositories.json" -ForegroundColor Green
}

# First run
Write-Host "`nStep 2: First run (should generate fresh data)..." -ForegroundColor Yellow
Write-Host "  Running: spark unified --user $user --max-repos $maxRepos`n" -ForegroundColor Gray

$firstRun = spark unified --user $user --max-repos $maxRepos 2>&1 | Out-String
$firstRunTime = (Get-Date)

Write-Host "  First run completed at: $firstRunTime" -ForegroundColor Green

# Check if generation happened
if ($firstRun -match "Fetching repositories for") {
    Write-Host "  ✓ Generated fresh data as expected" -ForegroundColor Green
} else {
    Write-Host "  ✗ ERROR: Expected to see 'Fetching repositories'" -ForegroundColor Red
}

# Record cache file timestamps
Write-Host "`nStep 3: Recording cache file timestamps..." -ForegroundColor Yellow
$cacheFilesBefore = Get-ChildItem .cache -Filter "*.json" -ErrorAction SilentlyContinue
if ($cacheFilesBefore) {
    Write-Host "  Found $($cacheFilesBefore.Count) cache files" -ForegroundColor Green
    $cacheFilesBefore | ForEach-Object {
        Write-Host "    $($_.Name): $($_.LastWriteTime)" -ForegroundColor Gray
    }
} else {
    Write-Host "  ⚠  WARNING: No cache files found!" -ForegroundColor Yellow
}

# Wait 2 seconds
Write-Host "`nStep 4: Waiting 2 seconds..." -ForegroundColor Yellow
Start-Sleep -Seconds 2

# Second run
Write-Host "`nStep 5: Second run (should skip generation)..." -ForegroundColor Yellow
Write-Host "  Running: spark unified --user $user --max-repos $maxRepos`n" -ForegroundColor Gray

$secondRun = spark unified --user $user --max-repos $maxRepos 2>&1 | Out-String
$secondRunTime = (Get-Date)

Write-Host "  Second run completed at: $secondRunTime" -ForegroundColor Green

# Check if skipped
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "VERIFICATION RESULTS" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$passed = 0
$failed = 0

# Check 1: Should see freshness check messages
Write-Host "Check 1: Freshness check messages visible" -ForegroundColor Yellow
if ($secondRun -match "Checking data freshness") {
    Write-Host "  ✓ PASS: Found 'Checking data freshness' message" -ForegroundColor Green
    $passed++
} else {
    Write-Host "  ✗ FAIL: Missing 'Checking data freshness' message" -ForegroundColor Red
    $failed++
}

# Check 2: Should skip generation
Write-Host "`nCheck 2: Generation skipped when data is fresh" -ForegroundColor Yellow
if ($secondRun -match "skipping generation") {
    Write-Host "  ✓ PASS: Found 'skipping generation' message" -ForegroundColor Green
    $passed++
} else {
    Write-Host "  ✗ FAIL: Missing 'skipping generation' message" -ForegroundColor Red
    $failed++
}

# Check 3: Should load existing data
Write-Host "`nCheck 3: Existing data loaded" -ForegroundColor Yellow
if ($secondRun -match "Loading existing data from|Loaded existing data with") {
    Write-Host "  ✓ PASS: Found 'Loading/Loaded existing data' message" -ForegroundColor Green
    $passed++
} else {
    Write-Host "  ✗ FAIL: Missing 'Loading existing data' message" -ForegroundColor Red
    $failed++
}

# Check 4: Should NOT fetch repositories
Write-Host "`nCheck 4: No repository fetching on second run" -ForegroundColor Yellow
if ($secondRun -notmatch "Fetching repositories for") {
    Write-Host "  ✓ PASS: Did not fetch repositories (as expected)" -ForegroundColor Green
    $passed++
} else {
    Write-Host "  ✗ FAIL: Unexpectedly fetched repositories" -ForegroundColor Red
    $failed++
}

# Check 5: Cache files should NOT be updated
Write-Host "`nCheck 5: Cache files unchanged on second run" -ForegroundColor Yellow
$cacheFilesAfter = Get-ChildItem .cache -Filter "*.json" -ErrorAction SilentlyContinue

if ($cacheFilesBefore -and $cacheFilesAfter) {
    $unchangedCount = 0
    $changedCount = 0
    
    foreach ($fileBefore in $cacheFilesBefore) {
        $fileAfter = $cacheFilesAfter | Where-Object { $_.Name -eq $fileBefore.Name }
        if ($fileAfter) {
            if ($fileAfter.LastWriteTime -eq $fileBefore.LastWriteTime) {
                $unchangedCount++
            } else {
                $changedCount++
                Write-Host "    ⚠  Changed: $($fileBefore.Name)" -ForegroundColor Yellow
            }
        }
    }
    
    if ($changedCount -eq 0) {
        Write-Host "  ✓ PASS: All $unchangedCount cache files unchanged" -ForegroundColor Green
        $passed++
    } else {
        Write-Host "  ✗ FAIL: $changedCount cache files were updated (should be 0)" -ForegroundColor Red
        $failed++
    }
} else {
    Write-Host "  ⚠  SKIP: Could not compare cache files" -ForegroundColor Yellow
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "SUMMARY" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$total = $passed + $failed
Write-Host "Passed: $passed/$total" -ForegroundColor Green
Write-Host "Failed: $failed/$total" -ForegroundColor $(if ($failed -eq 0) { "Green" } else { "Red" })

if ($failed -eq 0) {
    Write-Host "`n✅ ALL CHECKS PASSED! Smart cache refresh is working correctly.`n" -ForegroundColor Green
    exit 0
} else {
    Write-Host "`n❌ SOME CHECKS FAILED! Review the output above for details.`n" -ForegroundColor Red
    Write-Host "Common issues:" -ForegroundColor Yellow
    Write-Host "  1. GITHUB_TOKEN not set in environment" -ForegroundColor Gray
    Write-Host "  2. Logger not using spark.logger (check unified_data_generator.py)" -ForegroundColor Gray
    Write-Host "  3. Data older than 1 week (delete data/repositories.json and retry)" -ForegroundColor Gray
    exit 1
}
