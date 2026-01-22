# Repository Analysis Command

**Generate AI-powered repository analysis reports with comprehensive statistics**

## Overview

The `spark analyze` command generates detailed markdown reports analyzing your top GitHub repositories using:

- **Intelligent Ranking**: Composite algorithm balancing popularity, activity, and health
- **AI Summaries**: Claude Haiku-powered technical summaries with automatic fallbacks
- **Developer Profiles**: Overall analysis of your technology diversity and activity patterns
- **Activity Analysis**: Multi-window time decay (90d/180d/365d) for accurate ranking

## Quick Start

### Basic Usage

```bash
# Generate analysis report for a user
export GITHUB_TOKEN=your_github_token
export ANTHROPIC_API_KEY=your_anthropic_key  # Optional for AI summaries
spark analyze --user YOUR_USERNAME
```

This generates a comprehensive markdown report in `output/reports/YOUR_USERNAME-analysis.md`.

### Dry Run (List Only)

```bash
# Preview top repositories without generating report
spark analyze --user YOUR_USERNAME --list-only
```

### Custom Options

```bash
# Analyze top 25 repositories with custom output directory
spark analyze --user YOUR_USERNAME --top-n 25 --output custom/path

# Disable AI summaries (use template fallback only)
spark analyze --user YOUR_USERNAME --no-ai
```

## Command Options

| Option | Description | Default |
|--------|-------------|---------|
| `--user USERNAME` | GitHub username to analyze | Required |
| `--output PATH` | Output directory for reports | `output/reports/` |
| `--top-n N` | Number of top repositories to analyze | `50` |
| `--list-only` | Dry-run mode (list repos, don't generate report) | `false` |
| `--no-ai` | Disable AI summaries, use templates only | `false` |
| `--include-private` | Include private repositories | `false` (per constitution) |

## Setup Requirements

### 1. GitHub Token (Required)

The command requires a GitHub personal access token for API access:

```bash
# Option 1: Environment variable
export GITHUB_TOKEN=ghp_your_token_here

# Option 2: Config file (config/spark.yml)
# Not recommended - use environment variables for tokens
```

**Creating a GitHub token**:
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo`, `read:user`
4. Copy token and save securely

### 2. Anthropic API Key (Optional)

For AI-powered repository summaries:

```bash
# Set environment variable
export ANTHROPIC_API_KEY=sk-ant-your_key_here
```

**Getting an Anthropic API key**:
1. Sign up at [console.anthropic.com](https://console.anthropic.com)
2. Navigate to API Keys section
3. Create new API key
4. Copy key and save securely

**Cost**: ~$0.10-0.30 per 50-repository report with Claude Haiku

**Without API key**: The command automatically falls back to template-based summaries using repository metadata and README content.

### 3. Configuration (Optional)

Customize analysis behavior in `config/spark.yml`:

```yaml
analyzer:
  # Top N repositories to include in analysis report
  top_n: 50

  # AI Provider for repository summarization
  ai_provider: anthropic      # Options: anthropic, disabled

  # Model selection (if ai_provider enabled)
  ai_model: claude-haiku-3.5  # Cost-effective summaries

  # Ranking algorithm weights (must sum to 1.0)
  ranking_weights:
    popularity: 0.30          # Stars, forks, watchers
    activity: 0.45            # Recent commits, recency
    health: 0.25              # Documentation, maturity, issues
```

## Report Structure

Generated reports include:

### 1. Header Section
- Generation timestamp
- User profile link
- Report metadata

### 2. Overall Developer Profile
- Technology diversity analysis
- Activity patterns (commit frequency, consistency, trends)
- Contribution classification (active maintainer, hobbyist, specialist)
- AI-powered overall impression

### 3. Top Repositories Listing
For each repository (sorted by composite score):
- **Repository name and description**
- **Statistics**: Stars, forks, issues, creation date
- **Primary language** with language distribution
- **Activity metrics**: Recent commits (90d/180d/365d), commit velocity (commits/month)
- **Additional statistics**: Contributors count, repository size, number of languages
- **Quality indicators**: CI/CD workflows, tests directory, LICENSE file, documentation
- **Release information**: Total releases, latest release date with days ago
- **AI-generated summary** or template fallback
- **Technology stack** (if dependency files present)

### 4. Failure Notes (if any)
- Repositories that couldn't be analyzed
- API errors or rate limiting notices
- Recommendations for resolution

## Ranking Algorithm

Repositories are ranked using a composite score:

**Formula**: `Score = 30% Popularity + 45% Activity + 25% Health`

### Popularity Component (30%)
- Logarithmic scaling for stars, forks, watchers
- Prevents mega-repos from dominating
- Range: 0-100

### Activity Component (45%)
- Multi-window time decay:
  - 50% weight: Last 90 days
  - 30% weight: Last 180 days
  - 20% weight: Last 365 days
- Recency bonus for commits within 7 days
- Normalized by repository age
- Range: 0-100

### Health Component (25%)
- Documentation quality (README presence and length)
- Repository maturity (age, size)
- Issue management (open vs closed ratio)
- Archive penalty (-50% for archived repos)
- Range: 0-100

### Edge Case Handling

| Case | Treatment |
|------|-----------|
| **Archived repositories** | -50% popularity, -90% activity (preserved if >1000 stars) |
| **Forked repositories** | -70% all scores unless significantly diverged |
| **Zero-star active repos** | Activity boost to prevent penalizing new projects |
| **Empty repositories** | Excluded if zero commits and <10 KB size |

## AI Summary Generation

### Three-Tier Fallback Strategy

1. **Primary: Claude API Summary**
   - Uses Anthropic Claude Haiku for cost-effective summaries
   - Analyzes README content + repository metadata
   - Identifies commit patterns (frequency, recency, consistency)
   - Generates 2-3 sentence technical summary
   - Retry logic with exponential backoff

2. **Fallback 1: Enhanced Template**
   - Triggered if API key missing or API fails
   - Extracts key information from README
   - Combines with repository metadata
   - Uses template with smart extraction

3. **Fallback 2: Basic Template**
   - Last resort if README unavailable
   - Uses only repository metadata
   - Includes primary language and statistics

### Prompt Engineering

The AI prompt is optimized for technical repositories:
- Focus on technical purpose and architecture
- Identify key technologies and patterns
- Highlight unique features or approaches
- Keep summaries concise (2-3 sentences)
- Avoid marketing language

## Performance

The analyzer is optimized for speed:

| Scenario | Time Estimate | Notes |
|----------|---------------|-------|
| **First run (50 repos)** | 2.5-3 minutes | Cold cache |
| **Subsequent runs** | <2 minutes | Warm cache |
| **List-only mode** | 30-60 seconds | No report generation |
| **Without AI** | 1.5-2 minutes | Template fallback only |

**Performance budget**: <3 minutes for 50 repositories (meets specification SC-001)

### Optimization Tips

1. **Use caching**: Cache is content-addressed by repository pushed_at timestamp (valid until repo updates)
2. **Run during off-peak**: Lower GitHub API latency
3. **Parallel processing**: AI summaries process in parallel when possible
4. **Skip dependency analysis**: Use `--no-deps` flag if not needed (future enhancement)

## GitHub Actions Integration

Add to your workflow (`.github/workflows/generate-stats.yml`):

```yaml
name: Generate Repository Analysis

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly at midnight Sunday UTC
  workflow_dispatch:

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -e .

      - name: Generate analysis report
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          python -m spark.cli analyze --user ${{ github.repository_owner }}

      - name: Commit and push report
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add output/reports/
          git commit -m "Update repository analysis [skip ci]" || exit 0
          git push
```

**Required secrets**:
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions
- `ANTHROPIC_API_KEY`: Add to repository secrets (Settings → Secrets → Actions)

## Troubleshooting

### "API rate limit exceeded"

**Cause**: GitHub API rate limit (5,000 requests/hour for authenticated)

**Solution**:
- Enable caching (content-addressed by pushed_at timestamps)
- Wait for rate limit reset
- Run during off-peak hours

### "Anthropic API error"

**Cause**: Invalid API key, quota exceeded, or network issue

**Solution**:
- Verify API key is correct
- Check Anthropic console for quota/billing
- Command automatically falls back to templates

### "No repositories found"

**Cause**: User has no public repositories or token lacks permissions

**Solution**:
- Verify username is correct
- Check token has `repo` and `read:user` scopes
- Use `--include-private` if analyzing private repos (not recommended per constitution)

### "Report generation timeout"

**Cause**: Network latency, large number of dependencies

**Solution**:
- Reduce `--top-n` value (e.g., 25 instead of 50)
- Check network connection
- Use `--no-ai` for faster generation

## Examples

### Example 1: Standard Analysis

```bash
export GITHUB_TOKEN=ghp_your_token
export ANTHROPIC_API_KEY=sk-ant-your_key
spark analyze --user markhazleton
```

Output: `output/reports/markhazleton-analysis.md`

### Example 2: Dry Run Preview

```bash
spark analyze --user markhazleton --list-only
```

Output:
```
Fetching repositories for user: markhazleton
Found 127 public repositories

Top 50 Repositories (by composite score):
1. github-stats-spark (Score: 87.3) - Active, well-maintained
2. ProjectWebApplication (Score: 82.1) - Active, well-maintained
3. azure-docs (Score: 76.5) - Legacy, high-quality
...
```

### Example 3: Custom Configuration

```bash
spark analyze --user markhazleton --top-n 25 --output reports/custom
```

Analyzes top 25 repositories, saves to `reports/custom/markhazleton-analysis.md`

### Example 4: Template-Only (No AI)

```bash
export GITHUB_TOKEN=ghp_your_token
spark analyze --user markhazleton --no-ai
```

Generates report using template-based summaries only (no Anthropic API calls)

## Constitution Compliance

The analyze command adheres to the project constitution:

- **I. Python-First**: Pure Python implementation, importable modules
- **II. CLI Interface**: Full CLI access for local testing and automation
- **III. Data Privacy**: Explicit public-only repository filter (default)
- **IV. Testability**: Unit tests for all calculation logic (>80% coverage)
- **V. Observable**: Progress tracking and detailed error logging
- **VI. Performance**: Meets <3-minute target (specification SC-001)
- **VII. Configuration**: YAML-based config, environment variable overrides

## Related Documentation

- [Getting Started Guide](getting-started.md) - Setup and initial configuration
- [Configuration Guide](configuration.md) - All configuration options
- [API Reference](../api/api-reference.md) - Developer documentation
- [Embedding Guide](embedding-guide.md) - How to embed generated reports

## API Reference

For developers integrating the analyze functionality:

```python
from spark.ranker import RepositoryRanker
from spark.summarizer import RepositorySummarizer
from spark.report_generator import ReportGenerator

# Rank repositories
ranker = RepositoryRanker(config)
ranked_repos = ranker.rank_repositories(repositories)

# Generate AI summaries
summarizer = RepositorySummarizer(config)
summaries = [summarizer.summarize(repo) for repo in ranked_repos]

# Generate report
generator = ReportGenerator(config)
report_path = generator.generate(user_profile, ranked_repos, summaries)
```

See [API Reference](../api/api-reference.md) for complete module documentation.

---

**Questions or Issues?** [Report them on GitHub](https://github.com/markhazleton/github-stats-spark/issues)
