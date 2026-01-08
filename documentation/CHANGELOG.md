# Changelog

All notable changes to Stats Spark will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Change-Based Smart Caching**: Revolutionary caching system that eliminates time-based expiration
  - Compares repository `pushed_at` timestamps with cache timestamps
  - Only updates repositories when actual commits are detected
  - Updates metadata (stars, forks) in 2.1 seconds when no changes detected (was ~870 seconds)
  - **400x faster** for typical daily checks with no repository updates
  - Automatic removal of archived/private repositories from cache
  - Full backward compatibility with existing workflows
- **Testing Parameter**: `--max-repos` flag for quick cache validation with limited repositories
  - Useful for debugging and testing cache logic
  - Example: `spark unified --user USERNAME --max-repos 2`

### Changed
- **Removed TTL-Based Expiration**: Cache never expires based on time, only on actual repository changes
- **Intelligent Metadata Updates**: Lightweight metadata (stars, forks, pushed_at) updated separately from expensive processing
- Cache key format uses ISO week (`YYYYWWW`) for organizational purposes only (not expiration)
- `UnifiedDataGenerator.generate()` checks for repository changes before processing
- All datetime operations use timezone-aware UTC timestamps for cross-platform compatibility

### Fixed
- **Cross-Platform DateTime**: Fixed timezone handling to work on both Windows CLI and GitHub Actions (Linux)
- **Stale Repository List**: Repository list cache now cleared before freshness checks
- **Duplicate Processing**: Eliminated redundant commit fetching and tech stack analysis
  - All datetime operations now explicitly use `timezone.utc`
  - Handles multiple ISO 8601 timestamp formats (Z suffix, +00:00, naive)
  - No more `TypeError: can't subtract offset-naive and offset-aware datetimes`
  - Comprehensive cross-platform tests added

### Performance
- Typical weekly runs: <1 minute (was ~5 minutes) for repositories with few updates
- API calls reduced by 80-95% when most repositories are unchanged
- Cache hit rate improved from ~50% to ~95% for stable repositories

## [2.0.0] - 2026-01-02

### Added - Interactive Dashboard

#### Frontend Features
- **Repository Comparison View**: Side-by-side comparison of up to 5 repositories with color-coded metric highlighting
  - Green highlighting for highest values
  - Red highlighting for lowest values
  - Percentage difference calculations from maximum
  - Remove individual repositories from comparison
  - Clear all selections
- **Interactive Visualizations**: Three chart types using Recharts
  - Bar charts for metric comparison (top 50 repositories)
  - Line graphs for temporal trend analysis
  - Scatter plots for correlation visualization (commits vs. commit size)
  - Metric selection controls (commits, stars, forks, sizes, dates)
  - Click-to-drill-down on all chart elements
- **Repository Table**: Sortable, filterable table with all metrics
  - Click column headers to sort (ascending/descending)
  - Language filter dropdown
  - Checkbox multi-select for comparison
  - Row click for drill-down details
- **Drill-Down Details**: Comprehensive repository analysis modal
  - Commit history timeline (90d, 180d, 365d activity)
  - Language breakdown with percentages
  - Technology stack and dependency analysis
  - AI-generated summaries (when enabled)
  - Next/Previous navigation through repositories
- **Export Functionality**: Download data as CSV or JSON
  - Client-side generation (no server required)
  - Timestamped filenames
  - Works with filtered/sorted data
  - Integrated into table and comparison views
- **Responsive Design**: Mobile-friendly interface
  - CSS Modules for scoped styling
  - CSS custom properties for theming
  - Smooth animations and transitions
  - Breakpoints for mobile, tablet, desktop

#### Backend Features
- **Unified Data Generator** (`src/spark/unified_data_generator.py`):
  - Combines generate, analyze, and dashboard commands into single workflow
  - Generates comprehensive `repositories.json` (schema 2.0.0)
  - Includes commit metrics (avg, largest, smallest commits)
  - Tech stack analysis with dependency tracking
  - AI summaries (optional, when ANTHROPIC_API_KEY provided)
  - Repository ranking with composite scores
- **Enhanced Data Models**:
  - `DashboardData`, `DashboardRepository`, `DashboardMetadata` models
  - Nested structures: `commit_history`, `commit_metrics`, `tech_stack`, `summary`
  - First commit date tracking
  - Enhanced commit statistics
- **CLI Enhancements**:
  - `--dashboard` flag for unified data generation
  - `--force-refresh` to bypass cache
  - Progress logging with percentage completion
  - Error recovery with partial results

#### Build & Deployment
- **GitHub Actions Workflow**: Automated build and deployment
  - Python data generation step
  - Node.js setup and npm install
  - Frontend build (Vite)
  - Deployment to GitHub Pages (`/docs` directory)
  - Build verification checks
- **Vite Configuration**:
  - Base path: `/github-stats-spark/` for GitHub Pages
  - Output to `../docs` for deployment
  - Path aliases (`@/` → `src/`)
  - Custom middleware for `/data` serving in development
  - Postbuild script to copy data files

#### Developer Experience
- **Component Architecture**: 11 React components organized by feature
  - Common: LoadingState, Tooltip, FilterControls, ExportButton, ErrorBoundary
  - RepositoryTable: Table, Header, Row
  - Visualizations: Bar, Line, Scatter, Controls
  - Comparison: Selector, View
  - DrillDown: RepositoryDetail
- **Custom Hooks**: Reusable logic for data and UI state
  - `useRepositoryData`: Data fetching with loading/error states
  - `useTableSort`: Sorting and filtering logic
- **Services**: Utility modules for data operations
  - `dataService.js`: Data fetching and parsing
  - `metricsCalculator.js`: Chart transformations, formatting, comparisons
- **Error Handling**: ErrorBoundary component for graceful error recovery
- **Accessibility**: WCAG AA compliance
  - ARIA labels on interactive elements
  - Keyboard navigation (Tab, Enter, ESC)
  - Screen reader compatible
  - Focus management in modals

### Changed
- Updated GitHub Actions workflow to include frontend build steps
- Enhanced caching strategy for faster CI/CD
- Improved error messages with context for debugging

### Fixed
- Duplicate imports in ComparisonView component
- CSS nesting issues in component modules
- ESLint configuration for React 19 compatibility

### Performance
- React.memo optimization for table rows (100+ rows)
- useMemo for expensive chart transformations
- useCallback for event handlers
- Code splitting ready (React.lazy support)
- Optimized bundle sizes (tree-shaking, minification)

### Documentation
- Added `frontend/README.md` with setup instructions
- Updated main README.md with dashboard feature overview
- Added JSDoc comments to all React components
- Created implementation review document

## [1.0.0] - Previous Release

### Added
- **.NET/NuGet Support**: Added dependency analysis for .NET projects
  - Parses `.csproj` files (SDK-style projects for .NET Core/.NET 5+)
  - Detects .NET SDK version from `TargetFramework`
  - Checks NuGet package versions against api.nuget.org
  - Supports NuGet package currency assessment
- **Enhanced Date Display**: Repository reports now show "days ago" for dates
  - Created date with days since creation
  - Last modified (pushed) date with days since last commit
  - Special formatting for "today" and "yesterday"
- **Additional Repository Statistics**: Enriched reports with objective quality and activity metrics
  - **Tier 1 Quick Enhancement**: Contributors count, repository size (MB/KB), number of languages
  - **Quality Focus**: CI/CD detection (GitHub Actions), has tests directory, has LICENSE file, has documentation
  - **Activity Focus**: Release count, latest release date with days ago, commit velocity (commits/month)
  - Visual indicators with emojis for easy scanning

## [2.0.0] - 2025-12-29

### Added - AI-Powered Repository Analysis

#### Core Features
- **Repository Analysis Command**: New `spark analyze` command for generating comprehensive repository analysis reports
- **Intelligent Ranking Algorithm**: Composite scoring system (30% popularity, 45% activity, 25% health) for ranking repositories
- **AI-Powered Summaries**: Integration with Anthropic Claude Haiku for generating technical repository summaries
- **Three-Tier Fallback Strategy**: AI summaries → Enhanced template → Basic template for maximum reliability
- **Developer Profile Analysis**: Automatic generation of overall developer profile with technology diversity and activity patterns
- **Technology Stack Currency**: Dependency version checking across 5+ package ecosystems (NPM, PyPI, RubyGems, Go, Maven)
- **Multi-Window Activity Analysis**: Time-decay scoring using 90d/180d/365d commit windows
- **GitHub-Flavored Markdown Reports**: Professional markdown reports with embedded statistics

#### Data Models
- `Repository` model with comprehensive statistics tracking
- `CommitHistory` model with time-windowed commit analysis
- `TechnologyStack` model for dependency tracking
- `RepositorySummary` model with AI and fallback summaries
- `UserProfile` model for developer analysis
- `Report` model for complete report generation

#### New Modules
- `src/spark/ranker.py`: Repository ranking with composite scoring algorithm
- `src/spark/summarizer.py`: AI-powered summary generation with fallbacks
- `src/spark/report_generator.py`: Markdown report generation
- `src/spark/dependencies/parser.py`: Multi-ecosystem dependency file parsing
- `src/spark/dependencies/version_checker.py`: Package registry API clients
- `src/spark/dependencies/analyzer.py`: Dependency currency assessment

#### CLI Enhancements
- `spark analyze --user <username>`: Generate full analysis report
- `spark analyze --list-only`: Dry-run mode to preview top repositories
- `spark analyze --top-n <N>`: Customize number of repositories analyzed
- `spark analyze --output <path>`: Specify custom output directory
- Progress indicators showing current repository and completion percentage
- Graceful error handling with actionable guidance

#### Testing
- 17 comprehensive integration tests covering all user stories
- Unit tests for ranking algorithm, dependency parsing, version checking
- Edge case validation (no repos, unrecognized languages, unparseable dependencies, archived repos)
- Performance validation (3-minute target for 50 repositories)
- Accuracy metrics validation (90% AI summary accuracy, 95% tech identification)

#### Documentation
- Comprehensive [analyze command guide](guides/analyze-command.md)
- Updated [README.md](../README.md) with feature overview
- [Getting started guide](guides/getting-started.md) with API key setup instructions
- Sample report in `output/reports/markhazleton-analysis-20251229.md`

#### Configuration
- New `analyzer` section in `config/spark.yml`
- Configurable ranking weights, AI provider, dependency ecosystems
- 7-day cache TTL for package registry responses
- Hybrid caching strategy (file-based + in-memory)

#### Dependencies Added
- `anthropic>=0.40.0`: Claude API client for AI summaries
- `tenacity>=9.0.0`: Retry logic with exponential backoff
- `packaging>=23.0`: Semantic version comparison
- `tomli>=2.0.0`: TOML parsing for Python dependency files

### Enhanced
- **Fun Stats Visualization**: Now includes 8 creative measurements with personality-driven achievements
  - Coding Time Personality (Night Owl, Early Bird, Daytime Coder)
  - Commit Velocity classifications
  - Repository Collection tiers
  - Language Diversity (Specialist to Polyglot)
  - Community Recognition (stars earned)
  - Account Longevity badges
  - Commit Milestones with achievement levels
  - Pattern Personality messages
- **Release Cadence**: Added weekly/monthly repository diversity sparklines
- **Privacy Filter**: Explicit public-only repository filtering (constitution compliance)
- **Performance**: Optimized caching and API rate limit handling

### Fixed
- Improved error handling for GitHub API rate limits
- Enhanced fallback strategies for missing data
- Better handling of archived and forked repositories

### Performance
- Repository analysis completes in <3 minutes for 50 repositories
- 80-90% cache hit rate for dependency version checks
- Intelligent parallel processing for AI summaries
- Optimized GitHub API usage with 6-hour cache TTL

### Constitution Compliance
- ✅ Python-First: All modules independently importable
- ✅ CLI Interface: Full CLI access for local testing
- ✅ Data Privacy: Explicit public-only repository filter
- ✅ Testability: >80% test coverage for core modules
- ✅ Observable: Progress tracking and detailed logging
- ✅ Performance: Meets <3-minute performance target
- ✅ Configuration: YAML-based with environment overrides

## [1.0.0] - 2024-12-28

### Added - Initial Release
- **SVG Visualizations**: 6 beautiful SVG categories (overview, heatmap, languages, fun, streaks, release)
- **Spark Score**: Unique 0-100 metric combining consistency, volume, and collaboration
- **GitHub Actions Integration**: Fully automated daily generation at midnight UTC
- **Theme Support**: Dark, light, and custom themes with WCAG AA compliance
- **Local CLI**: `spark generate` command for local testing
- **Intelligent Caching**: 6-hour TTL with automatic cache invalidation
- **Rate Limit Handling**: Automatic retry logic for GitHub API limits
- **Selective Output**: Choose which statistics categories to generate
- **Configuration System**: YAML-based configuration with sensible defaults

### Documentation
- Getting started guide
- Configuration guide
- Embedding guide
- API reference for developers

---

## Version History

- **2.0.0** (2025-12-29): AI-Powered Repository Analysis feature
- **1.0.0** (2024-12-28): Initial release with SVG visualizations

[Unreleased]: https://github.com/markhazleton/github-stats-spark/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/markhazleton/github-stats-spark/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/markhazleton/github-stats-spark/releases/tag/v1.0.0
