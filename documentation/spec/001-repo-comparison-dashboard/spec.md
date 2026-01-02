# Feature Specification: Repository Comparison Dashboard

**Feature Branch**: `001-repo-comparison-dashboard`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "create a table of all public repos with columns for language, first commit, last commit, total commits, average commit size, biggest commit, smallest commit, then create world class visualization of the table with the ability to sort, graph and compare different repos for a given user"

## Clarifications

### Session 2025-12-31

- Q: How should repository data be updated on the published GitHub Pages site? → A: Automated on-demand updates - Updates whenever user pushes to repository
- Q: Should the dashboard support analyzing multiple GitHub users or just a single configured user? → A: Single user only - Dashboard is configured for one GitHub username and shows only that user's repositories
- Q: What specific immersive/interactive features should the dashboard include beyond table, charts, and comparisons? → A: Enhanced interactivity - Add animations, drill-down details, responsive tooltips, smooth transitions
- Q: What additional repository details should be shown in the drill-down view? → A: Everything in the current analyze and weekly job, all that we got in a very compelling user interface
- Q: What should be the GitHub Pages URL structure for accessing the dashboard? → A: username.github.io/github-stats-spark

### Session 2026-01-01

- Folder Structure Decision: Rename current `/docs` folder to `/documentation` (for specifications) and use `/docs` as the GitHub Pages publishing directory (for generated static files)
- Q: Which JavaScript framework/library should power the interactive dashboard? → A: React - Component-based library with extensive data visualization ecosystem
- Q: Which build tool should be used to bundle and optimize the React application into single site.js and site.css files? → A: Vite - Modern build tool optimized for speed with excellent React support
- Q: How should repository data be made available to the React frontend in the static GitHub Pages deployment? → A: JSON data file - Generate separate data.json file fetched by React at runtime
- Q: Which CSS approach should be used for styling the React components to produce optimized site.css? → A: CSS Modules - Scoped CSS files with automatic class name hashing
- Q: Which React data visualization library should be used for rendering the interactive charts (bar chart, line graph, scatter plot)? → A: Recharts

## User Scenarios & Testing *(mandatory)*

### User Story 1 - View Repository Overview Table (Priority: P1)

A user wants to see a comprehensive table displaying all their public repositories with key metrics to understand their development patterns and repository characteristics at a glance.

**Why this priority**: This is the foundational feature that provides essential data visibility. Without this, users cannot access any repository comparison functionality. It delivers immediate value by consolidating repository statistics that would otherwise require manual aggregation.

**Independent Test**: Can be fully tested by loading a user profile and verifying that all public repositories are displayed with accurate metrics in a tabular format. Delivers value as a standalone repository analytics tool.

**Acceptance Scenarios**:

1. **Given** a user with multiple public repositories, **When** they view the repository table, **Then** all public repositories are listed with language, first commit date, last commit date, total commits, average commit size, biggest commit, and smallest commit
2. **Given** a user with repositories in different programming languages, **When** viewing the table, **Then** each repository displays its primary programming language accurately
3. **Given** a repository with commit history, **When** commit size metrics are calculated, **Then** average, biggest, and smallest commit sizes reflect actual changes (files changed, lines added/deleted)
4. **Given** a user with no public repositories, **When** viewing the table, **Then** an appropriate message indicates no repositories are available

---

### User Story 2 - Sort and Filter Repository Data (Priority: P2)

A user wants to sort repositories by different metrics and filter the table to focus on specific subsets of their repositories for targeted analysis.

**Why this priority**: Sorting and filtering transform raw data into actionable insights, enabling users to identify patterns like most active repositories, newest projects, or largest code changes. This builds on P1 by making the data explorable.

**Independent Test**: Can be tested by interacting with column headers to sort and using filter controls to narrow down the repository list. Delivers value as an interactive data exploration tool.

**Acceptance Scenarios**:

1. **Given** the repository table is displayed, **When** a user clicks on a column header (e.g., "Total Commits"), **Then** the table sorts by that column in ascending or descending order
2. **Given** repositories sorted by one metric, **When** the user clicks a different column header, **Then** the table re-sorts by the new metric
3. **Given** the repository table, **When** a user applies a language filter (e.g., "Python"), **Then** only repositories with that primary language are displayed
4. **Given** filtered results, **When** the user clears the filter, **Then** all repositories are displayed again
5. **Given** a large number of repositories, **When** sorting or filtering, **Then** the operation completes within 2 seconds

---

### User Story 3 - Visualize Repository Metrics (Priority: P3)

A user wants to see graphical representations of repository metrics to identify trends, outliers, and patterns across their development portfolio.

**Why this priority**: Visualizations provide intuitive understanding of complex data relationships that tables cannot easily convey. This enhances analytical capabilities but depends on having the base data (P1) and exploration features (P2) in place.

**Independent Test**: Can be tested by selecting visualization options and verifying that charts accurately represent the repository data. Delivers value as an analytics dashboard with visual insights.

**Acceptance Scenarios**:

1. **Given** repository data is available, **When** a user selects a chart type (e.g., bar chart, line graph, scatter plot), **Then** the selected visualization is displayed with repository metrics
2. **Given** a visualization is displayed, **When** a user hovers over data points, **Then** detailed metric values are shown in a tooltip
3. **Given** multiple repositories, **When** viewing a commit activity timeline, **Then** first and last commit dates are plotted showing repository lifespans
4. **Given** repositories with varying commit counts, **When** viewing a commit distribution chart, **Then** outliers (most/least active repositories) are clearly identifiable
5. **Given** a visualization, **When** a user applies filters or sorts, **Then** the chart updates to reflect the filtered/sorted dataset

---

### User Story 4 - Compare Repositories Side-by-Side (Priority: P4)

A user wants to select multiple repositories and compare their metrics side-by-side to understand differences in development patterns, activity levels, and code churn.

**Why this priority**: Direct comparison enables benchmarking and identifying best practices across projects. This is an advanced analytical feature that builds on all previous priorities.

**Independent Test**: Can be tested by selecting 2+ repositories and viewing a comparison view that highlights differences and similarities. Delivers value as a repository benchmarking tool.

**Acceptance Scenarios**:

1. **Given** the repository table, **When** a user selects two or more repositories (via checkboxes or multi-select), **Then** a comparison view is activated
2. **Given** repositories are selected for comparison, **When** viewing the comparison, **Then** metrics are displayed side-by-side in a format that highlights differences (e.g., color-coded values, percentage differences)
3. **Given** comparing repositories, **When** viewing commit size metrics, **Then** differences in average, biggest, and smallest commits are clearly visible
4. **Given** repositories with different activity patterns, **When** comparing commit timelines, **Then** relative activity levels over time are shown
5. **Given** multiple repositories selected, **When** a user deselects one, **Then** the comparison updates to reflect only the remaining selections
6. **Given** comparison mode is active, **When** a user selects more than 5 repositories, **Then** the system either limits to 5 or provides a clear warning about performance impact

---

### User Story 5 - Drill Down into Repository Details (Priority: P2)

A user wants to click on a repository in the table or visualization to see detailed information, commit history insights, and additional metrics not shown in the overview.

**Why this priority**: Drill-down capabilities transform the dashboard from a static report into an interactive exploration tool, enabling users to investigate interesting patterns they discover in the overview. This enhances analytical depth without cluttering the main view.

**Independent Test**: Can be tested by clicking on repository entries and verifying that a detailed view appears with expanded metrics and insights. Delivers value as an interactive detail-on-demand feature.

**Acceptance Scenarios**:

1. **Given** the repository table is displayed, **When** a user clicks on a repository row, **Then** a detailed view opens showing expanded commit history, language breakdown, and activity timeline
2. **Given** a visualization is displayed, **When** a user clicks on a data point representing a repository, **Then** the same detailed view opens for that repository
3. **Given** a repository detail view is open, **When** a user clicks a close button or presses ESC, **Then** the view closes with a smooth transition back to the main dashboard
4. **Given** a repository detail view, **When** displayed, **Then** it includes links to the actual GitHub repository and key commits (biggest, most recent)
5. **Given** multiple repositories, **When** viewing details for one, **Then** navigation controls allow moving to the next/previous repository without closing the detail view

---

### Edge Cases

- What happens when a repository has no commits (empty repository)?
- How does the system handle repositories with thousands of commits (performance and display)?
- What happens when GitHub API rate limits are reached during data collection?
- How does the system handle repositories with missing or incomplete metadata (e.g., no language detected)?
- What happens when commit size data cannot be calculated (e.g., API access restrictions)?
- How does the system display repositories with very long names or special characters?
- What happens when a user has hundreds of public repositories (pagination, performance)?
- How does the system handle repositories that have been archived or made private after initial data collection?
- What happens when comparing repositories with vastly different scales (e.g., 10 commits vs 10,000 commits)?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST retrieve all public repositories for a given GitHub user
- **FR-002**: System MUST calculate and display the primary programming language for each repository
- **FR-003**: System MUST retrieve and display the date of the first commit for each repository
- **FR-004**: System MUST retrieve and display the date of the most recent commit for each repository
- **FR-005**: System MUST calculate and display the total number of commits for each repository
- **FR-006**: System MUST calculate and display the average commit size (measured by files changed and lines modified)
- **FR-007**: System MUST identify and display the biggest commit by size for each repository
- **FR-008**: System MUST identify and display the smallest commit by size for each repository
- **FR-009**: System MUST present repository data in a tabular format with all specified columns
- **FR-010**: Users MUST be able to sort the table by any column (ascending or descending)
- **FR-011**: Users MUST be able to filter repositories by programming language
- **FR-012**: System MUST provide multiple visualization types for repository metrics using Recharts library (minimum: bar chart, line graph, scatter plot)
- **FR-013**: Users MUST be able to select which metrics to visualize
- **FR-014**: Users MUST be able to select multiple repositories for side-by-side comparison
- **FR-015**: System MUST display comparison data in a format that highlights differences between selected repositories
- **FR-016**: System MUST handle API rate limiting gracefully with appropriate user feedback
- **FR-017**: System MUST generate repository data as JSON file(s) during the Python data collection phase for consumption by the React frontend
- **FR-018**: Visualizations MUST update dynamically when filters or sorts are applied
- **FR-019**: System MUST handle repositories with missing data by displaying clear indicators (e.g., "N/A", "Unknown")
- **FR-020**: System MUST provide export functionality for table data in common formats (CSV, JSON)
- **FR-021**: System MUST generate static HTML pages suitable for GitHub Pages deployment using React as the frontend framework, built and optimized with Vite, styled using CSS Modules for scoped component styles
- **FR-022**: System MUST automatically regenerate and deploy dashboard content when repository changes are pushed via GitHub Actions workflow
- **FR-032**: Build process MUST produce single optimized site.js bundle containing all React application code and dependencies
- **FR-033**: Build process MUST produce single optimized site.css bundle containing all component styles from CSS Modules
- **FR-034**: Vite build configuration MUST enable code splitting, tree-shaking, and minification for optimal bundle size
- **FR-035**: GitHub Actions workflow MUST execute Python data collection, generate JSON data files, build React application with Vite, and deploy to GitHub Pages /docs directory
- **FR-023**: Dashboard MUST be accessible via a public GitHub Pages URL
- **FR-024**: System MUST be configurable to specify which single GitHub username to analyze
- **FR-025**: Dashboard MUST provide smooth visual transitions between different views (table, charts, comparison)
- **FR-026**: Interactive elements MUST include animations for state changes (sorting, filtering, selection)
- **FR-027**: Users MUST be able to drill down into repository details by clicking on table rows or chart elements
- **FR-028**: All data points MUST display detailed information via responsive tooltips on hover
- **FR-029**: Repository detail view MUST include all analysis content from the current weekly report including AI-generated summaries, technology breakdown, quality indicators, contributor metrics, and comprehensive statistics
- **FR-030**: Dashboard MUST integrate existing SVG visualizations (overview, heatmap, streaks, languages, fun stats, release patterns) from the current Stats Spark implementation
- **FR-031**: Dashboard MUST be accessible at the URL pattern username.github.io/github-stats-spark (e.g., markhazleton.github.io/github-stats-spark)

### Technical Architecture

#### Backend (Data Collection & Processing)

- Python 3.11+ with PyGithub for GitHub API interaction
- Executes during GitHub Actions workflow on repository push
- Generates structured JSON data files containing repository metrics, analysis, and visualizations
- Outputs to `/data` directory (source data, separate from build output)

#### Frontend (Interactive Dashboard)

- React 19 as the component-based UI framework
- Vite 7 for development server and production build optimization
- Recharts 3 for declarative, interactive data visualizations (bar charts, line graphs, scatter plots)
- CSS Modules for component-scoped styling with automatic class name hashing
- ESLint 9 with flat config for code quality
- Single-page application (SPA) that fetches JSON data at runtime

#### Build & Deployment Pipeline

1. GitHub Actions workflow triggered on push to main/feature branch
2. Python scripts collect GitHub data via API and generate JSON files to `/data` directory
3. Node.js/npm install frontend dependencies
4. Vite builds React application with optimizations:
   - Code splitting and tree-shaking to eliminate unused code
   - Minification and compression of JavaScript and CSS
   - Single optimized `site.js` bundle (all React components + libraries)
   - Single optimized `site.css` bundle (all CSS Modules combined)
   - Clears `/docs` directory (`emptyOutDir: true`)
5. Postbuild script copies `/data` to `/docs/data`
6. Build artifacts (HTML, JS, CSS) and data (JSON) deployed to `/docs` directory
7. GitHub Pages serves static content from `/docs` at username.github.io/github-stats-spark

#### Data Flow

- Python → `/data/repositories.json` (repository metrics, analysis, SVG visualizations)
- Development: Custom Vite middleware serves `/data` directory
- Production: Postbuild copies `/data` to `/docs/data`
- JSON files → React components (fetch at runtime from `/data/repositories.json`)
- User interactions → React state updates → Recharts re-renders → Smooth animations

### Key Entities

- **Repository**: Represents a GitHub public repository with attributes including name, primary language, creation date, last update date, commit history metadata
- **Commit Metrics**: Aggregated statistics for a repository including total commits, first commit timestamp, last commit timestamp, average commit size, largest commit size, smallest commit size
- **Commit Size**: Measurement of a single commit's impact, calculated from files changed, lines added, and lines deleted
- **User Profile**: GitHub user account whose public repositories are being analyzed, with attributes including profile overview statistics, activity dashboard, commit activity heatmaps, technology breakdown, and release patterns
- **Visualization Configuration**: User preferences for chart type, selected metrics, filtering criteria, and comparison selections
- **Repository Analysis**: Comprehensive AI-generated analysis including technical summary, quality indicators (license, docs), contributor count, language breakdown, creation/modification dates, stars, forks, and commit activity over time periods
- **SVG Visualization**: Generated graphics including overview statistics, commit heatmap, coding streaks, language distribution, fun statistics, and release cadence patterns
- **JSON Data Model**: Structured data files containing repository metrics, analysis results, and visualization data, generated by Python backend and consumed by React frontend
- **Build Artifact**: Optimized static assets produced by Vite including index.html, site.js (bundled JavaScript), site.css (bundled styles), and data JSON files

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can view all public repositories with complete metrics in under 5 seconds for accounts with up to 50 repositories
- **SC-002**: Sorting and filtering operations complete within 1 second for datasets with up to 100 repositories
- **SC-003**: Visualizations render within 2 seconds of selection for datasets with up to 100 repositories
- **SC-004**: Users can successfully compare 2-5 repositories side-by-side with metrics displayed clearly
- **SC-005**: System maintains accuracy of 100% for commit counts and timestamps compared to GitHub API data
- **SC-006**: 95% of users can identify their most active repository within 30 seconds of viewing the dashboard
- **SC-007**: Export functionality successfully generates downloadable files in under 3 seconds
- **SC-008**: System handles API rate limiting without data loss or user-facing errors in 100% of cases
- **SC-009**: Dashboard remains responsive and functional for users with up to 200 public repositories
- **SC-010**: Users can switch between table view, visualization view, and comparison view with transitions completing in under 1 second
- **SC-011**: Animations and transitions render at 60 frames per second on modern browsers for smooth visual experience
- **SC-012**: Repository detail drill-down views open within 500 milliseconds of user interaction
- **SC-013**: Tooltips appear within 200 milliseconds of hover and display accurate, formatted metric information
- **SC-014**: Production build produces optimized site.js bundle under 500KB (gzipped) for initial page load performance
- **SC-015**: Production build produces optimized site.css bundle under 100KB (gzipped) for fast styling delivery
- **SC-016**: Lighthouse performance score of 90+ for the deployed GitHub Pages dashboard
- **SC-017**: GitHub Actions build and deployment workflow completes within 5 minutes for standard updates

## Assumptions

- GitHub API access is available and rate limits are sufficient for typical usage patterns (5000 requests/hour for authenticated users)
- Commit size is measured by combining files changed, lines added, and lines deleted (not actual byte size of changes)
- "Fully immersive exploration" and "world class visualization" are interpreted as providing multiple interactive chart types with smooth animations, drill-down capabilities, responsive tooltips, fluid transitions, and intuitive controls that create an engaging user experience
- Primary programming language is determined by GitHub's language detection algorithm
- Users will primarily analyze their own repositories or specific GitHub users they are researching
- Repository data can be cached for reasonable periods (e.g., 1 hour) to balance freshness with performance
- The dashboard will be web-based and accessible via modern browsers (Chrome, Firefox, Safari, Edge - latest 2 versions)
- Users have basic familiarity with GitHub concepts (repositories, commits, programming languages)
- Empty repositories (no commits) are valid edge cases that should be handled gracefully
- The feature focuses on public repositories only; private repositories are out of scope
- Dashboard will be deployed to GitHub Pages as static content (HTML, CSS, JavaScript)
- Automated updates will be triggered via GitHub Actions workflow on repository push events
- Data collection and page generation occur during the GitHub Actions build process, not at runtime in the browser
- Dashboard is configured for a single GitHub username (e.g., "markhazleton") and users who want their own dashboard can fork the repository
- The configured username is set via configuration file or environment variable, not hardcoded
- Dashboard will be accessible at username.github.io/github-stats-spark following standard GitHub Pages project page conventions
- The repository name "github-stats-spark" will be used as the base path for all GitHub Pages URLs
- Frontend technology stack: React 18+ for UI components, Vite 5+ for build tooling, Recharts for data visualization, CSS Modules for styling
- Build process will combine and optimize all client libraries into single site.js and site.css bundles using Vite's Rollup-based production build
- Python backend generates JSON data files during GitHub Actions workflow; React frontend fetches and renders this data
- Node.js 18+ and npm 9+ are available in the GitHub Actions runner environment
- Modern browsers (Chrome, Firefox, Safari, Edge - latest 2 versions) support ES2020+ JavaScript features produced by Vite
- CSS Modules automatic class name hashing prevents style conflicts across components
- Vite's code splitting and tree-shaking eliminate unused code for optimal bundle sizes
- GitHub Pages serves static files with appropriate caching headers for performance

## Out of Scope

- Analysis of private repositories
- Modification or management of repositories (this is read-only analytics)
- Detailed code quality metrics beyond commit statistics
- Pull request, issue, or contributor analysis
- Real-time monitoring or alerts for repository changes
- Collaboration features or sharing of comparison reports
- Historical trend analysis requiring data storage beyond current snapshot
- Integration with non-GitHub version control systems
- Mobile native applications (web-responsive design is in scope)
