# Dashboard Build Pipeline - Implementation Guide

## Overview

This guide provides step-by-step instructions for implementing the dashboard generation pipeline for GitHub Stats Spark. Follow the phases sequentially, completing all checklist items before moving to the next phase.

---

## Phase 1: Foundation Setup (Weeks 1-2)

### Goal
Establish the core infrastructure for data serialization, template rendering, and pipeline orchestration.

### 1.1 Update Dependencies

**File**: `requirements.txt`

Add the following lines at the end:

```
# Template rendering for HTML dashboard generation
jinja2>=3.0.0

# Required by jinja2 for HTML escaping
markupsafe>=2.1.1
```

**Verify**:
```bash
pip install -r requirements.txt
python -c "import jinja2; print(jinja2.__version__)"
```

### 1.2 Create Serializers Module

**File**: `src/spark/serializers/__init__.py`

```python
"""JSON serialization for dashboard data export."""

from .json_exporter import DashboardDataExporter

__all__ = ['DashboardDataExporter']
```

**File**: `src/spark/serializers/encoder.py`

```python
"""Custom JSON encoder for complex types."""

import json
from datetime import datetime, date
from decimal import Decimal


class DashboardJSONEncoder(json.JSONEncoder):
    """JSON encoder for dashboard data with support for Python types."""

    def default(self, obj):
        """Handle non-JSON-serializable types."""
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        elif hasattr(obj, 'to_dict'):
            return obj.to_dict()
        return super().default(obj)
```

**File**: `src/spark/serializers/json_exporter.py`

```python
"""Export dashboard data to JSON format."""

import json
from pathlib import Path
from typing import Dict, List, Optional

from spark.models import UnifiedReport, RepositoryAnalysis
from spark.logger import get_logger
from .encoder import DashboardJSONEncoder


class DashboardDataExporter:
    """Exports stats data from Python models to JSON for dashboard."""

    def __init__(self, report: UnifiedReport):
        """Initialize exporter with unified report.

        Args:
            report: UnifiedReport instance from analysis workflow
        """
        self.report = report
        self.logger = get_logger()

    def export_profile(self) -> Dict:
        """Convert UserProfile to JSON-safe dictionary.

        Returns:
            dict: Profile data with username, score, repo count, timestamp
        """
        return {
            'username': self.report.username,
            'spark_score': self.report.spark_score or 0,
            'total_repos': len(self.report.repositories),
            'avatar_url': getattr(
                self.report.user_profile, 'avatar_url', None
            ) if self.report.user_profile else None,
            'bio': getattr(
                self.report.user_profile, 'bio', None
            ) if self.report.user_profile else None,
            'generated_at': self.report.timestamp.isoformat()
        }

    def export_repositories(self, limit: Optional[int] = None) -> List[Dict]:
        """Convert repositories to JSON-safe list.

        Args:
            limit: Maximum number of repositories to export (default: all)

        Returns:
            list: Repository data with rankings, scores, metrics
        """
        repos = self.report.repositories[:limit] if limit else self.report.repositories

        return [
            {
                'rank': repo.rank,
                'name': repo.repository.name,
                'url': repo.repository.url,
                'score': round(repo.composite_score, 2),
                'stars': repo.repository.stars or 0,
                'forks': repo.repository.forks or 0,
                'language': repo.repository.primary_language or 'Unknown',
                'description': repo.repository.description or '',
                'commits_90d': (
                    repo.commit_history.recent_90d
                    if repo.commit_history else 0
                ),
                'contributors': repo.repository.contributors_count or 0,
                'size_kb': repo.repository.size_kb or 0,
                'license': getattr(
                    repo.repository, 'license', 'Unknown'
                ),
                'has_docs': repo.repository.has_docs or False,
                'summary': repo.summary.summary if repo.summary else None,
                'updated_at': (
                    repo.repository.updated_at.isoformat()
                    if repo.repository.updated_at else None
                ),
                'created_at': (
                    repo.repository.created_at.isoformat()
                    if repo.repository.created_at else None
                )
            }
            for repo in repos
        ]

    def export_statistics(self) -> Dict:
        """Convert statistics to JSON-safe dictionary.

        Returns:
            dict: Aggregate statistics about repositories and activity
        """
        total_repos = len(self.report.repositories)
        total_commits = sum(
            repo.commit_history.total if repo.commit_history else 0
            for repo in self.report.repositories
        )
        total_stars = sum(
            repo.repository.stars or 0
            for repo in self.report.repositories
        )

        # Calculate language distribution
        language_counts = {}
        for repo in self.report.repositories:
            lang = repo.repository.primary_language or 'Unknown'
            language_counts[lang] = language_counts.get(lang, 0) + 1

        return {
            'total_repositories': total_repos,
            'total_commits': total_commits,
            'total_stars': total_stars,
            'average_stars_per_repo': (
                round(total_stars / total_repos, 1) if total_repos > 0 else 0
            ),
            'languages': language_counts,
            'top_language': max(
                language_counts.items(),
                key=lambda x: x[1]
            )[0] if language_counts else 'Unknown',
            'generation_time_seconds': self.report.generation_time_seconds or 0,
            'success_rate': self.report.success_rate or 100
        }

    def save_json_files(self, output_dir: Path) -> None:
        """Save all JSON exports to files.

        Args:
            output_dir: Directory to save JSON files (typically /docs/api/)

        Raises:
            OSError: If file write operations fail
        """
        output_dir = Path(output_dir) / 'api'
        output_dir.mkdir(parents=True, exist_ok=True)

        try:
            # Export profile
            profile_data = self.export_profile()
            profile_json = json.dumps(
                profile_data,
                cls=DashboardJSONEncoder,
                indent=2
            )
            profile_file = output_dir / 'profile.json'
            profile_file.write_text(profile_json, encoding='utf-8')
            self.logger.info(f"Exported profile: {profile_file}")

            # Export repositories
            repos_data = self.export_repositories()
            repos_json = json.dumps(
                repos_data,
                cls=DashboardJSONEncoder,
                indent=2
            )
            repos_file = output_dir / 'repositories.json'
            repos_file.write_text(repos_json, encoding='utf-8')
            self.logger.info(f"Exported repositories: {repos_file}")

            # Export statistics
            stats_data = self.export_statistics()
            stats_json = json.dumps(
                stats_data,
                cls=DashboardJSONEncoder,
                indent=2
            )
            stats_file = output_dir / 'stats.json'
            stats_file.write_text(stats_json, encoding='utf-8')
            self.logger.info(f"Exported statistics: {stats_file}")

        except OSError as e:
            self.logger.error(f"Failed to write JSON files: {e}")
            raise
```

### 1.3 Create Renderers Module

**File**: `src/spark/renderers/__init__.py`

```python
"""HTML template rendering for dashboard generation."""

from .dashboard_renderer import DashboardRenderer

__all__ = ['DashboardRenderer']
```

**File**: `src/spark/renderers/dashboard_renderer.py`

```python
"""Render HTML dashboard from JSON data using Jinja2."""

import json
from pathlib import Path
from typing import Optional, Dict, Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from spark.logger import get_logger


class DashboardRenderer:
    """Renders HTML dashboard from JSON data using Jinja2 templates."""

    def __init__(self, template_dir: Optional[Path] = None):
        """Initialize renderer with Jinja2 environment.

        Args:
            template_dir: Path to templates directory
                         (default: src/spark/templates/)
        """
        self.logger = get_logger()

        # Determine template directory
        if template_dir is None:
            template_dir = Path(__file__).parent.parent / 'templates'

        # Initialize Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape(
                enabled_extensions=('html', 'xml'),
                default_for_string=True
            ),
            trim_blocks=True,
            lstrip_blocks=True
        )

        self._register_filters()
        self.logger.debug(f"Initialized renderer with templates: {template_dir}")

    def _register_filters(self) -> None:
        """Register custom Jinja2 filters for dashboard templates."""
        self.env.filters['format_number'] = self._format_number
        self.env.filters['format_percent'] = self._format_percent
        self.env.filters['score_level'] = self._score_level
        self.env.filters['score_stars'] = self._score_stars

    @staticmethod
    def _format_number(value: int) -> str:
        """Format number with thousands separator."""
        try:
            return f"{int(value):,}"
        except (ValueError, TypeError):
            return str(value)

    @staticmethod
    def _format_percent(value: float) -> str:
        """Format value as percentage."""
        try:
            return f"{float(value):.1f}%"
        except (ValueError, TypeError):
            return str(value)

    @staticmethod
    def _score_level(value: float) -> str:
        """Determine score level badge class."""
        if value >= 90:
            return 'excellent'
        elif value >= 75:
            return 'good'
        elif value >= 50:
            return 'fair'
        else:
            return 'poor'

    @staticmethod
    def _score_stars(value: float) -> str:
        """Convert score to star rating (max 5)."""
        stars = int(min(value / 20, 5))
        return '⭐' * stars

    def render_dashboard(self, profile_json: str,
                         repos_json: str,
                         stats_json: Optional[str] = None) -> str:
        """Render main dashboard HTML page.

        Args:
            profile_json: JSON string with profile data
            repos_json: JSON string with repositories data
            stats_json: JSON string with statistics data (optional)

        Returns:
            str: Rendered HTML content

        Raises:
            jinja2.TemplateNotFound: If template not found
            json.JSONDecodeError: If JSON is invalid
        """
        try:
            template = self.env.get_template('dashboard.html')

            context = {
                'profile': json.loads(profile_json),
                'repositories': json.loads(repos_json),
                'stats': json.loads(stats_json) if stats_json else {}
            }

            return template.render(**context)

        except Exception as e:
            self.logger.error(f"Dashboard rendering failed: {e}")
            raise

    def render_repository_detail(self, repo_data: Dict[str, Any]) -> str:
        """Render individual repository detail page.

        Args:
            repo_data: Dictionary with repository information

        Returns:
            str: Rendered HTML content

        Raises:
            jinja2.TemplateNotFound: If template not found
        """
        try:
            template = self.env.get_template('repository.html')
            return template.render(repo=repo_data)

        except Exception as e:
            self.logger.error(f"Repository detail rendering failed: {e}")
            raise

    def save_html_files(self, output_dir: Path,
                       profile_json: str,
                       repos_json: str,
                       stats_json: Optional[str] = None) -> None:
        """Generate and save all HTML files to disk.

        Args:
            output_dir: Output directory (typically /docs/)
            profile_json: JSON string with profile data
            repos_json: JSON string with repositories data
            stats_json: JSON string with statistics data

        Raises:
            OSError: If file write operations fail
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        try:
            # Render and save main dashboard
            self.logger.info("Rendering dashboard page...")
            html = self.render_dashboard(profile_json, repos_json, stats_json)
            index_file = output_dir / 'index.html'
            index_file.write_text(html, encoding='utf-8')
            self.logger.info(f"Saved dashboard: {index_file}")

            # Render and save repository listing
            self.logger.info("Rendering repository list page...")
            repos = json.loads(repos_json)
            repos_data = {
                'repositories': repos,
                'total_count': len(repos)
            }
            template = self.env.get_template('repos.html')
            html = template.render(**repos_data)
            repos_file = output_dir / 'repos.html'
            repos_file.write_text(html, encoding='utf-8')
            self.logger.info(f"Saved repository list: {repos_file}")

        except OSError as e:
            self.logger.error(f"Failed to write HTML files: {e}")
            raise
```

### 1.4 Create Orchestrators Module

**File**: `src/spark/orchestrators/__init__.py`

```python
"""Orchestration of dashboard generation pipeline."""

from .dashboard_builder import DashboardBuilder

__all__ = ['DashboardBuilder']
```

**File**: `src/spark/orchestrators/dashboard_builder.py`

```python
"""Orchestrate complete dashboard generation pipeline."""

import json
import shutil
from pathlib import Path
from typing import Optional

from spark.models import UnifiedReport
from spark.logger import get_logger
from spark.serializers import DashboardDataExporter
from spark.renderers import DashboardRenderer


class DashboardBuilder:
    """Orchestrates complete dashboard generation pipeline.

    Coordinates data serialization, template rendering, and asset management
    to generate a complete static HTML dashboard.
    """

    def __init__(self, report: UnifiedReport,
                 output_dir: Optional[Path] = None):
        """Initialize dashboard builder.

        Args:
            report: UnifiedReport instance with all analysis data
            output_dir: Output directory (default: Path('docs'))
        """
        self.report = report
        self.output_dir = Path(output_dir or 'docs')
        self.logger = get_logger()

        self.exporter = DashboardDataExporter(report)
        self.renderer = DashboardRenderer()

    def build(self) -> None:
        """Execute complete dashboard generation pipeline.

        Steps:
        1. Export data to JSON
        2. Render HTML from templates
        3. Copy static assets
        4. Optimize SVGs

        Raises:
            Exception: If any build step fails
        """
        try:
            self.logger.info("=" * 60)
            self.logger.info("Starting dashboard build...")
            self.logger.info("=" * 60)

            # Step 1: Export data to JSON
            self.logger.info("\n[1/4] Exporting statistics to JSON...")
            self._export_data()

            # Step 2: Render HTML from templates
            self.logger.info("\n[2/4] Rendering HTML templates...")
            self._render_html()

            # Step 3: Copy static assets
            self.logger.info("\n[3/4] Copying static assets...")
            self._copy_assets()

            # Step 4: Optimize and copy SVGs
            self.logger.info("\n[4/4] Optimizing SVG assets...")
            self._optimize_svgs()

            self.logger.info("\n" + "=" * 60)
            self.logger.info("Dashboard build complete!")
            self.logger.info(f"Output directory: {self.output_dir}")
            self.logger.info("=" * 60)

        except Exception as e:
            self.logger.error(f"\nDashboard build failed: {e}")
            raise

    def _export_data(self) -> None:
        """Export statistics data to JSON format."""
        api_dir = self.output_dir / 'api'
        self.exporter.save_json_files(self.output_dir)
        self.logger.info(f"✓ JSON files saved to: {api_dir}")

    def _render_html(self) -> None:
        """Render HTML pages from templates and JSON data."""
        # Load JSON data
        api_dir = self.output_dir / 'api'
        profile_json = (api_dir / 'profile.json').read_text()
        repos_json = (api_dir / 'repositories.json').read_text()
        stats_json = (api_dir / 'stats.json').read_text()

        # Render and save HTML
        self.renderer.save_html_files(
            self.output_dir,
            profile_json,
            repos_json,
            stats_json
        )
        self.logger.info(f"✓ HTML files rendered to: {self.output_dir}")

    def _copy_assets(self) -> None:
        """Copy static CSS, JavaScript, and other assets."""
        assets_dir = Path(__file__).parent.parent / 'static'

        if not assets_dir.exists():
            self.logger.warning(f"Assets directory not found: {assets_dir}")
            return

        # Copy CSS files
        css_src = assets_dir / 'css'
        css_dst = self.output_dir / 'assets' / 'css'
        if css_src.exists():
            css_dst.mkdir(parents=True, exist_ok=True)
            for css_file in css_src.glob('*.css'):
                shutil.copy(css_file, css_dst / css_file.name)
            self.logger.info(f"✓ CSS copied to: {css_dst}")

        # Copy JavaScript files
        js_src = assets_dir / 'js'
        js_dst = self.output_dir / 'assets' / 'js'
        if js_src.exists():
            js_dst.mkdir(parents=True, exist_ok=True)
            for js_file in js_src.glob('*.js'):
                shutil.copy(js_file, js_dst / js_file.name)
            self.logger.info(f"✓ JavaScript copied to: {js_dst}")

    def _optimize_svgs(self) -> None:
        """Copy and optimize SVG files from output/ to docs/assets/images/svg/."""
        output_dir = Path('output')
        svg_dst = self.output_dir / 'assets' / 'images' / 'svg'

        if not output_dir.exists():
            self.logger.warning(f"Output directory not found: {output_dir}")
            return

        svg_dst.mkdir(parents=True, exist_ok=True)

        for svg_file in output_dir.glob('*.svg'):
            shutil.copy(svg_file, svg_dst / svg_file.name)
            self.logger.info(f"✓ SVG copied: {svg_file.name}")

        self.logger.info(f"✓ SVGs optimized to: {svg_dst}")
```

### 1.5 Create Templates Directory Structure

```bash
mkdir -p src/spark/templates/components
mkdir -p src/spark/templates/macros
mkdir -p src/spark/static/css
mkdir -p src/spark/static/js
```

### 1.6 Create Base Template

**File**: `src/spark/templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="GitHub Statistics Dashboard - Stats Spark">

    <title>{% block title %}GitHub Stats Dashboard{% endblock %}</title>

    <!-- CSS Resources -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/normalize.css') | default('./assets/css/normalize.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') | default('./assets/css/dashboard.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') | default('./assets/css/theme.css') }}">

    {% block extra_css %}{% endblock %}
</head>
<body>
    <div class="container">
        <!-- Navigation Header -->
        {% include 'components/header.html' %}

        <!-- Main Content -->
        <main role="main" class="main-content">
            {% block content %}{% endblock %}
        </main>

        <!-- Footer -->
        {% include 'components/footer.html' %}
    </div>

    <!-- JavaScript Resources -->
    <script src="{{ url_for('static', filename='js/main.js') | default('./assets/js/main.js') }}"></script>

    {% block extra_js %}{% endblock %}
</body>
</html>
```

### 1.7 Unit Tests for Foundation

**File**: `tests/unit/test_json_exporter.py`

```python
"""Tests for JSON data exporter."""

import json
from datetime import datetime
from pathlib import Path
from unittest.mock import Mock

import pytest

from spark.serializers import DashboardDataExporter


@pytest.fixture
def mock_report():
    """Create mock UnifiedReport."""
    report = Mock()
    report.username = "testuser"
    report.spark_score = 75
    report.repositories = []
    report.timestamp = datetime(2025, 1, 1, 12, 0, 0)
    report.generation_time_seconds = 120
    report.success_rate = 100
    report.user_profile = None
    return report


def test_export_profile(mock_report):
    """Test profile export."""
    exporter = DashboardDataExporter(mock_report)
    profile = exporter.export_profile()

    assert profile['username'] == 'testuser'
    assert profile['spark_score'] == 75
    assert profile['total_repos'] == 0


def test_export_repositories_empty(mock_report):
    """Test repositories export with empty list."""
    exporter = DashboardDataExporter(mock_report)
    repos = exporter.export_repositories()

    assert repos == []


def test_export_statistics(mock_report):
    """Test statistics export."""
    exporter = DashboardDataExporter(mock_report)
    stats = exporter.export_statistics()

    assert stats['total_repositories'] == 0
    assert stats['total_commits'] == 0
    assert stats['total_stars'] == 0


def test_save_json_files(tmp_path, mock_report):
    """Test JSON file saving."""
    exporter = DashboardDataExporter(mock_report)
    exporter.save_json_files(tmp_path)

    # Check files exist
    assert (tmp_path / 'api' / 'profile.json').exists()
    assert (tmp_path / 'api' / 'repositories.json').exists()
    assert (tmp_path / 'api' / 'stats.json').exists()

    # Check JSON validity
    profile_data = json.loads(
        (tmp_path / 'api' / 'profile.json').read_text()
    )
    assert profile_data['username'] == 'testuser'
```

### 1.8 Checklist for Phase 1

- [ ] Added jinja2 to requirements.txt
- [ ] Created serializers/__init__.py
- [ ] Created serializers/encoder.py
- [ ] Created serializers/json_exporter.py
- [ ] Created renderers/__init__.py
- [ ] Created renderers/dashboard_renderer.py
- [ ] Created orchestrators/__init__.py
- [ ] Created orchestrators/dashboard_builder.py
- [ ] Created templates/ directory structure
- [ ] Created base.html template
- [ ] Created unit tests (test_json_exporter.py)
- [ ] All tests passing: `pytest tests/unit/test_json_exporter.py -v`
- [ ] Code review and approval

---

## Phase 2: Template Development (Weeks 2-3)

### Goal
Create all HTML templates, CSS styles, and JavaScript interactions.

### 2.1 Create Component Templates

**File**: `src/spark/templates/components/header.html`

```html
<header class="main-header">
    <nav class="navbar">
        <div class="navbar-brand">
            <h1><a href="./">⚡ GitHub Stats</a></h1>
        </div>
        <ul class="navbar-menu">
            <li><a href="./">Dashboard</a></li>
            <li><a href="./repos.html">Repositories</a></li>
            <li><a href="#" onclick="toggleTheme()">🌓 Theme</a></li>
        </ul>
    </nav>
</header>
```

**File**: `src/spark/templates/components/footer.html`

```html
<footer class="main-footer">
    <p>&copy; 2025 <strong>Stats Spark</strong> - GitHub Statistics Dashboard</p>
    <p>
        <a href="https://github.com/markhazleton/github-stats-spark" target="_blank">
            View on GitHub
        </a> •
        <a href="https://github.com/markhazleton/github-stats-spark/issues" target="_blank">
            Report Issues
        </a>
    </p>
</footer>
```

[Continue with remaining component templates...]

### 2.2 Create CSS Stylesheets

**File**: `src/spark/static/css/dashboard.css`

```css
/* Main Dashboard Styles */

:root {
    --primary-color: #0066cc;
    --accent-color: #ffcc00;
    --success-color: #28a745;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
    --info-color: #17a2b8;

    --text-color: #333;
    --bg-color: #fff;
    --border-color: #ddd;

    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;

    --font-size-sm: 12px;
    --font-size-base: 14px;
    --font-size-lg: 16px;
    --font-size-xl: 20px;
    --font-size-2xl: 28px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
                 Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
    color: var(--text-color);
    background: var(--bg-color);
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: var(--spacing-lg);
}

/* Header & Navigation */
.main-header {
    background: var(--primary-color);
    color: white;
    padding: var(--spacing-lg) 0;
    margin-bottom: var(--spacing-xl);
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.navbar-brand h1 {
    font-size: var(--font-size-2xl);
}

.navbar-brand a {
    color: white;
    text-decoration: none;
}

.navbar-menu {
    list-style: none;
    display: flex;
    gap: var(--spacing-lg);
}

.navbar-menu a {
    color: white;
    text-decoration: none;
}

.navbar-menu a:hover {
    opacity: 0.8;
}

/* Main Content */
.main-content {
    min-height: calc(100vh - 200px);
}

/* Cards & Sections */
.card {
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: var(--spacing-lg);
    margin-bottom: var(--spacing-lg);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card h2 {
    margin-bottom: var(--spacing-md);
    color: var(--primary-color);
}

/* Stats Grid */
.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
}

.stat-card {
    background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
    color: white;
    padding: var(--spacing-lg);
    border-radius: 8px;
    text-align: center;
}

.stat-card .label {
    font-size: var(--font-size-sm);
    opacity: 0.9;
    margin-bottom: var(--spacing-sm);
}

.stat-card .value {
    font-size: var(--font-size-2xl);
    font-weight: bold;
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        padding: var(--spacing-md);
    }

    .navbar {
        flex-direction: column;
        gap: var(--spacing-md);
    }

    .navbar-menu {
        flex-direction: column;
        gap: var(--spacing-md);
    }

    .metrics-grid {
        grid-template-columns: 1fr;
    }
}
```

[Continue with theme.css, responsive.css...]

### 2.3 Create JavaScript

**File**: `src/spark/static/js/main.js`

```javascript
/**
 * Dashboard Main JavaScript
 * Handles interactions, theme switching, dynamic content
 */

// Theme Management
function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}

// Initialize theme from localStorage
function initializeTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
}

// Load repository data dynamically
async function loadRepositories() {
    try {
        const response = await fetch('./api/repositories.json');
        const repos = await response.json();

        const container = document.getElementById('repositories-list');
        if (!container) return;

        // Render repositories
        repos.forEach(repo => {
            const row = createRepositoryRow(repo);
            container.appendChild(row);
        });
    } catch (error) {
        console.error('Failed to load repositories:', error);
    }
}

function createRepositoryRow(repo) {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td class="rank">#${repo.rank}</td>
        <td class="name">
            <a href="${repo.url}" target="_blank">${repo.name}</a>
        </td>
        <td class="score">
            <span class="badge badge-${scoreLevel(repo.score)}">
                ${repo.score.toFixed(1)}
            </span>
        </td>
        <td class="stars">⭐ ${formatNumber(repo.stars)}</td>
        <td class="language">${repo.language}</td>
    `;
    return row;
}

function formatNumber(num) {
    return num.toLocaleString();
}

function scoreLevel(score) {
    if (score >= 90) return 'excellent';
    if (score >= 75) return 'good';
    if (score >= 50) return 'fair';
    return 'poor';
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initializeTheme();
    loadRepositories();
});
```

### 2.4 Checklist for Phase 2

- [ ] Created all component templates
- [ ] Created dashboard.html template
- [ ] Created repositories.html template
- [ ] Created CSS stylesheet (dashboard.css)
- [ ] Created theme CSS (theme.css)
- [ ] Created responsive CSS (responsive.css)
- [ ] Created JavaScript (main.js)
- [ ] Templates render without errors
- [ ] CSS styles apply correctly
- [ ] JavaScript interactions work
- [ ] Manual testing in browser (local file://)
- [ ] Mobile responsiveness verified
- [ ] Code review and approval

---

## Phase 3: Integration (Weeks 3-4)

### Goal
Integrate dashboard generation into the existing workflow and GitHub Actions.

### 3.1 Add Dashboard Command to CLI

**File**: `src/spark/cli.py` (modify existing file)

Find the `@click.group()` section and add:

```python
@cli.command(name='dashboard')
@click.option(
    '--user',
    required=True,
    help='GitHub username to generate dashboard for'
)
@click.option(
    '--output',
    default='docs',
    help='Output directory for dashboard (default: docs)'
)
@click.option(
    '--verbose',
    is_flag=True,
    help='Enable verbose logging'
)
def dashboard_command(user, output, verbose):
    """Generate interactive HTML dashboard from statistics.

    This command generates a complete HTML dashboard with embedded
    visualizations and repository analysis. The dashboard is saved to
    the specified output directory (typically 'docs' for GitHub Pages).

    Examples:
        spark dashboard --user markhazleton
        spark dashboard --user markhazleton --output ./public
    """
    logger = setup_logging(verbose)

    try:
        logger.info(f"Generating dashboard for {user}...")

        # Step 1: Run analysis to get report
        report = run_analysis(user)

        # Step 2: Build dashboard
        from spark.orchestrators import DashboardBuilder
        builder = DashboardBuilder(report, Path(output))
        builder.build()

        logger.info(f"\n✓ Dashboard generated successfully!")
        logger.info(f"   View at: file://{Path(output).absolute()}/index.html")

    except Exception as e:
        logger.error(f"Dashboard generation failed: {e}")
        raise SystemExit(1)


# Register the command
cli.add_command(dashboard_command)
```

### 3.2 Update GitHub Actions Workflow

**File**: `.github/workflows/generate-stats.yml`

Replace the entire file with:

```yaml
# Stats Spark - Automated GitHub Statistics Generation
# Generates SVG visualizations and interactive dashboard weekly

name: Generate GitHub Statistics

on:
  # Automated weekly generation at midnight UTC on Sundays
  schedule:
    - cron: '0 0 * * 0'

  # Manual trigger from Actions tab
  workflow_dispatch:
    inputs:
      report_mode:
        description: 'Generation mode'
        required: false
        default: 'complete'
        type: choice
        options:
          - stats-only
          - dashboard-only
          - complete

  # Trigger on push to main branch (for testing)
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

      # Generate statistics and markdown reports
      - name: Generate statistics
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

      # [NEW] Generate interactive dashboard
      - name: Generate dashboard
        if: ${{ github.event.inputs.report_mode != 'stats-only' }}
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

          # Add output/ (SVGs, reports) and docs/ (dashboard)
          git add output/
          git add docs/

          # Only commit if there are changes
          git diff --staged --quiet || \
            git commit -m "Update GitHub stats and dashboard [skip ci]"

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
```

### 3.3 Create GitHub Pages Configuration

**File**: `docs/README.md`

```markdown
# GitHub Stats Dashboard

This directory contains the generated HTML dashboard and supporting files
for GitHub Pages deployment.

## Generated Files

- `index.html` - Main dashboard page
- `repos.html` - Detailed repository listing
- `api/` - JSON data files (profile, repositories, statistics)
- `assets/` - CSS, JavaScript, and optimized SVG files

## GitHub Pages Settings

This site is configured to deploy from this `/docs` directory on the `main` branch.

See [Settings → Pages](../../settings/pages) for configuration details.

## Accessing the Dashboard

The dashboard is automatically deployed to:
https://[username].github.io/github-stats-spark/

---

Generated by [Stats Spark](https://github.com/markhazleton/github-stats-spark)
```

### 3.4 Create Initial Docs Directory

```bash
mkdir -p docs/api
mkdir -p docs/assets/css
mkdir -p docs/assets/js
mkdir -p docs/assets/images/svg
touch docs/.gitkeep
touch docs/api/.gitkeep
```

### 3.5 Integration Tests

**File**: `tests/integration/test_dashboard_integration.py`

```python
"""Integration tests for complete dashboard pipeline."""

import json
from pathlib import Path
from unittest.mock import Mock

import pytest

from spark.models import UnifiedReport
from spark.orchestrators import DashboardBuilder


@pytest.fixture
def mock_unified_report():
    """Create a realistic mock UnifiedReport."""
    report = Mock(spec=UnifiedReport)
    report.username = "testuser"
    report.spark_score = 75
    report.repositories = []
    report.timestamp = __import__('datetime').datetime.now()
    report.generation_time_seconds = 120
    report.success_rate = 100
    report.user_profile = None
    return report


def test_dashboard_builder_creates_output_dir(tmp_path, mock_unified_report):
    """Test that dashboard builder creates output directory."""
    builder = DashboardBuilder(mock_unified_report, tmp_path / 'dashboard')
    builder.build()

    assert (tmp_path / 'dashboard').exists()
    assert (tmp_path / 'dashboard' / 'index.html').exists()


def test_dashboard_generates_json_files(tmp_path, mock_unified_report):
    """Test that JSON API files are generated."""
    builder = DashboardBuilder(mock_unified_report, tmp_path / 'dashboard')
    builder.build()

    api_dir = tmp_path / 'dashboard' / 'api'
    assert (api_dir / 'profile.json').exists()
    assert (api_dir / 'repositories.json').exists()
    assert (api_dir / 'stats.json').exists()


def test_dashboard_json_is_valid(tmp_path, mock_unified_report):
    """Test that generated JSON files are valid."""
    builder = DashboardBuilder(mock_unified_report, tmp_path / 'dashboard')
    builder.build()

    api_dir = tmp_path / 'dashboard' / 'api'

    # Profile JSON
    profile = json.loads((api_dir / 'profile.json').read_text())
    assert profile['username'] == 'testuser'
    assert profile['spark_score'] == 75

    # Repositories JSON
    repos = json.loads((api_dir / 'repositories.json').read_text())
    assert isinstance(repos, list)

    # Statistics JSON
    stats = json.loads((api_dir / 'stats.json').read_text())
    assert 'total_repositories' in stats


def test_dashboard_generates_html_files(tmp_path, mock_unified_report):
    """Test that HTML files are generated."""
    builder = DashboardBuilder(mock_unified_report, tmp_path / 'dashboard')
    builder.build()

    assert (tmp_path / 'dashboard' / 'index.html').exists()
    assert (tmp_path / 'dashboard' / 'repos.html').exists()


def test_dashboard_html_contains_data(tmp_path, mock_unified_report):
    """Test that HTML files contain expected data."""
    builder = DashboardBuilder(mock_unified_report, tmp_path / 'dashboard')
    builder.build()

    html = (tmp_path / 'dashboard' / 'index.html').read_text()
    assert 'testuser' in html
    assert 'GitHub' in html or 'Dashboard' in html
```

### 3.6 Checklist for Phase 3

- [ ] Added dashboard command to CLI
- [ ] Updated generate-stats.yml workflow
- [ ] Created docs/README.md
- [ ] Created docs directory structure
- [ ] Integration tests created
- [ ] Integration tests passing
- [ ] Local CLI testing successful
- [ ] GitHub Actions workflow tested (manual trigger)
- [ ] Dashboard files generated and pushed to repo
- [ ] GitHub Pages settings configured
- [ ] Dashboard accessible at GitHub Pages URL
- [ ] Code review and approval
- [ ] Deployment documentation created

---

## Phase 4: Optimization & Polish (Week 4+)

### Goal
Finalize the implementation with performance optimizations and documentation.

### 4.1 Asset Optimization

**File**: `src/spark/orchestrators/dashboard_builder.py` (enhancement)

Add minification methods:

```python
def _minify_css(self) -> None:
    """Minify CSS files."""
    try:
        import cssmin
        css_src = self.output_dir / 'assets' / 'css' / 'dashboard.css'
        css_min = self.output_dir / 'assets' / 'css' / 'dashboard.min.css'

        if css_src.exists():
            content = css_src.read_text()
            minified = cssmin.minify(content)
            css_min.write_text(minified)
            self.logger.info(f"✓ CSS minified: {css_min}")
    except ImportError:
        self.logger.debug("cssmin not installed, skipping CSS minification")


def _minify_js(self) -> None:
    """Minify JavaScript files."""
    try:
        import jsmin
        js_src = self.output_dir / 'assets' / 'js' / 'main.js'
        js_min = self.output_dir / 'assets' / 'js' / 'main.min.js'

        if js_src.exists():
            content = js_src.read_text()
            minified = jsmin.minify(content)
            js_min.write_text(minified)
            self.logger.info(f"✓ JavaScript minified: {js_min}")
    except ImportError:
        self.logger.debug("jsmin not installed, skipping JS minification")
```

### 4.2 Accessibility Improvements

Update templates with ARIA labels:

```html
<!-- Accessible heading structure -->
<h1 id="main-title">{{ profile.username }}'s GitHub Dashboard</h1>

<!-- Accessible table -->
<table role="table" aria-labelledby="repo-table-title">
    <caption id="repo-table-title">Top Repositories</caption>
    <thead>
        <tr>
            <th scope="col">Rank</th>
            <th scope="col">Name</th>
            <th scope="col">Score</th>
        </tr>
    </thead>
    <tbody>
        {% for repo in repositories %}
        <tr>
            <td>{{ repo.rank }}</td>
            <td>{{ repo.name }}</td>
            <td>{{ repo.score }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>

<!-- Skip links -->
<a href="#main-content" class="skip-link">Skip to main content</a>
```

### 4.3 Documentation

Create comprehensive user guide in `docs/DASHBOARD_GUIDE.md`

### 4.4 Checklist for Phase 4

- [ ] Asset optimization implemented
- [ ] CSS minification working
- [ ] JavaScript minification working
- [ ] SVG optimization working
- [ ] Accessibility audit completed
- [ ] ARIA labels added
- [ ] Color contrast verified (WCAG AA)
- [ ] Keyboard navigation tested
- [ ] Browser compatibility tested (Chrome, Firefox, Safari, Edge)
- [ ] Mobile responsiveness verified
- [ ] Performance benchmarks met
- [ ] Documentation completed
- [ ] User guide created
- [ ] API documentation updated
- [ ] Final code review and approval
- [ ] Deployment to production

---

## Testing Throughout All Phases

### Pytest Command

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_json_exporter.py -v

# Run with coverage
pytest --cov=spark --cov-report=html

# Run integration tests only
pytest tests/integration/ -v
```

### Manual Testing

```bash
# Generate dashboard locally
python -m spark.cli dashboard --user YOUR_USERNAME --output /tmp/dashboard --verbose

# Check output
ls -la /tmp/dashboard/
ls -la /tmp/dashboard/api/
ls -la /tmp/dashboard/assets/

# Validate JSON
cat /tmp/dashboard/api/profile.json | jq .

# Open in browser
open file:///tmp/dashboard/index.html  # macOS
start /tmp/dashboard/index.html        # Windows
xdg-open /tmp/dashboard/index.html     # Linux
```

---

## Summary

This implementation guide provides a complete roadmap for implementing the dashboard build pipeline. Follow each phase sequentially, ensuring all checklist items are completed before moving to the next phase.

**Key Success Factors**:
1. Follow the modular architecture (Serializer → Renderer → Orchestrator)
2. Write tests throughout development
3. Test locally before pushing to GitHub
4. Verify GitHub Pages configuration before final deployment
5. Document changes thoroughly

For questions or issues, refer to the architecture design documents:
- `DASHBOARD_BUILD_PIPELINE.md` - Complete architecture
- `DATA_FLOW_DIAGRAM.txt` - Visual data flow
- `QUICK_REFERENCE.md` - Quick lookup guide
