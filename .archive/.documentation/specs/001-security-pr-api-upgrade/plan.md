# Implementation Plan: Repository Security and PR Signals

**Branch**: `001-security-pr-api-upgrade` | **Date**: 2026-03-14 | **Spec**: `.documentation/specs/001-security-pr-api-upgrade/spec.md`
**Input**: Feature specification from `.documentation/specs/001-security-pr-api-upgrade/spec.md`

## Summary

Add repository-level pull request and security enrichment to the unified GitHub dataset by extending the existing fetch -> cache refresh -> assemble pipeline. The implementation will keep the `repositories.json` contract additive, record explicit availability states for permission-sensitive security data, and stage GitHub REST API migration to `2026-03-10` behind validation gates instead of switching the entire integration at once.

The implementation must continue enforcing public-repository-only processing before any enrichment runs, add explicit observability for staged API-upgrade decisions, and define mitigation/reporting behavior if enrichment pushes runtime beyond the existing budget.

## Technical Context

**Language/Version**: Python 3.11+ backend, JavaScript/React 19 frontend  
**Primary Dependencies**: PyGithub 2.1.1+, requests, tenacity, PyYAML, pytest, Vitest, Vite 7  
**Storage**: File-based outputs in `data/`, `output/`, `docs/`; content-addressed cache in `.cache/`  
**Testing**: `pytest` for backend unit/integration coverage, `vitest` for frontend contract consumers when needed  
**Target Platform**: Cross-platform CLI execution and GitHub Actions on Windows/Linux/macOS with GitHub.com REST API  
**Project Type**: Dual-stack CLI analytics pipeline with static dashboard consumer  
**Performance Goals**: Keep standard unified generation under 5 minutes for fewer than 500 repositories; preserve zero unnecessary API calls for unchanged repositories  
**Constraints**: Public repositories only, no silent failures, additive schema evolution, explicit unavailable states for permission-limited fields, no TTL-based cache invalidation, no new dependency unless justified  
**Scale/Scope**: Up to 500 repositories per run, one additive repository contract revision, targeted backend pipeline changes with optional dashboard consumption follow-up

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Pre-Design Gates**

- **Single Responsibility**: PASS. Planned changes stay separated across fetching (`fetcher.py`), caching/refresh (`cache_manager.py`), repository modeling (`models/repository.py`), and output assembly (`unified_data_generator.py`).
- **Data Privacy**: PASS. Existing `exclude_private=True` flow remains authoritative, and new enrichment only applies to already included public repositories.
- **Fail Fast, Fail Loud**: PASS. Enrichment failures will be logged with repository context and surfaced in output as `partial` or `unavailable`, not silently dropped.
- **Change-Driven Caching**: PASS. New repository enrichment caches will follow the existing `pushed_at`-based invalidation strategy and respect force-refresh behavior.
- **Accessibility First**: PASS. This feature is primarily backend/data-contract work. Any later dashboard exposure must remain additive and preserve WCAG AA expectations.
- **Quality Gates**: PASS WITH VALIDATION. New enrichment must preserve deterministic output, runtime budget, and testability; verification is required before implementation closes.

**Post-Design Re-Check**

- **Single Responsibility**: PASS. Data model and contract split keeps runtime behavior, transport contract, and migration guidance independent.
- **Data Privacy**: PASS. Security contract explicitly models unavailable states for admin-only signals instead of attempting broader collection.
- **Fail Fast, Fail Loud**: PASS. Contract requires availability status and collection reasons, and quickstart validation includes partial-result behavior.
- **Change-Driven Caching**: PASS. Research and contracts assume repository-scoped cached summaries keyed from the repository change signal, avoiding independent TTL refreshes.
- **Quality Gates**: PASS. Planned rollout gates include runtime measurement, schema validation, and compatibility testing under both default and explicit API versions.

## Execution Notes

- Privacy enforcement remains a blocking prerequisite: enrichment code must run only after the existing public-repository filters complete, and regression coverage must prove private repositories never receive PR or security enrichment.
- Enrichment caching must stay content-addressed by repository `pushed_at`, must not introduce TTL refreshes, and must honor the existing force-refresh path.
- Runtime validation must include mitigation or explicit budget-exceeded reporting if the added enrichment prevents standard runs from staying within the under-5-minute target. Candidate mitigations include: capping per-repo open-PR pages (max 3 pages / 100 PRs), skipping enrichment beyond a configurable repository limit, parallelizing enrichment requests where rate limits allow, and logging a budget-exceeded warning while continuing output without enrichment.
- Enrichment data (PR/security summaries) is cached per repository using `pushed_at` as the change signal. Because PR and security state can change without a repository push, consumers should understand that cached enrichment reflects the state at the last push. Use `--force-refresh` to bypass the cache when fresher data is needed.
- Upgrade rollout validation must surface the current staged-version decision in logs or generated artifacts rather than limiting that decision to static planning documents.

## Project Structure

### Documentation (this feature)

```text
.documentation/specs/001-security-pr-api-upgrade/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── repositories-json.md
└── tasks.md
```

### Source Code (repository root)

```text
src/
└── spark/
    ├── cache.py
    ├── cache_manager.py
    ├── fetcher.py
    ├── unified_data_generator.py
    ├── unified_report_workflow.py
    ├── dashboard_generator.py
    └── models/
        └── repository.py

tests/
├── fixtures/
├── integration/
└── unit/

frontend/
├── src/
└── tests/
```

**Structure Decision**: Use the existing dual-stack repository structure, but limit primary implementation work to the Python backend pipeline and the exported `data/repositories.json` contract. Frontend changes remain optional consumers of the new fields rather than part of the core collection design.

## Complexity Tracking

No constitution violations or special complexity justifications are required for this plan.
