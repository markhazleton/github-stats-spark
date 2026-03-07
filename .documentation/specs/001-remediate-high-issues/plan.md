# Implementation Plan: Audit High-Issue Remediation

**Branch**: `001-remediate-high-issues` | **Date**: 2026-03-07 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/.documentation/specs/001-remediate-high-issues/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.documentation/templates/commands/plan.md` for the execution workflow.

## Summary

Remediate the six HIGH audit findings by restoring configuration-driven theme selection, correcting dashboard aggregate totals, raising calculation and visualization verification coverage above the constitutional gate, extracting non-conflicting CLI and cache helper modules, and clarifying repository documentation ownership without breaking the existing public-repository, cache, and output contracts.

## Technical Context

**Language/Version**: Python 3.11+ backend, PowerShell 7 automation, Markdown documentation artifacts  
**Primary Dependencies**: PyGithub, PyYAML, svgwrite, tenacity, pytest/pytest-cov, existing theme helpers in `spark.visualizer`  
**Storage**: Filesystem-backed YAML, Markdown, SVG, JSON, and `.cache` content-addressed cache  
**Testing**: pytest, pytest-cov, targeted PowerShell script smoke checks, existing WCAG/theme unit tests, and dedicated CLI/cache-manager regression harnesses  
**Target Platform**: Windows development environment and GitHub Actions Linux runners
**Project Type**: Dual-stack CLI/report generator with static dashboard assets and Spec Kit planning automation  
**Performance Goals**: Preserve constitutional runtime under 5 minutes for <500 repositories and avoid introducing extra API calls during unchanged runs  
**Constraints**: Public repositories only, deterministic outputs, no silent failures, WCAG AA visual output, no cache key contract changes, minimal dependency growth  
**Scale/Scope**: Changes span `src/spark/`, `tests/unit/`, `.documentation/scripts/powershell/`, `.documentation/templates/`, `.github/agents/`, and feature artifacts under `.documentation/specs/001-remediate-high-issues/`

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Single Responsibility**: PASS after design. The plan isolates refactoring into bounded helper modules for CLI layout, CLI argument construction, cache filtering, cache refresh coordination, and workflow orchestration without converting existing top-level modules into packages mid-feature.
- **II. Data Privacy**: PASS. No design step introduces private-repository handling; existing `exclude_private` and repository validation behavior remains mandatory.
- **III. Fail Fast, Fail Loud**: PASS. The plan routes theme resolution through existing config validation paths and removes placeholder output values rather than masking them.
- **IV. Change-Driven Caching**: PASS. Cache key shape and `pushed_at` invalidation remain unchanged; refactoring is constrained to orchestration and reporting surfaces.
- **V. Accessibility First**: PASS. Theme selection remediation uses validated theme helpers and expands visualizer test coverage without relaxing WCAG checks.
- **Quality Gates**: PASS with work required. The implementation must demonstrate the constitutional threshold for core calculation and visualization verification before completion and must preserve deterministic outputs.
- **Governance/Documentation**: PASS with explicit classification. Speckit planning artifacts remain under `.documentation/`, user-facing project docs remain under `documentation/`, and generated-output Markdown must be cataloged as exceptions or output metadata rather than treated as primary user docs.

**Post-Design Re-check**: PASS. Phase 1 artifacts resolve planning unknowns without requiring a constitution exception. No gate violations need justification.

## Project Structure

### Documentation (this feature)

```text
.documentation/specs/001-remediate-high-issues/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/
└── spark/
    ├── cli.py
    ├── cli_argument_builders.py
    ├── cli_output_layout.py
    ├── cache_manager.py
    ├── cache_refresh_strategy.py
    ├── cache_repository_filter.py
    ├── dashboard_generator.py
    ├── unified_report_workflow.py
    ├── visualizer.py
    ├── config.py
    ├── cache.py
    ├── themes/
    └── models/

tests/
├── unit/
│   ├── test_calculator.py
│   ├── test_cli.py
│   ├── test_cache_manager.py
│   ├── test_visualizer.py
│   ├── test_config.py
│   └── test_wcag.py
└── integration/

.documentation/
├── scripts/powershell/
├── templates/
└── specs/001-remediate-high-issues/

.github/
└── agents/

documentation/
├── guides/
├── api/
└── architecture/
```

**Structure Decision**: Use the existing Python backend and test layout for runtime remediation, keep top-level modules such as `cli.py` and `cache.py` in place, add non-conflicting helper modules named `cli_output_layout.py`, `cli_argument_builders.py`, `cache_repository_filter.py`, and `cache_refresh_strategy.py`, keep Speckit planning artifacts under `.documentation/specs/001-remediate-high-issues/`, and limit documentation-governance changes to classification and path-alignment work in `.documentation/`, `.github/agents/`, and `documentation/` rather than redesigning the frontend application.

## Complexity Tracking

No constitution violations require justification for this plan.

## Completion Notes

- Implementation completed across runtime, tests, documentation governance, and audit workflow guidance.
- Runtime remediation now resolves visualization themes through shared configuration helpers and computes dashboard aggregate totals from the included repository set.
- Architecture remediation extracted dedicated CLI handler and cache refresh executor modules in addition to the planned helper boundaries so the follow-up audit could clear the remaining HIGH responsibility findings.
- Governance remediation updated contributor guidance, approved README exception handling, constitution language, and remaining agent prompts that referenced unsupported legacy path patterns.

## Final Validation Status

- `python -m spark.cli config --validate`: passed
- Focused remediation pytest run: passed (`52 passed`)
- Broader regression and coverage pytest run: passed (`79 passed`)
- Follow-up site audit: passed with no remaining HIGH findings
- Local bounded generation run via `run-spark-local.ps1 -Screenshots -MissingOnly`: passed
