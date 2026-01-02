# Interactive Dashboard Build Pipeline Architecture

**Document Version**: 1.0
**Created**: 2025-01-01
**Status**: Design Document
**Scope**: Static HTML dashboard generation from Python stats via GitHub Actions

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Research Findings](#research-findings)
3. [Architecture Design](#architecture-design)
4. [Data Flow Design](#data-flow-design)
5. [GitHub Pages Deployment Strategy](#github-pages-deployment-strategy)
6. [GitHub Actions Workflow Integration](#github-actions-workflow-integration)
7. [File Organization Strategy](#file-organization-strategy)
8. [Implementation Timeline](#implementation-timeline)

---

## Executive Summary

This document outlines the complete architecture for evolving the existing Stats Spark pipeline to generate an interactive HTML dashboard alongside current SVG and markdown outputs. The solution preserves all existing functionality while adding modern web-based visualization capabilities suitable for deployment to GitHub Pages.

**Key Decisions**:
- **Template Engine**: Jinja2 (recommended for Python integration)
- **Deployment Strategy**: Use `/docs` folder (simpler than gh-pages branch)
- **Data Flow**: SVG/Markdown → JSON → HTML Dashboard
- **GitHub Actions**: Minimal modifications to existing workflow

---

## Research Findings

### 1. Python Template Engine Evaluation

#### Candidates Evaluated
- **Jinja2** (Recommended)
- **Mako**
- **Chameleon**

#### Comparison Matrix

| Criteria | Jinja2 | Mako | Chameleon |
|----------|--------|------|-----------|
| **Python Integration** | Native, excellent | Embedded Python | Good |
| **Learning Curve** | Gentle (Django-like) | Steep (Python knowledge required) | Moderate |
| **Performance** | Very fast (~25k ops/sec) | Fast (~35k ops/sec) | Good (~15k ops/sec) |
| **Template Inheritance** | Excellent | Good | Excellent |
| **For-Loop Performance** | Optimized | Optimized | Good |
| **Auto-escaping** | Excellent, configurable | Good | Good |
| **Community & Documentation** | Largest ecosystem | Small ecosystem | Growing |
| **Security (XSS Prevention)** | Best-in-class | Good | Good |
| **Data Filtering** | Powerful filters | Limited | Good |
| **Async Support** | Yes (3.0+) | No | Limited |
| **GitHub Stats Use Case** | Perfect ✅ | Overkill | Good |

#### Recommendation: **Jinja2**

**Rationale**:

1. **Best for Stats Spark Context**
   - Already Python-centric project
   - Clean template syntax perfect for HTML/dashboard generation
   - Excellent filter system for formatting metrics (e.g., large numbers, percentages)
   - Outstanding community documentation and examples

2. **Integration Benefits**
   - Works seamlessly with existing Python 3.11+ codebase
   - Can reuse data structures directly from stats generation
   - Easy JSON serialization for dashboard data
   - No Python code execution in templates (security advantage)

3. **Performance**
   - Adequate for dashboard generation (compile once per run)
   - Pre-compilation avoids per-request overhead
   - Minimal memory footprint for static generation

4. **Ecosystem**
   - Extensive third-party extensions available
   - Large community with proven production use
   - Well-established patterns for static site generation
   - Good tooling for minification and asset management

**Why Not Mako?**
- Designed for embedded Python code - unnecessary complexity for stats dashboard
- Steeper learning curve for HTML generation context
- Smaller community, fewer resources

**Why Not Chameleon?**
- Better for XML/XHTML but not optimal for HTML5
- Smaller ecosystem than Jinja2
- No significant advantage over Jinja2 for this use case

---

### 2. Data Flow Architecture Research

#### Current Stats Spark Output Pipeline

```
GitHub API + Anthropic API
         ↓
    Python Processing
    (stats generation)
    ├─ SVG files (visualizer.py)
    ├─ Markdown reports
    │  (unified_report_generator.py)
    └─ Internal data structures
         (models/)
         ↓
    Output to filesystem
    ├─ /output/*.svg
    └─ /output/reports/*.md
```

#### Proposed Enhanced Pipeline

```
GitHub API + Anthropic API
         ↓
    Python Processing
    (unified_report_workflow.py)
    ├─ SVG Visualizations
    │  └─ /output/*.svg
    ├─ Markdown Reports
    │  └─ /output/reports/*.md
    └─ Data Models
        ├─ UnifiedReport
        ├─ RepositoryAnalysis
        ├─ UserProfile
        └─ TechnologyStack
         ↓
   [NEW] JSON Serialization Layer
    ├─ Report → dashboard_data.json
    ├─ Repositories → repositories.json
    └─ Profile → profile.json
         ↓
   [NEW] Jinja2 Template Rendering
    ├─ base.html (template)
    ├─ dashboard.html (template)
    ├─ repository.html (template)
    └─ Components/
        ├─ header.html
        ├─ metrics.html
        ├─ repositories.html
        └─ footer.html
         ↓
   [NEW] HTML Dashboard Generation
    ├─ index.html (main dashboard)
    ├─ repos.html (repository detail page)
    ├─ assets/
    │  ├─ css/
    │  │  └─ dashboard.css (generated + static)
    │  ├─ js/
    │  │  ├─ chart.min.js
    │  │  └─ interactions.js
    │  └─ images/
    │      └─ svg-optimized/
         ↓
   GitHub Pages Deployment
    ├─ /docs/index.html
    ├─ /docs/repos.html
    └─ /docs/assets/
```

#### Data Transformation Details

**Stage 1: Python Model → JSON**

```python
# From existing models in /src/spark/models/
report: UnifiedReport
    ├─ username: str
    ├─ repositories: List[RepositoryAnalysis]
    │  ├─ repository: Repository
    │  ├─ commit_history: CommitHistory
    │  ├─ tech_stack: TechnologyStack
    │  └─ summary: RepositorySummary
    └─ profile: UserProfile

# Convert to JSON structure:
{
    "profile": {
        "username": "markhazleton",
        "total_repos": 50,
        "spark_score": 72,
        "avatar_url": "...",
        "bio": "...",
        "generated": "2025-01-01T12:00:00Z"
    },
    "statistics": {
        "total_commits": 15234,
        "languages": [...],
        "activity_pattern": {...}
    },
    "repositories": [
        {
            "rank": 1,
            "name": "github-stats-spark",
            "url": "...",
            "score": 95.5,
            "stars": 150,
            "commits_90d": 45,
            "languages": ["Python", "HTML"],
            "summary": "..."
        }
    ]
}
```

**Stage 2: JSON → Jinja2 Context**

```python
# dashboard_generator.py
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('templates/'),
    autoescape=True  # XSS protection
)

# Prepare context
context = {
    'profile': json.loads(profile_json),
    'stats': json.loads(stats_json),
    'repositories': json.loads(repos_json),
    'generated_at': datetime.now(),
    'site_title': 'GitHub Stats Dashboard',
    'version': '1.0.0'
}

# Render templates
template = env.get_template('dashboard.html')
html = template.render(**context)
```

**Stage 3: Jinja2 → Static HTML**

```html
<!-- templates/dashboard.html -->
{% extends "base.html" %}

{% block content %}
<div class="profile-section">
    <h1>{{ profile.username }}'s GitHub Dashboard</h1>
    <div class="spark-score">{{ profile.spark_score }}/100</div>
</div>

<div class="stats-grid">
    {% for stat in stats %}
    <div class="stat-card">
        <h3>{{ stat.label }}</h3>
        <p class="value">{{ stat.value|format_number }}</p>
    </div>
    {% endfor %}
</div>

<section class="repositories">
    <h2>Top Repositories ({{ repositories|length }})</h2>
    {% include 'components/repositories.html' %}
</section>
{% endblock %}
```

---

### 3. GitHub Pages Deployment Strategy Research

#### Option A: `/docs` Folder (Recommended)

**Advantages**:
- ✅ Single branch configuration (main)
- ✅ All assets version-controlled with code
- ✅ Easier for Git history/blame/rollback
- ✅ GitHub Pages settings simpler (just point to `/docs`)
- ✅ Aligns with documentation-as-code philosophy
- ✅ Natural coexistence with markdown docs
- ✅ No branch merges between gh-pages and main

**Disadvantages**:
- ❌ Repository size grows with generated HTML
- ❌ Less suitable if HTML is very large (stats dashboards are small)

**File Structure**:
```
github-stats-spark/
├─ src/                    # Source code (unchanged)
├─ tests/                  # Tests (unchanged)
├─ output/                 # Generated stats (SVGs, markdown)
│  ├─ *.svg
│  └─ reports/
│      └─ *.md
├─ docs/                   # GitHub Pages root
│  ├─ index.html          # Main dashboard
│  ├─ repos.html          # Repository details page
│  ├─ api/
│  │  ├─ profile.json
│  │  ├─ repositories.json
│  │  └─ stats.json
│  ├─ assets/
│  │  ├─ css/
│  │  │  ├─ dashboard.css  (main styles)
│  │  │  └─ theme.css      (dark/light themes)
│  │  ├─ js/
│  │  │  ├─ main.js        (dashboard logic)
│  │  │  ├─ chart.min.js   (charting library)
│  │  │  └─ interactions.js (interactions)
│  │  └─ images/
│  │      └─ svg/          (optimized SVGs from output/)
│  ├─ README.md            # GitHub Pages info
│  ├─ _config.yml          # Jekyll config (if needed)
│  └─ CNAME                # Custom domain (optional)
├─ .github/
│  └─ workflows/
│      └─ generate-stats.yml
├─ requirements.txt        # Production deps
└─ README.md               # Main project README
```

**GitHub Pages Settings**:
1. Go to repo Settings → Pages
2. Source: Deploy from a branch
3. Branch: main
4. Folder: `/docs`

#### Option B: `gh-pages` Branch (Alternative)

**Advantages**:
- ✅ Keeps generated content separate from source
- ✅ Smaller main branch size
- ✅ Traditional GitHub Pages setup

**Disadvantages**:
- ❌ Requires branch management complexity
- ❌ Harder to correlate dashboard version with code version
- ❌ Additional git operations in workflow
- ❌ Risk of branch drift/inconsistency

**Decision**: Use `/docs` folder for simplicity, version control, and ease of maintenance.

---

## Architecture Design

### System Components

#### Component 1: Data Serialization Module
**Location**: `/src/spark/serializers/`

```python
# serializers/json_exporter.py

class DashboardDataExporter:
    """Exports stats data to JSON for dashboard consumption."""

    def __init__(self, report: UnifiedReport):
        self.report = report

    def export_profile(self) -> dict:
        """Convert UserProfile to JSON-safe dict."""
        return {
            'username': self.report.username,
            'spark_score': self.report.spark_score,
            'avatar_url': self.report.user_profile.avatar_url,
            'repositories_count': len(self.report.repositories),
            'generated_at': self.report.timestamp.isoformat()
        }

    def export_repositories(self) -> List[dict]:
        """Convert repositories to JSON-safe list."""
        return [
            {
                'rank': repo.rank,
                'name': repo.repository.name,
                'url': repo.repository.url,
                'score': repo.composite_score,
                'stars': repo.repository.stars,
                'summary': repo.summary.summary if repo.summary else None
            }
            for repo in self.report.repositories
        ]

    def export_statistics(self) -> dict:
        """Convert statistics to JSON-safe dict."""
        return {
            'total_commits': ...,
            'languages': [...],
            'activity': {...}
        }

    def save_json_files(self, output_dir: Path) -> None:
        """Save all JSON files to docs/api/."""
        ...
```

#### Component 2: Template Rendering Module
**Location**: `/src/spark/renderers/`

```python
# renderers/dashboard_renderer.py

class DashboardRenderer:
    """Renders HTML dashboard from JSON data using Jinja2."""

    def __init__(self, template_dir: Path = None):
        self.env = Environment(
            loader=FileSystemLoader(template_dir or Path('templates/')),
            autoescape=True,
            trim_blocks=True,
            lstrip_blocks=True
        )
        self._register_filters()

    def _register_filters(self):
        """Register custom Jinja2 filters."""
        self.env.filters['format_number'] = lambda x: f"{x:,}"
        self.env.filters['percent'] = lambda x: f"{x:.1f}%"
        self.env.filters['stars'] = lambda x: "⭐" * min(int(x/100), 5)

    def render_dashboard(self, profile_json: str,
                        repos_json: str) -> str:
        """Render main dashboard HTML."""
        template = self.env.get_template('dashboard.html')
        context = {
            'profile': json.loads(profile_json),
            'repositories': json.loads(repos_json),
            'generated_at': datetime.now()
        }
        return template.render(**context)

    def render_repository_detail(self, repo_data: dict) -> str:
        """Render individual repository detail page."""
        template = self.env.get_template('repository.html')
        return template.render(repo=repo_data)

    def save_html_files(self, output_dir: Path,
                       profile_json: str,
                       repos_json: str) -> None:
        """Generate and save all HTML files."""
        # Main dashboard
        html = self.render_dashboard(profile_json, repos_json)
        (output_dir / 'index.html').write_text(html)

        # Individual repo pages (optional)
        repos = json.loads(repos_json)
        for repo in repos[:10]:  # Top 10 get detail pages
            html = self.render_repository_detail(repo)
            filename = f"repos/{repo['name']}.html"
            (output_dir / filename).write_text(html)
```

#### Component 3: Dashboard Build Orchestrator
**Location**: `/src/spark/orchestrators/`

```python
# orchestrators/dashboard_builder.py

class DashboardBuilder:
    """Orchestrates complete dashboard generation pipeline."""

    def __init__(self, report: UnifiedReport,
                 output_dir: Path = Path('docs')):
        self.report = report
        self.output_dir = output_dir
        self.exporter = DashboardDataExporter(report)
        self.renderer = DashboardRenderer()
        self.logger = get_logger()

    def build(self) -> None:
        """Execute complete dashboard build pipeline."""
        try:
            self.logger.info("Starting dashboard build...")

            # Step 1: Export data to JSON
            self.logger.info("Exporting statistics to JSON...")
            profile_json = json.dumps(self.exporter.export_profile())
            repos_json = json.dumps(self.exporter.export_repositories())

            # Step 2: Save JSON API files
            api_dir = self.output_dir / 'api'
            api_dir.mkdir(parents=True, exist_ok=True)
            (api_dir / 'profile.json').write_text(profile_json)
            (api_dir / 'repositories.json').write_text(repos_json)

            # Step 3: Render and save HTML
            self.logger.info("Rendering HTML dashboard...")
            self.renderer.save_html_files(
                self.output_dir,
                profile_json,
                repos_json
            )

            # Step 4: Copy static assets
            self.logger.info("Copying static assets...")
            self._copy_assets()

            # Step 5: Optimize SVGs
            self.logger.info("Optimizing SVG assets...")
            self._optimize_svgs()

            self.logger.info(f"Dashboard build complete: {self.output_dir}")

        except Exception as e:
            self.logger.error(f"Dashboard build failed: {e}")
            raise

    def _copy_assets(self) -> None:
        """Copy static CSS, JS, images."""
        ...

    def _optimize_svgs(self) -> None:
        """Copy and optimize SVGs from output/ to docs/assets/images/svg/."""
        ...
```

---

## Data Flow Design

### Execution Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│            GitHub Actions Workflow (generate-stats.yml)         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    ┌─────────────────────┐
                    │  Setup Environment  │
                    │  - Python 3.11      │
                    │  - Dependencies     │
                    └─────────────────────┘
                              ↓
        ┌─────────────────────────────────────────────┐
        │    Existing Stats Generation Pipeline      │
        │  (unified_report_workflow.py)              │
        ├──────────────────────────────────────────┤
        │  1. Fetch GitHub & Anthropic data        │
        │  2. Calculate composite scores           │
        │  3. Generate SVG visualizations          │
        │  4. Generate markdown reports            │
        │  5. Create UnifiedReport model           │
        └──────────────────────────────────────────┘
                              ↓
        ┌─────────────────────────────────────────────┐
        │ [NEW] Dashboard Generation Pipeline       │
        ├──────────────────────────────────────────┤
        │                                           │
        │  DashboardBuilder.build()                │
        │    ↓                                      │
        │  1. JSON Serialization                  │
        │     DashboardDataExporter                │
        │     ├─ report → profile.json            │
        │     ├─ repositories → repositories.json  │
        │     └─ stats → stats.json               │
        │                                           │
        │  2. Template Rendering                  │
        │     DashboardRenderer (Jinja2)          │
        │     ├─ dashboard.html ← dashboard.j2   │
        │     ├─ repository.html ← repo.j2       │
        │     └─ components (header, footer, etc) │
        │                                           │
        │  3. Asset Management                    │
        │     ├─ Copy CSS/JS files                │
        │     ├─ Optimize SVGs                    │
        │     └─ Minify HTML/CSS                  │
        │                                           │
        └──────────────────────────────────────────┘
                              ↓
        ┌─────────────────────────────────────────────┐
        │         Generated Output Files             │
        ├──────────────────────────────────────────┤
        │                                           │
        │  /output/                                │
        │  ├─ *.svg (existing)                    │
        │  └─ reports/*.md (existing)             │
        │                                           │
        │  /docs/    [NEW GITHUB PAGES ROOT]       │
        │  ├─ index.html                         │
        │  ├─ repos.html                         │
        │  ├─ api/                               │
        │  │  ├─ profile.json                   │
        │  │  ├─ repositories.json              │
        │  │  └─ stats.json                     │
        │  ├─ assets/                            │
        │  │  ├─ css/                           │
        │  │  │  ├─ dashboard.css              │
        │  │  │  └─ theme.css                  │
        │  │  ├─ js/                            │
        │  │  │  ├─ main.js                    │
        │  │  │  └─ chart.min.js               │
        │  │  └─ images/                        │
        │  │      └─ svg/  [optimized SVGs]    │
        │  └─ README.md                          │
        │                                           │
        └──────────────────────────────────────────┘
                              ↓
        ┌─────────────────────────────────────────────┐
        │     Commit & Push Changes                  │
        ├──────────────────────────────────────────┤
        │  $ git add output/ docs/                 │
        │  $ git commit "Update stats & dashboard" │
        │  $ git push origin main                  │
        └──────────────────────────────────────────┘
                              ↓
        ┌─────────────────────────────────────────────┐
        │    GitHub Pages Auto-Deployment           │
        ├──────────────────────────────────────────┤
        │  Settings → Pages → Deploy from /docs/  │
        │  URL: https://markhazleton.github.io/   │
        │       github-stats-spark/               │
        └──────────────────────────────────────────┘
```

### Data Structure Transformations

**Step 1: Python Models → JSON**

```python
# Input: UnifiedReport (from unified_report_workflow.py)
UnifiedReport {
    username: "markhazleton"
    timestamp: datetime(2025-01-01, 12:00:00)
    repositories: [
        RepositoryAnalysis {
            rank: 1
            composite_score: 95.5
            repository: Repository {
                name: "github-stats-spark"
                url: "https://github.com/..."
                stars: 150
                primary_language: "Python"
            }
            summary: RepositorySummary {
                summary: "Automated GitHub statistics..."
            }
        }
    ]
}

# Output: JSON files
{
    // docs/api/profile.json
    {
        "username": "markhazleton",
        "spark_score": 72,
        "total_repos": 50,
        "generated_at": "2025-01-01T12:00:00Z"
    }

    // docs/api/repositories.json
    [
        {
            "rank": 1,
            "name": "github-stats-spark",
            "url": "https://github.com/...",
            "score": 95.5,
            "stars": 150,
            "language": "Python",
            "summary": "Automated GitHub statistics..."
        }
    ]
}
```

**Step 2: JSON → Jinja2 Context**

```python
context = {
    'profile': {
        'username': 'markhazleton',
        'spark_score': 72,
        'total_repos': 50,
        'generated_at': '2025-01-01T12:00:00Z'
    },
    'repositories': [
        {
            'rank': 1,
            'name': 'github-stats-spark',
            'url': 'https://github.com/...',
            'score': 95.5,
            'stars': 150,
            'language': 'Python',
            'summary': 'Automated GitHub statistics...'
        }
    ],
    'site': {
        'title': 'GitHub Stats Dashboard',
        'version': '1.0.0'
    }
}
```

**Step 3: Jinja2 Context → HTML**

```html
<!-- Template: dashboard.html -->
<h1>{{ profile.username }}'s GitHub Dashboard</h1>
<div class="spark-score">{{ profile.spark_score }}/100</div>

<!-- Repository Table -->
<table>
    {% for repo in repositories %}
    <tr>
        <td>#{{ repo.rank }}</td>
        <td>
            <a href="{{ repo.url }}">{{ repo.name }}</a>
        </td>
        <td>{{ repo.score|round(1) }}</td>
        <td>
            <a href="repos.html?repo={{ repo.name }}">Details</a>
        </td>
    </tr>
    {% endfor %}
</table>
```

---

## GitHub Pages Deployment Strategy

### Directory Structure

```
github-stats-spark/
│
├─ docs/                              ← GitHub Pages Root
│  ├─ index.html                     ← Main dashboard page
│  ├─ repos.html                     ← Repository list/detail
│  ├─ 404.html                       ← Custom 404 page
│  │
│  ├─ api/                           ← JSON data endpoints
│  │  ├─ profile.json               ← User profile data
│  │  ├─ repositories.json          ← Repository list data
│  │  └─ stats.json                 ← Aggregate statistics
│  │
│  ├─ assets/                        ← Static resources
│  │  ├─ css/
│  │  │  ├─ dashboard.css           ← Main styles
│  │  │  ├─ theme.css               ← Theme variables
│  │  │  ├─ responsive.css          ← Mobile optimizations
│  │  │  └─ normalize.css           ← CSS reset
│  │  │
│  │  ├─ js/
│  │  │  ├─ main.js                 ← Dashboard logic
│  │  │  ├─ chart.min.js            ← Charting library
│  │  │  └─ interactions.js         ← Interactive elements
│  │  │
│  │  └─ images/
│  │     ├─ svg/                    ← Optimized SVGs
│  │     │  ├─ overview.svg
│  │     │  ├─ heatmap.svg
│  │     │  ├─ languages.svg
│  │     │  ├─ streaks.svg
│  │     │  ├─ fun.svg
│  │     │  └─ release.svg
│  │     │
│  │     └─ icons/                  ← UI icons (optional)
│  │
│  ├─ _config.yml                    ← Jekyll config (if using Jekyll)
│  ├─ README.md                      ← Pages documentation
│  ├─ CNAME                          ← Custom domain (optional)
│  └─ .gitignore                     ← GitHub Pages ignore rules
│
├─ .github/
│  └─ workflows/
│     └─ generate-stats.yml          ← Updated workflow
│
└─ ... (other project files)
```

### GitHub Pages Configuration

**File: .github/settings.json** or **GitHub Web UI**

```yaml
# Repository Settings → Pages

Source:
  Deploy from a branch

Branch:
  main

Folder:
  /docs/

Custom domain:
  (optional) github-stats-spark.example.com

Enforce HTTPS:
  ✓ Enabled

Access:
  Public
```

### URL Structure

```
Base URL: https://markhazleton.github.io/github-stats-spark/

Routes:
  /                          → index.html (dashboard)
  /repos                     → repos.html (detailed repository list)
  /api/profile.json          → profile data endpoint
  /api/repositories.json     → repositories data endpoint
  /assets/css/dashboard.css  → stylesheet
  /assets/js/main.js         → client-side logic
  /assets/images/svg/        → SVG visualizations
```

### Deployment Process

1. **Generate phase** (in GitHub Actions):
   - Generate all stats (existing process)
   - Export to JSON (new)
   - Render HTML templates (new)
   - Copy/optimize assets (new)

2. **Commit phase**:
   ```bash
   git add output/ docs/
   git commit -m "Update GitHub stats and dashboard"
   git push origin main
   ```

3. **Deploy phase** (GitHub Pages automatic):
   - GitHub detects changes in `/docs/`
   - Builds site (no Jekyll processing needed)
   - Publishes to GitHub Pages URL

---

## GitHub Actions Workflow Integration

### Modified `generate-stats.yml`

```yaml
name: Generate GitHub Statistics

on:
  schedule:
    - cron: '0 0 * * 0'
  workflow_dispatch:
    inputs:
      report_mode:
        description: 'Report generation mode'
        required: false
        default: 'unified'
        type: choice
        options:
          - unified
          - dashboard-only
          - all
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  generate-stats:
    runs-on: ubuntu-latest
    name: Generate Statistics & Dashboard

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

      # Existing stats generation
      - name: Generate statistics (unified mode)
        if: ${{ github.event.inputs.report_mode != 'dashboard-only' }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITHUB_REPOSITORY: ${{ github.repository }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          python -m spark.cli analyze \
            --user ${{ github.repository_owner }} \
            --unified \
            --verbose

      # [NEW] Dashboard generation
      - name: Generate HTML dashboard
        if: ${{ github.event.inputs.report_mode != 'unified' }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python -m spark.cli dashboard \
            --user ${{ github.repository_owner }} \
            --output docs \
            --verbose

      - name: Commit generated files
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"

          # Add both SVGs/reports and dashboard files
          git add output/
          git add docs/

          # Commit only if changes exist
          git diff --staged --quiet || \
            git commit -m "Update GitHub stats & dashboard [skip ci]"

      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: generated-statistics
          path: |
            output/
            docs/
          retention-days: 30

      - name: Deploy to GitHub Pages
        if: success()
        uses: actions/upload-pages-artifact@v2
        with:
          path: 'docs'
```

### New CLI Command: `dashboard`

```python
# Add to src/spark/cli.py

@click.command()
@click.option('--user', required=True, help='GitHub username')
@click.option('--output', default='docs', help='Output directory')
@click.option('--verbose', is_flag=True, help='Verbose logging')
def dashboard(user, output, verbose):
    """Generate interactive HTML dashboard from stats."""

    logger = setup_logging(verbose)
    logger.info(f"Generating dashboard for {user}...")

    try:
        # Step 1: Run analysis (reuse existing)
        report = run_analysis(user)

        # Step 2: Build dashboard
        builder = DashboardBuilder(
            report=report,
            output_dir=Path(output)
        )
        builder.build()

        logger.info(f"Dashboard generated: {output}/index.html")

    except Exception as e:
        logger.error(f"Dashboard generation failed: {e}")
        raise
```

### Workflow Modes

The workflow supports three modes via `report_mode` input:

1. **unified** (default)
   - Generate SVG visualizations
   - Generate markdown reports
   - No dashboard generation

2. **dashboard-only**
   - Skip SVG/markdown generation
   - Generate only HTML dashboard
   - Faster for testing

3. **all**
   - Generate SVG visualizations
   - Generate markdown reports
   - Generate HTML dashboard
   - Complete suite

---

## File Organization Strategy

### Source Code Organization

```
src/spark/
│
├─ __init__.py
├─ cli.py                          ← Updated with dashboard command
│
├─ serializers/                    ← [NEW] JSON serialization
│  ├─ __init__.py
│  ├─ json_exporter.py
│  │  └─ DashboardDataExporter
│  └─ encoder.py                   ← Custom JSON encoder for datetime
│
├─ renderers/                      ← [NEW] Template rendering
│  ├─ __init__.py
│  └─ dashboard_renderer.py
│     └─ DashboardRenderer
│
├─ orchestrators/                  ← [NEW] Build orchestration
│  ├─ __init__.py
│  └─ dashboard_builder.py
│     └─ DashboardBuilder
│
├─ templates/                      ← [NEW] Jinja2 templates
│  ├─ base.html
│  ├─ dashboard.html
│  ├─ repository.html
│  ├─ components/
│  │  ├─ header.html
│  │  ├─ footer.html
│  │  ├─ repositories.html
│  │  ├─ metrics.html
│  │  └─ repo_card.html
│  └─ macros/
│     ├─ cards.j2
│     ├─ tables.j2
│     └─ badges.j2
│
├─ static/                         ← [NEW] Static assets
│  ├─ css/
│  │  ├─ dashboard.css
│  │  ├─ theme.css
│  │  └─ responsive.css
│  ├─ js/
│  │  ├─ main.js
│  │  └─ chart.min.js
│  └─ images/
│     └─ icons/
│
├─ (existing modules)
│  ├─ fetcher.py
│  ├─ calculator.py
│  ├─ visualizer.py
│  ├─ unified_report_generator.py
│  └─ ...
└─ ...
```

### Output Directory Organization

```
project-root/
│
├─ output/                         ← Existing outputs
│  ├─ overview.svg
│  ├─ heatmap.svg
│  ├─ languages.svg
│  ├─ streaks.svg
│  ├─ fun.svg
│  ├─ release.svg
│  └─ reports/
│     └─ {username}-analysis.md
│
├─ docs/                           ← [NEW] GitHub Pages root
│  ├─ index.html                  ← Main dashboard
│  ├─ repos.html                  ← Repo list/details
│  ├─ 404.html
│  │
│  ├─ api/                        ← JSON data
│  │  ├─ profile.json
│  │  ├─ repositories.json
│  │  └─ stats.json
│  │
│  ├─ assets/                     ← Static resources
│  │  ├─ css/
│  │  │  ├─ dashboard.css
│  │  │  ├─ theme.css
│  │  │  └─ responsive.css
│  │  ├─ js/
│  │  │  ├─ main.js
│  │  │  └─ chart.min.js
│  │  └─ images/
│  │     └─ svg/                 ← Symlinks to output/*.svg
│  │
│  └─ README.md
│
└─ templates/                      ← Jinja2 template source
   ├─ base.html
   ├─ dashboard.html
   ├─ repository.html
   ├─ components/
   │  ├─ header.html
   │  ├─ footer.html
   │  └─ repositories.html
   └─ macros/
      ├─ cards.j2
      └─ badges.j2
```

### Template File Organization

```
src/spark/templates/
│
├─ base.html                       ← Base layout
│  │
│  ├─ <!DOCTYPE html>
│  ├─ <head> with CSS
│  ├─ <header> with navigation
│  ├─ {% block content %}{% endblock %}
│  ├─ {% include 'components/footer.html' %}
│  └─ <script> tags
│
├─ dashboard.html                  ← Main page
│  │
│  ├─ {% extends "base.html" %}
│  ├─ {% block content %}
│  ├─ {% include 'components/profile_header.html' %}
│  ├─ {% include 'components/spark_score.html' %}
│  ├─ {% include 'components/metrics_grid.html' %}
│  ├─ {% include 'components/repositories.html' %}
│  └─ {% endblock %}
│
├─ repository.html                 ← Individual repo
│  │
│  ├─ {% extends "base.html" %}
│  ├─ Repository detail view
│  └─ Tech stack, commits, etc.
│
├─ components/
│  ├─ header.html
│  ├─ footer.html
│  ├─ profile_header.html          ← User profile card
│  ├─ spark_score.html             ← Spark score card
│  ├─ metrics_grid.html            ← Statistics grid
│  ├─ repositories.html            ← Repo table/grid
│  ├─ repo_card.html               ← Individual repo card
│  └─ language_bars.html           ← Language visualization
│
└─ macros/
   ├─ cards.j2                     ← Reusable card markup
   ├─ badges.j2                    ← Badge components
   └─ tables.j2                    ← Table components
```

---

## Implementation Timeline

### Phase 1: Foundation (Weeks 1-2)

**Deliverables**:
- [ ] Jinja2 template engine integration
- [ ] JSON serialization layer
- [ ] Base template structure
- [ ] Dashboard builder orchestrator

**Tasks**:
1. Add `jinja2` to `requirements.txt`
2. Create `serializers/json_exporter.py`
3. Create `renderers/dashboard_renderer.py`
4. Create `orchestrators/dashboard_builder.py`
5. Create base templates directory structure
6. Create base.html template with CSS framework
7. Write unit tests for serializers and renderer

**Estimated Effort**: 40-50 hours

### Phase 2: Template Development (Weeks 2-3)

**Deliverables**:
- [ ] Dashboard main page template
- [ ] Repository list/detail templates
- [ ] Component templates
- [ ] CSS styling (responsive, theme support)

**Tasks**:
1. Implement dashboard.html template
2. Implement repository.html template
3. Implement component templates (header, footer, metrics)
4. Create responsive CSS (dashboard.css, responsive.css)
5. Create theme CSS (dark/light modes)
6. Test templates with sample data
7. Optimize CSS for performance

**Estimated Effort**: 60-70 hours

### Phase 3: Integration (Weeks 3-4)

**Deliverables**:
- [ ] Updated CLI with dashboard command
- [ ] GitHub Actions workflow modifications
- [ ] Documentation updates
- [ ] Integration tests

**Tasks**:
1. Add dashboard command to CLI
2. Update generate-stats.yml workflow
3. Test complete pipeline end-to-end
4. Create GitHub Pages configuration
5. Add `docs/` directory structure
6. Write deployment documentation
7. Create user guide for dashboard

**Estimated Effort**: 30-40 hours

### Phase 4: Optimization & Polish (Week 4+)

**Deliverables**:
- [ ] Asset optimization (SVG, CSS, JS minification)
- [ ] Performance tuning
- [ ] Accessibility improvements
- [ ] Browser compatibility testing

**Tasks**:
1. Minify CSS and JavaScript
2. Optimize SVG files
3. Test on multiple browsers
4. Implement WCAG AA accessibility
5. Add loading indicators
6. Implement error handling/fallbacks
7. Create comprehensive documentation

**Estimated Effort**: 25-35 hours

**Total Estimated Effort**: 155-195 hours

---

## Technology Stack Summary

### Production Dependencies

```
# Current
PyGithub>=2.1.1
PyYAML>=6.0.1
svgwrite>=1.4.3
requests>=2.31.0
python-dateutil>=2.8.2
anthropic>=0.40.0
tenacity>=9.0.0
packaging>=23.0

# New for Dashboard
jinja2>=3.0.0          # Template rendering
markupsafe>=2.1.1      # Template escaping
click>=8.1.0           # (already in project)

# Optional (for optimization)
cssmin>=0.2.0          # CSS minification
jsmin>=3.0.0           # JavaScript minification
svgcleaner>=0.10.0     # SVG optimization
```

### Development Dependencies

```
# Testing
pytest>=7.0.0
pytest-cov>=4.0.0

# Code quality
ruff>=0.1.0
black>=23.0.0
mypy>=1.0.0

# Documentation
sphinx>=6.0.0
sphinx-rtd-theme>=1.2.0

# Template debugging
jinja2[i18n]>=3.0.0
```

---

## Risk Mitigation

### Identified Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Template rendering errors in production | Medium | High | Comprehensive unit tests, template linting |
| JSON serialization issues with complex types | Low | High | Custom JSON encoder with datetime handling |
| GitHub Pages deployment failures | Low | Medium | Separate `/docs` folder, git workflow testing |
| Asset loading failures (CSS/JS/SVG) | Low | Medium | Fallback styling, asset integrity checks |
| Performance issues with large dashboards | Low | Medium | Asset optimization, lazy loading of repos |
| Browser compatibility issues | Medium | Low | CSS framework (Normalize.css), testing |

### Monitoring & Alerting

- Monitor workflow run times (should be < 5 minutes additional)
- Monitor dashboard build errors in GitHub Actions logs
- Monitor GitHub Pages deployment status
- Set up alerts for workflow failures

---

## Success Metrics

1. **Functionality**
   - Dashboard generates without errors
   - All SVGs and JSON data properly embedded
   - Repository listings display correctly
   - Navigation works across pages

2. **Performance**
   - Dashboard loads in < 2 seconds
   - Dashboard file size < 500KB (including assets)
   - Workflow completes in < 5 minutes total

3. **User Experience**
   - Responsive on mobile, tablet, desktop
   - WCAG AA accessibility compliant
   - Theme switching works (dark/light)
   - SVGs display inline properly

4. **Reliability**
   - Zero broken links
   - GitHub Pages deployment 100% success rate
   - Fallback rendering when data is missing

---

## Appendix: Jinja2 Example Templates

### base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}GitHub Stats Dashboard{% endblock %}</title>

    <link rel="stylesheet" href="{{ url_for('static', filename='css/normalize.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}">

    {% block extra_css %}{% endblock %}
</head>
<body>
    <div class="container">
        {% include 'components/header.html' %}

        <main role="main">
            {% block content %}{% endblock %}
        </main>

        {% include 'components/footer.html' %}
    </div>

    <script src="{{ url_for('static', filename='js/chart.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>

    {% block extra_js %}{% endblock %}
</body>
</html>
```

### dashboard.html

```html
{% extends "base.html" %}

{% block title %}{{ profile.username }}'s GitHub Dashboard{% endblock %}

{% block content %}
<div class="dashboard">
    {% include 'components/profile_header.html' %}

    <section class="metrics-section">
        <h2>Key Metrics</h2>
        {% include 'components/metrics_grid.html' %}
    </section>

    <section class="repositories-section">
        <h2>Top Repositories ({{ repositories|length }})</h2>
        {% include 'components/repositories.html' %}
    </section>
</div>
{% endblock %}
```

### components/repositories.html

```html
<div class="repository-list">
    <table class="repo-table">
        <thead>
            <tr>
                <th>Rank</th>
                <th>Repository</th>
                <th>Score</th>
                <th>Stars</th>
                <th>Language</th>
                <th>Last Updated</th>
            </tr>
        </thead>
        <tbody>
            {% for repo in repositories %}
            <tr class="repo-row">
                <td class="rank">#{{ repo.rank }}</td>
                <td class="name">
                    <a href="{{ repo.url }}" target="_blank">
                        {{ repo.name }}
                    </a>
                </td>
                <td class="score">
                    <span class="badge badge-{{ repo.score|score_level }}">
                        {{ repo.score|round(1) }}
                    </span>
                </td>
                <td class="stars">⭐ {{ repo.stars|format_number }}</td>
                <td class="language">{{ repo.language }}</td>
                <td class="updated">{{ repo.updated|natural_date }}</td>
            </tr>
            {% else %}
            <tr>
                <td colspan="6" class="no-data">
                    No repositories found
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
```

---

## Conclusion

This architecture provides a solid foundation for adding interactive HTML dashboard capabilities to Stats Spark while maintaining backward compatibility with existing SVG and markdown outputs. The choice of Jinja2 as the template engine, combined with a clean separation of concerns via serialization, rendering, and orchestration layers, ensures maintainability and extensibility.

The deployment strategy leveraging GitHub's `/docs` folder simplifies deployment workflows while keeping all assets version-controlled. The modular design allows for incremental feature additions without disrupting the core stats generation pipeline.

**Key Advantages**:
✅ Minimal changes to existing code
✅ Clean data flow and architecture
✅ Easy to test and maintain
✅ Scalable for future enhancements
✅ GitHub Pages integration seamless
✅ No additional infrastructure required
