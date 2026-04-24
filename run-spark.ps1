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
    
.PARAMETER Screenshots
    Capture screenshots of repository websites using Playwright/Chromium.
    Only captures repos that have a homepage or GitHub Pages URL set.
    Uses cached screenshots when the repo has not changed since last capture.

.PARAMETER MissingOnly
    When combined with -Screenshots, skips repos that already have a
    screenshot PNG in output\screenshots\. Useful for filling gaps
    without re-capturing everything.

.PARAMETER CheckOnly
    Only check environment and configuration (dry run)

.EXAMPLE
    .\run-spark.ps1 -User markhazleton
    Generate complete stats without AI summaries (fast)

.EXAMPLE
    .\run-spark.ps1 -User markhazleton -IncludeAI
    Generate complete stats with AI-powered summaries

.EXAMPLE
    .\run-spark.ps1 -User markhazleton -Screenshots
    Generate stats and capture missing/stale screenshots

.EXAMPLE
    .\run-spark.ps1 -User markhazleton -Screenshots -MissingOnly
    Only capture screenshots for repos that have no PNG file yet

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
    [string]$User = "",   # Leave empty to process all users from config/spark.yml

    [Parameter(Mandatory=$false)]
    [switch]$IncludeAI,

    [Parameter(Mandatory=$false)]
    [switch]$ForceRefresh,

    [Parameter(Mandatory=$false)]
    [switch]$ClearCache,

    [Parameter(Mandatory=$false)]
    [switch]$Screenshots,

    [Parameter(Mandatory=$false)]
    [switch]$MissingOnly,

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
    
    # Check Playwright (optional - only needed for screenshots)
    if ($Screenshots) {
        Write-Host ""
        $playwrightInstalled = python -c "import playwright; print('installed')" 2>$null
        if ($playwrightInstalled -eq "installed") {
            # Check that Chromium browser binary is present
            $chromiumCheck = python -c "
from playwright.sync_api import sync_playwright
try:
    p = sync_playwright().start()
    b = p.chromium.launch(headless=True)
    b.close()
    p.stop()
    print('ok')
except Exception as e:
    print('missing')
" 2>$null
            if ($chromiumCheck -eq "ok") {
                Write-Success "Playwright Chromium ready"
            } else {
                Write-Warning "Playwright installed but Chromium not found - installing..."
                playwright install chromium
                Write-Success "Playwright Chromium installed"
            }
        } else {
            Write-Warning "Playwright not installed - installing..."
            pip install playwright | Out-Null
            playwright install chromium
            Write-Success "Playwright and Chromium installed"
        }
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

if (-not $env:SPARK_CACHE_DIR) {
    $env:SPARK_CACHE_DIR = ".cache/local"
}

# Ensure Python stdout is not buffered (visible even when piped/redirected)
$env:PYTHONUNBUFFERED = "1"

# ---------------------------------------------------------------------------
# Per-user pipeline runner
# ---------------------------------------------------------------------------
function Invoke-SparkPipeline {
    param([string]$UserName)

    $normalizedUser = $UserName.ToLower()
    $dataOutputDir = Join-Path "data\users" $normalizedUser
    $artifactOutputDir = Join-Path "output\users" $normalizedUser
    $reportOutputDir = Join-Path $artifactOutputDir "reports"
    $screenshotOutputDir = Join-Path $artifactOutputDir "screenshots"
    $repositoriesJsonPath = Join-Path $dataOutputDir "repositories.json"

    # Build command arguments
    $cmdArgs = @(
        "unified"
        "--user", $UserName
        "--output-dir", "data"
    )

    if ($IncludeAI) {
        $cmdArgs += "--include-ai-summaries"
    }

    if ($ForceRefresh) {
        $cmdArgs += "--force-refresh"
    }

    if ($Screenshots) {
        $cmdArgs += "--capture-screenshots"
    }

    if ($PSCmdlet.MyInvocation.BoundParameters["Verbose"].IsPresent) {
        $cmdArgs += "--verbose"
    }

    # Execute unified pipeline
    Write-Header "Executing 4-Phase Pipeline  [user: $UserName]"
    Write-Info "AI Summaries:  $(if ($IncludeAI) { 'Enabled' } else { 'Disabled' })"
    Write-Info "Screenshots:   $(if ($Screenshots) { 'Enabled' } else { 'Disabled' })"
    Write-Info "Missing Only:  $(if ($MissingOnly) { 'Yes (skip existing PNGs)' } else { 'No' })"
    Write-Info "Force Refresh: $(if ($ForceRefresh) { 'Yes' } else { 'No' })"
    Write-Info "Cache Dir:     $env:SPARK_CACHE_DIR"
    Write-Info "Data Dir:      $dataOutputDir"
    Write-Info "Artifact Dir:  $artifactOutputDir"
    Write-Info "Verbose Mode:  $(if ($PSCmdlet.MyInvocation.BoundParameters['Verbose'].IsPresent) { 'Yes' } else { 'No' })"
    Write-Host ""

    # If MissingOnly, temporarily move existing screenshots aside so the pipeline
    # only sees repos without a file. After the run we restore them.
    $hiddenDir = $null
    if ($Screenshots -and $MissingOnly) {
        if (Test-Path $screenshotOutputDir) {
            $existingPngs = Get-ChildItem $screenshotOutputDir -Filter "*.png" -ErrorAction SilentlyContinue
            if ($existingPngs.Count -gt 0) {
                $hiddenDir = "$screenshotOutputDir\.missing-only-backup"
                New-Item -ItemType Directory -Path $hiddenDir -Force | Out-Null
                $existingPngs | Move-Item -Destination $hiddenDir -Force
                Write-Info "MissingOnly: temporarily moved $($existingPngs.Count) existing PNGs aside"
            } else {
                Write-Info "MissingOnly: no existing PNGs found - will capture all"
            }
        }
    }

    $startTime = Get-Date

    # Run the unified command with periodic heartbeat messages so long quiet
    # periods (API/cache work) still show visible progress.
    $heartbeatIntervalSeconds = 20
    $heartbeatDeadline = (Get-Date).AddSeconds($heartbeatIntervalSeconds)
    $exitCode = 1

    $sparkJob = Start-Job -ScriptBlock {
        param([string]$repoRoot, [string[]]$cliArgs)
        Set-Location $repoRoot
        python -m spark.cli @cliArgs
        [pscustomobject]@{ __sparkExitCode = $LASTEXITCODE }
    } -ArgumentList $PSScriptRoot, $cmdArgs

    Write-Info "Pipeline process started (heartbeat every $heartbeatIntervalSeconds seconds during quiet periods)"

    while ($true) {
        $completed = Wait-Job -Job $sparkJob -Timeout 1
        $jobOutput = Receive-Job -Job $sparkJob -ErrorAction SilentlyContinue

        if ($jobOutput) {
            foreach ($item in $jobOutput) {
                if ($item -and $item.PSObject -and ($item.PSObject.Properties.Name -contains '__sparkExitCode')) {
                    $exitCode = [int]$item.__sparkExitCode
                } elseif ($null -ne $item) {
                    Write-Host $item
                }
            }
            $heartbeatDeadline = (Get-Date).AddSeconds($heartbeatIntervalSeconds)
        }

        if (-not $completed -and (Get-Date) -ge $heartbeatDeadline) {
            $elapsed = (Get-Date) - $startTime
            $elapsedLabel = '{0:hh\:mm\:ss}' -f $elapsed
            Write-Info "Still working... elapsed $elapsedLabel"
            $heartbeatDeadline = (Get-Date).AddSeconds($heartbeatIntervalSeconds)
        }

        if ($completed) {
            break
        }
    }

    $remainingOutput = Receive-Job -Job $sparkJob -ErrorAction SilentlyContinue
    if ($remainingOutput) {
        foreach ($item in $remainingOutput) {
            if ($item -and $item.PSObject -and ($item.PSObject.Properties.Name -contains '__sparkExitCode')) {
                $exitCode = [int]$item.__sparkExitCode
            } elseif ($null -ne $item) {
                Write-Host $item
            }
        }
    }

    Remove-Job -Job $sparkJob -Force -ErrorAction SilentlyContinue

    $endTime = Get-Date
    $duration = $endTime - $startTime

    # Restore previously-existing screenshots (MissingOnly mode)
    if ($null -ne $hiddenDir -and (Test-Path $hiddenDir)) {
        $backedUp = Get-ChildItem $hiddenDir -Filter "*.png" -ErrorAction SilentlyContinue
        foreach ($png in $backedUp) {
            $dest = Join-Path $screenshotOutputDir $png.Name
            if (-not (Test-Path $dest)) {
                Move-Item $png.FullName -Destination $dest -Force
            }
        }
        Remove-Item $hiddenDir -Recurse -Force -ErrorAction SilentlyContinue
        Write-Info "MissingOnly: restored backed-up screenshots"
    }

    # Results summary
    Write-Host ""
    Write-Header "Pipeline Results  [user: $UserName]"

    if ($exitCode -eq 0) {
        Write-Success "Pipeline completed successfully!"
        Write-Info "Duration: $($duration.ToString('mm\:ss'))"
        Write-Host ""

        # Validate outputs
        Write-Info "Verifying outputs..."

        if (Test-Path $repositoriesJsonPath) {
            $fileSize = [math]::Round((Get-Item $repositoriesJsonPath).Length / 1KB, 2)
            Write-Success "repositories.json created ($fileSize KB)"

            try {
                $data = Get-Content $repositoriesJsonPath -Raw | ConvertFrom-Json
                Write-Info "  Repositories analyzed: $($data.repositories.Count)"
                Write-Info "  Schema version: $($data.metadata.schema_version)"
                Write-Info "  Generated: $($data.metadata.generated_at)"
            } catch {
                Write-Warning "Could not parse JSON output"
            }
        } else {
            Write-Warning "repositories.json not found"
        }

        if (Test-Path $reportOutputDir) {
            $reportCount = (Get-ChildItem $reportOutputDir -Filter "*.md" -ErrorAction SilentlyContinue).Count
            if ($reportCount -gt 0) {
                Write-Success "Generated $reportCount markdown reports"
            }
        }

        if ($Screenshots -and (Test-Path $screenshotOutputDir)) {
            $pngCount    = (Get-ChildItem $screenshotOutputDir -Filter "*.png" -ErrorAction SilentlyContinue).Count
            $totalSizeKB = [math]::Round(
                (Get-ChildItem $screenshotOutputDir -Filter "*.png" -ErrorAction SilentlyContinue |
                 Measure-Object -Property Length -Sum).Sum / 1KB, 1)
            Write-Success "Screenshots: $pngCount PNGs in $screenshotOutputDir\ ($totalSizeKB KB total)"
        }

        Write-Host ""
        Write-Info "Data:    $repositoriesJsonPath"
        Write-Info "Reports: $reportOutputDir\"
        if ($Screenshots) {
            Write-Info "PNGs:    $screenshotOutputDir\"
        }
    } else {
        Write-Error "Pipeline failed with exit code: $exitCode"
        Write-Info "Review the log output above for details"
        Write-Host ""
        Write-Info "Common issues:"
        Write-Info "  - Rate limit exceeded: Wait or check cache"
        Write-Info "  - Invalid token: Verify GITHUB_TOKEN"
        Write-Info "  - Network issues: Check internet connection"
        return $exitCode
    }

    return 0
}

# ---------------------------------------------------------------------------
# Clear cache (once, before any per-user run)
# ---------------------------------------------------------------------------
if ($ClearCache) {
    Write-Header "Cache Management"
    Write-Info "Clearing all caches..."
    python -m spark.cli cache --clear --dir $env:SPARK_CACHE_DIR
    Write-Success "Cache cleared"
}

# ---------------------------------------------------------------------------
# Resolve user list
# ---------------------------------------------------------------------------
if ($User -ne "") {
    $usersToProcess = @($User)
} else {
    # Read users list from config/spark.yml
    $configUsers = python -c @"
try:
    from spark.config import SparkConfig
    c = SparkConfig('config/spark.yml')
    c.load()
    users = c.get_users()
    print('\n'.join(users) if users else 'markhazleton')
except Exception as e:
    print('markhazleton')
"@ 2>$null
    $usersToProcess = @($configUsers -split "`n" | Where-Object { $_ -match '\S' } | ForEach-Object { $_.Trim() })
    if (-not $usersToProcess -or $usersToProcess.Count -eq 0) {
        $usersToProcess = @("markhazleton")
    }
}

Write-Info "Users to process: $($usersToProcess -join ', ')"

# ---------------------------------------------------------------------------
# Run pipeline for each user
# ---------------------------------------------------------------------------
$overallExit = 0
foreach ($currentUser in $usersToProcess) {
    $result = Invoke-SparkPipeline -UserName $currentUser
    if ($result -ne 0) {
        $overallExit = $result
    }
}

# Final next-steps hint (shown once after all users)
Write-Host ""
Write-Header "Next Steps"
Write-Info "1. Build dashboard: cd frontend && npm run build"
Write-Info "2. Deploy: Copy docs\ to hosting platform"
if (-not $Screenshots) {
    Write-Info "3. Capture screenshots: .\run-spark-local.ps1 -Screenshots"
}
Write-Host ""

if ($overallExit -ne 0) {
    exit $overallExit
}
