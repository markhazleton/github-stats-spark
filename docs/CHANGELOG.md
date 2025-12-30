# Changelog

All notable changes to Stats Spark will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
- Comprehensive [analyze command guide](docs/analyze-command.md)
- Updated [README.md](README.md) with feature overview
- [Getting started guide](docs/getting-started.md) with API key setup instructions
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
