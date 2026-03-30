# Phase 0 Research

## Decision 1: Build the repository pull request summary from `GET /repos/{owner}/{repo}/pulls?state=open`

**Decision**: Use the REST pull request list endpoint as the primary source for repository-level open PR signals, and derive a compact summary from the returned open PR collection.

**Rationale**:

- The endpoint works for public repositories without special authentication beyond public access or read-level pull request permissions.
- The response already includes the fields needed for compact roll-ups such as `draft`, `created_at`, `requested_reviewers`, and `requested_teams`.
- A summary can be computed without storing per-PR payloads in `repositories.json`, which keeps the dataset compact and aligned with the existing repository-centric contract.
- This approach avoids per-PR follow-up requests to determine mergeability or file-level details, which protects the existing runtime budget.

**Alternatives considered**:

- Calling `GET /repos/{owner}/{repo}/pulls/{pull_number}` for each open PR: rejected because it materially increases API cost for little additional value in the planned compact summary.
- GraphQL pull request queries: rejected for this phase because the current integration is PyGithub/REST-centric and the migration goal is versioned REST adoption, not a transport rewrite.

## Decision 2: Model security warnings from both status signals and active alert counts

**Decision**: Represent repository security warnings using a combined security summary that merges repository status signals and active warning counts.

**Rationale**:

- `GET /repos/{owner}/{repo}` can expose `security_and_analysis` settings, but only when the caller has admin or security-manager visibility. This is appropriate for feature/status signals, but not enough by itself.
- `GET /repos/{owner}/{repo}/vulnerability-alerts` and `GET /repos/{owner}/{repo}/automated-security-fixes` provide additional repository-level security state, though both are permission-sensitive.
- `GET /repos/{owner}/{repo}/dependabot/alerts` provides the active alert collection needed to produce counts by severity, which satisfies the requirement for active warning counts.
- Combining these sources allows the output to distinguish `clear`, `warning_present`, and `unavailable` without pretending that missing permissions are the same as zero findings.

**Alternatives considered**:

- Only using `security_and_analysis`: rejected because it does not provide active warning counts.
- Only using Dependabot alerts: rejected because it does not represent repository security feature posture and would miss the status-signal half of the requirement.
- Organization-level Dependabot alerts endpoints: rejected as the primary mechanism because the dataset is repository-centric and many target accounts are user accounts rather than organizations.

## Decision 3: Standardize availability with explicit states instead of nullable omission

**Decision**: Every new repository enrichment object must include an explicit availability status and an optional reason code, rather than relying on omitted fields or ambiguous `null` values.

**Rationale**:

- The specification explicitly requires downstream consumers to distinguish `none found` from `not collected`.
- Security endpoints have different permission requirements from pull request endpoints; explicit status is necessary to preserve trust in partial runs.
- The existing pipeline already tolerates per-repository failures during assembly, so explicit availability metadata fits the current partial-result model.

**Alternatives considered**:

- Omitting the enrichment object when unavailable: rejected because consumers cannot distinguish schema drift from collection gaps.
- Using only booleans such as `has_security_data`: rejected because it cannot represent partial data or a reason for unavailability.

## Decision 4: Treat REST API version `2026-03-10` as a staged target behind validation gates

**Decision**: Keep the current default behavior as the baseline, explicitly support opt-in requests with `X-GitHub-Api-Version: 2026-03-10`, and promote the new version to the default only after validation gates pass.

**Rationale**:

- GitHub documents that requests without `X-GitHub-Api-Version` default to `2022-11-28`; that preserves the current baseline while migration work is validated.
- GitHub documents both `2022-11-28` and `2026-03-10` as supported versions, so parallel validation is viable.
- Relevant `2026-03-10` breaking changes include removal of `merge_commit_sha` from pull request responses, removal of the singular `assignee` field from issue and pull request payloads, removal of deprecated repository field `has_downloads`, and removal of deprecated `rate` from the rate limit endpoint.
- The current feature work does not require those deprecated fields, so the upgrade risk is manageable if existing parsing paths are audited before cutover.

**Alternatives considered**:

- Immediate hard cutover to `2026-03-10`: rejected because existing PyGithub-backed calls may still rely on default-version behavior or undocumented payload assumptions.
- Deferring version work entirely: rejected because this feature expands the GitHub surface area and is the right moment to add version-awareness and validation gates.

## Decision 5: Keep cache invalidation tied to repository change signals

**Decision**: Cache pull request and security summaries per repository using the same repository change addressability pattern already used elsewhere in the pipeline.

**Rationale**:

- The constitution forbids TTL-driven cache invalidation and requires `pushed_at`-based change tracking.
- The existing pipeline already uses repository-scoped cache entries keyed from sanitized `pushed_at` timestamps.
- Even though PR and security state can change without a push, the project constitution prioritizes no unnecessary API calls for unchanged repositories; the design must therefore use explicit force refresh or future targeted overrides rather than introducing TTL.

**Alternatives considered**:

- A separate short-lived TTL for PR/security data: rejected because it violates the constitution's caching rule.
- No caching for new enrichment: rejected because it risks breaching the runtime budget for accounts near the 500-repository limit.
