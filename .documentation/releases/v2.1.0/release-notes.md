# Release Notes: v2.1.0

## Release Metadata

| Field | Value |
|-------|-------|
| **Version** | v2.1.0 |
| **Release Date** | 2026-04-19 |
| **Previous Version** | 2.0.0 |
| **Commits** | 235 |
| **Contributors** | 2 (Mark Hazleton, github-actions[bot]) |
| **Merged PRs** | 1 (#2) |

## Highlights

Stats Spark v2.1.0 delivers three major capability areas on top of the 2.0.0 interactive dashboard foundation:

**Schema 2.2.0 Repository Enrichment** — every repository record in `repositories.json` now carries additive `pull_request_summary` and `security_summary` payloads, attention ranking fields (`attention_score`, `attention_rank`, `attention_metrics`), and dependency version coverage metadata. These are purely additive; pre-2.2.0 data files continue to load without errors.

**Change-Based Smart Caching** — the previous time-based TTL cache has been replaced by a content-addressed system keyed on repository `pushed_at` timestamps. Repositories with no new commits since the last run skip all expensive processing. Typical daily runs that touch only a handful of active repos complete in under one minute (down from ~5 minutes), with API calls reduced 80–95%.

**Cross-Platform Reliability** — all datetime operations now use explicit `timezone.utc`, eliminating the `offset-naive / offset-aware` errors on Windows CI and GitHub Actions. Chart series rendering for release cadence and weekly diversity has been stabilized, and cache refresh now consistently populates SVG and dashboard analytics.

## New Features

### Schema 2.2.0 Repository Enrichment

- Attention ranking fields: `attention_score`, `attention_rank`, `attention_metrics` — surfaces repositories needing the most maintenance attention with a dedicated frontend Needs Attention page.
- Repository enrichment payloads: `pull_request_summary` (compact open PR signals) and `security_summary` (alert counts and posture) added to every unified output record.
- Explicit availability semantics (`available`, `partial`, `unavailable`) with reason codes on enrichment objects.
- Dependency version coverage metadata added to `tech_stack` (known-version and registry-resolution coverage).
- Staged GitHub REST API version rollout controls in `config/spark.yml` (`github.api_version.*`).

### Schema 2.3.0 Dashboard Visual Enhancements (in-progress, spec `001`)

- Interactive contribution heatmap calendar (trailing 365 days, custom CSS Grid) sourced from `profile.activity_calendar`.
- Multi-series activity timeline chart (weekly commits + active repos over 52 weeks) sourced from `profile.weekly_activity`.
- Dark mode toggle (light / dark / system) with `localStorage` persistence and `prefers-color-scheme` fallback via `ThemeContext`.
- Commit volume metrics per repository: `total_additions`, `total_deletions`, `code_churn`.
- Bus factor indicator: integer with color-coded health badge (`critical` / `warning` / `healthy`).
- Export enhancements: `ExportButton` CSV/JSON includes all new 2.3.0 fields.
- New backend methods: `fetch_contributor_stats()`, `fetch_code_frequency()` in `fetcher.py`; `calculate_bus_factor()` in `calculator.py`.
- Dashboard markdown rendering for AI-generated summaries via `react-markdown` + `remark-gfm`.

### Change-Based Smart Caching

- `pushed_at`-keyed content-addressed cache replaces time-based TTL.
- Metadata (stars, forks) updated in ~2 seconds for unchanged repos; full processing only when new commits detected.
- `--max-repos` flag for quick cache validation during development.
- Automatic removal of archived/private repositories from cache.

## Changed

- Unified data assembly emits additive enrichment objects for every repository record.
- Unified workflow logs staged API-version decision state; warns when runtime budget exceeds 5 minutes.
- Frontend detail views render GitHub-flavored markdown summaries.
- Frontend repository detail views surface dependency version coverage from `tech_stack`.
- Cache key format uses ISO week for organizational purposes only (not expiration).
- All datetime operations use timezone-aware UTC timestamps.

## Bug Fixes

- Release cadence and weekly repository diversity charts handle nested/cached commit-history shapes correctly.
- Commit activity heatmap, streak calculations, time-pattern analysis, and Lightning Round stats share the same normalized commit timestamp path.
- Cache refresh treats `commits_stats` as a first-class refresh category.
- Cross-platform datetime: handles `Z` suffix, `+00:00`, and naive ISO 8601 timestamps uniformly.
- Stale repository list cache cleared before freshness checks.
- Eliminated redundant commit fetching and tech stack analysis.

## Removed

- **Version Checker Module** (`src/spark/dependencies/version_checker.py`, 271 lines) — out of scope for a reporting tool; Dependabot/Renovate cover this use case.
- Removed fields from `DependencyStatus` and `RepositoryDependencyReport` related to version currency.

## Deferred Features

- **`001-dashboard-visual-enhancements`** (schema 2.3.0): Full implementation spec in progress — planned for next release cycle.

## Performance

| Metric | Before | After |
|--------|--------|-------|
| Typical daily run (few changed repos) | ~5 min | <1 min |
| API calls (no new commits) | 100% | 5–20% |
| Cache hit rate | ~50% | ~95% |

## Upgrade Guide

No breaking changes. Existing `repositories.json` files (pre-2.2.0) load without errors — new fields render as empty states when absent. Update with:

```bash
spark unified --user USERNAME
```

## Metrics

| Metric | Value |
|--------|-------|
| Features Delivered | 3 major areas |
| Bugs Fixed | 6 |
| PRs Merged | 1 |
| ADRs Created | 0 |
| Contributors | 2 |
| Commits | 235 |

---

*Release documentation generated by /devspark.release v2.1.0 — 2026-04-19*
