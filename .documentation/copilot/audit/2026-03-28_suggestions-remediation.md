# Site Audit Suggestions Remediation (2026-03-28)

## Plan

1. Remove audit scanner noise from generated artifacts.
2. Fix package discovery to include frontend npm manifest.
3. Replace placeholder cache hit metric with measured values.
4. Implement learning streak calculation.
5. Add regression tests for new behavior.
6. Add root version marker for deterministic local version checks.
7. Add core-module coverage enforcement gate.
8. Re-run validation and pre-scan.

## Execution Results

### 1) Scanner noise and build classification

- Updated `.documentation/scripts/powershell/site-audit.ps1` to:
  - Exclude generated publish artifacts (`docs/assets`, `docs/data`, `docs/output`, `htmlcov`) from source/security scans.
  - Classify `.github/workflows/*` as build files before config classification.
- Validation result: `insecure_patterns_total` dropped to `0` and `files.counts.build` is now `1`.

### 2) Frontend npm manifest detection

- Updated `.documentation/scripts/powershell/site-audit.ps1` to include known workspace manifests (`package.json`, `frontend/package.json`) and merge direct/dev dependency sets.
- Validation result: `packages.manager` now reports `multi`, with `npm_manifests` including `frontend/package.json`.

### 3) Cache hit tracking

- Updated `src/spark/unified_report_workflow.py` to count cache hits for:
  - user profile cache read,
  - repositories cache read,
  - per-repository commit counts cache read.
- Removed placeholder behavior and now returns measured `cache_hit_count`.

### 4) Learning streak implementation

- Updated `src/spark/calculator.py`:
  - Implemented learning streak calculation based on first-seen language introductions across commit history.
  - Added helpers for extracting commit language and repository language mapping.

### 5) Regression tests

- Added test in `tests/unit/test_calculator.py`:
  - `test_learning_streak_tracks_new_languages`
- Added test in `tests/unit/test_unified_report_workflow.py`:
  - `test_workflow_tracks_cache_hit_count`
- Validation result: targeted test run passed (`2 passed`).

### 6) Root version marker

- Added root `CHANGELOG.md` with current version heading and pointer to `documentation/CHANGELOG.md`.

### 7) Coverage gate

- Updated `.github/workflows/generate-stats.yml`:
  - Added `pytest-cov` install path via `requirements-dev.txt`.
  - Added `Enforce Core Module Coverage Gate` step (on push) requiring `>=80%` for core modules.

### 8) Validation rerun

- Site-audit pre-scan rerun succeeded and saved to:
  - `.documentation/copilot/audit/_latest_prescan_after_fixes.json`

## Current Coverage Gate Snapshot

Updated remediation check (targeted suite used for coverage recovery):

- `src/spark/fetcher.py`: 81.48% (PASS)
- `src/spark/cache.py`: 84.69% (PASS)
- `src/spark/summarizer.py`: 88.11% (PASS)
- `src/spark/unified_report_workflow.py`: 81.32% (PASS)

Command used:

- `python -m pytest tests/unit/test_coverage_remediation.py tests/unit/test_fetcher.py tests/unit/test_cache.py tests/unit/test_unified_report_workflow.py -q --cov=spark --cov-report=json:coverage-remediation.json`

Result: all previously failing coverage modules now meet the >=80% gate in the remediation run.
