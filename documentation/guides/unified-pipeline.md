# Stats Spark Unified Pipeline

## Overview

The Stats Spark unified pipeline is a streamlined 4-phase architecture that generates complete GitHub analytics from a single command. This document explains the pipeline design, execution flow, and best practices.

## Architecture

### Clean 4-Phase Design

The pipeline follows a strict separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    Phase 1: FETCH                           │
│  Get current repository list from GitHub API (1 API call)  │
│  Output: List of repositories with metadata                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Phase 2: REFRESH                          │
│  Smart cache validation - only update changed repos         │
│  Compare pushed_at timestamps, refresh if different         │
│  Output: RefreshSummary with API call count                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Phase 3: ASSEMBLE                         │
│  Read-only data assembly from cache                         │
│  Calculate rankings, scores, aggregate metrics              │
│  Output: UnifiedData object (JSON-serializable)            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Phase 4: OUTPUT                           │
│  Generate JSON files, SVG visualizations, reports           │
│  Pure functions - no API calls or cache writes              │
│  Output: repositories.json, *.svg, *.md reports            │
└─────────────────────────────────────────────────────────────┘
```

### Key Principles

1. **Single Responsibility**: Each phase has one job
2. **No Side Effects**: Reading doesn't write, writing doesn't read
3. **Zero Redundancy**: Single API pass, no duplicate calls
4. **Deterministic**: Same input → same output
5. **Observable**: Every operation logs timing and metrics

## Quick Start

### Using the PowerShell Script (Recommended)

```powershell
# Check environment setup
.\run-spark.ps1 -CheckOnly

# Run complete pipeline with AI summaries
.\run-spark.ps1 -User markhazleton -IncludeAI -Verbose

# Force fresh data (clear cache first)
.\run-spark.ps1 -User markhazleton -ClearCache -IncludeAI
```

### Using Python CLI Directly

```bash
# Basic usage
spark unified --user YOUR_USERNAME

# With AI summaries and verbose logging
spark unified --user YOUR_USERNAME --include-ai-summaries --verbose

# Force refresh all caches
spark unified --user YOUR_USERNAME --force-refresh
```

## Command Options

### PowerShell Script Options

| Option | Description | Default |
|--------|-------------|---------|
| `-User` | GitHub username | markhazleton |
| `-IncludeAI` | Generate AI summaries (requires ANTHROPIC_API_KEY) | false |
| `-ForceRefresh` | Force refresh all caches | false |
| `-ClearCache` | Clear all caches before running | false |
| `-Verbose` | Enable detailed logging | false |
| `-CheckOnly` | Validate environment without running | false |

### Python CLI Options

| Option | Description | Default |
|--------|-------------|---------|
| `--user` | GitHub username (required) | - |
| `--include-ai-summaries` | Generate AI summaries | false |
| `--force-refresh` | Force refresh all data | false |
| `--output-dir` | Output directory for JSON | data |
| `--config` | Config file path | config/spark.yml |
| `--verbose` | Enable verbose logging | false |
| `--max-repos` | Override max repositories | from config |

## Environment Setup

### Required Environment Variables

```powershell
# Required for all operations
$env:GITHUB_TOKEN = "ghp_your_token_here"

# Optional for AI summaries
$env:ANTHROPIC_API_KEY = "sk-ant-api03-your_key_here"
```

### Python Environment

```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

## Output Files

The pipeline generates three categories of output:

### 1. Unified Data (Phase 4)

**File**: `data/repositories.json`

Single source of truth consumed by dashboard and visualizations:

```json
{
  "profile": {
    "username": "markhazleton",
    "total_commits": 5234,
    "spark_score": 87
  },
  "repositories": [
    {
      "name": "github-stats-spark",
      "language": "Python",
      "stars": 42,
      "rank": 1,
      "composite_score": 85.3,
      "commit_history": { ... },
      "tech_stack": { ... },
      "ai_summary": { ... }
    }
  ],
  "metadata": {
    "generated_at": "2026-01-18T22:43:37Z",
    "schema_version": "2.0.0"
  }
}
```

### 2. SVG Visualizations (Phase 4)

**Directory**: `output/`

Six categories of embeddable SVGs:

- `overview.svg` - Key metrics and Spark Score
- `heatmap.svg` - Commit calendar heatmap
- `languages.svg` - Language distribution
- `streaks.svg` - Contribution streaks
- `fun.svg` - Personality-based achievements
- `release.svg` - Release history timeline

### 3. Markdown Reports (Phase 4)

**Directory**: `output/reports/`

Comprehensive analysis reports:

- `{username}-analysis.md` - Complete profile analysis
- `{username}-top-repositories.md` - Top N ranked repos
- Individual repository reports (optional)

## Performance

### Expected Timings (< 500 repos)

- **Phase 1 (Fetch)**: 1-3 seconds
- **Phase 2 (Refresh)**: 30-180 seconds (depends on changes)
- **Phase 3 (Assemble)**: 5-15 seconds
- **Phase 4 (Output)**: 10-30 seconds

**Total**: < 5 minutes (constitutional requirement)

### Cache Efficiency

- **First run**: Fetches all data from GitHub API
- **Subsequent runs**: Only refreshes changed repositories
- **Zero-change run**: Completes in < 10 seconds (no API calls)

### Rate Limit Management

- **Authenticated**: 5000 requests/hour
- **Smart caching**: Reduces calls by 80%+
- **Automatic retry**: Exponential backoff (1s, 2s, 4s, 8s)

## Troubleshooting

### Common Issues

#### "GITHUB_TOKEN not set"

```powershell
$env:GITHUB_TOKEN = "ghp_your_token_here"
```

Get token: https://github.com/settings/tokens

#### "AI summaries failed"

Set Anthropic API key or run without `-IncludeAI`:

```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."
```

#### "Rate limit exceeded"

Wait for limit reset or use cache:

```powershell
# Check when cache was last updated
spark cache --info

# List repos needing refresh
spark cache --list-refresh-needed --user YOUR_USERNAME
```

#### "Virtual environment not found"

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

### Debug Mode

Enable verbose logging to see detailed execution:

```powershell
.\run-spark.ps1 -User markhazleton -Verbose
```

Or with Python CLI:

```bash
spark unified --user markhazleton --verbose
```

## Advanced Usage

### Custom Configuration

Edit `config/spark.yml` to customize:

```yaml
dashboard:
  data_generation:
    max_repositories: 200
    top_n_repos: 50
    include_ai_summaries: false

analyzer:
  ranking_weights:
    popularity: 0.30
    activity: 0.45
    health: 0.25

cache:
  ttl_hours: 6
```

### Selective Cache Refresh

Clear only AI summaries and tech stack data:

```bash
spark refresh --user YOUR_USERNAME --clear-summaries
```

### Testing with Limited Repos

Test pipeline with only 5 repositories:

```bash
spark unified --user YOUR_USERNAME --max-repos 5
```

## Integration

### GitHub Actions Automation

The pipeline runs automatically via GitHub Actions:

- **Trigger**: Weekly on Sundays at midnight UTC
- **Manual**: Workflow dispatch in Actions tab
- **Secrets**: `GITHUB_TOKEN` (auto), `ANTHROPIC_API_KEY` (optional)

See `.github/workflows/generate-stats.yml` for configuration.

### Frontend Dashboard

Build and deploy the React dashboard:

```bash
cd frontend
npm install
npm run build  # Outputs to ../docs/
```

GitHub Pages serves from `docs/` directory.

## Best Practices

### Development Workflow

1. **Use the unified script** for local testing
2. **Enable verbose mode** during development
3. **Check environment** before running
4. **Clear cache** when debugging issues
5. **Review outputs** in data/ and output/ directories

### Production Deployment

1. **Set secrets** in GitHub repository settings
2. **Enable GitHub Actions** in repository settings
3. **Test manually** with workflow dispatch
4. **Configure schedule** to run weekly/daily
5. **Monitor outputs** for data quality

### Configuration Management

1. **Keep spark.yml in version control**
2. **Use environment variables for secrets**
3. **Document custom changes**
4. **Test config changes locally first**
5. **Validate with `spark config --show`**

## Related Documentation

- [Getting Started Guide](../guides/getting-started.md)
- [Configuration Reference](../guides/configuration.md)
- [API Reference](../api/api-reference.md)
- [Architecture Overview](../architecture/README.md)
- [Frontend Dashboard](../../frontend/README.md)

## Support

- **Issues**: https://github.com/markhazleton/github-stats-spark/issues
- **Discussions**: https://github.com/markhazleton/github-stats-spark/discussions
- **Contributing**: See [CONTRIBUTING.md](../../CONTRIBUTING.md)
