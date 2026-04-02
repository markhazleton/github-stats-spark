# Feature Specification: Dashboard Visual Enhancements

**Feature Branch**: `001-dashboard-visual-enhancements`  
**Created**: 2026-04-02  
**Status**: Draft  
**Input**: User description: "Implement top recommendations from git-spark analysis — add interactive contribution heatmap calendar, multi-series timeline charts, author profile cards, dark mode toggle, commit size metrics, bus factor calculation, and CSV/JSON export. Supplement existing SVGs (valuable marketing assets), focus on quick wins with data already gathered via GitHub API with minor additions. Recognize GitHub API rate-limit constraints vs. local git reads."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Interactive Contribution Heatmap Calendar (Priority: P1)

A visitor to the GitHub Pages dashboard wants to see commit activity over the past year displayed as a GitHub-style calendar heatmap with color-coded intensity levels, so they can quickly understand the user's coding consistency and patterns.

**Why this priority**: The heatmap is the single most visually impactful element from git-spark. Commit timestamps are already collected in `commit_history` data. This is the highest-visibility, lowest-effort improvement.

**Independent Test**: Can be fully tested by loading the dashboard with existing `repositories.json` data and verifying the heatmap renders with correct dates, intensity levels, and tooltips.

**Acceptance Scenarios**:

1. **Given** a loaded dashboard with repository data, **When** the user views the profile section, **Then** a trailing-365-day calendar heatmap (7 rows × up to 53 columns) displays with color-coded cells representing daily commit counts across all repositories.
2. **Given** a heatmap cell for a specific date, **When** the user hovers over it, **Then** a tooltip shows the date and commit count for that day.
3. **Given** days with zero commits, **When** displayed in the heatmap, **Then** those cells appear in the lowest intensity color (not blank), maintaining the full calendar grid.

---

### User Story 2 - Multi-Series Activity Timeline (Priority: P1)

A visitor wants to see how repository activity has changed over time across multiple metrics (commits per week, active repositories per week) displayed as an interactive line/area chart with toggleable datasets.

**Why this priority**: Timeline charts provide the narrative context that static SVGs lack. Weekly commit counts and active-repo counts are derivable from existing `commit_history` and `pushed_at` timestamps already in `repositories.json`.

**Independent Test**: Can be tested by rendering the timeline component with sample data and verifying both series display, toggle on/off independently, and axis labels are correct.

**Acceptance Scenarios**:

1. **Given** the dashboard is loaded, **When** the user navigates to the visualizations section, **Then** a multi-series timeline chart displays weekly commit counts and active repository counts over the trailing 52 weeks.
2. **Given** both series are displayed, **When** the user clicks a legend item (e.g., "Active Repos"), **Then** that series toggles off and the chart rescales.
3. **Given** a point on the timeline, **When** the user hovers over it, **Then** a tooltip shows the week, commit count, and active repo count.

---

### User Story 3 - Dark Mode Toggle (Priority: P2)

A visitor using the dashboard at night or in a dark-themed environment wants to toggle between light and dark themes, with their preference persisted across visits.

**Why this priority**: Dark mode is a standard UX expectation and the project already defines `spark-dark` and `spark-light` themes in `config/themes.yml`. Implementation primarily involves CSS and a toggle component.

**Independent Test**: Can be tested by toggling the theme switch, verifying all dashboard sections adopt the new palette, and confirming the preference persists after page reload via localStorage.

**Acceptance Scenarios**:

1. **Given** the dashboard is loaded, **When** the user clicks the theme toggle, **Then** the entire dashboard switches between dark and light color schemes.
2. **Given** the user selected dark mode, **When** they reload the page, **Then** dark mode is still active (preference stored in localStorage).
3. **Given** no prior preference, **When** the dashboard loads, **Then** it respects the user's operating system dark/light preference via `prefers-color-scheme`.

---

### User Story 4 - One-Click Data Export (Priority: P2)

> **Note**: Core CSV and JSON export functionality already exists in `ExportButton.jsx`. This story covers extending the existing export with new fields (commit volume, bus factor) added by this feature.

A visitor or developer wants to download the repository data in CSV or JSON format directly from the dashboard, including newly added metrics, enabling further analysis in spreadsheets or other tools.

**Why this priority**: Export enhancement is a quick win — the export infrastructure exists and data is already in memory. Adding new fields to the existing export maintains feature parity as new metrics are introduced.

**Independent Test**: Can be tested by clicking the export button, verifying the downloaded file contains correct data, and validating CSV structure opens correctly in a spreadsheet application.

**Acceptance Scenarios**:

1. **Given** the dashboard is loaded with repository data, **When** the user clicks "Export JSON", **Then** a `repositories.json` file downloads containing all displayed repository data.
2. **Given** the dashboard is loaded, **When** the user clicks "Export CSV", **Then** a CSV file downloads with columns for repository name, language, stars, forks, commit count, Spark Score, and last updated date.
3. **Given** filters are applied in the table, **When** the user exports, **Then** only the currently visible/filtered repositories are included in the export.

---

### User Story 5 - Commit Size & Volume Metrics Display (Priority: P3)

A visitor wants to understand the scale of code changes across repositories — seeing total lines added/deleted and commit size classifications — to get a sense of development velocity.

**Why this priority**: Commit stats (additions/deletions) are available per-repository from the GitHub API via `repo.get_stats_contributors()` but require a minor data-gathering addition. This adds analytical depth that differentiates from basic star/fork counting.

**Independent Test**: Can be tested by verifying new metrics appear in the repository detail view and that aggregate totals display correctly in the profile summary.

**Acceptance Scenarios**:

1. **Given** commit stats have been gathered, **When** the user views a repository's detail panel, **Then** total lines added, lines deleted, and net lines changed are displayed.
2. **Given** aggregate commit stats are available, **When** the user views the profile overview, **Then** total code churn (additions + deletions) across all repositories is shown.
3. **Given** commit stats are unavailable for some repositories (API limits), **When** displayed, **Then** those repositories show "Stats not available" rather than zero counts.

---

### User Story 6 - Bus Factor Indicator (Priority: P3)

A visitor evaluating repository health wants to see a "bus factor" metric that indicates how many contributors account for the majority of commits, revealing knowledge concentration risk.

**Why this priority**: Contributor counts are already fetched. Calculating bus factor requires the GitHub contributor stats endpoint (1 call per repo), which provides per-contributor commit counts.

**Independent Test**: Can be tested by calculating bus factor for sample repositories with known contributor distributions and verifying the displayed value matches expected results.

**Acceptance Scenarios**:

1. **Given** a repository with contributor data, **When** the user views repository details, **Then** a bus factor indicator shows the minimum number of contributors responsible for 50% of commits.
2. **Given** a single-contributor repository, **When** the bus factor is displayed, **Then** it shows "1" with a visual warning indicator (e.g., red/orange badge).
3. **Given** a well-distributed repository (many active contributors), **When** the bus factor is displayed, **Then** it shows a higher number with a healthy indicator (e.g., green badge).

---

### Edge Cases

- What happens when the GitHub API rate limit prevents fetching commit stats for all repositories? The system gracefully degrades, showing available data and marking incomplete repositories.
- How does the heatmap handle users with zero commits in the analysis period? It renders a full empty calendar grid with the lowest intensity level.
- What happens when a repository has no contributor data? Bus factor displays as "N/A" rather than zero.
- How does the CSV export handle repositories with special characters in names or descriptions? Values are properly escaped per CSV RFC 4180.
- What if the user's browser has localStorage disabled? Dark mode defaults to system preference and does not persist, with no error shown.
- How does the timeline handle weeks where no data exists (user created account mid-year)? Those weeks show zero activity, maintaining a continuous x-axis.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Dashboard MUST render an interactive 52-week contribution heatmap calendar from existing commit timestamp data in `repositories.json`.
- **FR-002**: Dashboard MUST display a multi-series timeline chart showing weekly commit counts and active repository counts, with toggleable datasets.
- **FR-003**: Dashboard MUST include a persistent dark/light mode toggle that respects system preference as default and stores choice in localStorage.
- **FR-004**: Dashboard MUST provide one-click export of repository data in both JSON and CSV formats, respecting any active filters.
- **FR-005**: Python backend MUST gather per-repository commit stats (total additions, total deletions) from the GitHub API when available, with graceful fallback when rate-limited.
- **FR-006**: Dashboard MUST display commit volume metrics (lines added, lines deleted, net change) per repository and in aggregate.
- **FR-007**: Python backend MUST calculate a bus factor metric (minimum contributors for 50% of commits) per repository from available contributor/commit data.
- **FR-008**: Dashboard MUST display bus factor with color-coded health indicators (red/orange/green).
- **FR-009**: All new React visualizations MUST supplement, not replace, existing SVG outputs — SVGs continue to be generated and served as marketing assets.
- **FR-010**: New data fields MUST be added to the `repositories.json` schema in a backward-compatible manner (optional fields with sensible defaults).
- **FR-011**: All new dashboard components MUST work within the existing Chart.js + react-chartjs-2 architecture (React 19). The contribution heatmap uses a custom CSS Grid component requiring no new library.
- **FR-012**: Dark mode color palette MUST meet WCAG AA contrast requirements (4.5:1 ratio for text), drawing from existing `spark-dark` and `spark-light` theme definitions.

### Key Entities

- **CommitStats**: Per-repository aggregate of total additions, total deletions, and commit count with stats. Stored as optional fields on the repository object in `repositories.json`.
- **BusFactor**: Per-repository integer representing minimum contributors for 50% of commits, plus a health classification (critical/warning/healthy). Derived from contributor commit distribution.
- **WeeklyActivity**: Aggregated per-week summary of commit count and active repository count across all repositories, derived from commit timestamps. Used by the timeline chart.
- **DailyCommitCount**: Per-day commit count across all repositories for the trailing 365 days, used by the heatmap calendar. Derived from `activity_calendar` field persisted in `repositories.json` (sourced from `calculator.py` `commits_by_day` output).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Visitors can visually assess a full year of coding activity within 2 seconds of page load via the contribution heatmap.
- **SC-002**: The multi-series timeline allows users to identify activity trends across at least 52 weeks of data with interactive tooltips.
- **SC-003**: Theme toggle switches the entire dashboard appearance in under 200ms with no layout shift.
- **SC-004**: Users can export repository data to CSV and open it successfully in common spreadsheet applications (Excel, Google Sheets).
- **SC-005**: Commit volume metrics are populated for at least 80% of repositories within standard API rate limits (5000 requests/hour authenticated).
- **SC-006**: Bus factor is calculated for all repositories that have contributor data, with results matching manual verification within 1% tolerance.
- **SC-007**: All new visualizations render correctly on viewports from 768px to 2560px wide.
- **SC-008**: All new text elements in both themes meet WCAG AA contrast ratio (4.5:1).
- **SC-009**: Existing SVG generation pipeline is completely unaffected — all current SVGs remain identical before and after this feature.
- **SC-010**: The `spark unified` command completes within the existing 5-minute budget for under 500 repositories, with no more than 10% additional time from commit stats gathering.

## Assumptions

- The `commits_by_day` dictionary (mapping `"YYYY-MM-DD"` → count) is already computed by `calculator.py` from per-repo commit lists and used for SVG heatmap generation. It will be persisted to `repositories.json` as `activity_calendar` to power both the interactive heatmap and timeline charts without additional API calls.
- The GitHub API `GET /repos/{owner}/{repo}/stats/contributors` endpoint provides per-contributor weekly commit data, enabling bus factor calculation with 1 API call per repository.
- Commit stats (additions/deletions) can be gathered via GitHub stats endpoints or sampled from recent commits, staying within rate limits by leveraging the existing pushed_at-based cache strategy.
- The contribution heatmap will be implemented as a custom CSS Grid component (~100 lines JSX), avoiding any new frontend dependency. This aligns with the constitution's preference for standard solutions over external packages.
- Users primarily view the dashboard on desktop browsers; mobile responsiveness is desirable but not a primary target for this iteration.
- The existing `data/repositories.json` schema version can be incremented from 2.2.0 to 2.3.0 (minor, backward-compatible) to accommodate new optional fields.

## Constraints

- **GitHub API rate limits**: Unlike git-spark which reads local git history directly, this project operates through the GitHub REST API with 5000 requests/hour. New data gathering must fit within this budget alongside existing fetching. File-level analysis (hotspots, coupling, per-file churn) is explicitly out of scope because it would require per-commit diff API calls that exceed rate limits for profiles with hundreds of repositories.
- **No SVG replacement**: Existing SVG visualizations (overview, heatmap, languages, streaks, fun, release) are marketing assets embedded in GitHub README profiles and MUST NOT be modified or removed.
- **Minimal new dependencies**: Per the project constitution, new dependencies require justification. At most one new frontend dependency (calendar heatmap) may be added.
- **Schema backward compatibility**: Frontend must gracefully handle `repositories.json` files that lack the new optional fields (generated before this feature).
- **Performance budget**: The unified command must remain under 5 minutes for under 500 repositories. Any new API calls must be cached using the existing content-addressed cache strategy.
