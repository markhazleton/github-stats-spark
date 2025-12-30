# Feature Specification: Unified Profile Report

**Feature Branch**: `001-unified-profile-report`
**Created**: 2025-12-30
**Status**: Draft
**Input**: User description: "consolidate the 2 different output into a single comprehensive overview report that includes both a user profile summary AND the analysis of each public repository for the user, this will create all the .svg for the profile and a single /output/report/ that is not dated for the user i.e. markhazleton-analysis.md this will all be updated in the weekly job generate-stats.yml. The markhazleton-analysis.md will have all the .svg files AND the full top 50 repository report in a markdown format that can be linked from their user profile page."

## Clarifications

### Session 2025-12-30

- Q: When the weekly workflow fails (e.g., GitHub API timeout, rate limit, network error), how should the system respond? → A: Retry automatically up to 3 times with exponential backoff (1 min, 5 min, 15 min delays), then alert on final failure
- Q: The unified report will combine profile SVGs and repository analysis. What should be the overall section structure and ordering? → A: Header/Metadata → Profile Overview (with embedded SVGs) → Top 50 Repository Analysis → Footer

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Automated Weekly Profile Report Generation (Priority: P1)

A GitHub user wants an automated, comprehensive profile report that combines visual statistics and detailed repository analysis into a single, up-to-date markdown file that can be embedded in their profile README.

**Why this priority**: This is the core value proposition - consolidating two separate output workflows into one automated process. Delivers immediate value by creating a linkable, comprehensive profile report without manual intervention.

**Independent Test**: Can be fully tested by triggering the weekly workflow and verifying that a single, non-dated markdown report is generated in `/output/reports/` containing both embedded SVG references and the top 50 repository analysis. Success is measured by the presence and completeness of the unified report file.

**Acceptance Scenarios**:

1. **Given** the weekly workflow runs on Sunday at midnight UTC, **When** the workflow completes successfully, **Then** a unified report file named `{username}-analysis.md` exists in `/output/reports/` with current data
2. **Given** a unified report exists from a previous run, **When** the weekly workflow runs again, **Then** the existing report is overwritten with updated statistics and repository rankings
3. **Given** the workflow generates all SVG files, **When** the unified report is created, **Then** the report includes markdown image references to all six SVG files (overview, heatmap, languages, fun, streaks, release)
4. **Given** repository analysis is complete, **When** the unified report is generated, **Then** the report includes ranked analysis of the top 50 repositories with scores, metrics, and technology stack information

---

### User Story 2 - Embedded SVG Visualizations in Report (Priority: P2)

A user wants to view visual statistics (SVGs) directly within their comprehensive markdown report without navigating to separate files or directories.

**Why this priority**: Enhances user experience by providing a self-contained report that combines visual and textual information. Supports the goal of creating a linkable profile page with all relevant information in one place.

**Independent Test**: Can be tested by opening the generated markdown report in a markdown viewer and verifying that all six SVG visualizations render inline within the document structure. Success is measured by visual verification and proper markdown image syntax.

**Acceptance Scenarios**:

1. **Given** all SVG files are generated successfully, **When** the unified report is created, **Then** each SVG is referenced using relative path markdown image syntax that works when the report is viewed from the repository
2. **Given** a user views the markdown report on GitHub, **When** they scroll through the report, **Then** all SVG visualizations display inline without broken image links
3. **Given** SVG files are organized in `/output/`, **When** the report references them, **Then** the relative paths correctly point to `../overview.svg`, `../heatmap.svg`, etc.

---

### User Story 3 - Repository Analysis Integration (Priority: P1)

A user wants to see detailed analysis of their top 50 repositories, including rankings, technology stacks, and quality metrics, as part of their unified profile report.

**Why this priority**: This is essential functionality that provides the "analysis" component of the consolidation. Without this, the report would only contain SVGs without deeper insights.

**Independent Test**: Can be tested by verifying that the unified report contains a structured section with the top 50 repositories, each showing composite score, ranking position, technology stack, activity metrics, and quality indicators. Success is measured by completeness and accuracy of repository data.

**Acceptance Scenarios**:

1. **Given** a user has more than 50 public repositories, **When** the unified report is generated, **Then** exactly the top 50 repositories ranked by composite score are included in the analysis section
2. **Given** repository analysis includes technology stack detection, **When** a repository analysis is displayed, **Then** the report shows identified technologies with currency indicators (current, needs update, outdated)
3. **Given** repositories have varying activity levels, **When** the report ranks repositories, **Then** the composite score reflects the configured weights (popularity 30%, activity 45%, health 25%)
4. **Given** AI summarization is available, **When** generating repository analysis, **Then** summaries are included for repositories where summarization succeeds, with graceful fallback to template-based descriptions when AI is unavailable

---

### User Story 4 - Manual and Workflow-Triggered Generation (Priority: P3)

A developer wants to trigger unified report generation both manually (on-demand) and automatically through the weekly workflow to support both testing and production use cases.

**Why this priority**: Provides flexibility for development, testing, and debugging. Lower priority than core functionality but important for operational workflows.

**Independent Test**: Can be tested by manually running the generation command and verifying output matches workflow-generated output. Can also be tested by triggering the workflow via `workflow_dispatch` and confirming the same unified report is produced.

**Acceptance Scenarios**:

1. **Given** a developer wants to test changes locally, **When** they run the unified report generation command manually, **Then** the report is generated with the same structure and content as the automated workflow produces
2. **Given** the workflow is triggered manually via GitHub Actions, **When** the workflow completes, **Then** the unified report is generated and committed to the repository
3. **Given** multiple trigger mechanisms exist (manual, scheduled, push events), **When** any trigger executes the workflow, **Then** the unified report generation produces consistent output regardless of trigger type

---

### Edge Cases

- **What happens when SVG generation fails?** The unified report should still be generated with repository analysis, but include a notice where SVG visualizations would appear indicating which visualizations failed to generate.

- **What happens when repository analysis fails for some repositories?** The report should include successfully analyzed repositories and note any repositories that failed analysis without blocking the entire report generation.

- **What happens when a user has fewer than 50 public repositories?** The report should include all available repositories (e.g., if only 20 exist, show all 20) without errors or padding.

- **What happens when the user has no public repositories?** The report should generate with profile summary and SVG visualizations only, with a note that no repositories were available for analysis.

- **What happens when GitHub API rate limits are hit?** The system should handle rate limit errors gracefully by implementing automatic retry with exponential backoff (1 minute, 5 minutes, 15 minutes delays) up to 3 attempts. If all retries fail, the workflow should log a clear error message indicating rate limit exhaustion and rely on the next scheduled weekly run for recovery.

- **What happens to existing dated reports?** Existing dated reports (e.g., `markhazleton-analysis-20251230.md`) should remain untouched. Only the non-dated unified report (`markhazleton-analysis.md`) should be created/updated.

- **What happens when the report is viewed outside the repository context?** Image references should work correctly when the markdown is viewed on GitHub profile pages, in repository browsers, and in local markdown viewers.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST generate a single, non-dated unified report file named `{username}-analysis.md` in the `/output/reports/` directory for each user profile analyzed

- **FR-002**: System MUST preserve all existing dated report files (e.g., `{username}-analysis-{YYYYMMDD}.md`) when generating the unified report - only the non-dated file should be overwritten

- **FR-003**: System MUST include references to all six SVG visualization files (overview, heatmap, languages, fun, streaks, release) within the unified report using proper markdown image syntax with relative paths

- **FR-004**: System MUST include analysis of the top 50 public repositories ranked by composite score in the unified report, or all available repositories if fewer than 50 exist

- **FR-005**: System MUST structure the unified report in the following order: (1) Header with metadata (username, generation date, report version), (2) Profile Overview section with all six embedded SVG visualizations, (3) Top 50 Repository Analysis section with ranked repositories and detailed metrics, (4) Footer with generation information and data sources

- **FR-006**: System MUST calculate composite scores for repository ranking using the configured weights: popularity (30%), activity (45%), and health (25%)

- **FR-007**: System MUST include technology stack information for each analyzed repository, showing detected dependencies and currency status (current, needs update, outdated)

- **FR-008**: System MUST execute unified report generation as part of the weekly scheduled workflow (Sunday midnight UTC)

- **FR-009**: System MUST support manual triggering of unified report generation through both command-line interface and GitHub Actions workflow_dispatch

- **FR-010**: System MUST commit only the non-dated unified report file (`{username}-analysis.md`) and SVG files to the repository after successful generation

- **FR-011**: System MUST handle partial failures gracefully - if SVG generation fails, the report should still be created with repository analysis and a notice about missing visualizations

- **FR-012**: System MUST handle repository analysis failures for individual repositories without blocking the entire report generation - include successfully analyzed repositories and note failures

- **FR-013**: System MUST use AI-powered summarization for repository descriptions when available, with automatic fallback to template-based descriptions when AI services are unavailable or fail

- **FR-014**: System MUST log all generation steps, errors, and warnings to support troubleshooting and monitoring of the automated workflow

- **FR-015**: Unified report MUST be viewable and render correctly on GitHub profile pages, repository browsers, and local markdown viewers with all SVG images displaying properly

- **FR-016**: System MUST implement automatic retry with exponential backoff (1 minute, 5 minutes, 15 minutes) for workflow failures, attempting up to 3 retries before final failure and logging appropriate error messages at each retry attempt

- **FR-017**: System MUST organize SVG visualizations within the Profile Overview section in a logical grouping: overview dashboard first, followed by activity visualizations (heatmap, streaks, release), then detailed breakdowns (languages, fun stats)

### Key Entities

- **Unified Profile Report**: A single markdown document structured in four main sections: (1) Header with metadata (username, generation timestamp, report version), (2) Profile Overview with all six embedded SVG visualizations in logical grouping (overview dashboard, activity visualizations, detailed breakdowns), (3) Top 50 Repository Analysis with ranked repositories and detailed metrics, (4) Footer with generation information and data sources. Replaces the current dual-output system (separate SVGs + dated reports).

- **Repository Analysis Record**: Detailed analysis data for a single repository including composite score, ranking position, technology stack, activity metrics (commits, recency), popularity metrics (stars, forks, watchers), health indicators (documentation, maturity, issues), and optional AI-generated summary. Ordered by composite score in the unified report.

- **SVG Visualization Set**: Collection of six visualization files (overview, heatmap, languages, fun, streaks, release) that provide graphical representation of user statistics. Referenced from the unified report via relative paths and displayed inline.

- **Technology Stack Profile**: Aggregated view of dependencies and technologies used across repositories, including language distribution, framework usage, and currency status. Derived from dependency file analysis across multiple package ecosystems (npm, pypi, rubygems, go, maven, nuget).

- **Composite Repository Score**: Calculated ranking metric combining popularity (30%), activity (45%), and health (25%) dimensions to determine the top 50 repositories for inclusion in the unified report.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can access a single, comprehensive profile report at a consistent URL path (`/output/reports/{username}-analysis.md`) that is automatically updated weekly without manual intervention

- **SC-002**: The unified report generation workflow completes within 10 minutes for users with up to 200 public repositories under normal GitHub API conditions

- **SC-003**: 100% of successfully generated SVG visualizations render correctly inline within the unified markdown report when viewed on GitHub

- **SC-004**: The top 50 repository analysis section includes complete data (composite score, technology stack, metrics) for at least 95% of analyzed repositories, with clear error notices for any failures

- **SC-005**: The weekly automated workflow produces a unified report with zero manual intervention required - from generation to repository commit

- **SC-006**: Users can link to the unified report from their GitHub profile README, and all content (text, SVGs, formatting) displays correctly without broken references

- **SC-007**: Report generation handles GitHub API rate limiting gracefully, completing successfully on retry within the weekly schedule window even under rate limit conditions

- **SC-008**: The unified report provides value for users with any number of repositories - from 1 to 200+ - by adapting content to show all available repositories when fewer than 50 exist

## Assumptions *(optional)*

- **ASM-001**: Users have a valid GitHub API token with appropriate permissions to access repository data, commit history, and dependency files

- **ASM-002**: The repository already has infrastructure for SVG generation and repository analysis - this feature consolidates existing capabilities rather than building from scratch

- **ASM-003**: The weekly workflow schedule (Sunday midnight UTC) is acceptable for the target user base and does not need to be configurable per user

- **ASM-004**: Relative path references to SVG files (`../overview.svg`) will work correctly when the unified report is viewed in standard GitHub contexts (profile README, repository browser)

- **ASM-005**: The existing composite scoring algorithm (popularity 30%, activity 45%, health 25%) is considered appropriate and does not require changes as part of this consolidation

- **ASM-006**: GitHub API rate limits are sufficient to analyze up to 50 repositories, generate SVGs, and commit results within a single weekly workflow execution for typical users

- **ASM-007**: The AI summarization service (Claude Haiku) is available for enhanced repository descriptions, but the system can operate successfully with template-based fallbacks when AI is unavailable

- **ASM-008**: Users are comfortable with the unified report overwriting on each weekly run (non-dated) while dated historical reports remain available for archival purposes

- **ASM-009**: The `/output/reports/` directory structure is acceptable for hosting the unified report alongside existing dated reports

- **ASM-010**: Markdown rendering engines used by GitHub, VSCode, and other common viewers support inline SVG image references using standard markdown image syntax

## Dependencies & Constraints *(optional)*

### External Dependencies

- **GitHub API**: Required for fetching user profile data, repository information, commit history, and dependency files. Subject to rate limiting (5,000 requests/hour for authenticated requests).

- **Anthropic Claude API**: Optional dependency for AI-powered repository summarization. System must function with graceful degradation when unavailable.

- **GitHub Actions Environment**: Workflow execution depends on GitHub-hosted runners, Python 3.11 availability, and pip package installation.

### Internal Dependencies

- **Existing SVG Generation System**: The unified report relies on the current `StatisticsVisualizer` to produce the six SVG files that will be embedded in the report.

- **Repository Analysis Pipeline**: The unified report depends on `RepositoryRanker`, `RepositorySummarizer`, and `RepositoryDependencyAnalyzer` to generate repository analysis data.

- **Configuration System**: Report generation parameters (top N repositories, ranking weights, enabled visualizations) are controlled by `config/spark.yml`.

### Constraints

- **GitHub API Rate Limits**: Must complete all API calls for a user's profile and up to 50 repositories within rate limit constraints (typically 5,000 requests/hour).

- **Workflow Execution Time**: GitHub Actions has a maximum job execution time of 6 hours, but practical completion target is under 10 minutes for responsiveness.

- **File Size Constraints**: Generated markdown reports should remain under 1MB to ensure fast loading and reasonable git repository size growth.

- **Backward Compatibility**: Existing dated reports must remain functional and unchanged. The new unified report is additive, not destructive.

- **Markdown Compatibility**: Report format must be compatible with GitHub-flavored markdown to ensure proper rendering on GitHub profile pages and repository views.

## Out of Scope *(optional)*

- **Historical Trend Analysis**: Tracking changes in statistics or repository rankings over time across multiple report generations. The unified report reflects current state only.

- **Multi-User Support in Single Workflow**: The workflow processes one user at a time. Batch processing of multiple users is not included.

- **Custom Report Templates**: Users cannot customize the structure, styling, or content organization of the unified report. The format is standardized.

- **Interactive Visualizations**: SVGs are static images. No interactive charts, drill-downs, or dynamic filtering capabilities are included.

- **Notification System**: No alerts, emails, or notifications when the unified report is generated or updated. Users must check the repository for updates.

- **Report Versioning**: No version history or diff capabilities for the unified report itself. Git history provides the only tracking of changes.

- **Custom Ranking Algorithms**: The composite scoring weights (popularity 30%, activity 45%, health 25%) are fixed. Users cannot define custom ranking criteria.

- **Private Repository Analysis**: Only public repositories are analyzed. Private repository support is not included.

- **PDF or HTML Export**: The unified report is markdown only. No alternative output formats are provided.

- **Real-Time Updates**: Reports are generated on a weekly schedule only. No real-time or on-commit updates.
