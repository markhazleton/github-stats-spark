# Dashboard Build Pipeline - Quick Reference Guide

## At a Glance

| Aspect | Decision |
|--------|----------|
| **Template Engine** | Jinja2 (v3.0+) |
| **Deployment Target** | GitHub Pages (`/docs` folder) |
| **Data Format** | Python Models → JSON → HTML |
| **Primary Language** | Python 3.11+ |
| **Build Orchestration** | New DashboardBuilder class |
| **CI/CD Platform** | GitHub Actions (enhanced existing workflow) |
| **Total Effort** | ~155-195 hours (4 weeks) |

---

## Core Components Quick Map

### 1. Serialization Layer (Convert Models to JSON)

**File**: `src/spark/serializers/json_exporter.py`

```python
class DashboardDataExporter:
    def export_profile() -> dict       # UnifiedReport → profile.json
    def export_repositories() -> List  # RepositoryAnalysis[] → repositories.json
    def export_statistics() -> dict    # Aggregates → stats.json
    def save_json_files(output_dir)    # Write to /docs/api/
```

**Input**: `UnifiedReport` (from existing workflow)
**Output**: JSON files in `/docs/api/`

---

### 2. Rendering Layer (Convert JSON to HTML)

**File**: `src/spark/renderers/dashboard_renderer.py`

```python
class DashboardRenderer:
    def __init__(template_dir)         # Load Jinja2 environment
    def _register_filters()            # Custom Jinja2 filters
    def render_dashboard(profile_json, repos_json) -> str  # Main HTML
    def render_repository_detail(repo_data) -> str        # Repo page
    def save_html_files(output_dir, ...)                  # Write to /docs/
```

**Input**: JSON strings
**Output**: HTML files in `/docs/`

---

### 3. Orchestration Layer (Coordinate Pipeline)

**File**: `src/spark/orchestrators/dashboard_builder.py`

```python
class DashboardBuilder:
    def __init__(report: UnifiedReport, output_dir: Path)
    def build() -> None                # Execute full pipeline
        ├─ Export data to JSON
        ├─ Render HTML templates
        ├─ Copy static assets
        └─ Optimize SVGs
```

**Entry Point**: Called after stats generation in workflow

---

### 4. Template Structure

**Location**: `src/spark/templates/`

```
templates/
├── base.html                    ← Master layout (DOCTYPE, head, body)
├── dashboard.html               ← Main page (extends base)
├── repository.html              ← Detail page (extends base)
├── components/
│   ├── header.html             ← Navigation
│   ├── footer.html             ← Copyright
│   ├── profile_header.html      ← User card
│   ├── metrics_grid.html        ← Stats cards
│   ├── repositories.html        ← Repo table
│   └── repo_card.html           ← Single repo
└── macros/
    ├── cards.j2                ← Reusable card markup
    └── badges.j2               ← Badge components
```

**Inheritance Pattern**:
```
dashboard.html
  ├─ {% extends "base.html" %}
  ├─ {% include 'components/profile_header.html' %}
  ├─ {% include 'components/metrics_grid.html' %}
  └─ {% include 'components/repositories.html' %}
```

---

### 5. Static Assets

**Location**: `src/spark/static/`

```
static/
├── css/
│   ├── dashboard.css            ← Main styles
│   ├── theme.css                ← CSS variables (dark/light)
│   └── responsive.css           ← Mobile optimizations
└── js/
    ├── main.js                  ← Dashboard logic
    └── chart.min.js             ← Charting library (third-party)
```

**Deployment**: Copy to `/docs/assets/` during build

---

## Workflow Integration Points

### Modified GitHub Actions Workflow

**File**: `.github/workflows/generate-stats.yml`

```yaml
# Existing steps (unchanged)
- name: Generate statistics
  run: python -m spark.cli analyze --user ${{ github.repository_owner }}

# [NEW] Dashboard generation step
- name: Generate HTML dashboard
  run: python -m spark.cli dashboard --user ${{ github.repository_owner }} --output docs

# Existing commit/push (now includes /docs/)
- name: Commit generated files
  run: |
    git add output/ docs/
    git commit -m "Update GitHub stats & dashboard [skip ci]"
```

### New CLI Command

**File**: `src/spark/cli.py`

```python
@click.command()
@click.option('--user', required=True)
@click.option('--output', default='docs')
@click.option('--verbose', is_flag=True)
def dashboard(user, output, verbose):
    """Generate interactive HTML dashboard."""
    report = run_analysis(user)
    builder = DashboardBuilder(report, Path(output))
    builder.build()
```

**Usage**:
```bash
python -m spark.cli dashboard --user markhazleton --output docs --verbose
```

---

## Data Transformation Pipeline

### Step 1: Python Models → JSON

**Input Type**: `UnifiedReport` (from analysis)
```python
report.username = "markhazleton"
report.spark_score = 72
report.repositories = [RepositoryAnalysis(...), ...]
```

**Output Type**: JSON strings
```json
{
    "username": "markhazleton",
    "spark_score": 72,
    "repositories": [...]
}
```

---

### Step 2: JSON → Jinja2 Context

**Input Type**: JSON strings
```python
context = {
    'profile': json.loads(profile_json),
    'repositories': json.loads(repos_json),
    'generated_at': datetime.now()
}
```

**Jinja2 Processing**:
- Load template: `template = env.get_template('dashboard.html')`
- Render: `html = template.render(**context)`

---

### Step 3: Jinja2 → HTML

**Template Syntax Examples**:
```html
<!-- Variable interpolation -->
<h1>{{ profile.username }}'s Dashboard</h1>

<!-- Loops -->
{% for repo in repositories %}
  <tr>{{ repo.name }}</tr>
{% endfor %}

<!-- Conditionals -->
{% if repo.score > 90 %}
  <span class="badge-excellent">Excellent</span>
{% endif %}

<!-- Filters -->
<p>{{ repo.stars|format_number }}</p>
```

**Output Type**: HTML string (written to `/docs/index.html`)

---

## GitHub Pages Configuration

### URL Structure

```
Base: https://markhazleton.github.io/github-stats-spark/

Routes:
├── / ........................... /docs/index.html (main dashboard)
├── /repos ...................... /docs/repos.html (detailed list)
├── /api/profile.json ........... /docs/api/profile.json
├── /api/repositories.json ...... /docs/api/repositories.json
├── /assets/css/dashboard.css ... /docs/assets/css/dashboard.css
├── /assets/js/main.js ......... /docs/assets/js/main.js
└── /assets/images/svg/*.svg .... /docs/assets/images/svg/
```

### GitHub Pages Settings

**Settings → Pages**:
1. **Source**: Deploy from a branch
2. **Branch**: main
3. **Folder**: /docs/
4. **Custom domain**: (optional)
5. **Enforce HTTPS**: ✓ Enabled

---

## Key Files & Responsibilities

| File | Purpose | Status |
|------|---------|--------|
| `cli.py` | Add dashboard command | NEW |
| `serializers/json_exporter.py` | Models → JSON | NEW |
| `renderers/dashboard_renderer.py` | JSON → HTML | NEW |
| `orchestrators/dashboard_builder.py` | Coordinate pipeline | NEW |
| `templates/base.html` | Master layout | NEW |
| `templates/dashboard.html` | Main page | NEW |
| `templates/components/*.html` | Components | NEW |
| `static/css/*.css` | Styles | NEW |
| `static/js/*.js` | Client logic | NEW |
| `.github/workflows/generate-stats.yml` | Add dashboard step | MODIFIED |
| `requirements.txt` | Add jinja2 | MODIFIED |

---

## Dependencies to Add

```
# requirements.txt
jinja2>=3.0.0                  # Template engine
markupsafe>=2.1.1             # HTML escaping (jinja2 dependency)

# Optional for optimization
cssmin>=0.2.0                 # CSS minification (optional)
jsmin>=3.0.0                  # JS minification (optional)
```

---

## Testing Strategy

### Unit Tests

```python
# tests/unit/test_json_exporter.py
def test_export_profile(): ...
def test_export_repositories(): ...

# tests/unit/test_dashboard_renderer.py
def test_render_dashboard(): ...
def test_render_with_missing_data(): ...

# tests/unit/test_dashboard_builder.py
def test_build_creates_files(): ...
def test_build_with_empty_data(): ...
```

### Integration Tests

```python
# tests/integration/test_dashboard_pipeline.py
def test_full_pipeline_execution(): ...
def test_output_file_structure(): ...
def test_html_validity(): ...
def test_json_endpoints(): ...
```

### Manual Testing

```bash
# Run locally
python -m spark.cli dashboard --user markhazleton --output /tmp/docs --verbose

# Check output
ls -la /tmp/docs/
cat /tmp/docs/index.html
cat /tmp/docs/api/profile.json | jq .

# Open in browser
open file:///tmp/docs/index.html
```

---

## Common Jinja2 Filters (Custom)

```python
env.filters['format_number'] = lambda x: f"{x:,}"
env.filters['percent'] = lambda x: f"{x:.1f}%"
env.filters['stars'] = lambda x: "⭐" * min(int(x/100), 5)
env.filters['natural_date'] = lambda x: humanize.naturaldate(x)
env.filters['score_level'] = lambda x: 'excellent' if x > 90 else 'good' if x > 70 else 'fair'
```

**Usage in Templates**:
```html
{{ 15234|format_number }}  → 15,234
{{ 0.725|percent }}        → 72.5%
{{ 250|stars }}            → ⭐⭐
{{ repo.updated|natural_date }}  → 2 days ago
```

---

## Performance Considerations

| Metric | Target | Notes |
|--------|--------|-------|
| Dashboard build time | < 30s | Including all steps |
| Dashboard page load | < 2s | Initial load, 3G network |
| JSON file size | < 100KB | Gzip-compressed |
| HTML file size | < 200KB | Minified + gzipped |
| Total assets size | < 500KB | All files combined |
| Workflow duration | < 5min | Dashboard step only |

---

## Common Issues & Solutions

### Issue: Template Not Found

```python
# Problem: TemplateNotFound: 'dashboard.html'
# Solution: Ensure templates are in correct directory
loader=FileSystemLoader('src/spark/templates/')  # Absolute path
```

### Issue: JSON Serialization Error

```python
# Problem: Object of type datetime is not JSON serializable
# Solution: Use custom JSON encoder
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

json.dumps(data, cls=DateTimeEncoder)
```

### Issue: Relative Path Issues in HTML

```html
<!-- Problem: Images don't load in GitHub Pages -->
<!-- Solution: Use absolute paths from /docs root -->
<img src="/github-stats-spark/assets/images/svg/overview.svg">
<!-- OR use relative paths if files are colocated -->
<img src="./assets/images/svg/overview.svg">
```

### Issue: CSS Not Loading

```html
<!-- Problem: Styles don't apply in GitHub Pages -->
<!-- Solution: Use correct relative paths -->
<link rel="stylesheet" href="./assets/css/dashboard.css">  <!-- Correct -->
<link rel="stylesheet" href="/assets/css/dashboard.css">   <!-- Wrong for GitHub Pages -->
```

---

## Quick Start Implementation Checklist

### Phase 1: Foundation
- [ ] Add jinja2 to requirements.txt
- [ ] Create serializers/json_exporter.py
- [ ] Create renderers/dashboard_renderer.py
- [ ] Create orchestrators/dashboard_builder.py
- [ ] Create templates/ directory structure
- [ ] Create base.html template

### Phase 2: Templates & Styling
- [ ] Implement dashboard.html
- [ ] Implement components/ templates
- [ ] Create static/css/ stylesheets
- [ ] Create static/js/ scripts
- [ ] Test templates locally

### Phase 3: Integration
- [ ] Add dashboard CLI command
- [ ] Update GitHub Actions workflow
- [ ] Create docs/ directory
- [ ] Test full pipeline

### Phase 4: Polish
- [ ] Minify CSS/JS
- [ ] Optimize SVGs
- [ ] Add accessibility improvements
- [ ] Test on multiple browsers
- [ ] Document deployment

---

## References & Resources

### Jinja2 Documentation
- **Main Docs**: https://jinja.palletsprojects.com/
- **Template Designer**: https://jinja.palletsprojects.com/templates/
- **API Reference**: https://jinja.palletsprojects.com/api/

### GitHub Pages Documentation
- **Setup Guide**: https://docs.github.com/en/pages/getting-started-with-github-pages
- **Deploying from /docs**: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

### Related Tech Stack
- **Python 3.11**: https://www.python.org/downloads/
- **GitHub Actions**: https://docs.github.com/en/actions
- **SVGwrite**: https://github.com/mozman/svgwrite
- **PyGithub**: https://github.com/PyGithub/PyGithub

---

## Next Steps

1. **Review** this design with team
2. **Create** architecture ADR (Architecture Decision Record)
3. **Prioritize** implementation phases
4. **Assign** tasks to developers
5. **Start** Phase 1 (Foundation)
6. **Track** progress using GitHub Issues or project board
