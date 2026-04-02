# Research: Dashboard Visual Enhancements

**Feature**: 001-dashboard-visual-enhancements  
**Date**: 2026-04-02

## Research Tasks & Findings

### R1: Daily Commit Data Availability

**Question**: The spec assumes daily commit timestamps exist for the heatmap and timeline. What data is actually available?

**Finding**: `commits_by_day` (a `Dict[str, int]` mapping `"YYYY-MM-DD"` → count) is already calculated in `calculator.py` line 59-64 from per-repo commit lists fetched via `repo.get_commits()`. It is used for SVG heatmap generation (`unified_report_workflow.py` line 491) but **not persisted** in `data/repositories.json`.

**Decision**: Persist `commits_by_day` as a new top-level field in `repositories.json` under `profile` or as a separate `activity_calendar` key. This requires zero additional API calls — the data is already computed.

**Rationale**: This is the lowest-cost path. The calculator already iterates all commits and groups by day. We just need to serialize the result into the JSON output.

**Alternatives considered**:
- GitHub Events API (`/users/{username}/events`): Only 90 days, would lose full-year coverage
- Per-repo `stats/commit_activity`: Would add 1 API call per repo (50-500 extra calls)

---

### R2: Chart Library — Chart.js, Not Recharts

**Question**: The spec references Recharts (FR-011). What does the frontend actually use?

**Finding**: The frontend uses **Chart.js 4.5.1** via `react-chartjs-2 5.3.1`. There is no Recharts dependency. All existing charts (BarChart, LineGraph, PieChart, ScatterPlot) use Chart.js.

**Decision**: All new chart components must use Chart.js / react-chartjs-2. The spec's reference to Recharts is incorrect and should be treated as "existing chart library."

**Rationale**: Consistency with existing codebase; no justification for a second chart library.

**Calendar heatmap**: Chart.js has a `chartjs-chart-matrix` plugin that can render calendar heatmaps. Alternatively, a custom SVG/CSS grid component (no library needed) can produce a GitHub-style heatmap with ~100 lines of JSX. This avoids adding any dependency.

---

### R3: Export Functionality — Already Exists

**Question**: US4 describes one-click CSV/JSON export. Does it exist?

**Finding**: `ExportButton.jsx` already supports both CSV and JSON export with 30+ fields including commit history, PR summaries, security alerts, and tech stack. It's integrated into `RepositoryTable`.

**Decision**: US4 is **already implemented**. Mark as pre-existing in the plan. Consider minor enhancements (export from visualizations view, or adding new fields to export) but no new component needed.

**Rationale**: No work needed for core functionality. If new fields (commit volume, bus factor) are added to data, they should also be added to the export column definitions.

---

### R4: Dark Mode Implementation Strategy

**Question**: How should the manual toggle integrate with existing OS-preference dark mode?

**Finding**: The frontend already has comprehensive dark mode CSS via `@media (prefers-color-scheme: dark)` blocks in `global.css` and component CSS files. CSS custom properties (`:root` and dark overrides) are already defined for all colors.

**Decision**: Implement a `ThemeContext` React context that:
1. On first load, reads localStorage for saved preference; if absent, reads `prefers-color-scheme`
2. Applies a `data-theme="dark"` or `data-theme="light"` attribute on `<html>`
3. Refactor existing `@media (prefers-color-scheme: dark)` blocks to `[data-theme="dark"]` selectors
4. Toggle button sets localStorage and updates the attribute

**Rationale**: This is the standard pattern for persistent dark mode with system-preference fallback. The CSS variables are already defined — we just change the trigger from media query to data attribute.

---

### R5: GitHub Contributor Stats API for Bus Factor

**Question**: What API endpoint provides per-contributor commit counts?

**Finding**: `GET /repos/{owner}/{repo}/stats/contributors` returns an array of contributors with weekly commit counts. PyGithub exposes this via `repo.get_stats_contributors()`. Returns `StatsContributor` objects with `.total` (total commits) and `.weeks[]` (weekly breakdown).

**Decision**: Add a `fetch_contributor_stats()` method to `fetcher.py` that calls this endpoint. Cache the result using the existing pushed_at strategy. Calculate bus factor in `calculator.py` as: sort contributors by total commits descending, find minimum count where cumulative commits >= 50% of total.

**Rationale**: 1 API call per repo, cacheable, provides exact data needed. For 50 repos = 50 additional calls, well within 5000/hr budget.

**Rate limit concern**: The `/stats/contributors` endpoint may return 202 (computing) on first call. Must handle this with a retry (already standard for PyGithub stats endpoints).

---

### R6: Commit Volume Metrics (Additions/Deletions)

**Question**: How to get per-repo total additions/deletions?

**Finding**: The `/stats/contributors` endpoint (same as R5) returns per-contributor weekly additions/deletions. Alternatively, `repo.get_stats_code_frequency()` returns weekly aggregate additions/deletions for the entire repo.

**Decision**: Use `repo.get_stats_code_frequency()` — it's a single call per repo returning weekly `[timestamp, additions, deletions]` tuples. Sum across all weeks for totals. This can share the same cache entry and API call batch as contributor stats.

**Rationale**: Simpler than iterating individual commits. One call per repo. Weekly granularity is sufficient for aggregate totals.

**Alternatives considered**:
- `repo.get_commits()` with `stat` expansion: Too expensive (1 call per commit)
- GraphQL API: Would require parallel implementation alongside existing REST; unjustified for this scope

---

### R7: Calendar Heatmap Rendering Approach

**Question**: Should we use a library or build a custom component for the heatmap?

**Finding**: Options evaluated:
1. `chartjs-chart-matrix` plugin: Adds matrix chart type to Chart.js; can render heatmap-like grids
2. `react-calendar-heatmap`: Lightweight (~5KB), purpose-built for GitHub-style heatmaps
3. Custom CSS Grid/SVG component: ~80-120 lines of JSX, no dependency

**Decision**: Build a custom CSS Grid component. The GitHub-style calendar heatmap is a 7-row × 53-column grid of colored squares with tooltips. Chart.js matrix plugin is overkill and doesn't produce the right visual. A custom component gives exact control over the GitHub-familiar appearance with zero dependencies.

**Rationale**: Avoids adding any new dependency (constitution principle: "prefer standard library solutions over external packages"). The component is simple: map 365 date objects to colored cells using CSS Grid, with a Tooltip component (already exists in Common/).

---

## Summary of Spec Corrections Needed

| Spec Claim | Reality | Action |
|------------|---------|--------|
| FR-011: "Recharts + React 19" | Chart.js + react-chartjs-2 | Plan uses Chart.js |
| US4: Export is new | ExportButton.jsx already exists | US4 marked as enhancement-only |
| Assumption: commit timestamps in JSON | Only window aggregates | Persist `commits_by_day` from calculator |
| Schema version 2.0.0 → 2.1.0 | Currently 2.2.0 | Increment to 2.3.0 |
| Assumption: Recharts heatmap | Chart.js ecosystem | Custom CSS Grid component (no library) |
