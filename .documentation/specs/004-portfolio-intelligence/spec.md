---
classification: full-spec
risk_level: medium
target_workflow: specify-full
required_artifacts: spec, plan, tasks
recommended_next_step: plan
required_gates: checklist, analyze, critic
---

# Feature Specification: Portfolio Intelligence System

**Feature Branch**: `004-portfolio-intelligence`
**Created**: 2026-04-24
**Status**: Complete
**Input**: Reposition github-stats-spark from a GitHub metrics dashboard into a Portfolio Intelligence System for analyzing, classifying, and curating engineering signal.

## User Scenarios & Testing *(mandatory)*

### User Story 1 – Portfolio Owner Reviews Their Signal Profile (Priority: P1)

An engineer visits their portfolio intelligence dashboard and immediately sees their repositories organized into three tiers: Core (primary systems), Supporting (complementary tools), and Archive (historical or low-priority work). Each tier is visually distinct and includes a signal score that communicates how representative each repository is of their current expertise.

**Why this priority**: This is the central value proposition. Without classification and signal scoring, the system is indistinguishable from any other GitHub stats tool.

**Independent Test**: The dashboard can be fully tested by loading the generated output and verifying that every repository is assigned a tier, has a signal score, and is grouped correctly by classification. This delivers the core value of "portfolio at a glance."

**Acceptance Scenarios**:

1. **Given** a portfolio with mixed-age repositories, **When** the dashboard loads, **Then** each repository is displayed under one of three classification headers (Core, Supporting, Archive) with a visible signal score
2. **Given** a portfolio where `devspark` is manually configured as Core, **When** the dashboard loads, **Then** `devspark` appears in the Core tier regardless of its recent commit activity
3. **Given** a repository with no recent commits and no manual override, **When** classification runs, **Then** it is assigned to Archive by default

---

### User Story 2 – Portfolio Owner Configures Manual Overrides (Priority: P2)

An engineer edits a YAML configuration file to declare which repositories are Core, Supporting, or Archive. The system reads this config during data generation and applies overrides before automated classification rules run. A wildcard entry sets the default for all unspecified repositories.

**Why this priority**: Automated rules cannot capture intent. Manual overrides are essential for accurate representation and prevent misclassification of recently-inactive but strategically important projects.

**Independent Test**: Fully testable by editing the config file, regenerating data, and confirming the overrides appear in the output JSON and dashboard.

**Acceptance Scenarios**:

1. **Given** a config file with `devspark: core`, **When** classification runs, **Then** `devspark` is classified as Core regardless of automated signals
2. **Given** a config file with `"*": archive` as the wildcard default, **When** an unlisted repository is processed, **Then** it receives Archive classification
3. **Given** a malformed or missing config file, **When** classification runs, **Then** the system applies fully automated classification and logs a clear warning — it does not fail

---

### User Story 3 – Site Visitor Understands Engineer's Expertise at a Glance (Priority: P3)

A recruiter or collaborator visits the portfolio intelligence page and sees a narrative explaining the signal vs noise concept, followed by a visual breakdown of Core, Supporting, and Archive repositories. The visitor can understand the engineer's primary focus areas without reading individual repository descriptions.

**Why this priority**: The external audience is a key beneficiary. The system must communicate signal effectively to non-technical visitors, not just serve the portfolio owner.

**Independent Test**: Testable by reviewing the generated site/dashboard without prior context and verifying that the narrative, classification breakdown, and signal scores are understandable to a non-technical reader.

**Acceptance Scenarios**:

1. **Given** a generated portfolio page, **When** a visitor reads the page, **Then** a narrative section explains the signal vs noise concept in plain language within the first visible section
2. **Given** a portfolio with repositories across all three tiers, **When** the portfolio breakdown visualization is displayed, **Then** the Core/Supporting/Archive distribution is visible as a chart or summary without scrolling
3. **Given** a Core repository, **When** it is displayed, **Then** its notes field (from config or auto-generated) briefly explains why it is significant

---

### User Story 4 – Site Integration Consumer Embeds Portfolio Data (Priority: P4)

The markhazleton.com site reads the generated JSON export and renders a portfolio intelligence widget or section without additional data transformation. The JSON schema is stable, documented, and includes all classification fields.

**Why this priority**: Integration without transformation is a key requirement from the spec. If the JSON requires transformation before embedding, integration becomes fragile.

**Independent Test**: Testable by reading the generated JSON directly and verifying that all required fields (`classification`, `signal_score`, `relevance`, `notes`) are present and correctly typed.

**Acceptance Scenarios**:

1. **Given** the portfolio data generation runs successfully, **When** the JSON output is inspected, **Then** every repository entry includes `classification`, `signal_score`, `relevance`, and `notes` fields
2. **Given** a repository marked as Core in the config, **When** the JSON is exported, **Then** the `classification` field is `"core"` and `relevance` is `"high"`
3. **Given** the JSON export, **When** consumed by an external site, **Then** no additional API calls or transformations are required to render a classification summary

---

### Edge Cases

- What happens when all repositories are forks? The system filters forks by default; if all repos are forks, the output is empty — an explicit empty-state message is shown
- What happens when a config override names a repository that no longer exists? The override is silently ignored; a warning is logged
- How does the system handle repositories with identical activity scores? Tie-breaking uses recency (most recently pushed takes priority for a higher tier)
- What happens when the config file has no wildcard entry? The system defaults to Archive for unspecified repositories
- How does signal scoring behave for a brand-new repository with no commits? It receives a minimum signal score and Archive classification

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST classify each non-forked public repository as exactly one of: Core, Supporting, or Archive using rule-based thresholds — classification is deterministic and does not depend on AI availability. Rules are evaluated in priority order (first match wins):
  - **Core**: pushed ≤90 days ago AND ≥5 commits in the last 90 days AND (has_tests OR has_ci_cd)
  - **Supporting**: pushed ≤365 days ago OR ≥1 commit in the last 90 days (and not already Core)
  - **Archive**: all remaining repositories
- **FR-001a**: System MUST store the AI portfolio intelligence `role` field (when available) alongside the rule-based classification as informational reference data; the AI field does not override the computed classification
- **FR-002**: System MUST read `config/portfolio.yml` to apply manual classification overrides before automated rules
- **FR-003**: System MUST support a wildcard (`"*"`) entry in the config file to set the default classification for all unspecified repositories
- **FR-004**: System MUST compute a signal score (0–100) for each repository using equal-weight contributions: recency (33%), 90-day commit volume (33%), and classification tier (34% — Core=100, Supporting=60, Archive=20)
- **FR-005**: System MUST set `relevance` to `"high"` for Core, `"medium"` for Supporting, and `"low"` for Archive
- **FR-006**: System MUST include a `notes` field on each repository in the output: populated verbatim from the config override when present; otherwise auto-generated as a short phrase based on the assigned classification tier and activity signals (e.g., "Actively maintained system with high recent activity")
- **FR-007**: System MUST export an enriched JSON file with all classification fields alongside existing repository metadata
- **FR-008**: System MUST generate a portfolio breakdown visualization showing counts and proportions of Core, Supporting, and Archive repositories
- **FR-009**: System MUST generate a signal distribution visualization showing relative signal weight across repositories
- **FR-010**: System MUST include a narrative section on the portfolio page explaining the signal vs noise concept in plain language
- **FR-011**: System MUST NOT process private repositories or expose any private repository metadata in any output
- **FR-012**: System MUST log a warning (not an error) when the classification config file is missing or malformed, then proceed with automated classification
- **FR-013**: System MUST filter fork repositories from all classification and visualization outputs
- **FR-014**: README MUST be updated to describe the system as a portfolio intelligence tool, following the required section structure

### Key Entities

- **Repository**: A public, non-forked code repository with metadata (name, last updated, activity score) plus enriched fields: classification (Core/Supporting/Archive), signalScore (0–100, computed as equal-weight average of recency, 90-day commit volume, and tier score), relevance (high/medium/low, derived from classification), notes (string, from config override or auto-generated phrase)
- **ClassificationConfig**: A YAML file mapping repository names to explicit tiers, with an optional wildcard default; serves as the manual override layer
- **PortfolioBreakdown**: Aggregated counts and proportions of repositories per classification tier, used for visualization
- **SignalDistribution**: Ranked list of repositories by signal score, used to show relative portfolio weight

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A visitor to the portfolio page understands the engineer's primary focus areas without reading individual repository descriptions — validated by reading the page cold with no prior context
- **SC-002**: An engineer can describe their portfolio positioning in under 30 seconds using only the dashboard output
- **SC-003**: 100% of non-forked public repositories receive a classification — no unclassified repositories in the output
- **SC-004**: The JSON output is consumable by markhazleton.com without any additional transformation or intermediate processing step
- **SC-005**: Manual classification overrides take effect within one data generation run after the config file is updated
- **SC-006**: The portfolio breakdown visualization is visible without scrolling on standard desktop and mobile viewports
- **SC-007**: The system processes a portfolio of up to 100 repositories and produces all outputs within the existing execution time budget (under 5 minutes total)

## Assumptions

- The existing GitHub API integration and caching layer remain unchanged; this spec extends the data model without replacing the data source
- The classification config file lives at `config/portfolio.yml`, co-located with the existing `config/spark.yml`
- Signal scoring uses only data already available in the existing data model (commit frequency, recency, star count, etc.) — no new API calls are required
- `notes` for repositories without a config override are auto-generated as a short phrase derived from the assigned classification tier and activity signals; the GitHub description field is not used for this purpose
- The Activity vs Relevance Matrix and Evolution Timeline visualizations are deferred to a future iteration; this spec covers Portfolio Breakdown and Signal Distribution only
- markhazleton.com integration (Option A) is out of scope for this spec; the JSON export format is the integration boundary
- The existing SVG visualization pipeline remains the primary output format; any new visualizations follow the same rendering approach

## Clarifications

### Session 2026-04-24

- Q: Does classification use the AI portfolio intelligence `role` output, rule-based thresholds, or a hybrid? → A: Rule-based primary — classification is computed from thresholds (commit activity + recency); AI `role` is stored alongside as informational context only and never overrides the computed classification.
- Q: What should the `notes` field contain for repositories without a manual config override? → A: Auto-generated short phrase based on the assigned classification tier and activity signals (e.g., "Actively maintained system with high recent activity"); GitHub description field is not used.
- Q: What thresholds define automated Core/Supporting/Archive classification? → A: Three-factor, priority-ordered rules: Core = pushed ≤90d AND ≥5 commits (90d) AND (has_tests OR has_ci_cd); Supporting = pushed ≤365d OR ≥1 commit (90d); Archive = all else.
- Q: Where does the classification config file live? → A: `config/portfolio.yml`, co-located with `config/spark.yml`.
- Q: What are the signal score weights across recency, commit volume, and classification tier? → A: Equal thirds — recency 33%, 90-day commit volume 33%, classification tier 34% (Core=100, Supporting=60, Archive=20).

## Constraints (from Constitution)

- All outputs MUST only include public repository data (Constitution Principle II — non-negotiable)
- New modules introduced MUST stay under 500 lines of code (Constitution Principle I)
- All visual outputs MUST meet WCAG AA contrast requirements (Constitution Principle V)
- Generated classification data files MUST be added to `scan.exclude_paths` in `config/spark.yml` (Constitution Principle VI)
