#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Stats Spark - Unified 4-Phase GitHub Analytics Pipeline
    
.DESCRIPTION
    Complete pipeline to generate GitHub statistics, visualizations, and reports:
    Phase 1: Fetch repository list from GitHub
    Phase 2: Validate & refresh caches (smart incremental updates)
    Phase 3: Assemble data from cache (read-only)
    Phase 4: Generate outputs (repositories.json, SVGs, reports)
    
.PARAMETER User
    GitHub username to analyze (required)
    
.PARAMETER IncludeAI
    Generate AI summaries using Anthropic Claude (requires ANTHROPIC_API_KEY)
    
.PARAMETER ForceRefresh
    Force refresh all caches (ignores timestamps)
    
.PARAMETER ClearCache
    Clear all caches before running
    
.PARAMETER Verbose
    Enable verbose logging
    
.PARAMETER CheckOnly
    Only check environment and configuration (dry run)
    
.EXAMPLE
    .\run-spark.ps1 -User markhazleton
    Generate complete stats without AI summaries (fast)
    
.EXAMPLE
    .\run-spark.ps1 -User markhazleton -IncludeAI
    Generate complete stats with AI-powered summaries
    
.EXAMPLE
    .\run-spark.ps1 -User markhazleton -ClearCache -IncludeAI
    Fresh generation from scratch (clears all caches)
    
.EXAMPLE
    .\run-spark.ps1 -CheckOnly
    Verify environment setup and configuration
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [string]$User = "markhazleton",
    
    [Parameter(Mandatory=$false)]
    [switch]$IncludeAI,
    
    [Parameter(Mandatory=$false)]
    [switch]$ForceRefresh,
    
    [Parameter(Mandatory=$false)]
    [switch]$ClearCache,
    
    [Parameter(Mandatory=$false)]
    [switch]$CheckOnly
)

# Color functions
function Write-Header {
    param([string]$Message)
    Write-Host "`n$('=' * 70)" -ForegroundColor Cyan
    Write-Host $Message -ForegroundColor Cyan
    Write-Host "$('=' * 70)" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "✓ $Message" -ForegroundColor Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "⚠ $Message" -ForegroundColor Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "✗ $Message" -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host "  $Message" -ForegroundColor White
}

# Environment check
function Test-Environment {
    Write-Header "Environment Validation"
    
    $allGood = $true
    
    # Check virtual environment
    if ($env:VIRTUAL_ENV) {
        Write-Success "Virtual environment activated: $env:VIRTUAL_ENV"
    } else {
        Write-Warning "Virtual environment not activated"
        Write-Info "Activating .venv..."
        if (Test-Path ".\.venv\Scripts\Activate.ps1") {
            & ".\.venv\Scripts\Activate.ps1"
            Write-Success "Virtual environment activated"
        } else {
            Write-Error "Virtual environment not found at .\.venv"
            Write-Info "Run: python -m venv .venv"
            Write-Info "Then: .\.venv\Scripts\Activate.ps1"
            Write-Info "Then: pip install -r requirements.txt"
            return $false
        }
    }
    
    # Check Python package
    Write-Host ""
    $sparkInstalled = python -c "import spark; print('installed')" 2>$null
    if ($sparkInstalled -eq "installed") {
        Write-Success "Spark package installed"
    } else {
        Write-Warning "Spark package not installed"
        Write-Info "Installing in editable mode..."
        pip install -e . | Out-Null
        Write-Success "Spark package installed"
    }
    
    # Check GITHUB_TOKEN
    Write-Host ""
    if ($env:GITHUB_TOKEN) {
        $tokenLength = $env:GITHUB_TOKEN.Length
        Write-Success "GITHUB_TOKEN set ($tokenLength chars)"
    } else {
        Write-Error "GITHUB_TOKEN not set"
        Write-Info "Required for GitHub API access"
        Write-Info "Set with: `$env:GITHUB_TOKEN = 'ghp_your_token_here'"
        Write-Info "Get token: https://github.com/settings/tokens"
        $allGood = $false
    }
    
    # Check ANTHROPIC_API_KEY (optional for AI summaries)
    if ($IncludeAI) {
        if ($env:ANTHROPIC_API_KEY) {
            $keyLength = $env:ANTHROPIC_API_KEY.Length
            Write-Success "ANTHROPIC_API_KEY set ($keyLength chars)"
        } else {
            Write-Warning "ANTHROPIC_API_KEY not set - AI summaries will be skipped"
            Write-Info "Get API key: https://console.anthropic.com/"
            Write-Info "Set with: `$env:ANTHROPIC_API_KEY = 'sk-ant-api03-...'"
        }
    }
    
    # Check configuration files
    Write-Host ""
    if (Test-Path "config\spark.yml") {
        Write-Success "Configuration file exists: config\spark.yml"
    } else {
        Write-Error "Configuration file missing: config\spark.yml"
        $allGood = $false
    }
    
    if (Test-Path "config\themes.yml") {
        Write-Success "Themes file exists: config\themes.yml"
    } else {
        Write-Warning "Themes file missing: config\themes.yml"
    }
    
    return $allGood
}

# Main execution
Write-Header "Stats Spark - GitHub Analytics Pipeline"

# Validate environment
$envValid = Test-Environment

if (-not $envValid) {
    Write-Host ""
    Write-Error "Environment validation failed - cannot proceed"
    exit 1
}

if ($CheckOnly) {
    Write-Host ""
    Write-Success "Environment check complete - ready to run!"
    Write-Host ""
    Write-Info "Run without -CheckOnly to execute pipeline"
    exit 0
}

# Build command arguments
$cmdArgs = @(
    "unified"
    "--user", $User
    "--output-dir", "data"
)

if ($IncludeAI) {
    $cmdArgs += "--include-ai-summaries"
}

if ($ForceRefresh) {
    $cmdArgs += "--force-refresh"
}

if ($PSCmdlet.MyInvocation.BoundParameters["Verbose"].IsPresent) {
    $cmdArgs += "--verbose"
}

# Clear cache if requested
if ($ClearCache) {
    Write-Header "Cache Management"
    Write-Info "Clearing all caches..."
    python -m spark.cli cache --clear --dir .cache
    Write-Success "Cache cleared"
}

# Execute unified pipeline
Write-Header "Executing 4-Phase Pipeline"
Write-Info "User: $User"
Write-Info "AI Summaries: $(if ($IncludeAI) { 'Enabled' } else { 'Disabled' })"
Write-Info "Force Refresh: $(if ($ForceRefresh) { 'Yes' } else { 'No' })"
Write-Info "Verbose Mode: $(if ($PSCmdlet.MyInvocation.BoundParameters['Verbose'].IsPresent) { 'Yes' } else { 'No' })"
Write-Host ""

$startTime = Get-Date

# Run the unified command
python -m spark.cli @cmdArgs

$exitCode = $LASTEXITCODE
$endTime = Get-Date
$duration = $endTime - $startTime

# Results summary
Write-Host ""
Write-Header "Pipeline Results"

if ($exitCode -eq 0) {
    Write-Success "Pipeline completed successfully!"
    Write-Info "Duration: $($duration.ToString('mm\:ss'))"
    Write-Host ""
    
    # Validate outputs
    Write-Info "Verifying outputs..."
    
    if (Test-Path "data\repositories.json") {
        $fileSize = [math]::Round((Get-Item "data\repositories.json").Length / 1KB, 2)
        Write-Success "repositories.json created ($fileSize KB)"
        
        try {
            $data = Get-Content "data\repositories.json" -Raw | ConvertFrom-Json
            Write-Info "  Repositories analyzed: $($data.repositories.Count)"
            Write-Info "  Schema version: $($data.metadata.schema_version)"
            Write-Info "  Generated: $($data.metadata.generated_at)"
        } catch {
            Write-Warning "Could not parse JSON output"
        }
    } else {
        Write-Warning "repositories.json not found"
    }
    
    if (Test-Path "output\reports") {
        $reportCount = (Get-ChildItem "output\reports" -Filter "*.md" -ErrorAction SilentlyContinue).Count
        if ($reportCount -gt 0) {
            Write-Success "Generated $reportCount markdown reports"
        }
    }
    
    Write-Host ""
    Write-Header "Next Steps"
    Write-Info "1. View data: data\repositories.json"
    Write-Info "2. View reports: output\reports\"
    Write-Info "3. Build dashboard: cd frontend && npm run build"
    Write-Info "4. Deploy: Copy docs\ to hosting platform"
    
} else {
    Write-Error "Pipeline failed with exit code: $exitCode"
    Write-Info "Review the log output above for details"
    Write-Host ""
    Write-Info "Common issues:"
    Write-Info "  - Rate limit exceeded: Wait or check cache"
    Write-Info "  - Invalid token: Verify GITHUB_TOKEN"
    Write-Info "  - Network issues: Check internet connection"
    exit $exitCode
}

Write-Host ""
