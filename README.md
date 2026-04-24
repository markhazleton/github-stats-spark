# GitHub Stats Spark ⚡

> Portfolio Intelligence System — analyze, classify, and curate the engineering signal in your GitHub profile

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

**📊 [View Sample Analysis Report](output/users/markhazleton/reports/markhazleton-analysis.md)** · **🎨 [View Interactive Dashboard](https://markhazleton.github.io/github-stats-spark/)**

---

## What This Is

GitHub Stats Spark is a **portfolio intelligence system** that classifies your public GitHub repositories into three tiers — Core, Supporting, and Archive — based on commit activity, recency, and quality signals. It computes a signal score (0–100) for each repository and exports enriched data that can be embedded anywhere without additional transformation.

Most GitHub profiles accumulate over time, creating noise that obscures real expertise. This system applies structured analysis to identify core systems, highlight meaningful work, and de-emphasize outdated experiments.

> Your GitHub profile is not a history of what you've built. It is a system that communicates how you think.

---

## Why It Exists

Generic GitHub stats tools report activity. This system interprets it. The goal is not to track how much you've committed — it's to help you understand what your repository portfolio communicates to recruiters, collaborators, and future employers.

---

## Core Idea

A GitHub profile is a communication system, not an archive. Every repository either strengthens or weakens the signal of your expertise. This system makes that signal explicit:

- **Core**: Actively maintained, high-quality systems that represent your current capabilities
- **Supporting**: Complementary projects that demonstrate breadth without being central
- **Archive**: Historical work and experiments that provide context but should not dominate perception

---

## How It Works

```text
GitHub API (public repos only)
        ↓
Repository Filter (non-forked, public)
        ↓
Classification Engine (rule-based thresholds)
  ├── config/portfolio.yml overrides (manual)
  └── Automated rules: recency + commit volume + quality indicators
        ↓
Signal Score Formula (0–100)
  └── Equal weight: recency (33%) + 90-day commits (33%) + tier score (34%)
        ↓
Enriched JSON Output + SVG Visualizations
```

---

## Output

Each repository in `data/repositories.json` receives four new fields:

| Field | Type | Description |
|---|---|---|
| `classification` | string | `core` / `supporting` / `archive` |
| `signal_score` | integer | 0–100 portfolio signal strength |
| `relevance` | string | `high` / `medium` / `low` |
| `notes` | string | Context phrase from config or auto-generated |

Two new SVG visualizations are generated:
- **Portfolio Breakdown** — Core/Supporting/Archive distribution chart
- **Signal Distribution** — Repositories ranked by signal score

---

## Classifying Your Portfolio

Edit `config/portfolio.yml` to override the automated classification for any repository:

```yaml
repos:
  devspark: core
  TailwindSpark: core
  BootstrapSpark: supporting
  "*": archive    # default for all others
```

The system applies your overrides first, then falls back to automated rules. Missing or malformed config logs a warning and proceeds — it never fails.

---

## Relationship to DevSpark Ecosystem

| Project | Role |
|---|---|
| DevSpark | Build systems with spec-driven development |
| DocSpecSpark | Define systems with structured specifications |
| RepoSpark | Curate systems across repositories |
| **GitHub Stats Spark** | **Analyze systems — portfolio intelligence** |

---

## 🎯 What is Stats Spark?

Stats Spark is a comprehensive GitHub analytics suite that transforms your GitHub activity into actionable insights and stunning visualizations. It combines automated SVG generation for profile statistics with AI-powered repository analysis to give you a complete picture of your development work.

**Perfect for:**

- 👨‍💻 Developers wanting to showcase their GitHub activity professionally
- 📊 Teams analyzing repository health and contribution patterns
- 🎯 Technical leaders reviewing developer productivity and technology usage
- 🚀 Open source maintainers tracking project momentum and community engagement

## 🌟 Why Stats Spark?

### Beautiful Profile Statistics

- **Automated Weekly Updates**: GitHub Actions workflow runs at midnight UTC on Sundays
- **6 Visual Categories**: Overview, heatmap, languages, streaks, fun stats, and release cadence
- **Unique Spark Score**: 0-100 metric combining consistency, volume, and collaboration
- **Theme Customization**: Dark, light, and custom themes with WCAG AA accessibility
- **Zero Maintenance**: Set it once, updates automatically every week

### AI-Powered Analysis

- **Intelligent Repository Ranking**: Composite algorithm weighing popularity, activity, and health
- **AI-Generated Summaries**: Claude Haiku creates technical summaries with 97%+ success rate
- **Developer Profiling**: Technology diversity, activity patterns, contribution classification
- **Comprehensive Reports**: GitHub-flavored markdown with embedded visualizations
- **Performance Optimized**: Under 5 minutes for up to 500 repositories with smart caching

### Interactive Dashboard

- **Mobile-First Design**: Touch-optimized interface with 44x44px touch targets and responsive layouts (320px-768px viewports)
- **Bottom Sheet Navigation**: Native mobile patterns for filters, sort controls, and detailed views
- **Swipe Gestures**: Touch-friendly interactions including swipe-to-delete and horizontal navigation
- **Needs Attention View**: Ranks repositories by combined security alerts, PR backlog, dependency drift, and staleness
- **Visual Analytics**: Interactive Chart.js + react-chartjs-2 visualizations optimized for mobile with touch tooltips
- **Drill-Down Details**: Comprehensive repository analysis with commit history, enriched dependency coverage, and rendered markdown summaries
- **Export Functionality**: Download filtered data as CSV or JSON
- **Performance Optimized**: Lighthouse CI configured targeting <2s First Contentful Paint with 0.9+ performance score
- **Offline Support**: IndexedDB caching with Dexie for offline access and 7-day retention
- **Accessibility**: WCAG 2.1 AA compliant with screen reader support and keyboard navigation
- **GitHub Pages Deployment**: Automatically updates with your latest statistics

### Enterprise-Ready

- **Smart Caching**: Intelligent API request optimization
- **Rate Limit Handling**: Automatic retry with exponential backoff
- **Flexible Configuration**: YAML-based configuration for all options
- **Local Development**: Full CLI for testing before deployment
- **Extensible Architecture**: Modular design for easy customization

Stats Spark automatically analyzes your GitHub activity and generates stunning SVG visualizations that you can embed in your profile README. Get insights into your coding patterns, track your streaks, and showcase your Spark Score!

## ✨ Features

### 📊 SVG Profile Statistics

Generate beautiful, embeddable SVG visualizations that update automatically:

#### Overview Dashboard

- ⚡ **Spark Score**: Unique 0-100 metric (40% consistency, 35% volume, 25% collaboration)
- 📈 **Key Metrics**: Total commits, repositories, languages, active days
- ⏰ **Activity Patterns**: Identify your peak coding hours (night owl, early bird, daytime coder)
- ⚡ **Lightning Rating**: 1-5 bolts based on your overall activity level

#### Commit Heatmap

- 📅 **Calendar View**: GitHub-style contribution calendar
- 🔥 **Intensity Visualization**: Color-coded commit frequency
- 📊 **Pattern Recognition**: Identify consistency and work rhythms

#### Language Statistics

- 🌐 **Technology Stack**: Comprehensive language breakdown with percentages
- 📊 **Visual Distribution**: Clean bar charts showing language usage
- 🎯 **Diversity Metrics**: Track your polyglot programming journey

#### Streaks & Consistency

- 🔥 **Current Streak**: Active coding streak counter
- 🏆 **Longest Streak**: Your personal best
- 📈 **Consistency Tracking**: Visualize regular contribution patterns

#### Fun Stats ⚡ ENHANCED

8 personality-driven achievements with emoji flair:

- 🦉 **Coding Time Personality**: Night Owl, Early Bird, or Daytime Coder
- 🚀 **Commit Velocity**: From "Quality over Quantity" to "Commit Machine"
- 📚 **Repository Collection**: Achievement tiers from Focused to Collector
- 🌐 **Language Diversity**: Specialist to Polyglot Programmer
- ⭐ **Community Recognition**: Stars earned across all repositories
- 🏛️ **Account Longevity**: Experience badges from newcomer to veteran
- 💥 **Commit Milestones**: Total commits with achievement levels
- 🌙 **Pattern Personality**: Custom messages based on coding style

#### Release Cadence

- 📊 **Sparklines**: Weekly and monthly repository diversity
- 🚀 **Activity Breadth**: Highlights how many unique repositories were touched in each period, not raw commit volume
- 📈 **Trend Visualization**: Track activity patterns over time

### 🤖 AI-Powered Repository Analysis

Generate comprehensive markdown reports with intelligent insights:

#### Intelligent Repository Ranking

- **30% Popularity Weight**: Stars and forks from community engagement
- **45% Activity Weight**: Recent commits with time-decay (90d/180d/365d windows)
- **25% Health Weight**: Documentation, licensing, and maintenance signals
- **Smart Algorithm**: Balances established projects with active development

#### Attention Ranking and Dependency Insights

- **Schema 2.2.0**: Unified repository records now include `attention_score`, `attention_rank`, and `attention_metrics`
- **Dependency Coverage**: `tech_stack` now tracks known versions, registry resolution coverage, and unknown-version gaps
- **Maintenance Signals**: Attention scoring blends PR pressure, security findings, staleness, and dependency health
- **Markdown-Aware UI**: AI summaries are rendered as GitHub-flavored markdown in both desktop and mobile drill-down views

#### AI-Generated Technical Summaries

- **Claude Haiku Integration**: Enterprise-grade AI summaries for each repository
- **Three-Tier Fallback**: Claude → README extraction → Basic metadata
- **97%+ Success Rate**: Consistent high-quality summaries
- **Technical Focus**: Architecture, tech stack, use cases, and unique features

#### Developer Profile Analysis

- **Technology Diversity**: Language usage patterns and specialization metrics
- **Activity Patterns**: Coding time preferences and consistency analysis
- **Contribution Classification**: Creator, contributor, maintainer patterns
- **Observable Trends**: Long-term patterns and development focus areas

#### Comprehensive Reports

- **GitHub-Flavored Markdown**: Perfect formatting for GitHub rendering
- **Embedded Visualizations**: Includes all SVG statistics inline
- **Rich Metadata**: Stars, forks, commits, languages, file sizes
- **Quality Indicators**: License and documentation status badges
- **Navigation**: Quick links to jump between sections

#### Performance & Reliability

- ⚡ **Fast**: Under 5 minutes for up to 500 repositories
- 🔄 **Smart Caching**: Reduces API calls by 80%+ through content-addressed cache invalidation (keyed by `pushed_at` timestamp)
- 🧠 **Intelligent Refresh**: Only updates repositories with new commits
- 🛡️ **Rate Limit Safe**: Automatic handling and retry logic
- 📊 **Progress Tracking**: Real-time feedback during generation
- ♿ **Accessible**: WCAG AA compliant visualizations

### 🔧 Developer Features

- **🎯 Selective Output**: Choose which statistics and reports to generate
- **🖥️ Local CLI**: Full command-line interface for testing and development
- **📝 YAML Configuration**: Centralized configuration for themes, options, and behavior
- **🚀 GitHub Actions**: Pre-configured workflow for automated weekly updates
- **🎨 Custom Themes**: Define your own color schemes and styles
- **📦 Modular Architecture**: Clean separation of concerns for easy extension
- **🧪 Comprehensive Tests**: 19+ Python test modules (target: 80%+ core module coverage)
- **📚 Full Documentation**: Detailed guides, API reference, and examples

## 🚀 Quick Start

### ⚡ Unified Pipeline Script (Recommended)

The easiest way to run the complete 4-phase pipeline:

```powershell
# Windows PowerShell
.\run-spark.ps1 -User YOUR_USERNAME -IncludeAI -Verbose

# Preserve outputs for multiple users side by side
.\run-spark.ps1 -User YOUR_USERNAME -MultiUser

# Check environment first
.\run-spark.ps1 -CheckOnly
```

**Script handles:**

- ✅ Environment validation (virtual env, tokens, config)
- ✅ Python package installation
- ✅ Cache management
- ✅ Complete 4-phase pipeline execution
- ✅ Output verification and summary

**Options:**

- `-User` - GitHub username (default: markhazleton)
- `-IncludeAI` - Generate AI summaries
- `-MultiUser` - Store outputs under per-user folders instead of overwriting shared files
- `-ClearCache` - Clear all caches before running
- `-ForceRefresh` - Force refresh all data
- `-Screenshots` - Capture repository website screenshots (requires Playwright)
- `-MissingOnly` - Only capture screenshots where PNG doesn't exist yet
- `-Verbose` - Enable detailed logging
- `-CheckOnly` - Validate environment only

### 📦 Manual Setup & CLI

For direct Python CLI usage:

```bash
# 1. Install dependencies
python -m venv .venv
source .venv/bin/activate  # Unix/Mac
# .\.venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
pip install -e .

# 2. Set environment variables
export GITHUB_TOKEN=your_github_token_here
export ANTHROPIC_API_KEY=your_anthropic_key_here  # Optional

# 3. Run unified command
spark unified --user YOUR_GITHUB_USERNAME --include-ai-summaries
```

**This single command generates:**

- ✅ `/data/repositories.json` - Complete unified dataset for frontend
- ✅ `/output/users/{username}/*.svg` - All 6 visual analytics (overview, heatmap, languages, streaks, fun, release)
- ✅ `/output/users/{username}/reports/*.md` - Comprehensive markdown analysis report
- ✅ AI summaries for each repository (if API key provided)

**Notable unified data additions in schema 2.2.0:**

- ✅ Attention ranking fields for maintenance triage
- ✅ Pull request and security summary payloads with explicit availability semantics
- ✅ Enriched dependency version coverage and latest-version resolution metrics

**Benefits:**

- 🚀 ~60% faster than separate commands
- 💾 Single API pass (fewer rate limit issues)
- 🎯 Consistent data snapshot across all outputs
- ⚡ Optimized data gathering and caching

**Testing/Debugging Options:**

```bash
# Test with only 2 repositories (fast cache validation)
spark unified --user YOUR_USERNAME --max-repos 2

# Force refresh all data (bypass cache)
spark unified --user YOUR_USERNAME --force-refresh

# Verbose logging for debugging
spark unified --user YOUR_USERNAME --verbose
```

See [QUICKSTART_UNIFIED.md](.documentation/quickstart/QUICKSTART_UNIFIED.md) for detailed instructions.

---

### GitHub Actions Automation

**Or** set up automatic weekly updates:

### 1. Fork This Repository

Click the "Fork" button in the top right to create your own copy.

### 2. Enable GitHub Actions

1. Go to **Settings** → **Actions** → **General**
2. Select "Allow all actions and reusable workflows"
3. Click **Save**

### 3. Run the Workflow

1. Navigate to **Actions** tab
2. Select "Generate GitHub Statistics"
3. Click "Run workflow" → "Run workflow"
4. Wait 2-5 minutes for completion

### 4. Embed in Your Profile

Add to your profile README (`username/username/README.md`):

```markdown
![GitHub Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/users/YOUR_USERNAME/overview.svg)
```

**Replace `YOUR_USERNAME`** with your GitHub username!

Full instructions: [Getting Started Guide](.documentation/guides/getting-started.md)

## 📊 Statistics Categories

Stats Spark generates 6 SVG categories for your GitHub profile:

| Category | Description | Output File | Sample |
|----------|-------------|-------------|--------|
| **Overview** | Spark Score, commits, languages, time pattern | `overview.svg` | ![Overview](output/users/markhazleton/overview.svg) |
| **Heatmap** | Commit frequency calendar | `heatmap.svg` | ![Heatmap](output/users/markhazleton/heatmap.svg) |
| **Languages** | Programming language breakdown | `languages.svg` | ![Languages](output/users/markhazleton/languages.svg) |
| **Streaks** | Current and longest coding streaks | `streaks.svg` | ![Streaks](output/users/markhazleton/streaks.svg) |
| **Fun Stats** ⚡ | 8 personality-driven achievements | `fun.svg` | ![Fun Stats](output/users/markhazleton/fun.svg) |
| **Release Cadence** | Weekly + monthly repo diversity sparklines | `release.svg` | ![Release](output/users/markhazleton/release.svg) |

### ⚡ Enhanced Fun Stats (New!)

The Fun Stats visualization now showcases **8 creative measurements** with personality:

- 🦉 **Coding Time Personality** - Night Owl, Early Bird, or Daytime Coder
- 🚀 **Commit Velocity** - From "Quality over Quantity" to "Commit Machine"
- 📚 **Repository Collection** - Achievement tiers from Focused to Collector
- 🌐 **Language Diversity** - Specialist to Polyglot Programmer
- ⭐ **Community Recognition** - Stars earned across all repositories
- 🏛️ **Account Longevity** - Experience badges from newcomer to veteran
- 💥 **Commit Milestones** - Total commits with achievement levels
- 🌙 **Pattern Personality** - Custom messages based on your coding style

---

## 🤖 Repository Analysis Reports

Stats Spark's AI-powered analysis feature generates comprehensive markdown reports that showcase your complete GitHub profile:

### Report Structure

1. **Profile Overview Section**
   - Embedded SVG visualizations (all 5 categories)
   - Quick navigation links to major sections
   - Generation metadata and statistics

2. **Top Repositories Listing** (default: top 50)
   - Ranked by composite algorithm (popularity + activity + health)
   - AI-generated technical summaries for each repository
   - Rich metadata: stars, forks, languages, commit activity
   - Quality indicators: license and documentation badges
   - Repository statistics: contributors, file size, commit velocity

3. **Developer Profile Insights**
   - Overall technology diversity and language specialization
   - Activity patterns and coding time preferences
   - Contribution classification (creator vs. contributor)
   - Observable trends and development focus

4. **Report Metadata**
   - Generation timestamp and version information
   - AI summary success rate and coverage statistics
   - Tool attribution and data sources

### Sample Output

**📊 [View Full Sample Report](output/users/markhazleton/reports/markhazleton-analysis.md)**

The sample report demonstrates:

- ✅ 37 repositories analyzed with AI-powered summaries
- ✅ Detailed technical summaries for each major project
- ✅ Complete activity visualizations and metrics
- ✅ Professional GitHub-flavored markdown formatting
- ✅ Easy navigation and comprehensive insights

## ⚡ Spark Score

The Spark Score is a 0-100 metric reflecting your GitHub activity:

**Formula**: `40% Consistency + 35% Volume + 25% Collaboration`

**Lightning Rating**: 1-5 bolts based on your score

- ⚡⚡⚡⚡⚡ (80-100): Exceptional
- ⚡⚡⚡⚡ (60-79): Strong
- ⚡⚡⚡ (40-59): Good
- ⚡⚡ (20-39): Growing
- ⚡ (0-19): Starting

## 🎨 Themes

- **spark-dark** (default): Dark theme with electric blue and gold
- **spark-light**: Light theme with WCAG AA colors
- **custom**: Define your own in `config/themes.yml`

See [Configuration Guide](.documentation/guides/configuration.md) for theme customization.

## 💻 Local CLI

Stats Spark provides a comprehensive command-line interface for local development and testing.

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/github-stats-spark.git
cd github-stats-spark

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export GITHUB_TOKEN=your_github_token
export ANTHROPIC_API_KEY=your_anthropic_key  # Optional for AI summaries
```

### Generate SVG Statistics

Create beautiful visualizations for your GitHub profile:

```bash
# Generate all statistics
spark generate --user YOUR_USERNAME

# Use custom theme (via config file)
spark generate --user YOUR_USERNAME --output-dir ./my-stats

# Force refresh all data (bypass cache)
spark generate --user YOUR_USERNAME --force-refresh

# Generate dashboard JSON data
spark generate --user YOUR_USERNAME --dashboard

# Preview theme without generating
spark preview --theme spark-dark

# Validate configuration
spark config --validate
```

### 🆕 Generate AI-Powered Analysis Reports

Create comprehensive markdown reports with repository analysis:

```bash
# Analyze top 50 repositories and generate full report
spark analyze --user YOUR_USERNAME

# List top repositories without generating report (dry-run)
spark analyze --user YOUR_USERNAME --list-only

# Customize analysis
spark analyze --user YOUR_USERNAME --top-n 25 --output output/reports

# Generate unified report (SVGs + analysis in one pass)
spark analyze --user YOUR_USERNAME --unified

# Also keep a dated copy alongside the unified report
spark analyze --user YOUR_USERNAME --unified --keep-dated

# Store outputs under per-user folders
spark analyze --user YOUR_USERNAME --unified

# Verbose output for debugging
spark analyze --user YOUR_USERNAME --verbose
```

**Analysis Command Features**:

- 📊 Intelligent repository ranking with composite scoring
- 🤖 AI-powered technical summaries (requires ANTHROPIC_API_KEY)
- 📈 Multi-window activity analysis (90d/180d/365d)
- 👤 Developer profile generation with observable patterns
- 📝 GitHub-flavored markdown output with embedded visualizations
- ⚡ High performance with smart caching to minimize API calls

**Options**:

- `--user USERNAME`: GitHub username to analyze (required)
- `--top-n N`: Number of top repositories to include (default: 50)
- `--output DIR`: Output directory for reports (default: output/reports)
- `--list-only`: List top repositories without generating report
- `--unified`: Generate unified report (SVGs + analysis) instead of dated report
- `--keep-dated`: Also generate dated report when using --unified mode
- `--verbose`: Enable detailed logging

See [Analyze Command Guide](.documentation/guides/analyze-command.md) for detailed documentation.

### 🔄 Cache & Refresh Commands

Manage cached data and perform incremental updates:

```bash
# Show cache information
spark cache --info

# Show per-repository cache status
spark cache --status --user YOUR_USERNAME

# List repositories needing cache refresh
spark cache --list-refresh-needed --user YOUR_USERNAME

# Clear all cached data
spark cache --clear

# Prune old cache entries (keep last 2 weeks)
spark cache --prune

# Smart incremental refresh (updates only changed repos)
spark refresh --user YOUR_USERNAME

# Refresh and regenerate AI summaries for changed repos
spark refresh --user YOUR_USERNAME --include-ai-summaries

# Clear AI summaries to force regeneration
spark refresh --user YOUR_USERNAME --clear-summaries
```

## 📚 Documentation

Comprehensive guides and references for all features:

### Getting Started

- **[Getting Started Guide](.documentation/guides/getting-started.md)** - Complete setup instructions for GitHub Actions
- **[Configuration Guide](.documentation/guides/configuration.md)** - All configuration options and customization
- **[Embedding Guide](.documentation/guides/embedding-guide.md)** - How to embed SVGs in your profile README

### Feature Documentation

- **[Analyze Command Guide](.documentation/guides/analyze-command.md)** - AI-powered repository analysis deep dive
- **[API Reference](.documentation/api/api-reference.md)** - Developer documentation for core modules
- **[Changelog](.documentation/CHANGELOG.md)** - Version history and release notes

### Examples

- **[Sample Analysis Report](output/users/markhazleton/reports/markhazleton-analysis.md)** - Real-world output with AI-powered insights
- **[Theme Gallery](config/themes.yml)** - Available themes and customization options

### Support

- **[Issues](https://github.com/markhazleton/github-stats-spark/issues)** - Report bugs or request features
- **[Discussions](https://github.com/markhazleton/github-stats-spark/discussions)** - Ask questions and share ideas

## 🔧 Troubleshooting

### Common Issues

#### GitHub Actions Workflow Fails

**Problem**: Workflow runs but doesn't complete successfully

**Solutions**:

1. Check Actions logs in the Actions tab
2. Verify GitHub Actions is enabled: Settings → Actions → General
3. Ensure `GITHUB_TOKEN` permissions are correct
4. Check if rate limits were hit (workflow handles automatically)

#### SVGs Don't Display in Profile

**Problem**: Embedded images show broken or don't load

**Solutions**:

1. Verify URLs use your correct username
2. Check files exist in `output/users/{username}/` directory
3. Ensure branch name is correct (usually `main`)
4. Try accessing the raw image URL directly
5. Clear browser cache and refresh

Example correct URL:

```markdown
![GitHub Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/users/YOUR_USERNAME/overview.svg)
```

#### Rate Limiting Issues

**Problem**: Getting rate limit errors from GitHub API

**Solutions**:

- Workflow automatically handles with caching and retries
- For local development, wait for rate limit reset
- Use authenticated requests (GITHUB_TOKEN is recommended)
- Enable caching in configuration

#### AI Summaries Not Generating

**Problem**: Repository analysis runs but summaries are missing

**Solutions**:

1. Verify `ANTHROPIC_API_KEY` is set correctly
2. Check API key has sufficient credits/quota
3. Review logs for API errors
4. Try `--no-ai` flag to use README extraction fallback

#### Local CLI Issues

**Problem**: Commands fail or produce errors

**Solutions**:

1. Verify Python 3.11+ is installed: `python --version`
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables correctly
4. Run with `--verbose` flag for detailed output
5. Check configuration with `spark config --validate`

### Getting Help

Still stuck? We're here to help:

- 📖 Check [Getting Started Guide](.documentation/guides/getting-started.md) for detailed setup
- 🔍 Search [existing issues](https://github.com/markhazleton/github-stats-spark/issues)
- 💬 Start a [discussion](https://github.com/markhazleton/github-stats-spark/discussions)
- 🐛 [Open a new issue](https://github.com/markhazleton/github-stats-spark/issues/new) with details

## 🤝 Contributing

We welcome contributions of all kinds! Stats Spark is an open-source project that thrives on community involvement.

### Ways to Contribute

#### 🐛 Report Bugs

Found an issue? [Open a bug report](https://github.com/markhazleton/github-stats-spark/issues/new?labels=bug) with:

- Clear description of the problem
- Steps to reproduce
- Expected vs. actual behavior
- Environment details (Python version, OS, etc.)

#### 💡 Suggest Features

Have an idea? [Start a discussion](https://github.com/markhazleton/github-stats-spark/discussions) or [open a feature request](https://github.com/markhazleton/github-stats-spark/issues/new?labels=enhancement) describing:

- The problem you're trying to solve
- Proposed solution or feature
- Use cases and benefits
- Any relevant examples or mockups

#### 🔧 Submit Pull Requests

Ready to code? We'd love your contributions:

1. **Fork the repository** and create a feature branch
2. **Make your changes** following our code style
3. **Add tests** for new functionality
4. **Update documentation** as needed
5. **Submit a PR** with a clear description

**Good First Issues**: Look for issues labeled [`good first issue`](https://github.com/markhazleton/github-stats-spark/labels/good%20first%20issue) for beginner-friendly tasks.

#### 📖 Improve Documentation

- Fix typos or clarify existing docs
- Add examples or tutorials
- Improve code comments
- Create guides for common use cases

#### 🎨 Share Your Usage

- Show how you're using Stats Spark
- Share your custom themes
- Write blog posts or tutorials
- Spread the word on social media

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/github-stats-spark.git
cd github-stats-spark

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=spark --cov-report=html

# View coverage report
start htmlcov/index.html  # Windows
open htmlcov/index.html   # macOS
xdg-open htmlcov/index.html  # Linux
```

### Code Quality Standards

- ✅ Follow PEP 8 style guidelines
- ✅ Write descriptive commit messages
- ✅ Add docstrings to public functions/classes
- ✅ Include type hints where appropriate
- ✅ Maintain or improve test coverage (target: 80%+ core modules)
- ✅ Update relevant documentation

### Architecture Overview

For contributors, see [API Reference](.documentation/api/api-reference.md) for detailed module documentation including:

- Core modules: `fetcher`, `calculator`, `visualizer`, `summarizer`, `config`
- Analysis modules: `ranker`, `report_generator`, `unified_report_workflow`, `unified_data_generator`
- Cache modules: `cache`, `cache_manager`, `cache_status`, `cache_refresh_strategy`
- Utilities: `logger`, `time_utils`, `screenshot`
- CLI: `cli`, `cli_argument_builders`, `cli_output_layout`

## 🧪 Testing

Stats Spark maintains comprehensive test coverage to ensure reliability and quality.

### Running Tests

```bash
# Run all tests
pytest

# Run with detailed output
pytest -v

# Run specific test file
pytest tests/unit/test_calculator.py

# Run tests matching pattern
pytest -k "test_spark_score"

# Run with coverage report
pytest --cov=spark --cov-report=html

# View coverage in browser
start htmlcov/index.html  # Windows
open htmlcov/index.html   # macOS
```

### Coverage Statistics

| Module | Coverage | Status |
|--------|----------|--------|
| **visualizer.py** | 91% | ✅ Excellent |
| **config.py** | 88% | ✅ Excellent |
| **calculator.py** | 87% | ✅ Excellent |
| **cache.py** | 63% | 🔶 Improving |
| **ranker.py** | 26% | ⚠️ Needs work |
| **summarizer.py** | 19% | ⚠️ Needs work |
| **fetcher.py** | 13% | ⚠️ Needs work |
| **Overall** | 34% | 🔶 Improving |

**Target**: 80%+ coverage for all core modules. A coverage remediation suite is in progress.

### Test Organization

```text
tests/
├── unit/              # Unit tests for individual modules
│   ├── test_cache.py
│   ├── test_cache_manager.py
│   ├── test_calculator.py
│   ├── test_cli.py
│   ├── test_config.py
│   ├── test_dashboard_generator.py
│   ├── test_dependency_parser.py
│   ├── test_fetcher.py
│   ├── test_fetcher_api_version.py
│   ├── test_profile_generator.py
│   ├── test_ranker.py
│   ├── test_report_generator.py
│   ├── test_summarizer.py
│   ├── test_unified_data_generator_enrichment.py
│   ├── test_unified_report_workflow.py
│   ├── test_visualizer.py
│   ├── test_wcag.py
│   └── ...
├── integration/       # Integration tests
│   ├── test_dependency_analysis.py
│   ├── test_unified_repository_enrichment.py
│   └── ...
└── fixtures/          # Test data and configurations
    ├── sample_config.yml
    ├── sample_repositories.json
    └── ...
```

> **Note:** Frontend tests (Vitest) are configured in `frontend/package.json` but test files have not yet been written.

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

This project is free and open-source. You can:

- ✅ Use commercially
- ✅ Modify and distribute
- ✅ Use privately
- ✅ Sublicense

Attribution appreciated but not required!

## 🙏 Acknowledgments

Stats Spark is built on the shoulders of giants:

### Core Technologies

- **[PyGithub](https://github.com/PyGithub/PyGithub)** - GitHub API wrapper for Python
- **[svgwrite](https://github.com/mozman/svgwrite)** - SVG generation library
- **[Anthropic Claude](https://www.anthropic.com/)** - AI-powered repository summaries
- **[Python 3.11+](https://www.python.org/)** - Modern Python features and performance

### Inspiration

- GitHub's contribution graph and profile statistics
- Open source community for continuous feedback and ideas

### Contributors

Thank you to all contributors who have helped make Stats Spark better!

[View all contributors →](https://github.com/markhazleton/github-stats-spark/graphs/contributors)

## 🌟 Star History

If you find Stats Spark useful, please consider giving it a star! ⭐

It helps others discover the project and motivates continued development.

[![Star History Chart](https://api.star-history.com/svg?repos=markhazleton/github-stats-spark&type=Date)](https://star-history.com/#markhazleton/github-stats-spark&Date)

## 📊 Usage Examples

### In Profile README

```markdown
# Your Name

![GitHub Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/users/YOUR_USERNAME/overview.svg)

## Activity

![Commit Heatmap](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/users/YOUR_USERNAME/heatmap.svg)

## Languages

![Language Distribution](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/users/YOUR_USERNAME/languages.svg)

## Analysis

Check out my [detailed GitHub analysis](output/users/YOUR_USERNAME/reports/YOUR_USERNAME-analysis.md) with AI-powered insights!
```

### In Project README

```markdown
## Developer Activity

![GitHub Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)

*Updated weekly via [Stats Spark](https://github.com/markhazleton/github-stats-spark)*
```

### Custom Sections

Create themed sections in your profile:

```markdown
<div align="center">

# ⚡ GitHub Activity Dashboard

![Overview](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)

![Languages](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/languages.svg)
![Streaks](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/streaks.svg)

![Fun Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/fun.svg)

</div>
```

---

<div align="center">

## ⚡ Powered by Stats Spark

**Illuminate your GitHub activity with beautiful statistics and AI-powered insights**

[![Get Started](https://img.shields.io/badge/Get%20Started-Quick%20Setup-blue?style=for-the-badge)](#-quick-start)
[![View Sample](https://img.shields.io/badge/View%20Sample-Analysis%20Report-green?style=for-the-badge)](output/reports/markhazleton-analysis.md)
[![Documentation](https://img.shields.io/badge/Read-Documentation-orange?style=for-the-badge)](.documentation/README.md)

[Quick Start](#-quick-start) • [Features](#-features) • [Documentation](.documentation/README.md) • [Report Issue](https://github.com/markhazleton/github-stats-spark/issues) • [Contribute](#-contributing)

Made with ❤️ by developers, for developers

</div>
