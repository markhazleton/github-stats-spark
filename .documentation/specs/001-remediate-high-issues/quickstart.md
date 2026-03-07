# Quickstart

## Goal

Validate the remediation feature end to end for configuration accuracy, aggregate totals, verification coverage, and Speckit path alignment.

## Prerequisites

1. Activate the project virtual environment.
2. Ensure `GITHUB_TOKEN` is available for workflow validation runs.
3. Use the canonical demo account `markhazleton` for manual output checks.

## Validation Flow

1. Validate configuration:

```powershell
spark config --validate
```

Observed result: passed via `python -m spark.cli config --validate` in the repo virtual environment.

2. Run targeted unit tests for remediation-sensitive areas:

```powershell
pytest tests/unit/test_visualizer.py tests/unit/test_config.py tests/unit/test_cache.py tests/unit/test_wcag.py
```

Observed result: the remediation-specific regression harness expanded beyond this initial set and passed in the focused run (`52 passed`).

3. Run coverage for the core Python package and confirm the visualization module meets the constitutional threshold:

```powershell
pytest --cov=spark --cov-report=html
```

Observed result: broader validation passed with `79 passed`, and the HTML coverage report was generated successfully.

4. Run a bounded unified workflow to verify configuration-driven output and aggregate totals without full-scale execution:

```powershell
spark unified --user markhazleton --max-repos 2 --verbose
```

Observed result: not executed in the shell validation step because `GITHUB_TOKEN` was missing from the terminal environment at execution time. Unit coverage, config validation, and the follow-up audit were completed successfully instead.

5. Confirm the active feature artifacts are stored under `.documentation/specs/001-remediate-high-issues/` and not in a legacy root `specs/` directory.

Observed result: confirmed. Current planning artifacts and follow-up governance updates use the supported `.documentation/...` structure.

6. Re-run the site audit after implementation and confirm the in-scope HIGH findings are cleared.

Observed result: passed. The follow-up report at `.documentation/copilot/audit/2026-03-07_followup-high-findings-remediation-check.md` reports no remaining HIGH findings.

## Expected Outcomes

- Theme selection is driven by config, not hard-coded defaults.
- Dashboard profile totals match the included repositories.
- Visualizer verification meets or exceeds the constitutional threshold.
- Speckit feature artifacts live under `.documentation/specs/`.
- Documentation ownership is explicit for affected Markdown assets.

## Completion Snapshot

- Config validation passed.
- Focused remediation suites passed.
- Broader regression and coverage validation passed.
- Follow-up site audit cleared all baseline HIGH findings.
- The only skipped validation step was the bounded unified shell run, blocked by a missing terminal `GITHUB_TOKEN`.