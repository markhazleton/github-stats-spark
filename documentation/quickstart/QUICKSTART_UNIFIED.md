# Quick Start: All-In-One Unified Generation

## Overview

The **`spark unified`** command is your **all-in-one solution** for GitHub statistics:

- ✅ Gathers **ALL repository data** and attributes
- ✅ Generates **AI summaries** for each repository (optional)
- ✅ Creates **SVG visualizations** (activity heatmaps, language charts, etc.)
- ✅ Produces **markdown reports** with comprehensive analysis
- ✅ Outputs **unified JSON** (`/data/repositories.json`) for frontend dashboard

**Everything in a single optimized run!**

---

## Prerequisites

1. **GitHub Personal Access Token** (required)
   ```bash
   export GITHUB_TOKEN=your_github_token_here
   ```

2. **Anthropic API Key** (optional, for AI summaries)
   ```bash
   export ANTHROPIC_API_KEY=your_anthropic_key_here
   ```

3. **Python Environment** (Python 3.9+)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## Basic Usage

### 1. Generate Everything (Recommended)

```bash
spark unified --user YOUR_GITHUB_USERNAME
```

**This single command will:**
- Fetch all repository data and metrics
- Calculate commit statistics (avg size, largest, smallest)
- Analyze technology stacks and dependencies
- Rank repositories by composite score
- Generate SVG visualizations
- Create markdown analysis report
- Save unified JSON to `/data/repositories.json`

**Output:**
- `/data/repositories.json` - Complete dataset for frontend
- `/output/*.svg` - Activity heatmaps, language charts, streak calendars
- `/output/reports/YOUR_USERNAME-analysis.md` - Comprehensive markdown report

---

### 2. With AI Summaries (Recommended for Deep Insights)

```bash
spark unified --user YOUR_GITHUB_USERNAME --include-ai-summaries
```

**Adds AI-generated summaries for each repository:**
- Code quality assessment
- Technology stack analysis
- Contribution patterns
- Recommendations for improvement

**Requires:** `ANTHROPIC_API_KEY` environment variable

---

### 3. Force Fresh Data

```bash
spark unified --user YOUR_GITHUB_USERNAME --force-refresh
```

**Bypasses cache and fetches fresh data from GitHub API**

---

## What Gets Generated

### 1. Unified Data (`/data/repositories.json`)

Complete dataset with all attributes:
```json
{
  "repositories": [
    {
      "name": "my-repo",
      "description": "...",
      "language": "Python",
      "stars": 42,
      "commit_history": {
        "total_commits": 150,
        "last_commit_date": "2026-01-02T...",
        "first_commit_date": "2025-01-01T..."
      },
      "commit_metrics": {
        "avg_size": 45.2,
        "largest_commit": {...},
        "smallest_commit": {...}
      },
      "tech_stack": {
        "frameworks": ["Flask", "React"],
        "dependencies": [...]
      },
      "summary": {
        "text": "AI-generated summary...",
        "ai_generated": true
      },
      "rank": 1,
      "composite_score": 87.3
    }
  ],
  "profile": {...},
  "metadata": {...}
}
```

### 2. SVG Visualizations (`/output/*.svg`)

- **Activity Heatmap** - Contribution calendar
- **Language Chart** - Programming language distribution
- **Streak Calendar** - Coding streak visualization
- **Repository Cards** - Top repository highlights
- **Statistics Dashboard** - Key metrics overview

### 3. Markdown Report (`/output/reports/USERNAME-analysis.md`)

Comprehensive analysis including:
- Repository rankings and scores
- Technology stack breakdown
- Commit patterns and velocity
- Quality indicators (README, tests, CI/CD)
- AI insights (if enabled)

---

## Advanced Options

### Custom Output Directory

```bash
spark unified --user YOUR_USERNAME --output-dir custom/path
```

### Custom Config File

```bash
spark unified --user YOUR_USERNAME --config path/to/spark.yml
```

### Verbose Logging

```bash
spark unified --user YOUR_USERNAME --verbose
```

---

## Optimization Benefits

**Why use `spark unified` instead of separate commands?**

1. **Single API Pass** - All data fetched in one go (faster, fewer rate limit issues)
2. **Shared Cache** - Commit data, languages, and metadata shared across all outputs
3. **Consistent Data** - SVGs, reports, and JSON use identical data snapshot
4. **Time Savings** - ~60% faster than running commands separately
5. **Simplified Workflow** - One command instead of three

**Before (3 separate commands):**
```bash
spark generate --user markhazleton --dashboard  # 30s
spark analyze --user markhazleton --unified      # 45s
# Manual JSON merging required
```

**After (all-in-one):**
```bash
spark unified --user markhazleton  # 35s total ✅
```

---

## Frontend Integration

The generated `/data/repositories.json` powers the interactive dashboard:

```bash
cd frontend
npm install
npm run dev  # Development server at http://localhost:5173
npm run build  # Production build to /docs
```

**Dashboard Features:**
- Repository table with sorting and filtering
- Interactive visualizations (bar charts, line graphs, scatter plots)
- Drill-down into individual repository details
- Side-by-side comparison (up to 5 repos)

---

## Troubleshooting

### Issue: "GITHUB_TOKEN environment variable not set"

**Solution:**
```bash
export GITHUB_TOKEN=ghp_your_token_here
```

### Issue: "ANTHROPIC_API_KEY not set - AI summaries will be skipped"

**Solution (if you want AI summaries):**
```bash
export ANTHROPIC_API_KEY=sk-ant-your_key_here
```

**Or run without AI summaries:**
```bash
spark unified --user YOUR_USERNAME  # Summaries optional
```

### Issue: GitHub API rate limit exceeded

**Solution:**
- Wait for rate limit to reset (check with `curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/rate_limit`)
- Use `--force-refresh` sparingly (respects cache by default)
- Ensure `GITHUB_TOKEN` is set (authenticated requests have higher limits)

### Issue: Missing commit metrics (N/A values in table)

**Solution:**
- Delete `/data/repositories.json` and regenerate
- Run with `--force-refresh` to bypass cache
- Check GitHub API access to repository commit history

---

## Next Steps

1. **Explore the Dashboard:**
   ```bash
   cd frontend
   npm run dev
   # Open http://localhost:5173/github-stats-spark/
   ```

2. **Customize Configuration:**
   - Edit `config/spark.yml` to adjust ranking weights, themes, etc.

3. **Schedule Regular Updates:**
   ```bash
   # Add to crontab (daily at 2 AM)
   0 2 * * * cd /path/to/github-stats-spark && spark unified --user YOUR_USERNAME
   ```

4. **Deploy to GitHub Pages:**
   ```bash
   git add docs/
   git commit -m "Update dashboard"
   git push origin main
   # Enable GitHub Pages in repository settings (source: /docs)
   ```

---

## Summary

```bash
# ⚡ ONE COMMAND TO RULE THEM ALL ⚡
spark unified --user YOUR_GITHUB_USERNAME --include-ai-summaries
```

**Generates:**
- ✅ `/data/repositories.json` - Complete unified dataset
- ✅ `/output/*.svg` - Visual analytics
- ✅ `/output/reports/*.md` - Comprehensive report
- ✅ AI summaries for every repository
- ✅ Ready-to-use frontend dashboard data

**All in a single optimized run!**
