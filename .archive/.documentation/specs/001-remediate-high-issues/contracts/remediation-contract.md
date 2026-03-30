# Remediation Contract

## Purpose

Document the stable behavioral contracts that must remain true while the HIGH audit findings are remediated.

## Contract 1: Theme Resolution

- **Input**: Configured visualization theme from `config/spark.yml`
- **Behavior**:
  - Unified report generation must resolve its theme from configuration
  - Supported built-in themes continue to resolve through the shared theme helper
  - Invalid or unsupported custom theme requests fail before output generation completes
- **Must Remain Stable**:
  - Theme names `spark-dark` and `spark-light`
  - WCAG-oriented theme validation behavior

## Contract 2: Dashboard Aggregate Totals

- **Input**: Included repository set used for dashboard generation
- **Behavior**:
  - `total_stars` equals the sum of included repository stars
  - `total_forks` equals the sum of included repository forks
  - Totals remain deterministic for the same repository input
- **Must Remain Stable**:
  - No extra API dependency to derive totals
  - Only public repositories contribute to totals

## Contract 3: Cache and Workflow Stability

- **Input**: Existing `APICache` category/repo/week access pattern and unified workflow return types
- **Behavior**:
  - Refactoring may reorganize orchestration code but must preserve cache invalidation semantics and public command behavior
  - No added API calls for unchanged repositories
- **Must Remain Stable**:
  - Content-addressed cache strategy keyed by repository change state
  - Existing CLI command names and top-level workflow entry points

## Contract 4: Speckit Feature Artifact Location

- **Input**: Active feature branch identifier
- **Behavior**:
  - Feature planning artifacts for this repo live under `.documentation/specs/<feature>/`
  - Helper scripts and templates must resolve paths using that location
- **Must Remain Stable**:
  - `spec.md`, `plan.md`, `research.md`, `data-model.md`, `quickstart.md`, `contracts/`, and `tasks.md` stay grouped under the feature directory
