# Phase 0 Research

## Decision 1: Keep Speckit feature artifacts under `.documentation/specs/`

- **Decision**: Use `.documentation/specs/<feature>/` as the canonical location for plan/spec/tasks artifacts for this feature.
- **Rationale**: The current helper scripts already resolve feature paths from `.documentation/specs/`, and the feature creation workflow was updated to write there. Keeping planning artifacts in one tool-owned location removes the path split that caused the latest mismatch.
- **Alternatives considered**:
  - Root `specs/`: rejected because it conflicts with the current helper scripts and the intended latest Spec Kit Spark layout.
  - `documentation/spec/`: rejected for this feature because the active automation and feature-path helpers do not use it, and changing all project documentation governance in the same step would expand scope beyond the six HIGH issues.

## Decision 2: Resolve workflow theme selection through existing config and theme helpers

- **Decision**: Route unified workflow theme selection through `SparkConfig.get_theme()` and `spark.visualizer.get_theme(...)` rather than instantiating a hard-coded theme in the workflow.
- **Rationale**: This preserves existing configuration semantics, uses the repo’s current validation path, and satisfies the fail-fast and accessibility principles without adding new theme selection logic.
- **Alternatives considered**:
  - Keep `SparkDarkTheme()` hard-coded: rejected because it directly violates configuration governance.
  - Implement custom theme branching inside `UnifiedReportWorkflow`: rejected because `get_theme(...)` already centralizes theme resolution and custom-theme validation.

## Decision 3: Calculate dashboard aggregate totals from included repository data

- **Decision**: Compute `total_stars` and `total_forks` from the repository set already included in dashboard generation.
- **Rationale**: The required data is already present in the generation flow, the calculation is deterministic, and it avoids introducing a second source of truth or extra API calls.
- **Alternatives considered**:
  - Use user-level aggregate data from the GitHub user profile: rejected because the existing user fetch path does not provide the exact included-repository totals required by the feature.
  - Leave placeholders and document them: rejected because the audit classified the behavior as a HIGH accuracy issue.

## Decision 4: Reduce single-responsibility risk through staged extractions rather than a rewrite

- **Decision**: Refactor in bounded slices by extracting low-risk helpers first, then isolating cache refresh coordination and workflow stages behind the existing public contracts.
- **Rationale**: The repo already exposes stable contracts that other modules depend on, including cache access shape, workflow return types, and CLI command names. Incremental extraction lowers regression risk while still addressing the architectural findings.
- **Alternatives considered**:
  - Full CLI/cache/workflow rewrite: rejected because it would change too many interacting surfaces at once.
  - Ignore architectural findings and only add tests: rejected because the feature scope explicitly includes the HIGH module-responsibility issues.

## Decision 5: Raise visualizer coverage using targeted branch tests in existing unit suites

- **Decision**: Add focused tests to `tests/unit/test_visualizer.py` that exercise rendering loops, threshold branches, and theme/error cases with parametrized inputs.
- **Rationale**: Existing tests already validate basic SVG structure and theme usage. Extending that suite is the fastest way to cover currently missed branches without rewriting `visualizer.py` or adding new frameworks.
- **Alternatives considered**:
  - Broad visualizer rewrite for testability first: rejected because coverage can be raised with less churn.
  - Snapshot-heavy SVG golden tests: rejected because they add maintenance cost without directly targeting the missing branches identified in the audit.

## Decision 6: Treat documentation governance as classification plus path alignment, not mass relocation

- **Decision**: Keep Speckit/framework artifacts in `.documentation/`, keep established project guides in `documentation/`, and classify generated or deployment README files as output metadata or explicit exceptions.
- **Rationale**: This resolves the practical tool-path problem immediately while containing the HIGH documentation issue to a governance and discoverability problem instead of turning this feature into a repo-wide documentation migration.
- **Alternatives considered**:
  - Move all Markdown under `.documentation/`: rejected because the active constitution and published project docs still treat `documentation/` as the user-facing guide surface.
  - Leave the documentation issue untouched: rejected because the audit identified it as HIGH severity.

## Post-Implementation Evidence

- Config validation completed successfully with `python -m spark.cli config --validate`.
- Focused remediation regression execution passed with `52 passed` after adding the CLI, cache manager, dashboard generator, and unified workflow harnesses.
- Broader unit and coverage validation passed with `79 passed` and generated the HTML coverage report.
- The first follow-up site audit confirmed the configuration, aggregate-total, and test findings were resolved but still reported `ARCH1`, `ARCH2`, `DOC1`, and `VER3`, which led to the extraction of `src/spark/cli_handlers.py`, `src/spark/cache_refresh_executor.py`, and the constitution and agent-path updates.
- The final follow-up audit at `.documentation/copilot/audit/2026-03-07_followup-high-findings-remediation-check.md` reported no remaining HIGH findings.
- A local bounded generation run via `run-spark-local.ps1 -Screenshots -MissingOnly` completed successfully in the current workspace terminal session.