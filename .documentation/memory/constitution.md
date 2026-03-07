# Stats Spark Constitution

## Purpose

This constitution defines **architectural principles and non-negotiable boundaries** for the Stats Spark project. It guides decision-making without prescribing implementation details.

---

## Core Principles

### I. Single Responsibility

Each module MUST have one well-defined purpose. Business logic MUST be testable independently of infrastructure (GitHub Actions, CLI, caching). When a module does "too much," split it.

### II. Data Privacy (NON-NEGOTIABLE)

- System MUST ONLY process **public repositories**
- Private repository data MUST be explicitly filtered, even if token provides access
- No credentials, tokens, or private activity data MUST persist to cache or output
- **Privacy violations are grounds for immediate rejection—no exceptions**

### III. Fail Fast, Fail Loud

- Validate configuration before expensive operations (API calls, file generation)
- All errors MUST include context and actionable guidance
- No silent failures—operations log to stdout/stderr with timestamps
- Rate limit handling MUST use exponential backoff

### IV. Change-Driven Caching

- Cache invalidation MUST be content-addressed (based on data change, not time)
- Repository data invalidates when `pushed_at` timestamp changes
- Unchanged data MUST NOT trigger API calls
- Force-refresh flag MUST bypass cache when explicitly requested

### V. Accessibility First

- All visual output MUST meet WCAG AA contrast compliance (4.5:1 for text)
- Themes MUST validate color requirements before generation
- No accessibility regressions allowed

---

## Quality Gates

| Metric | Requirement |
|--------|-------------|
| **Test Coverage** | >80% for core calculation and visualization modules |
| **Execution Time** | <5 minutes for users with <500 repositories |
| **Accuracy** | <1% discrepancy vs GitHub native insights |
| **Determinism** | Same input MUST produce same output |
| **SVG Size** | <500KB per visualization |

---

## Boundaries

### What We Process
- Public repositories only
- Repositories owned by or contributed to by the specified user
- Maximum 500 repositories per run (configurable)
- Maximum 365 days of commit history for heatmaps

### What We Never Do
- Process private repository data
- Store API tokens or credentials in output
- Fail silently without logging
- Make API calls for unchanged data
- Merge code that violates privacy principles

---

## Governance

### Dependency Decisions
- New dependencies MUST replace significant custom code OR provide critical functionality
- Prefer standard library solutions over external packages
- Abstractions MUST solve demonstrated problems (no premature optimization)

### Configuration Philosophy
- Configuration options MUST have clear, documented use cases
- Defaults MUST work for 90% of users without modification
- Invalid configuration MUST fail before any processing begins

### Documentation Standards
- Documentation lives in `/documentation` (exception: root `README.md`)
- Generated outputs go to `output/` and `data/`
- Examples use canonical demo account: `markhazleton`

### Versioning
- **MAJOR**: Breaking configuration or output format changes
- **MINOR**: New features, new statistics categories
- **PATCH**: Bug fixes, performance improvements

---

## The Constitution Test

Before merging code, ask:

1. **Privacy**: Does this touch private repository data? → If yes, reject
2. **Testability**: Can this be unit tested without external services? → If no, refactor
3. **Observability**: Does failure produce actionable error messages? → If no, improve
4. **Efficiency**: Does this avoid unnecessary API calls? → If no, add caching
5. **Accessibility**: Does visual output meet WCAG AA? → If no, fix colors

---

*Last Amended: 2026-01-26*
