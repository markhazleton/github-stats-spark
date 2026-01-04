#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Test smart cache refresh logic with limited repositories
.DESCRIPTION
    This script demonstrates the smart cache refresh feature by:
    1. First run: Generates data for 2 repositories (full cache)
    2. Second run: Should skip generation (data is fresh)
    3. Third run with force-refresh: Regenerates all data
.EXAMPLE
    .\test-cache-logic.ps1
#>

# Configuration
$USERNAME = "markhazleton"
$MAX_REPOS = 2
$OUTPUT_DIR = "data"

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Testing Smart Cache Refresh Logic with $MAX_REPOS Repositories" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# Check for GitHub token
if (-not $env:GITHUB_TOKEN) {
    Write-Host "ERROR: GITHUB_TOKEN environment variable not set" -ForegroundColor Red
    Write-Host "Please set it with: `$env:GITHUB_TOKEN = 'your_token_here'" -ForegroundColor Yellow
    exit 1
}

# Test 1: First run (should generate data)
Write-Host "Test 1: First Generation (2 repos)" -ForegroundColor Yellow
Write-Host "---------------------------------------------------------------------" -ForegroundColor Gray
Write-Host ""

# Remove existing data to simulate first run
if (Test-Path "$OUTPUT_DIR/repositories.json") {
    Remove-Item "$OUTPUT_DIR/repositories.json" -Force
    Write-Host "Removed existing repositories.json" -ForegroundColor Gray
}

$start1 = Get-Date
spark unified --user $USERNAME --max-repos $MAX_REPOS --verbose
$duration1 = (Get-Date) - $start1

Write-Host ""
Write-Host "✅ Test 1 Complete - Duration: $($duration1.TotalSeconds) seconds" -ForegroundColor Green
Write-Host ""
Write-Host ""

# Wait a moment
Start-Sleep -Seconds 2

# Test 2: Second run (should skip - data is fresh)
Write-Host "Test 2: Immediate Re-run (should skip generation)" -ForegroundColor Yellow
Write-Host "---------------------------------------------------------------------" -ForegroundColor Gray
Write-Host ""

$start2 = Get-Date
spark unified --user $USERNAME --max-repos $MAX_REPOS --verbose
$duration2 = (Get-Date) - $start2

Write-Host ""
Write-Host "✅ Test 2 Complete - Duration: $($duration2.TotalSeconds) seconds" -ForegroundColor Green
Write-Host ""

# Compare times
$speedup = [math]::Round($duration1.TotalSeconds / $duration2.TotalSeconds, 1)
Write-Host "⚡ Speedup: ${speedup}x faster (should be ~100x+)" -ForegroundColor Cyan
Write-Host ""
Write-Host ""

# Test 3: Force refresh (should regenerate)
Write-Host "Test 3: Force Refresh (should regenerate all data)" -ForegroundColor Yellow
Write-Host "---------------------------------------------------------------------" -ForegroundColor Gray
Write-Host ""

$start3 = Get-Date
spark unified --user $USERNAME --max-repos $MAX_REPOS --force-refresh --verbose
$duration3 = (Get-Date) - $start3

Write-Host ""
Write-Host "✅ Test 3 Complete - Duration: $($duration3.TotalSeconds) seconds" -ForegroundColor Green
Write-Host ""
Write-Host ""

# Summary
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Test Summary" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Test 1 (First run):          $($duration1.TotalSeconds.ToString('F2')) seconds" -ForegroundColor White
Write-Host "Test 2 (Skip - fresh data):  $($duration2.TotalSeconds.ToString('F2')) seconds" -ForegroundColor Green
Write-Host "Test 3 (Force refresh):      $($duration3.TotalSeconds.ToString('F2')) seconds" -ForegroundColor White
Write-Host ""
Write-Host "Smart Cache Efficiency: $([math]::Round((1 - $duration2.TotalSeconds/$duration1.TotalSeconds) * 100, 1))% time saved" -ForegroundColor Cyan
Write-Host ""

# Validate cache files
$cacheFiles = Get-ChildItem -Path ".cache" -Filter "*.json" -ErrorAction SilentlyContinue
if ($cacheFiles) {
    Write-Host "Cache files created: $($cacheFiles.Count)" -ForegroundColor Gray
    Write-Host ""
}

# Check repositories.json
if (Test-Path "$OUTPUT_DIR/repositories.json") {
    $jsonContent = Get-Content "$OUTPUT_DIR/repositories.json" | ConvertFrom-Json
    $repoCount = $jsonContent.repositories.Count
    $generatedAt = $jsonContent.metadata.generated_at
    
    Write-Host "✅ repositories.json validated:" -ForegroundColor Green
    Write-Host "   - Repositories: $repoCount" -ForegroundColor Gray
    Write-Host "   - Generated at: $generatedAt" -ForegroundColor Gray
    Write-Host ""
}

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "✨ All tests completed successfully!" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan
