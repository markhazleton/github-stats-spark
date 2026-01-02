#!/usr/bin/env pwsh
# Test script for unified data generation
# This script tests the new unified data generator that merges all CLI commands

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "Testing Unified Data Generation" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment is activated
if (-not $env:VIRTUAL_ENV) {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & ".\.venv\Scripts\Activate.ps1"
}

# Check for GitHub token
if (-not $env:GITHUB_TOKEN) {
    Write-Host "ERROR: GITHUB_TOKEN environment variable not set" -ForegroundColor Red
    Write-Host "Please set your GitHub Personal Access Token:" -ForegroundColor Yellow
    Write-Host '  $env:GITHUB_TOKEN = "your_token_here"' -ForegroundColor Yellow
    exit 1
}

# Test 1: Display help
Write-Host "Test 1: Display unified command help" -ForegroundColor Green
Write-Host "------------------------------------------------------------------"
python -m spark.cli unified --help
Write-Host ""

# Test 2: Generate unified data for a test user (without AI summaries for speed)
Write-Host "Test 2: Generate unified data for markhazleton" -ForegroundColor Green
Write-Host "------------------------------------------------------------------"
python -m spark.cli unified `
    --user markhazleton `
    --output-dir data `
    --verbose

Write-Host ""

# Test 3: Check if output file was created
Write-Host "Test 3: Verify output file" -ForegroundColor Green
Write-Host "------------------------------------------------------------------"
$outputFile = "data\repositories.json"
if (Test-Path $outputFile) {
    Write-Host "✅ Output file created: $outputFile" -ForegroundColor Green
    
    # Display file size
    $fileSize = (Get-Item $outputFile).Length / 1KB
    Write-Host "   File size: $([math]::Round($fileSize, 2)) KB" -ForegroundColor Cyan
    
    # Parse and display summary
    try {
        $data = Get-Content $outputFile -Raw | ConvertFrom-Json
        Write-Host ""
        Write-Host "   Data Summary:" -ForegroundColor Cyan
        Write-Host "   - Repositories: $($data.repositories.Count)" -ForegroundColor White
        Write-Host "   - Username: $($data.profile.username)" -ForegroundColor White
        Write-Host "   - Schema Version: $($data.metadata.schema_version)" -ForegroundColor White
        Write-Host "   - Generated At: $($data.metadata.generated_at)" -ForegroundColor White
        
        # Display first repository as sample
        if ($data.repositories.Count -gt 0) {
            $repo = $data.repositories[0]
            Write-Host ""
            Write-Host "   Sample Repository (first):" -ForegroundColor Cyan
            Write-Host "   - Name: $($repo.name)" -ForegroundColor White
            Write-Host "   - Language: $($repo.language)" -ForegroundColor White
            Write-Host "   - Stars: $($repo.stars)" -ForegroundColor White
            Write-Host "   - Commits: $($repo.commit_history.total_commits)" -ForegroundColor White
            if ($repo.rank) {
                Write-Host "   - Rank: $($repo.rank)" -ForegroundColor White
                Write-Host "   - Score: $($repo.composite_score)" -ForegroundColor White
            }
            if ($repo.tech_stack) {
                Write-Host "   - Dependencies: $($repo.tech_stack.total_dependencies)" -ForegroundColor White
                Write-Host "   - Currency Score: $($repo.tech_stack.currency_score)/100" -ForegroundColor White
            }
        }
        
    } catch {
        Write-Host "⚠️  Could not parse JSON: $_" -ForegroundColor Yellow
    }
    
} else {
    Write-Host "❌ Output file not found: $outputFile" -ForegroundColor Red
}

Write-Host ""
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "Testing Complete!" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Review the generated data/repositories.json file" -ForegroundColor White
Write-Host "2. Test with --include-ai-summaries flag (requires Anthropic API key)" -ForegroundColor White
Write-Host "3. Use the unified data in your frontend application" -ForegroundColor White
Write-Host ""
