# Phase 1 Data Model

## RepositoryPullRequestSummary

**Purpose**: Compact repository-level pull request health signal stored on every included repository record.

**Fields**:

- `availability`: enum, one of `available`, `partial`, `unavailable`
- `reason`: optional enum, one of `none`, `permission_denied`, `api_error`, `not_requested`, `unknown`
- `total_open`: integer, minimum `0`
- `draft_count`: integer, minimum `0`
- `review_requested_count`: integer, minimum `0`
- `oldest_open_age_days`: integer or `null`, minimum `0`
- `has_open_pull_requests`: boolean
- `source`: string, expected value `rest.pulls.list`

**Validation rules**:

- Object MUST be present for every included repository.
- When `availability = available`, numeric fields MUST be populated and internally consistent.
- When `total_open = 0`, `has_open_pull_requests` MUST be `false` and `oldest_open_age_days` MUST be `null`.
- When `availability = unavailable`, counters default to `0`, but `reason` MUST explain the collection gap.

## RepositorySecuritySummary

**Purpose**: Repository-level security posture and active alert summary stored on every included repository record.

**Fields**:

- `availability`: enum, one of `available`, `partial`, `unavailable`
- `reason`: optional enum, one of `none`, `permission_denied`, `api_error`, `not_supported`, `not_requested`, `unknown`
- `overall_state`: enum, one of `clear`, `warning_present`, `unavailable`
- `feature_status`: object
- `feature_status.advanced_security`: enum `enabled`, `disabled`, `unavailable`, `unknown`
- `feature_status.secret_scanning`: enum `enabled`, `disabled`, `unavailable`, `unknown`
- `feature_status.secret_scanning_push_protection`: enum `enabled`, `disabled`, `unavailable`, `unknown`
- `feature_status.dependency_alerts`: enum `enabled`, `disabled`, `unavailable`, `unknown`
- `feature_status.automated_security_fixes`: enum `enabled`, `disabled`, `paused`, `unavailable`, `unknown`
- `active_alert_counts`: object
- `active_alert_counts.total_open`: integer, minimum `0`
- `active_alert_counts.critical`: integer, minimum `0`
- `active_alert_counts.high`: integer, minimum `0`
- `active_alert_counts.medium`: integer, minimum `0`
- `active_alert_counts.low`: integer, minimum `0`
- `sources`: array of strings from `rest.repos.get`, `rest.repos.vulnerability-alerts`, `rest.repos.automated-security-fixes`, `rest.dependabot.alerts`

**Validation rules**:

- Object MUST be present for every included repository.
- `overall_state = clear` is only valid when `availability` is `available` or `partial` and `active_alert_counts.total_open = 0`.
- `overall_state = warning_present` is only valid when any active alert count is non-zero.
- `overall_state = unavailable` is required when collection produced no trustworthy signal.
- Severity counts MUST sum to less than or equal to `total_open`; unmatched alerts are allowed only if GitHub returns alerts without mapped severities and should be called out in logs.

## DataAvailabilityStatus

**Purpose**: Shared semantics for partial and unavailable enrichment.

**Fields**:

- `availability`: enum `available`, `partial`, `unavailable`
- `reason`: enum `none`, `permission_denied`, `api_error`, `not_supported`, `not_requested`, `unknown`

**Usage**:

- Pull request and security summaries both embed this status model.
- `partial` means at least one planned source succeeded and at least one failed or was restricted.
- `unavailable` means no trustworthy enrichment result was collected for that domain.

## RepositoryContractRevision

**Purpose**: Additive revision of the unified repository JSON contract.

**Fields added to each repository**:

- `pull_request_summary: RepositoryPullRequestSummary`
- `security_summary: RepositorySecuritySummary`

**Versioning rule**:

- `metadata.schema_version` advances from `2.0.0` to `2.1.0` because the dataset gains additive fields without removing prior ones.

## UpgradeAssessment

**Purpose**: Planning-only entity captured in documentation rather than runtime JSON.

**Fields**:

- `current_rest_baseline`: string
- `target_rest_version`: string
- `affected_paths`: array of source modules or API paths
- `breaking_changes`: array of documented compatibility risks
- `validation_gates`: array of rollout checks
- `fallback_strategy`: string

**State transitions**:

- `assessed` -> `validated-in-shadow` -> `default-enabled`
- `assessed` -> `deferred` if validation gates fail or unknown parser dependencies remain