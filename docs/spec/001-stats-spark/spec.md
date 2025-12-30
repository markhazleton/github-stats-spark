# Feature Specification: Stats Spark - GitHub Profile Statistics Generator

**Feature Branch**: `001-stats-spark`
**Created**: 2025-12-28
**Status**: Draft
**Input**: User description: "GitHub profile statistics generator with automated SVG visualizations, comprehensive coding analytics, and customizable themes - Stats Spark illuminates your GitHub activity with beautiful, automated statistics for your User GitHub Profile README.md"

## Clarifications

### Session 2025-12-28

- Q: When the workflow fails or produces unexpected results, how should users diagnose issues? → A: Basic logging with error details and timestamps to workflow output
- Q: How long should the system cache GitHub API data to reduce rate limiting and improve performance? → A: Cache for 6 hours with force-refresh option
- Q: What is the maximum number of repositories the system should process to prevent performance issues and excessive API calls? → A: Process top 500 most active repositories (configurable)
- Q: Should statistics include data from private repositories that the user has access to, or only public repositories? → A: Public repositories only - Excludes all private repo data for privacy
- Q: What should be the relative importance weights for calculating the Spark Score (0-100 scale)? → A: Balanced: 40% consistency, 35% commit volume, 25% collaboration
- Q: What GitHub account should be used for demo and testing? → A: markhazleton (repository owner)
- Q: Should the system include detailed setup instructions for embedding stats in GitHub profile README? → A: Yes, include step-by-step instructions in documentation

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Automated Daily Statistics Generation (Priority: P1)

As a GitHub user, I want my profile statistics to update automatically every day so that my GitHub profile always displays current information without manual intervention.

**Why this priority**: This is the core value proposition - automation. Without this, the tool is just a manual stat generator with limited value. This delivers immediate value by ensuring users never have outdated statistics.

**Independent Test**: Can be fully tested by setting up the GitHub Actions workflow, waiting for scheduled execution, and verifying that new SVG files are generated in the output directory with current date timestamps.

**Acceptance Scenarios**:

1. **Given** a user has forked the repository and configured their GitHub token, **When** the daily scheduled workflow runs at midnight UTC, **Then** all enabled statistics SVGs are regenerated with current data
2. **Given** a user manually triggers the workflow from the Actions tab, **When** the workflow completes, **Then** the output directory contains updated SVG files with timestamps showing the current generation time
3. **Given** the workflow runs successfully, **When** a user embeds the SVG URLs in their GitHub profile README, **Then** the latest statistics are displayed without requiring any manual updates

---

### User Story 2 - Comprehensive Statistics Dashboard (Priority: P1)

As a developer, I want to see a visual overview of my GitHub activity including commits, languages, timing patterns, and collaboration metrics so that I can understand my coding habits and showcase my work to potential employers or collaborators.

**Why this priority**: This is the primary user-facing feature that delivers the core value. Without comprehensive statistics, the tool doesn't fulfill its purpose of "illuminating GitHub activity."

**Independent Test**: Can be fully tested by running the stat generation for a test user account and verifying that the overview SVG contains all expected metrics (total commits, languages used, contribution patterns, collaboration stats) rendered correctly.

**Acceptance Scenarios**:

1. **Given** a user with diverse GitHub activity, **When** the overview SVG is generated, **Then** it displays commit totals, primary languages with percentages, contribution frequency, and star/fork counts
2. **Given** a user who codes at various times, **When** the timing pattern statistics are generated, **Then** the visualization shows peak coding hours and identifies user as "night owl," "early bird," or balanced
3. **Given** a user who collaborates on repositories, **When** social statistics are generated, **Then** the output shows repository count, collaboration metrics, and community engagement indicators
4. **Given** a new GitHub user with minimal activity, **When** statistics are generated, **Then** the system displays available data gracefully without errors and indicates "starter" status

---

### User Story 3 - Theme Customization (Priority: P2)

As a user concerned about visual consistency, I want to choose between dark, light, and custom themes for my statistics visualizations so that they match my GitHub profile's appearance and personal branding.

**Why this priority**: Visual customization is important for user satisfaction but the tool can deliver value with just the default theme. This enhances the product but isn't critical for MVP.

**Independent Test**: Can be fully tested by changing the theme setting in the configuration file, regenerating statistics, and verifying that the SVG files use the expected color scheme and styling.

**Acceptance Scenarios**:

1. **Given** a user configures theme as "spark-dark" in spark.yml, **When** statistics are generated, **Then** all SVG outputs use electric blue (#0EA5E9) and dark backgrounds with appropriate contrast
2. **Given** a user configures theme as "spark-light", **When** statistics are generated, **Then** all SVG outputs use bright backgrounds suitable for light mode profiles
3. **Given** a user defines custom colors in themes.yml, **When** statistics are generated with "custom" theme, **Then** SVG outputs apply the user-specified color scheme
4. **Given** a user enables visual effects (glow, gradient) in configuration, **When** statistics are generated, **Then** the SVG files include the specified visual enhancements

---

### User Story 4 - Selective Statistics Output (Priority: P2)

As a user with specific preferences, I want to enable or disable individual statistics categories (overview, heatmap, languages, fun stats) so that I only generate and display the visualizations that are relevant to my profile goals.

**Why this priority**: This provides user control and reduces processing time, but all statistics being enabled by default still delivers full value. This is an optimization and personalization feature.

**Independent Test**: Can be fully tested by modifying the enabled statistics list in spark.yml, running generation, and confirming that only specified statistics produce output files.

**Acceptance Scenarios**:

1. **Given** a user enables only "overview" and "languages" in spark.yml, **When** statistics are generated, **Then** only spark-overview.svg and spark-languages.svg are created in the output directory
2. **Given** a user disables "fun" statistics, **When** generation completes, **Then** spark-fun.svg is not created and no processing occurs for quirky metrics
3. **Given** a user enables all statistics categories, **When** generation completes, **Then** all SVG files (overview, heatmap, languages, fun, streaks) are present in the output directory

---

### User Story 5 - Local Preview and Testing (Priority: P3)

As a developer setting up Stats Spark, I want to run the statistics generator locally with a CLI tool so that I can preview different themes and validate my configuration before committing to the automated workflow.

**Why this priority**: This is a convenience feature for power users and developers. The GitHub Actions workflow can serve as the testing mechanism for most users, making this a nice-to-have enhancement.

**Independent Test**: Can be fully tested by running CLI commands like `spark generate --user username` and `spark preview --theme spark-dark` and verifying that local SVG files are generated correctly.

**Acceptance Scenarios**:

1. **Given** a user runs `spark generate --user testuser` locally, **When** the command completes, **Then** statistics for the specified user are generated in a local output directory
2. **Given** a user runs `spark preview --theme spark-light`, **When** the command completes, **Then** sample statistics are generated using the light theme for visual inspection
3. **Given** a user runs `spark config --set theme=custom`, **When** the configuration is updated, **Then** subsequent local generations use the custom theme

---

### User Story 6 - Profile README Setup Documentation (Priority: P2)

As a new user, I want clear step-by-step instructions for embedding the generated statistics in my GitHub profile README so that I can showcase my stats without guessing the correct markdown syntax or file URLs.

**Why this priority**: Documentation quality directly impacts user adoption. Without clear setup instructions, users may struggle with the final integration step, reducing the perceived value of the tool. This is important but not critical for MVP since technically-inclined users can figure it out.

**Independent Test**: Can be fully tested by following the documentation instructions from scratch with a fresh fork, and verifying that stats display correctly in the profile README without additional troubleshooting.

**Acceptance Scenarios**:

1. **Given** a user has completed the workflow setup, **When** they follow the README embedding instructions, **Then** they can successfully add statistics to their profile using the provided markdown examples
2. **Given** documentation includes the markhazleton account as a demo, **When** users view the example, **Then** they see a working reference implementation of embedded statistics
3. **Given** a user needs to customize their display, **When** they consult the documentation, **Then** they find instructions for selecting specific statistics categories and arranging multiple SVGs

---

### Edge Cases

- What happens when a GitHub user has no public repositories or commits? (System should display graceful message like "Start your coding journey!" rather than empty charts or errors)
- How does the system handle API rate limiting from GitHub? (See FR-013 and FR-022 for rate limiting and caching strategy)
- What happens when a repository is deleted or made private after being included in statistics? (Historical data should remain in stats but be marked as unavailable for current data)
- How does the system handle users with thousands of repositories? (System processes top 500 most active repositories by default; this limit is configurable via spark.yml for power users)
- What happens when a user's GitHub token expires or is revoked? (Workflow should fail gracefully with clear error message instructing user to update the token)
- How does the system handle timezone differences for "daily" updates? (Uses UTC midnight as documented, users can manually trigger anytime)
- What happens when commit messages contain special characters or extremely long text? (Should sanitize and truncate for SVG rendering)
- How does the system handle languages that GitHub doesn't recognize? (Should group as "Other" or skip if no detection available)
- What happens when a user has mostly private repositories? (System only processes public repositories; statistics reflect public activity only, protecting privacy of confidential projects)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST fetch user's GitHub activity data including commits, repositories, languages, stars, forks, and collaboration metrics via GitHub API
- **FR-002**: System MUST generate SVG visualization files for enabled statistics categories (overview, heatmap, languages, fun stats, streaks)
- **FR-003**: System MUST run automatically on a daily schedule at midnight UTC via GitHub Actions workflow
- **FR-004**: Users MUST be able to manually trigger statistics generation from the GitHub Actions workflow interface
- **FR-005**: System MUST support theme customization with at least two built-in themes (spark-dark, spark-light) and custom theme capability
- **FR-006**: Users MUST be able to selectively enable/disable statistics categories via configuration file
- **FR-007**: System MUST calculate "Spark Score" as a proprietary metric (0-100 scale) using weighted formula: 40% consistency, 35% commit volume, 25% collaboration. Normalization: Each component score is calculated independently (0-100), then weighted sum produces final score. Consistency score penalizes gaps in commit history; volume score uses logarithmic scaling to prevent extreme outliers; collaboration score aggregates stars, forks, and contributor metrics.
- **FR-008**: System MUST identify and display coding time patterns categorizing users as night owl, early bird, or balanced based on commit timestamps
- **FR-009**: System MUST generate language breakdown statistics showing percentage distribution of programming languages used
- **FR-010**: System MUST create commit heatmap showing contribution frequency over time
- **FR-011**: System MUST calculate and display streak metrics including coding streaks and learning streaks (new languages)
- **FR-012**: System MUST output all statistics as SVG files compatible with GitHub profile README embedding
- **FR-013**: System MUST handle GitHub API rate limiting gracefully with exponential backoff retry logic (1s, 2s, 4s, 8s delays) and error messaging that includes rate limit reset time
- **FR-014**: System MUST authenticate to GitHub API using user-provided Personal Access Token stored in repository secrets
- **FR-015**: System MUST validate configuration file syntax and provide clear error messages for invalid settings (e.g., "Invalid theme 'neon-blue': theme not found in themes.yml or built-in themes. Available: spark-dark, spark-light, custom", "Repository limit must be positive integer, got: 'unlimited'")
- **FR-016**: System MUST support visual effects configuration including glow effects and gradient fills
- **FR-017**: System MUST display "Lightning Round Stats" as punchy one-liners (max 80 characters each) highlighting interesting metrics using pattern "{{metric_name}}: {{insight}}" (e.g., "Night owl confirmed: 68% of commits after 10pm", "Language diversity: 12 languages mastered")
- **FR-018**: System MUST include branding footer showing "Powered by Stats Spark" when enabled in configuration
- **FR-019**: System MUST support auto-detection of GitHub username from repository context
- **FR-020**: System MUST persist generated SVG files to output directory for embedding in profile README
- **FR-021**: System MUST log error details and timestamps to workflow output for troubleshooting failures and unexpected results
- **FR-022**: System MUST cache GitHub API responses for 6 hours to reduce rate limiting impact and improve performance
- **FR-023**: Users MUST be able to force-refresh cached data to retrieve immediate updates when needed
- **FR-024**: System MUST limit repository processing to the top 500 most active repositories by default, with this limit configurable via spark.yml
- **FR-025**: System MUST only process public repositories and exclude all private repository data to protect user privacy
- **FR-026**: Documentation MUST include detailed step-by-step instructions for embedding generated statistics SVGs in GitHub profile README with example markdown code
- **FR-027**: System MUST support testing and demonstration using the markhazleton account as a reference implementation
- **FR-028**: System MUST mark deleted or private repositories as "unavailable" in historical statistics data without removing them from cached metrics

### Key Entities

- **User Profile**: Represents the GitHub user whose statistics are being generated; includes username, total repositories, total commits, join date, and collaboration indicators
- **Commit**: Represents a single code commit; includes timestamp, repository, message, and language context used for timing patterns and frequency analysis
- **Repository**: Represents a GitHub repository; includes name, primary language, star count, fork count, commit count, and last activity date
- **Language Statistics**: Represents aggregated data about programming language usage; includes language name, percentage of total code, commit count per language
- **Time Pattern**: Represents temporal analysis of coding activity; includes hourly distribution, daily distribution, categorization (night owl/early bird/balanced)
- **Streak**: Represents consecutive activity periods; includes streak type (coding, learning), current streak length, longest streak length, and date ranges
- **Spark Score**: Represents overall activity metric; includes numeric score (0-100) calculated as weighted sum (40% consistency, 35% commit volume, 25% collaboration), component scores for each factor, and lightning bolt rating (1-5 bolts)
- **Theme Configuration**: Represents visual styling settings; includes primary color, accent color, background color, effects settings (glow, gradient, animations)
- **Statistics Output**: Represents a generated SVG visualization; includes category (overview, heatmap, languages, fun), file path, generation timestamp, theme applied

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users (developers familiar with GitHub Actions) can set up automated statistics generation in under 10 minutes by following the README quick start guide
- **SC-002**: Statistics generation workflow completes in under 5 minutes for users with typical activity levels (fewer than 500 repositories)
- **SC-003**: Generated SVG files render correctly in GitHub profile READMEs across desktop and mobile browsers with no display issues
- **SC-004**: System successfully handles GitHub API rate limits without data loss for 95% of executions
- **SC-005**: Theme switching produces visually distinct outputs that maintain readability and proper contrast ratios (WCAG AA compliance for text, validated programmatically with minimum 4.5:1 contrast ratio for normal text)
- **SC-006**: Statistics accurately reflect GitHub activity with less than 1% discrepancy compared to GitHub's native insights for users with public activity
- **SC-007**: System gracefully handles edge cases (no commits, API errors, large datasets) without workflow failures in 99% of scenarios
- **SC-008**: Users can embed generated statistics in their profile README and see updates within 24 hours of commit activity
- **SC-009**: Configuration changes (theme, enabled stats) take effect in the next generation cycle without requiring code modifications
- **SC-010**: Spark Score calculation produces consistent results for the same activity data across multiple generation runs
- **SC-011**: New users can successfully embed statistics in their GitHub profile README by following documentation without external assistance in under 5 minutes
