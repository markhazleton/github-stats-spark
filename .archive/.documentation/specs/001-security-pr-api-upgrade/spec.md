# Feature Specification: Repository Security and PR Signals

**Feature Branch**: `001-security-pr-api-upgrade`  
**Created**: 2026-03-14  
**Status**: Draft  
**Input**: User description: "Create a plan to add checks for security warnings and open pull requests to the data gathered from GitHub Repositories. Research the new GitHub API version for any upgrade possibilities and create a plan to move to latest version of API"

## Clarifications

### Session 2026-03-14

- Q: What should the spec treat as repository security warnings? → A: Track both security feature/status signals and active warning counts.
- Q: How should the spec position GitHub REST version 2026-03-10? → A: Treat 2026-03-10 as the target, but migrate in stages behind validation gates.
- Q: What level of open pull request detail should each repository record include? → A: Use a compact summary with total open PRs plus roll-up indicators such as draft count and oldest-open age.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Enriched Repository Signals (Priority: P1)

As a maintainer or dashboard consumer, I want each included repository to expose security warning signals and open pull request activity so I can judge repository health without checking GitHub manually.

**Why this priority**: This is the direct user-facing value of the feature. Without these repository signals, the feature does not meet its purpose.

**Independent Test**: Run a standard data generation flow for an account with repositories that have open pull requests and visible repository security signals, then verify that each repository entry includes the new security and pull request fields or an explicit empty state.

**Acceptance Scenarios**:

1. **Given** a repository has open pull requests and security warning data is available, **When** repository data is generated, **Then** that repository entry includes a compact open pull request summary and a security warning summary.
2. **Given** a repository has no open pull requests and no active security warning signals, **When** repository data is generated, **Then** the repository entry records a zero or clear state instead of omitting the fields.

---

### User Story 2 - Transparent Partial Availability (Priority: P2)

As a maintainer, I want the data output to distinguish between "no findings" and "data unavailable" so I can trust the results even when GitHub access rules or data-source limitations prevent full collection.

**Why this priority**: Security-related data is permission-sensitive. Silent gaps would be misleading and would reduce confidence in the generated report.

**Independent Test**: Generate data with credentials that can read public repository metadata but cannot read all security-related repository signals, then verify that repository entries continue to be produced and unavailable fields are marked explicitly.

**Acceptance Scenarios**:

1. **Given** a repository's security data cannot be read because of missing permissions, **When** repository data is generated, **Then** the output marks that security data as unavailable and records why collection was incomplete.
2. **Given** one or more enrichment requests fail during generation, **When** the run completes, **Then** existing repository data is still produced and the output records that the run contains partial enrichment results.

---

### User Story 3 - API Upgrade Readiness (Priority: P3)

As a maintainer, I want a documented upgrade assessment for moving from the current GitHub integration baseline to GitHub REST API version 2026-03-10 so I can decide whether to migrate now, defer, or stage the change safely.

**Why this priority**: The new repository signals increase GitHub API surface area. A version upgrade plan reduces compatibility risk before implementation work begins.

**Independent Test**: Review the generated planning artifact for the feature and confirm it identifies the current baseline, version 2026-03-10 as the target baseline, affected data sources, required access levels, validation gates, and staged rollout decision points.

**Acceptance Scenarios**:

1. **Given** GitHub REST API version 2026-03-10 differs from the behavior currently used by the integration, **When** the upgrade assessment is completed, **Then** it identifies impacted repository and pull request collection paths and the validations required before migration.
2. **Given** the upgrade assessment finds unresolved blockers, **When** the plan is reviewed, **Then** it states whether migration should proceed, be staged, or be deferred and explains the reason.

### Edge Cases

- Repository security settings are not visible for a public repository because the available access level is not sufficient to expose them.
- A repository has many open pull requests, but the generated output must remain compact and avoid unbounded per-pull detail in the main repository record. The system caps open-PR collection at 100 items (3 API pages) per repository; `total_open` reflects the fetched count and any higher total is noted via the GitHub response `total_count` header when available.
- A repository has open pull requests from forks, bots, or drafts; the summary must still reflect the open state consistently.
- A repository is public but archived, forked, or otherwise excluded by existing rules; the new feature must not bypass current exclusion behavior.
- GitHub REST API version 2026-03-10 introduces breaking response changes for fields the integration may read; the feature must still produce a staged rollout decision and not leave the upgrade state ambiguous.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST enrich each included public repository record with a compact open pull request summary.
- **FR-002**: The open pull request summary MUST identify whether open pull requests exist, how many are currently open for the repository, and include roll-up indicators—specifically draft count, review-requested count, and oldest-open age in days—that help judge the age or review state of the open pull request set.
- **FR-003**: The system MUST enrich each included public repository record with a security summary that includes both repository-level security feature/status signals and active warning counts when those signals are available.
- **FR-004**: The security summary MUST distinguish between a clear state, a warning-present state, and an unavailable state.
- **FR-005**: The system MUST preserve existing repository inclusion rules so that private repositories remain excluded from collection, enrichment, cache entries, and output.
- **FR-006**: The system MUST continue producing repository data when pull request or security enrichment fails for an individual repository, while marking the affected fields as partial or unavailable.
- **FR-007**: The generated output MUST make it possible for downstream consumers to determine whether a missing security or pull request value means "none found" or "not collected."
- **FR-008**: The feature MUST define the expected output contract changes for repository data so existing consumers can adopt the new fields intentionally.
- **FR-009**: The feature MUST document the GitHub access requirements needed to collect the new repository security and pull request signals.
- **FR-010**: The feature MUST include an upgrade assessment from the current GitHub integration baseline to GitHub REST API version 2026-03-10.
- **FR-011**: The upgrade assessment MUST identify affected repository and pull request data sources, expected compatibility risks, validation gates, and a fallback decision if full migration to 2026-03-10 cannot be completed safely.
- **FR-012**: The feature MUST provide a clear rollout recommendation that positions 2026-03-10 as the target baseline and uses staged adoption behind validation gates.
- **FR-013**: The feature MUST maintain the project's existing performance target for standard repository generation runs or explicitly identify mitigation steps and budget-exceeded reporting when the new enrichment scope threatens that target. Candidate mitigations include: capping per-repo open-PR pages (max 3), skipping enrichment for repositories beyond a configurable limit, parallelizing enrichment requests where rate limits allow, and logging a budget-exceeded warning while continuing output without enrichment.
- **FR-014**: The feature MUST preserve observability by reporting enrichment warnings, partial-result conditions, and upgrade assessment conclusions in generated artifacts or logs.

### Key Entities *(include if feature involves data)*

- **Repository Pull Request Summary**: A repository-level record describing whether open pull requests exist, how many are open, compact roll-up indicators such as draft count or oldest-open age, and whether the pull request data was fully available.
- **Repository Security Summary**: A repository-level record describing repository security feature/status signals, active warning counts, and whether those security signals were available to collect.
- **Data Availability Status**: A shared status concept used to distinguish a confirmed zero state from a permissions gap, endpoint limitation, or failed collection attempt.
- **Upgrade Assessment**: A planning artifact that records the current baseline behavior, GitHub REST API version 2026-03-10 as the target baseline, impacted data sources, required access levels, validation criteria, and rollout recommendation.

### Assumptions

- "Security warnings" refers to both repository-level security feature/status signals and active warning counts that can be collected consistently for included public repositories, rather than a full remediation workflow for every advisory.
- Open pull request coverage is limited to currently open pull requests for repositories already included in the generated dataset after the existing public-repository filters run.
- Open pull request coverage uses a compact repository-level summary rather than embedding a per-pull list in the main repository payload.
- GitHub REST API version 2026-03-10 is the evaluated migration target for this feature, but adoption is expected to occur in stages behind explicit validation gates rather than as a single cutover.
- Cached PR and security enrichment reflects the repository state at the time of the last `pushed_at` change. Changes between pushes (new PRs opened, Dependabot alerts filed) are not reflected until the next push or an explicit `--force-refresh` run.
- Open-PR collection is capped at 100 items (3 API pages) per repository to protect the runtime budget. Repositories with more open PRs will report the fetched count; consumers should treat the count as a lower bound when the cap is reached.
- This feature includes planning, output contract definition, and migration readiness work; it does not require a separate dashboard redesign beyond making the new repository data consumable.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of included repository records expose either an open pull request summary or an explicit unavailable state after generation completes.
- **SC-002**: 100% of included repository records expose either a security summary or an explicit unavailable state after generation completes.
- **SC-003**: A maintainer can determine within 10 minutes of reviewing the generated specification and related planning artifacts whether migration toward GitHub REST API version 2026-03-10 should proceed through the staged rollout, require additional gates, or be deferred.
- **SC-004**: Standard generation for accounts with fewer than 500 included repositories continues to meet the existing under-5-minute target, or the output clearly identifies the enrichment scope that prevents meeting that target.
- **SC-005**: Existing repository fields remain intact so downstream consumers can adopt the new enrichment fields without losing previously available repository metadata.
