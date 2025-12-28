# Implementation Plan: Stats Spark - GitHub Profile Statistics Generator

**Branch**: `001-stats-spark` | **Date**: 2025-12-28 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-stats-spark/spec.md`

**Note**: This plan details the implementation approach for creating a Python-based GitHub statistics generator that runs via GitHub Actions and produces SVG visualizations for GitHub profile READMEs.

## Summary

Stats Spark is an automated GitHub profile statistics generator that fetches user activity data via the GitHub API, calculates comprehensive metrics (Spark Score, language breakdown, time patterns, streaks), and generates beautiful SVG visualizations. The system runs automatically via GitHub Actions (daily at midnight UTC) and allows users to embed the generated stats in their profile README. Default demo uses the markhazleton account.

**Primary Technical Approach**:
- Python 3.11+ for core logic (data fetching, calculations, SVG generation)
- GitHub Actions for automated scheduling and execution
- PyGithub library for GitHub API interactions
- Custom SVG generation using Python SVG libraries
- YAML-based configuration for user customization
- File-based caching (6-hour TTL) for API response management

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**:
- PyGithub (GitHub API client)
- PyYAML (configuration parsing)
- svgwrite or similar (SVG generation)
- requests (HTTP with retry logic)
- python-dateutil (timezone/date handling)

**Storage**: File-based caching (.cache/ directory) + SVG output (output/ directory)
**Testing**: pytest with pytest-mock for unit tests, integration tests for API interactions
**Target Platform**: GitHub Actions (Ubuntu latest runner)
**Project Type**: Single Python application with CLI interface
**Performance Goals**: Complete generation in <5 minutes for <500 repositories; <1% discrepancy vs GitHub native stats
**Constraints**:
- GitHub API rate limits (5000 requests/hour for authenticated requests)
- Must handle 99% of edge cases without workflow failures
- WCAG AA contrast compliance for themes
- 6-hour cache TTL, configurable repository limit (default 500)

**Scale/Scope**:
- Process up to 500 repositories (configurable)
- Generate 5 SVG output categories (overview, heatmap, languages, fun stats, streaks)
- Support 3 built-in themes + custom theme capability

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Status**: ✅ Constitution exists at `.specify/memory/constitution.md` (ratified 2025-12-28)

**Constitution Alignment Verification**:

1. **Python-First** (Principle I): ✅ Compliant
   - Plan specifies modular structure (fetcher.py, calculator.py, visualizer.py, cache.py, config.py)
   - Each module has single responsibility per constitution requirement

2. **CLI Interface** (Principle II): ✅ Compliant
   - Plan includes src/main.py (GitHub Actions) and src/cli.py (local development)
   - Commands specified: generate, preview, config, cache (matches constitution)

3. **Data Privacy** (Principle III): ✅ Compliant - NON-NEGOTIABLE
   - FR-025 mandates public repositories only
   - T107 implements privacy check
   - Constitution principle strictly enforced

4. **Testability** (Principle IV): ⚠️ REQUIRES ADJUSTMENT
   - Constitution mandates >80% coverage for core modules
   - Current tasks.md defers all tests to Phase 9 (T109-T113)
   - **ACTION REQUIRED**: Restructure tasks to pair tests with implementation (see tasks.md updates)

5. **Observable** (Principle V): ✅ Compliant
   - T020 implements logging utility
   - T029 adds error logging with timestamps and context
   - Constitution logging requirements met

## Project Structure

### Documentation (this feature)

```text
specs/001-stats-spark/
├── plan.md              # This file (/speckit.plan command output)
├── spec.md              # Feature specification
├── research.md          # Phase 0 output (technology decisions)
├── data-model.md        # Phase 1 output (entity models)
├── quickstart.md        # Phase 1 output (user guide)
├── contracts/           # Phase 1 output (API schemas if needed)
└── checklists/          # Quality validation checklists
    └── requirements.md
```

### Source Code (repository root)

```text
stats-spark/
├── src/
│   ├── __init__.py
│   ├── spark/                      # Core package
│   │   ├── __init__.py
│   │   ├── fetcher.py              # GitHub API interactions
│   │   ├── calculator.py           # Statistics calculations
│   │   ├── visualizer.py           # SVG generation coordinator
│   │   ├── cache.py                # 6-hour cache management
│   │   ├── config.py               # YAML configuration loading
│   │   └── themes/
│   │       ├── __init__.py
│   │       ├── spark_dark.py       # Default theme
│   │       ├── spark_light.py      # Light theme
│   │       └── custom.py           # Custom theme loader
│   ├── main.py                     # Entry point for GitHub Actions
│   └── cli.py                      # CLI interface for local use
│
├── output/                         # Generated SVG files
│   ├── .gitkeep                    # Ensure directory exists
│   └── README.md                   # Usage instructions
│
├── config/
│   ├── spark.yml                   # Main configuration
│   └── themes.yml                  # Theme definitions
│
├── .cache/                         # API response cache (gitignored)
│
├── tests/
│   ├── unit/
│   │   ├── test_calculator.py      # Spark Score, streaks logic
│   │   ├── test_cache.py           # Cache TTL logic
│   │   ├── test_config.py          # YAML parsing
│   │   └── test_visualizer.py      # SVG generation
│   ├── integration/
│   │   ├── test_fetcher.py         # GitHub API interactions
│   │   └── test_end_to_end.py      # Full workflow test
│   └── fixtures/
│       ├── sample_user_data.json   # Mock GitHub responses
│       └── sample_config.yml       # Test configurations
│
├── .github/
│   └── workflows/
│       └── generate-stats.yml      # Scheduled + manual trigger
│
├── docs/
│   ├── getting-started.md
│   ├── configuration.md
│   ├── embedding-guide.md          # Profile README instructions
│   └── api-reference.md
│
├── assets/
│   ├── logo.svg                    # Stats Spark logo
│   └── examples/                   # Example outputs
│       └── markhazleton/           # Demo account examples
│
├── requirements.txt                # Production dependencies
├── requirements-dev.txt            # Development dependencies
├── setup.py                        # Package installation
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
└── .gitignore
```

**Structure Decision**: Single Python application structure chosen because Stats Spark is a standalone statistics generator with no separate frontend/backend. All functionality is contained in a single Python package (`spark`) with clear module separation for API fetching, calculations, and visualization.

## Complexity Tracking

> **Not applicable** - No constitution violations. This is the foundational project that will inform the constitution.

## Phase 0: Research & Technology Decisions

### Research Tasks

1. **Python SVG Generation Libraries**
   - **Decision**: Research best library for programmatic SVG creation
   - **Options**: svgwrite, drawSvg, svgutils
   - **Criteria**: Ease of use, text rendering, gradient/effects support, WCAG compliance

2. **GitHub API Best Practices**
   - **Decision**: Determine optimal PyGithub usage patterns
   - **Focus**: Rate limit handling, pagination, caching strategies, authentication
   - **Reference**: GitHub REST API v3 documentation

3. **Cache Storage Strategy**
   - **Decision**: File-based vs in-memory cache for 6-hour TTL
   - **Consideration**: GitHub Actions ephemeral environment, cache persistence between runs
   - **Approach**: Simple JSON file cache with timestamp validation

4. **Spark Score Calculation Algorithm**
   - **Decision**: Define precise formulas for consistency, commit volume, collaboration scores
   - **Weights**: 40% consistency, 35% commit volume, 25% collaboration
   - **Normalization**: 0-100 scale calculation methodology

5. **Time Pattern Analysis**
   - **Decision**: Hour categorization for night owl/early bird detection
   - **Thresholds**: Night owl hours (22-4), early bird hours (5-9), balanced otherwise
   - **Statistical approach**: Weighted hour distribution analysis

6. **GitHub Actions Workflow Configuration**
   - **Decision**: Cron schedule, manual trigger setup, secret management
   - **Permissions**: Required GitHub token scopes (read:user, repo)
   - **Error handling**: Workflow failure notifications, retry strategy

7. **SVG Rendering Optimization**
   - **Decision**: Performance techniques for complex visualizations
   - **Considerations**: File size, browser compatibility, mobile rendering
   - **Constraints**: GitHub README rendering limitations

### Output Artifact

**File**: `research.md`

**Contents**:
- Technology selection rationale for each decision
- Alternatives considered and why rejected
- Best practices identified for GitHub API usage
- Spark Score formula specification with examples
- SVG generation patterns and WCAG compliance approach
- GitHub Actions workflow configuration details

## Phase 1: Design & Contracts

### Data Model (`data-model.md`)

**Entities to Model**:

1. **UserProfile** - GitHub user metadata
   - username, total_repos, total_commits, join_date, collaboration_score

2. **Commit** - Individual commit record
   - sha, timestamp, repo_name, message, language

3. **Repository** - Repository metadata
   - name, language, stars, forks, commit_count, last_activity

4. **LanguageStats** - Aggregated language usage
   - language_name, percentage, commit_count, lines_of_code

5. **TimePattern** - Temporal analysis
   - hour_distribution, day_distribution, category (night_owl/early_bird/balanced)

6. **Streak** - Consecutive activity tracking
   - streak_type, current_length, longest_length, start_date, end_date

7. **SparkScore** - Overall activity metric
   - total_score, consistency_score, volume_score, collaboration_score, lightning_rating

8. **ThemeConfig** - Visualization styling
   - primary_color, accent_color, background_color, glow_enabled, gradient_enabled

9. **StatisticsOutput** - Generated artifact
   - category, file_path, generation_timestamp, theme_applied

### API Contracts (`contracts/`)

**GitHub API Integration Contract** (not a REST API we expose, but our usage of GitHub API):

```yaml
# contracts/github-api-usage.yml
github_api_endpoints:
  user_info:
    endpoint: GET /users/{username}
    rate_limit: 5000/hour
    cache_ttl: 6 hours

  user_repos:
    endpoint: GET /users/{username}/repos
    pagination: true
    max_pages: calculate_from_repo_limit
    rate_limit: 5000/hour
    cache_ttl: 6 hours

  repo_commits:
    endpoint: GET /repos/{owner}/{repo}/commits
    pagination: true
    max_commits: 100_per_repo
    rate_limit: 5000/hour
    cache_ttl: 6 hours

  repo_languages:
    endpoint: GET /repos/{owner}/{repo}/languages
    rate_limit: 5000/hour
    cache_ttl: 6 hours
```

**Configuration Schema Contract**:

```yaml
# contracts/spark-config-schema.yml
spark_config:
  version: string
  user: string  # Username or "auto"

stats:
  enabled:
    type: array
    items: [overview, heatmap, languages, fun, streaks]
    note: "5 output categories as defined in spec.md FR-002"
  thresholds:
    graveyard_months: integer
    starter_commits: integer
    power_user_commits: integer
    night_owl_hours: array[integer]
    early_bird_hours: array[integer]

visualization:
  theme: string  # spark-dark, spark-light, custom
  style: string  # electric, minimal, detailed
  outputs: array[string]
  effects:
    glow: boolean
    animations: boolean
    gradient: boolean

branding:
  show_logo: boolean
  show_powered_by: boolean
  custom_footer: string
```

### Quick Start Guide (`quickstart.md`)

**Sections**:
1. **Prerequisites** - GitHub account, repository fork, Personal Access Token
2. **5-Minute Setup** - Step-by-step workflow configuration
3. **Embedding Stats** - Markdown examples for profile README with `markhazleton` demo
4. **Customization** - Theme selection and statistics category configuration
5. **Troubleshooting** - Common issues and workflow logs

### Implementation Modules

**Core Modules to Implement** (details in `data-model.md`):

1. **fetcher.py** - GitHub API client
   - Class: `GitHubFetcher`
   - Methods: `fetch_user_profile()`, `fetch_repositories()`, `fetch_commits()`, `fetch_languages()`
   - Handles: Authentication, pagination, rate limiting, caching

2. **calculator.py** - Statistics computation
   - Class: `StatsCalculator`
   - Methods: `calculate_spark_score()`, `analyze_time_patterns()`, `calculate_streaks()`, `aggregate_languages()`
   - Implements: Weighted formulas, temporal analysis, streak logic

3. **visualizer.py** - SVG generation
   - Class: `StatisticsVisualizer`
   - Methods: `generate_overview()`, `generate_heatmap()`, `generate_languages()`, `generate_fun_stats()`, `generate_streaks()`
   - Handles: Theme application, WCAG compliance, layout

4. **cache.py** - Response caching
   - Class: `APICache`
   - Methods: `get()`, `set()`, `is_expired()`, `clear()`
   - Implements: 6-hour TTL, JSON file storage

5. **config.py** - Configuration management
   - Class: `SparkConfig`
   - Methods: `load()`, `validate()`, `get_theme()`
   - Handles: YAML parsing, schema validation, defaults

6. **themes/*.py** - Theme definitions
   - Classes: `SparkDarkTheme`, `SparkLightTheme`, `CustomTheme`
   - Properties: Colors, effects, layout parameters

7. **main.py** - GitHub Actions entry point
   - Function: `main()`
   - Flow: Load config → Fetch data → Calculate stats → Generate SVGs → Output files

8. **cli.py** - Command-line interface
   - Commands: `generate`, `preview`, `config`, `validate`
   - Enables: Local testing, theme preview, configuration validation

## Phase 2: Task Decomposition

**Not included in this plan** - Phase 2 is handled by the `/speckit.tasks` command, which will:
- Break down implementation into specific coding tasks
- Order tasks by dependencies
- Assign priorities based on user story rankings
- Generate `tasks.md` with actionable items

Tasks will be generated after this plan is approved and will cover:
- Setting up project structure and dependencies
- Implementing core modules (fetcher, calculator, visualizer)
- Creating GitHub Actions workflow
- Writing unit and integration tests
- Generating documentation and examples
- Creating demo with markhazleton account

## Next Steps

1. **Review & Approve Plan** - Validate technical approach and structure
2. **Phase 0 Execution** - Research agents will populate `research.md` with technology decisions
3. **Phase 1 Execution** - Generate `data-model.md`, `contracts/`, and `quickstart.md`
4. **Ready for Tasks** - Run `/speckit.tasks` to generate implementation task list

---

**Plan Status**: ✅ Ready for Phase 0 Research
**Estimated Completion**: Plan generated 2025-12-28
