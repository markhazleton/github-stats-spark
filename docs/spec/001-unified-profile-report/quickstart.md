# Quickstart Guide: Unified Profile Report

**Feature**: Unified Profile Report
**Date**: 2025-12-30
**Audience**: Developers and GitHub Actions users

## Overview

This guide shows you how to generate unified profile reports that combine SVG visualizations with detailed repository analysis in a single, comprehensive markdown file.

**Output**: `{username}-analysis.md` at `/output/reports/` (non-dated, auto-updating)

---

## Prerequisites

1. **Python 3.11+** installed
2. **GitHub Personal Access Token** with `repo` scope
3. **Anthropic API Key** (optional, for AI summaries)
4. **Dependencies** installed: `pip install -r requirements.txt`

---

## Quick Start (Local CLI)

### 1. Install Stats Spark

```bash
# Clone repository
git clone https://github.com/markhazleton/github-stats-spark.git
cd github-stats-spark

# Install dependencies
python -m pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
# Set GitHub token (required)
export GITHUB_TOKEN="ghp_your_token_here"

# Set Anthropic API key (optional - enables AI summaries)
export ANTHROPIC_API_KEY="sk-ant-your_key_here"
```

### 3. Generate Unified Report

```bash
# Generate unified report (SVGs + analysis)
python -m spark.cli analyze --user markhazleton --unified --verbose
```

**Output**:
```
output/
├── overview.svg
├── heatmap.svg
├── languages.svg
├── fun.svg
├── streaks.svg
├── release.svg
└── reports/
    └── markhazleton-analysis.md  ← Unified report
```

---

## CLI Command Options

### Basic Usage

```bash
spark analyze --user <username> --unified [OPTIONS]
```

### Common Options

| Option | Description | Default |
|--------|-------------|---------|
| `--user USERNAME` | GitHub username to analyze | Required |
| `--unified` | Generate unified report (vs dated) | `false` |
| `--keep-dated` | Also generate dated report | `false` |
| `--output DIR` | Output directory path | `output/reports` |
| `--top-n N` | Number of repositories to analyze | `50` |
| `--config FILE` | Custom config file | `config/spark.yml` |
| `--verbose` | Enable detailed logging | `false` |

### Examples

**Generate unified report only**:
```bash
spark analyze --user markhazleton --unified
```

**Generate both unified and dated reports**:
```bash
spark analyze --user markhazleton --unified --keep-dated
```

**Analyze top 25 repositories**:
```bash
spark analyze --user markhazleton --unified --top-n 25
```

**Custom output directory**:
```bash
spark analyze --user markhazleton --unified --output /custom/path
```

---

## GitHub Actions Workflow

### Setup

**1. Create GitHub Secrets** (Settings → Secrets and variables → Actions):
- `GITHUB_TOKEN`: Automatically available (no setup needed)
- `ANTHROPIC_API_KEY`: Your Anthropic API key (optional)

**2. Create Workflow File**: `.github/workflows/generate-stats.yml`

```yaml
name: Generate GitHub Statistics

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sundays at midnight UTC
  workflow_dispatch:      # Manual trigger

jobs:
  generate-stats:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Generate unified report
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          python -m spark.cli analyze \
            --user ${{ github.repository_owner }} \
            --unified \
            --verbose

      - name: Commit generated files
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add output/*.svg output/reports/*-analysis.md
          git diff --staged --quiet || git commit -m "Update GitHub statistics [skip ci]"

      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}
```

**3. Trigger Workflow**:
- **Automatic**: Runs weekly on Sundays
- **Manual**: Actions tab → "Generate GitHub Statistics" → "Run workflow"

---

## Configuration

### Config File: `config/spark.yml`

```yaml
# Report Generation Settings
report:
  mode: unified               # Options: unified, dated, both
  keep_historical: false      # Generate dated reports alongside unified
  output_directory: output/reports

# Analyzer Settings
analyzer:
  top_repositories: 50        # Number of repositories to analyze (max 50)

  ranking_weights:
    popularity: 0.30          # Stars, forks, watchers
    activity: 0.45            # Recent commits, recency
    health: 0.25              # Documentation, issues, maturity

  ai_provider: anthropic      # Options: anthropic, none
  ai_model: claude-3-5-haiku-20241022

  unified_report:
    include_svgs: true
    svg_order: [overview, heatmap, streaks, release, languages, fun]
    fallback_on_missing_svg: true
    include_footer_metadata: true

# Visualization Settings
visualization:
  theme: spark-dark           # Options: spark-dark, spark-light, custom
  enable_effects: true

  categories:
    overview: true
    heatmap: true
    languages: true
    fun: true
    streaks: true
    release: true
```

---

## Output Structure

### Generated Files

```
output/
├── overview.svg                    # Profile overview dashboard
├── heatmap.svg                     # Commit frequency heatmap
├── languages.svg                   # Programming language breakdown
├── fun.svg                         # Fun statistics
├── streaks.svg                     # Coding streaks
├── release.svg                     # Release cadence sparklines
└── reports/
    ├── {username}-analysis.md      # NEW: Unified report (non-dated)
    └── {username}-analysis-{YYYYMMDD}.md  # Legacy: Dated reports
```

### Report Structure

The unified report contains 4 main sections:

1. **Header**: Metadata, navigation, generation info
2. **Profile Overview**: All 6 SVG visualizations embedded inline
3. **Repository Analysis**: Top 50 repositories ranked by composite score
4. **Footer**: Report metadata, data sources, attribution

---

## Embedding in GitHub Profile

### 1. Link from Profile README

**Method 1: Direct Embedding** (if repo is public):

```markdown
# Your Profile

Check out my comprehensive analysis:

[View Full Analysis](https://github.com/yourusername/github-stats-spark/blob/main/output/reports/yourusername-analysis.md)
```

**Method 2: SVG Badges** (inline visualizations):

```markdown
![GitHub Stats](https://github.com/yourusername/github-stats-spark/blob/main/output/overview.svg)
![Commit Heatmap](https://github.com/yourusername/github-stats-spark/blob/main/output/heatmap.svg)
```

### 2. Create Dedicated Stats Repository

```bash
# Create new repository
gh repo create github-stats --public

# Copy workflow and config
cp .github/workflows/generate-stats.yml /path/to/github-stats/.github/workflows/
cp config/spark.yml /path/to/github-stats/config/

# Push and run
cd /path/to/github-stats
git push
gh workflow run generate-stats.yml
```

---

## Troubleshooting

### Issue: "No module named 'spark'"

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: "GitHub API rate limit exceeded"

**Solution**: Configure GitHub token
```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

### Issue: "SVG generation failed"

**Symptom**: Report generated but some SVGs missing

**Solution**: Check logs for specific SVG errors. Report will continue with available SVGs (FR-011).

```bash
# Check which SVGs failed
grep "Failed to generate" <log-output>
```

### Issue: "AI summarization not working"

**Symptom**: Summaries are template-based instead of AI-generated

**Solution**: Set Anthropic API key (optional - system falls back to templates)
```bash
export ANTHROPIC_API_KEY="sk-ant-your_key_here"
```

### Issue: "File size too large"

**Symptom**: Report exceeds 1MB

**Solution**: Reduce analyzed repository count
```bash
spark analyze --user markhazleton --unified --top-n 25
```

---

## Migration from Dated Reports

### Current Behavior (Before Unified)

```bash
# Old command (generates dated reports only)
spark analyze --user markhazleton

# Output: output/reports/markhazleton-analysis-20251230.md
```

### New Unified Behavior

```bash
# New command (generates unified report)
spark analyze --user markhazleton --unified

# Output: output/reports/markhazleton-analysis.md
```

### Transition Period (Generate Both)

```bash
# Generate both for comparison
spark analyze --user markhazleton --unified --keep-dated

# Outputs:
#   - output/reports/markhazleton-analysis.md (unified)
#   - output/reports/markhazleton-analysis-20251230.md (dated)
```

---

## Best Practices

### 1. Cache Management

**Clear cache** when API data seems stale:
```bash
spark cache --clear
```

**Cache location**: `.cache/` directory (6-hour TTL)

### 2. Workflow Scheduling

**Recommended**: Weekly (Sunday midnight UTC)
- Balances freshness vs API rate limits
- Avoids overwhelming GitHub API during business hours

**Not recommended**: Daily or more frequent
- Risk of hitting rate limits
- Minimal statistical changes day-to-day

### 3. API Key Security

**GitHub Actions**: Use repository secrets (never commit keys)

**Local development**: Use environment variables (never commit `.env` files)

```bash
# Create .env file (add to .gitignore)
echo "GITHUB_TOKEN=ghp_..." >> .env
echo "ANTHROPIC_API_KEY=sk-ant-..." >> .env

# Load environment
source .env
```

### 4. Output Directory Management

**Recommended structure**:
```
output/
├── *.svg           # Commit to git (small, frequently updated)
└── reports/
    ├── *-analysis.md          # Commit to git (unified report)
    └── *-analysis-*.md        # Optionally exclude from git (historical)
```

**Git configuration**:
```gitignore
# .gitignore

# Keep unified reports, exclude dated reports
output/reports/*-analysis-*.md

# Keep SVGs and unified reports
!output/*.svg
!output/reports/*-analysis.md
```

---

## Example: Complete Workflow

### Step-by-Step

**1. Setup**:
```bash
git clone https://github.com/markhazleton/github-stats-spark.git
cd github-stats-spark
pip install -r requirements.txt
export GITHUB_TOKEN="ghp_your_token"
```

**2. Generate Report**:
```bash
python -m spark.cli analyze --user markhazleton --unified --verbose
```

**3. View Output**:
```bash
# View markdown in terminal
cat output/reports/markhazleton-analysis.md

# Open in VSCode with markdown preview
code output/reports/markhazleton-analysis.md
```

**4. Commit and Deploy**:
```bash
git add output/*.svg output/reports/markhazleton-analysis.md
git commit -m "Update unified profile report"
git push
```

---

## Resources

- **Feature Specification**: [spec.md](spec.md)
- **Data Model**: [data-model.md](data-model.md)
- **API Contracts**: [contracts/](contracts/)
- **Configuration Reference**: [config/spark.yml](../../config/spark.yml)
- **Main Repository**: https://github.com/markhazleton/github-stats-spark

---

## Support

- **Issues**: https://github.com/markhazleton/github-stats-spark/issues
- **Discussions**: https://github.com/markhazleton/github-stats-spark/discussions
- **Documentation**: [docs/](../../docs/)
