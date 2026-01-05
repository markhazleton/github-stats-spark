#!/usr/bin/env pwsh
# Test script for cache status tracking functionality
# This script demonstrates the new cache status features

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Cache Status Tracking Test Script" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Ensure virtual environment is activated
if (-not $env:VIRTUAL_ENV) {
    Write-Host "⚠️  Virtual environment not detected. Activating..." -ForegroundColor Yellow
    & .\.venv\Scripts\Activate.ps1
}

$username = "markhazleton"

# Step 1: Update cache status in repositories file
Write-Host "Step 1: Updating cache status for all repositories..." -ForegroundColor Green
Write-Host "-----------------------------------------------" -ForegroundColor Gray
spark cache --update-status --user $username
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to update cache status" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 2: Show cache statistics
Write-Host "Step 2: Displaying cache statistics..." -ForegroundColor Green
Write-Host "-----------------------------------------------" -ForegroundColor Gray
spark cache --status --user $username
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to get cache statistics" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 3: List repositories needing refresh
Write-Host "Step 3: Listing repositories that need refresh..." -ForegroundColor Green
Write-Host "-----------------------------------------------" -ForegroundColor Gray
spark cache --list-refresh-needed --user $username
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to list refresh-needed repos" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 4: Show general cache info
Write-Host "Step 4: General cache information..." -ForegroundColor Green
Write-Host "-----------------------------------------------" -ForegroundColor Gray
spark cache --info
Write-Host ""

# Step 5: Verify repositories cache file has cache_status
Write-Host "Step 5: Verifying cache_status in repositories file..." -ForegroundColor Green
Write-Host "-----------------------------------------------" -ForegroundColor Gray
$reposCacheFile = ".cache\repositories_${username}_True_False.json"
if (Test-Path $reposCacheFile) {
    $content = Get-Content $reposCacheFile -Raw | ConvertFrom-Json
    $firstRepo = $content.value[0]
    
    if ($firstRepo.cache_status) {
        Write-Host "✅ cache_status found in repository entry:" -ForegroundColor Green
        Write-Host "   Repository: $($firstRepo.name)" -ForegroundColor Cyan
        Write-Host "   Has cache: $($firstRepo.cache_status.has_cache)" -ForegroundColor Cyan
        Write-Host "   Refresh needed: $($firstRepo.cache_status.refresh_needed)" -ForegroundColor Cyan
        Write-Host "   Cache date: $($firstRepo.cache_status.cache_date)" -ForegroundColor Cyan
        
        if ($firstRepo.cache_status.cache_age_hours) {
            Write-Host "   Cache age: $([math]::Round($firstRepo.cache_status.cache_age_hours, 2)) hours" -ForegroundColor Cyan
        }
        
        if ($firstRepo.cache_status.refresh_reasons -and $firstRepo.cache_status.refresh_reasons.Count -gt 0) {
            Write-Host "   Refresh reasons: $($firstRepo.cache_status.refresh_reasons -join ', ')" -ForegroundColor Yellow
        }
    } else {
        Write-Host "❌ cache_status not found in repository entry" -ForegroundColor Red
    }
} else {
    Write-Host "❌ Repositories cache file not found: $reposCacheFile" -ForegroundColor Red
}
Write-Host ""

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "✅ Cache Status Test Complete!" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  • Run 'spark unified --user $username' to do a full refresh" -ForegroundColor Gray
Write-Host "  • The system will now skip repos where refresh_needed = false" -ForegroundColor Gray
Write-Host "  • Check .cache\repositories_${username}_True_False.json for detailed cache status" -ForegroundColor Gray
Write-Host ""
