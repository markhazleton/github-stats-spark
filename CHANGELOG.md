# Changelog

## [2.1.1] - 2026-05-05

- Resolved ARCH1 by updating `.devspark/scripts/powershell/site-audit.ps1` to source scan exclusions from `config/spark.yml` and enforce source-scope filtering.
- Resolved QUAL1 by refactoring `frontend/src/components/DrillDown/RepositoryDetail.jsx` into focused hooks, utility helpers, and section components.
- Refreshed `.documentation/copilot/audit/2026-05-05_results.md` with rerun evidence showing zero insecure-pattern findings from generated artifact paths.
- Canonical project changelog remains at .documentation/CHANGELOG.md.

## [2.1.0] - 2026-04-19

- Upgraded DevSpark framework from v1.5.0 to v2.1.0 (Workflow Engine release).
- Added new commands: `/devspark.address-pr-review`, `/devspark.commit-audit`, `/devspark.update-pr`.
- Updated 25 existing command prompt templates in `.devspark/defaults/commands/`.
- Updated 20 PowerShell scripts in `.devspark/scripts/powershell/`.
- Added new scripts: `address-pr-review.ps1`, `generate-atomic-shims.ps1`, `release-history-context.ps1`, `run-workflow.ps1`.
- Canonical project changelog remains at .documentation/CHANGELOG.md.

## [1.5.1] - 2026-03-28

- Added root version marker to support local Spec Kit version checks in automated site audits.
- Canonical project changelog remains at .documentation/CHANGELOG.md.
