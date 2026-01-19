# Stats Spark Quick Reference

## One Command to Rule Them All

```powershell
.\run-spark.ps1 -User YOUR_USERNAME -IncludeAI -Verbose
```

## Common Commands

### Environment Check
```powershell
.\run-spark.ps1 -CheckOnly
```

### Basic Run (No AI)
```powershell
.\run-spark.ps1 -User YOUR_USERNAME
```

### Complete Run (With AI)
```powershell
.\run-spark.ps1 -User YOUR_USERNAME -IncludeAI
```

### Fresh Start
```powershell
.\run-spark.ps1 -User YOUR_USERNAME -ClearCache -IncludeAI
```

### Force Refresh
```powershell
.\run-spark.ps1 -User YOUR_USERNAME -ForceRefresh
```

## Python CLI Alternatives

```bash
# Environment check
spark config --show

# Basic generation
spark unified --user YOUR_USERNAME

# With AI summaries
spark unified --user YOUR_USERNAME --include-ai-summaries --verbose

# Force refresh
spark unified --user YOUR_USERNAME --force-refresh

# Cache management
spark cache --clear
spark cache --info
spark cache --status --user YOUR_USERNAME
```

## Required Setup

```powershell
# 1. Virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install packages
pip install -r requirements.txt
pip install -e .

# 3. Set tokens
$env:GITHUB_TOKEN = "ghp_..."
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."  # Optional
```

## Output Locations

| Output | Location | Purpose |
|--------|----------|---------|
| Unified data | `data/repositories.json` | Dashboard data source |
| SVG files | `output/*.svg` | Profile visualizations |
| Reports | `output/reports/*.md` | Analysis reports |
| Cache | `.cache/` | API response cache |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Token not set | `$env:GITHUB_TOKEN = "ghp_..."` |
| Venv not active | `.\.venv\Scripts\Activate.ps1` |
| Rate limit hit | Wait or check cache age |
| AI summaries fail | Set `ANTHROPIC_API_KEY` or skip AI |
| Package not found | `pip install -e .` |

## Performance Metrics

- **First run**: 3-5 minutes (fetches all data)
- **Incremental**: 30-90 seconds (only changed repos)
- **No changes**: < 10 seconds (cache only)
- **API calls**: 1-100 per run (depends on changes)

## Pipeline Phases

1. **Fetch** (1-3s) - Get repo list from GitHub
2. **Refresh** (30-180s) - Update caches for changed repos
3. **Assemble** (5-15s) - Read cache and calculate metrics
4. **Output** (10-30s) - Generate JSON, SVGs, reports

## Configuration

Edit `config/spark.yml` to customize:

```yaml
dashboard:
  data_generation:
    max_repositories: 200      # Limit repos processed
    top_n_repos: 50           # Top N in reports
    include_ai_summaries: true # Enable AI by default
```

## Key Features

- ✅ **Zero maintenance** - Set once, runs forever
- ✅ **Smart caching** - Only refreshes changed repos
- ✅ **Rate limit safe** - Automatic retry with backoff
- ✅ **Constitutional guarantees** - <5 min, <1% error
- ✅ **Privacy first** - Private repos excluded
- ✅ **Mobile optimized** - Dashboard works on phones
- ✅ **Accessible** - WCAG AA compliant

## Documentation

- **Full Guide**: [documentation/guides/unified-pipeline.md](documentation/guides/unified-pipeline.md)
- **Getting Started**: [documentation/guides/getting-started.md](documentation/guides/getting-started.md)
- **Configuration**: [documentation/guides/configuration.md](documentation/guides/configuration.md)
- **API Reference**: [documentation/api/api-reference.md](documentation/api/api-reference.md)

## Support

- **Issues**: https://github.com/markhazleton/github-stats-spark/issues
- **Discussions**: https://github.com/markhazleton/github-stats-spark/discussions
