# Implementation Plan: Dashboard Visual Enhancements

**Branch**: `001-dashboard-visual-enhancements` | **Date**: 2026-04-02 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/.documentation/specs/001-dashboard-visual-enhancements/spec.md`

## Summary

Enhance the React dashboard with interactive visualizations (trailing-365-day contribution heatmap calendar, multi-series activity timeline), a manual dark mode toggle, commit volume metrics, and bus factor indicators — all supplementing existing SVG outputs. The key architectural insight is that `commits_by_day` is already calculated in the Python backend but not persisted in the JSON export; exposing it (plus a few new fields) unlocks the highest-value frontend features with minimal backend changes.

## Technical Context

**Language/Version**: Python 3.11+ backend, React 19 + Vite frontend  
**Primary Dependencies**: PyGithub (backend), Chart.js + react-chartjs-2 (frontend) — NOT Recharts  
**Storage**: JSON files (`data/repositories.json`), file-based cache (`.cache/`)  
**Testing**: pytest (backend), Vitest (frontend)  
**Target Platform**: GitHub Pages static site + Python CLI  
**Project Type**: CLI + static web dashboard (dual-stack)  
**Performance Goals**: `spark unified` <5 minutes for <500 repos; dashboard page load <2 seconds  
**Constraints**: GitHub API 5000 req/hr; no SVG modifications; zero new frontend dependencies (heatmap is custom CSS Grid)  
**Scale/Scope**: Typically 50-200 repositories per user profile

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| **I. Single Responsibility** | PASS | New metrics added to calculator.py; new components are independent React files |
| **II. Data Privacy** | PASS | Only public repos; no new data sources beyond public GitHub API |
| **III. Fail Fast, Fail Loud** | PASS | Contributor/code-frequency fetches require timestamped degradation logs and explicit 1s/2s/4s/8s backoff before fallback |
| **IV. Change-Driven Caching** | PASS | New API calls (contributor stats) cached via existing pushed_at strategy |
| **V. Accessibility First** | PASS | Dark mode must meet WCAG AA; FR-012 explicitly requires 4.5:1 contrast |

| Quality Gate | Status | Notes |
|--------------|--------|-------|
| Test Coverage >80% core | PASS | New calculator methods need tests; new components need explicit Vitest coverage tasks |
| Execution <5 min | PASS | SC-010 limits additional time to 10%; contributor stats are 1 call/repo, cached |
| Accuracy <1% | PASS | Bus factor is deterministic from contributor data |
| Determinism | PASS | Same input → same output for all new metrics |
| SVG <500KB | N/A | No SVG changes |

**No violations. Gate passes.**

## Project Structure

### Documentation (this feature)

```text
.documentation/specs/001-dashboard-visual-enhancements/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (JSON schema changes)
└── tasks.md             # Phase 2 output (created by /speckit.tasks)
```

### Source Code (repository root)

```text
# Backend changes
src/spark/
├── calculator.py            # Add bus_factor calculation
├── fetcher.py               # Add contributor stats fetching
├── unified_data_generator.py # Persist commits_by_day + new fields in JSON
└── models/
    └── commit.py            # Add ContributorStats model (if needed)

# Frontend changes
frontend/src/
├── components/
│   ├── Visualizations/
│   │   ├── ContributionHeatmap.jsx    # NEW: Calendar heatmap
│   │   ├── ContributionHeatmap.module.css
│   │   ├── ActivityTimeline.jsx       # NEW: Multi-series timeline
│   │   └── ActivityTimeline.module.css
│   ├── Common/
│   │   ├── ThemeToggle.jsx            # NEW: Dark/light mode toggle
│   │   ├── ThemeToggle.module.css
│   │   └── ExportButton.jsx           # EXISTING: Already supports CSV+JSON
│   └── DrillDown/
│       └── RepositoryDetail.jsx       # MODIFY: Add commit volume + bus factor
├── contexts/
│   └── ThemeContext.jsx               # NEW: Theme state provider
├── styles/
│   └── global.css                     # MODIFY: Add CSS custom properties + toggle
└── services/
    └── metricsCalculator.js           # MODIFY: Add heatmap/timeline data aggregation

# Tests
tests/unit/
└── test_calculator.py                 # Add bus factor + contributor tests
frontend/tests/
├── ContributionHeatmap.test.jsx       # NEW
├── ActivityTimeline.test.jsx          # NEW
└── ThemeToggle.test.jsx               # NEW
```

**Structure Decision**: Dual-stack with backend modifications in `src/spark/` and frontend additions in `frontend/src/components/`. No new top-level directories needed.

## Verification Focus

- Frontend test coverage includes explicit Vitest tasks for `ContributionHeatmap`, `ActivityTimeline`, and `ThemeToggle`.
- Dashboard verification includes heatmap load timing, theme-switch latency and layout stability, filtered export compatibility with spreadsheet tools, and representative manual bus-factor spot checks.
- Backend verification confirms degraded API paths log clearly while preserving the existing unified-command runtime budget.

## Complexity Tracking

No constitution violations — table not needed.
