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

2. Run targeted unit tests for remediation-sensitive areas:

```powershell
pytest tests/unit/test_visualizer.py tests/unit/test_config.py tests/unit/test_cache.py tests/unit/test_wcag.py
```

3. Run coverage for the core Python package and confirm the visualization module meets the constitutional threshold:

```powershell
pytest --cov=spark --cov-report=html
```

4. Run a bounded unified workflow to verify configuration-driven output and aggregate totals without full-scale execution:

```powershell
spark unified --user markhazleton --max-repos 2 --verbose
```

5. Confirm the active feature artifacts are stored under `.documentation/specs/001-remediate-high-issues/` and not in a legacy root `specs/` directory.

6. Re-run the site audit after implementation and confirm the in-scope HIGH findings are cleared.

## Expected Outcomes

- Theme selection is driven by config, not hard-coded defaults.
- Dashboard profile totals match the included repositories.
- Visualizer verification meets or exceeds the constitutional threshold.
- Speckit feature artifacts live under `.documentation/specs/`.
- Documentation ownership is explicit for affected Markdown assets.