# Stats Spark Constitution

## Core Principles

### I. Python-First

Core functionality MUST be implemented as importable Python modules with clear separation of concerns. All business logic (data fetching, calculations, visualizations) MUST be testable independently of GitHub Actions workflow. Each module MUST have a single, well-defined responsibility:

- `fetcher.py` - GitHub API interactions only
- `calculator.py` - Statistics calculations only
- `visualizer.py` - SVG generation only
- `cache.py` - API response caching only
- `config.py` - Configuration management only

### II. CLI Interface

All functionality MUST be accessible via command-line interface for local testing and GitHub Actions execution. The CLI MUST support:

- `spark generate --user <username>` - Generate statistics for a specific user
- `spark preview --theme <theme>` - Preview theme without API calls
- `spark config --validate` - Validate configuration syntax
- `spark cache --clear` - Clear cached API responses

Entry points: `src/main.py` (GitHub Actions) and `src/cli.py` (local development)

### III. Data Privacy (NON-NEGOTIABLE)

System MUST ONLY process public repositories. Private repository data MUST be explicitly filtered out, even if the GitHub token provides access. No user credentials, tokens, or private activity data MUST ever be persisted to cache or output files. Privacy violations are grounds for immediate rejection.

### IV. Testability

Unit tests MUST cover all calculation logic (Spark Score, streaks, time patterns) with predictable inputs/outputs. Integration tests MUST validate GitHub API interactions with mock data. Test fixtures MUST be provided in `tests/fixtures/` for consistent testing:

- `sample_user_data.json` - Mock GitHub API responses
- `sample_config.yml` - Test configurations
- Coverage target: >80% for core modules (calculator, visualizer, cache)

### V. Observable

All operations MUST log to stdout/stderr for GitHub Actions workflow debugging. Error messages MUST include timestamps, context, and actionable guidance (e.g., "GitHub token expired - update repository secret GITHUB_TOKEN"). Cache hits/misses, API rate limit status, and generation progress MUST be logged. No silent failures allowed.

## Performance & Scalability Standards

**API Rate Limiting**:

- MUST implement 6-hour cache TTL for all GitHub API responses
- MUST support force-refresh flag to bypass cache when needed
- MUST handle rate limit errors with exponential backoff (1s, 2s, 4s, 8s)
- MUST limit repository processing to top 500 by default (configurable via `spark.yml`)

**Execution Time**:

- Statistics generation MUST complete in <5 minutes for users with <500 repositories
- SVG file size MUST NOT exceed 500KB per visualization
- Heatmap generation MUST NOT load more than 365 days of commit data

**Accuracy**:

- Statistics MUST have <1% discrepancy vs GitHub native insights
- Spark Score calculation MUST be deterministic (same input = same output)
- Language percentages MUST sum to 100% ± 0.1% (rounding tolerance)

## Configuration & Customization

**YAML-Based Configuration**:

- `config/spark.yml` - Main configuration (user, enabled stats, repository limit)
- `config/themes.yml` - Theme definitions (colors, effects, layout)
- Configuration validation MUST occur before API calls to fail fast

**Documentation Organization**:

- ALL markdown documentation files MUST be placed in `/documentation` folder
- Only exception: Root-level `README.md` for repository overview
- Generated analysis reports (SVGs, JSON) go to `output/` and `data/` directories
- This organization ensures clean project structure and prevents documentation sprawl

**Theme Requirements**:

- All themes MUST maintain WCAG AA contrast compliance (4.5:1 for text)
- Built-in themes: `spark-dark` (default), `spark-light`
- Custom themes MUST validate color hex codes and required fields

**Selective Statistics**:

- Users MUST be able to enable/disable individual categories: overview, heatmap, languages, fun, streaks
- Only enabled categories MUST be processed (no wasted API calls)

## Governance

**Constitution Compliance**:

- All pull requests MUST verify alignment with these principles
- Violations MUST be documented and justified before merge
- Privacy violations (III. Data Privacy) MUST NOT be merged under any circumstances

**Complexity Justification**:

- New dependencies MUST be justified (does it replace significant custom code?)
- Abstractions MUST solve real problems (no premature optimization)
- Configuration options MUST have clear use cases (avoid feature creep)

**Demo Account**:

- The `markhazleton` GitHub account is the canonical demo/test user
- All documentation examples MUST use this account for consistency
- Generated examples in `assets/examples/markhazleton/` MUST be kept current

**Version Management**:

- Follow semantic versioning: MAJOR.MINOR.PATCH
- Breaking config changes = MAJOR version bump
- New statistics categories = MINOR version bump
- Bug fixes and optimizations = PATCH version bump

**Development Guidance**:

- Use `docs/spec/001-stats-spark/plan.md` as the technical reference
- Use `docs/spec/001-stats-spark/spec.md` for user-facing requirements
- Use `docs/spec/001-stats-spark/tasks.md` for implementation order

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
