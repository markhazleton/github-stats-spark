# GitHub Stats Spark - AI Coding Agent Instructions

## Project Overview

**Stats Spark** is a dual-stack GitHub analytics platform combining Python backend analysis with a React dashboard. It generates SVG visualizations, AI-powered repository reports, and interactive web interfaces for GitHub profile statistics.

**Core Architecture:** Python 3.11+ backend orchestrates GitHub data fetching → statistical analysis → SVG generation → AI summarization → unified JSON export. React 19 frontend consumes JSON to build interactive visualizations.

## Critical Workflows

### Primary Development Command (All-in-One)
```bash
# Single command generates everything: data/repositories.json + SVGs + markdown reports
spark unified --user USERNAME --include-ai-summaries --verbose

# Test locally before deployment
.\test-unified-data.ps1  # Windows PowerShell
./test-unified-data.sh   # Unix/macOS
```

**Why unified?** ~60% faster than separate commands, single API pass, consistent data snapshot. This is the ONLY command users should run for complete generation. Constitution requires <5 minute execution time for <500 repositories.

### Environment Setup
```bash
# Python backend (required first)
pip install -r requirements.txt
pip install -e .  # Install CLI as 'spark' command

# Frontend (only if working on dashboard)
cd frontend && npm install
```

### Testing & Quality
```bash
# Python tests (52% overall coverage, 80%+ core modules per constitution)
pytest --cov=spark --cov-report=html

# Frontend tests
cd frontend && npm test

# Validate configuration (constitutional requirement)
spark config --validate

# Constitution requires: Statistics MUST have <1% discrepancy vs GitHub
# Constitution requires: Spark Score MUST be deterministic
```

### Deployment Flow
1. Python generates `data/repositories.json` (unified data source)
2. Frontend builds to `docs/` directory (GitHub Pages serves from here)
3. GitHub Actions workflow runs weekly, commits generated files

## Module Architecture

### Python Backend (`src/spark/`)

**Data Flow Pipeline:**
```
GitHubFetcher → StatsCalculator → StatisticsVisualizer
     ↓              ↓                    ↓
  APICache    RepositoryRanker    SVG outputs
     ↓              ↓
RepositorySummarizer (AI)    UnifiedReportWorkflow (orchestrator)
```

**Core Modules:**
- **`fetcher.py`**: PyGithub wrapper with smart caching and rate limit handling
- **`calculator.py`**: Spark Score formula (40% consistency + 35% volume + 25% collaboration), streak detection, time patterns
- **`visualizer.py`**: SVG generation with `svgwrite` (overview/heatmap/languages/streaks/fun/release)
- **`ranker.py`**: Composite scoring (30% popularity + 45% activity + 25% health) with time-decay windows
- **`summarizer.py`**: Anthropic Claude Haiku integration, three-tier fallback (AI → README → metadata)
- **`unified_report_workflow.py`**: Orchestrates entire generation pipeline with partial failure handling
- **`cli.py`**: Click-style CLI with `unified`, `generate`, `analyze` commands

**Models (`src/spark/models/`):**
Dataclasses for Repository, CommitHistory, TechnologyStack, RepositorySummary, UserProfile, UnifiedReport, GitHubData. All models use type hints.

**Configuration (`config/spark.yml`):**
- Repository exclusions (private repos MUST be excluded - constitutional requirement)
- Theme selection (spark-dark default, spark-light) - all themes MUST meet WCAG AA contrast (4.5:1)
- Analyzer settings: top_n repositories (default 50, max 500), ranking weights, AI provider
- Cache TTL: 6 hours (constitutional requirement for rate limit protection)

### React Frontend (`frontend/src/`)

**Component Structure:**
```
App.jsx (routing + state)
├── RepositoryTable/ (sortable table with selection)
├── Visualizations/ (Recharts: Bar/Line/Scatter)
├── Comparison/ (side-by-side up to 5 repos)
├── DrillDown/ (detailed repository view)
└── Common/ (LoadingState, Tooltip, FilterControls, ExportButton, ErrorBoundary)
```

**Data Contract:**
Frontend expects `data/repositories.json` with schema version 2.0.0. Key fields:
- `repositories[]`: Array with `name`, `language`, `stars`, `commit_history`, `commit_metrics`, `tech_stack`, `ai_summary`
- `profile`: User metadata (`username`, `total_commits`)
- `metadata`: Generation info (`generated_at`, `schema_version`)

**Build Target:** Vite builds to `../docs/` (GitHub Pages root), base path `/github-stats-spark/`

## Project-Specific Conventions

### Naming Patterns
- Python modules: lowercase_underscore (`unified_report_workflow.py`)
- Python classes: PascalCase with descriptive suffixes (`GitHubFetcher`, `StatsCalculator`)
- React components: PascalCase, one component per file (`RepositoryTable.jsx`)
- Config files: kebab-case YAML (`spark.yml`, `themes.yml`)

### Error Handling
- **Python**: Custom exceptions in `exceptions.py` (`WorkflowError`, `ConfigurationError`)
- **Retry logic**: Use `@retry` from tenacity for API calls (exponential backoff: 1s, 2s, 4s, 8s per constitution)
- **Logging**: All operations MUST log to stdout/stderr for GitHub Actions debugging (constitutional requirement)
- **No silent failures**: Errors MUST include timestamps, context, and actionable guidance
- **Frontend**: React ErrorBoundary wraps all major sections

### Testing Conventions
- **Python**: `tests/unit/test_*.py` for modules, `tests/integration/` for workflows
- Coverage targets: Core modules >80% (constitutional requirement), overall >50%
- Use fixtures from `tests/fixtures/` (sample_user_data.json, sample_config.yml)
- **Frontend**: Vitest for component tests (run with `npm test`)
- **Privacy**: ALL tests must verify private repositories are filtered out (constitutional requirement)

### Configuration Precedence
1. CLI arguments (highest priority)
2. Environment variables (`GITHUB_TOKEN`, `ANTHROPIC_API_KEY`)
3. `config/spark.yml` defaults
4. Hardcoded fallbacks in code

## Integration Points

### GitHub API Rate Limits
- Authenticated: 5000 requests/hour
- **Smart caching** in `cache.py` reduces calls by 80% (6-hour TTL)
- Workflow handles `RateLimitExceededException` with automatic retry

### AI Summarization (Optional)
- **Provider**: Anthropic Claude Haiku 3.5 (cost-effective, fast)
- **Fallback chain**: Claude → README parsing → basic metadata
- **Success rate**: 97%+ in production
- Skip with `--no-ai` flag for faster analysis without summaries

### GitHub Actions Workflow
- **Trigger**: Weekly on Sundays 00:00 UTC, manual dispatch, push to main
- **Secrets required**: `GITHUB_TOKEN` (auto-provided), `ANTHROPIC_API_KEY` (optional)
- **Artifacts**: Commits generated files (output/, data/, docs/) with `[skip ci]` message

## Common Tasks

### Adding a New SVG Category
1. Add category name to `config/spark.yml` → `stats.enabled`
2. Implement generation in `visualizer.py` → `generate_*_svg()` method
3. Update `StatsCalculator` if new metrics needed
4. Add to CLI help text in `cli.py`

### Modifying Ranking Algorithm
Edit `ranker.py` → `RepositoryRanker.calculate_composite_score()`:
- Adjust weights in `config/spark.yml` → `analyzer.ranking_weights`
- Three components: popularity (stars/forks), activity (commits with time decay), health (docs/license)

### Customizing Frontend Dashboard
- Edit chart configurations in `frontend/src/components/Visualizations/`
- Use Recharts components (ResponsiveContainer, BarChart, LineChart, ScatterChart)
- Update metric formatters in `frontend/src/services/metricsCalculator.js`

### Debugging API Issues
```bash
# Enable verbose logging
spark unified --user USERNAME --verbose

# Check cache contents
ls -la .cache/

# Clear cache for fresh data
spark cache --clear  # Or delete .cache/ directory
```

## Anti-Patterns to Avoid

- **Don't** run `spark generate` and `spark analyze` separately (use `spark unified` instead)
- **Don't** commit generated files manually (let GitHub Actions handle it)
- **Don't** modify SVG files directly (regenerate through Python)
- **NEVER** process private repository data (constitutional violation - immediate rejection)
- **Don't** add dependencies without justification (constitutional requirement)
- **Don't** create abstractions without solving real problems (avoid premature optimization)
- **Don't** hardcode usernames in config (use CLI args or env vars)
- **Don't** ignore rate limit errors (workflow handles automatically with cache)
- **NEVER** create markdown documentation files outside `/documentation` folder (constitutional requirement)

## Key Files Reference

- [src/spark/unified_report_workflow.py](src/spark/unified_report_workflow.py) - Main orchestration logic
- [src/spark/cli.py](src/spark/cli.py) - CLI entry point (MUST support: generate, preview, config, cache commands per constitution)
- [config/spark.yml](config/spark.yml) - Central configuration (themes, thresholds, features)
- [config/themes.yml](config/themes.yml) - Theme definitions (WCAG AA compliance required)
- [frontend/src/App.jsx](frontend/src/App.jsx) - React app root with routing/state
- [.github/workflows/generate-stats.yml](.github/workflows/generate-stats.yml) - CI/CD automation
- [data/repositories.json](data/repositories.json) - Unified data contract between backend/frontend
- [.specify/memory/constitution.md](.specify/memory/constitution.md) - Project constitution (NON-NEGOTIABLE rules)

## Constitutional Requirements (MUST Follow)

1. **Data Privacy**: NEVER process private repositories - violations = immediate rejection
2. **Module Separation**: Each Python module MUST have single responsibility (fetcher, calculator, visualizer, cache, config)
3. **CLI Interface**: MUST support `generate`, `preview`, `config`, `cache` commands
4. **Testability**: >80% coverage for core modules, fixtures in `tests/fixtures/`
5. **Observable**: All operations MUST log to stdout/stderr, no silent failures
6. **Performance**: <5 min for <500 repos, 6-hour cache TTL, exponential backoff (1s, 2s, 4s, 8s)
7. **Accuracy**: <1% discrepancy vs GitHub, deterministic Spark Score
8. **Themes**: WCAG AA contrast compliance (4.5:1 for text)
9. **Demo Account**: Use `markhazleton` for all examples
10. **Versioning**: Semantic versioning (breaking config = MAJOR, new features = MINOR, fixes = PATCH)
11. **Documentation Location**: ALL markdown documentation MUST be in `/documentation` folder (except root README.md)

## Documentation Locations

- User guides: [documentation/guides/](documentation/guides/)
- API reference: [documentation/api/api-reference.md](documentation/api/api-reference.md)
- Feature specs: [documentation/spec/](documentation/spec/)
- Frontend docs: [frontend/README.md](frontend/README.md)
