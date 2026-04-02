# Repository Story: github-stats-spark

> Generated 2026-04-02 | Window: 12 months (95-day active history) | Scope: full

## Executive Summary

**github-stats-spark** is a dual-stack GitHub analytics platform that turns raw GitHub API data into a live, interactive intelligence product. Its Python backend fetches repository data, calculates proprietary scoring metrics, generates SVG visualizations, and optionally enriches results with AI-generated summaries via Anthropic Claude Haiku. Its React 19 frontend renders the unified JSON output as an interactive dashboard published to GitHub Pages — visible to anyone at the project's public URL without configuration or authentication.

The platform reached production-grade scale with remarkable velocity. In just 95 days (first commit: 2025-12-28, latest: 2026-04-02), the repository accumulated **225 commits** from **2 contributors**, delivered **6 major feature integrations** totalling over **100,000 lines of differential change**, and evolved from a single-purpose script into a governed multi-user analytics pipeline with a documented constitution, archived specifications, and automated weekly publishing.

Delivery cadence followed a classic build → consolidate → accelerate arc. January 2026 saw 113 commits — a founding sprint that established the architecture, AI integration, and initial dashboard. February dropped to 18 as the team absorbed complexity. March rebounded to 47 with a quality sprint (coverage gates, refactoring, spec closure). April has opened with 14 commits in its first two days alone, driven by schema 2.3.0 and DevSpark framework installation — signals of continued momentum.

Team posture is collaborative with clear ownership. Bus factor concentration is measurable but not alarming for a product at this stage: the Lead Architect holds 73% of commits (165 of 225), and Developer A contributes reliably every month. The structured handoff model — where Developer A owns automated weekly data regeneration — demonstrates intentional role separation and resilience for a two-person team.

The most important business signal is governance maturity. This project does not merely accumulate features; it accumulates process. A project constitution was authored, amended twice in one session, and is now enforced through automated site-audit tooling. Ten specification archives and four governance artifacts evidence a team practicing disciplined software lifecycle management at a scale most two-person teams do not attempt.

---

## Technical Analysis

### Development Velocity

Monthly commit distribution tells a story of three distinct phases:

| Month | Commits | Interpretation |
|-------|---------|---------------|
| 2025-12 | 33 | Bootstrap — architecture established, first SVG outputs |
| 2026-01 | 113 | Founding sprint — AI integration, Repository Comparison Dashboard, mobile-first UI |
| 2026-02 | 18 | Consolidation — absorbed January's structural complexity |
| 2026-03 | 47 | Quality sprint — spec closure, coverage gates, refactoring, security audit |
| 2026-04 | 14 (partial) | Enhancement cycle — schema 2.3.0, DevSpark migration |

January's 113-commit peak (50.2% of all commits) aligns with the two largest feature merges in the project's history: the Repository Comparison Dashboard (29,763 lines, 135 files) and the AI-Powered Repository Analysis v2.0.0 (21,986 lines, 59 files). These are not incremental additions — they represent foundational architectural layers that every downstream feature builds upon.

The most recent acceleration is April 2026. In just 2 calendar days, 14 commits landed covering: spec 001 merge (dashboard visual enhancements, 16,054 lines), user-scoped directory restructuring, `spark.yml` as single source of config truth, frontend heatmap and timeline components, and the DevSpark governance framework installation. This density signals a productively aggressive development pace with no signs of slowdown.

Commit subject analysis shows **87 feature commits** as the dominant category, followed by **65 CI/build commits** (reflecting a pattern of generated artifact updates via GitHub Actions automation), 16 refactors, 15 fixes, 10 documentation commits, and 4 test-focused commits. The 29% CI/build proportion is elevated but expected given the weekly automated data regeneration pipeline — Developer A's "[skip ci]" commits account for the bulk of that category.

### Contributor Dynamics

The project runs on a two-person model with clearly differentiated roles:

| Role | Commits | Share | Primary Pattern |
|------|---------|-------|----------------|
| Lead Architect | 165 | 73.3% | Feature work, refactoring, governance, planning |
| Developer A | 60 | 26.7% | Automated weekly data regeneration ([skip ci]) |

Bus factor for deliberate feature decisions is effectively 1. The Lead Architect authors all meaningful architectural changes. Developer A's role is production automation — running the weekly pipeline and committing generated outputs. This is an intentional design, not a risk oversight: the automated contributor cannot be a single point of failure for human decisions, only for data freshness.

Monthly continuity is consistent: both contributors are active every month in the window. No evidence of gaps or abrupt contraction. The April burst shows the Lead Architect operating at January-level intensity, which suggests feature commitment rather than maintenance mode.

### Quality Signals

Testing investment is substantial and structurally embedded. With **644 test files** against an estimated source corpus, the test infrastructure is deep. Twenty-six test-related commits reflect ongoing investment rather than a one-time test-writing episode. The project's constitution mandates >80% coverage for core modules — a target the team has enforced through automated coverage gates in GitHub Actions.

Commit message quality has improved since the prior story. Conventional commits now account for **65 of 225 (28.9%)**, up from 24.88% as of 2026-03-28. Prefix diversity includes `feat`, `fix`, `docs`, `chore`, `refactor`, and `test` — broader than the 3-prefix set observed in March. Six commits carry explicit spec references, demonstrating traceability between planned work and committed change. Only 1 informal commit is recorded in the window — effectively zero noise in the semantic signal set.

One quality observation: commit prefix `ci` does not yet appear in the conventional corpus, despite 65 CI/build subject-classified commits. Adopting the `ci:` prefix for GitHub Actions workflow and automated data commits would improve machine-readability and separate infrastructure signal from product signal.

### Governance & Process Maturity

Governance posture is the project's most distinctive technical signal relative to a typical two-person early-stage repository.

**Constitution**: `/.documentation/memory/constitution.md` exists, is versioned (v1.1.0), and has been amended twice via the CAP governance process. Current principles include Single Responsibility with explicit LOC thresholds (SHOULD <500, MUST justify 500–799, MUST split ≥800), Interface Stability, Test Discipline, Observable Operations, Performant Architecture, and the new Generated Artifact Boundary (Principle VI). The constitution governs tooling — `site-audit.ps1` reads exclusion paths from `config/spark.yml` and applies Principle VI automatically.

**Specification lifecycle**: 10 archived specification directories + 1 active spec. The archiving discipline means completed work cannot be mistaken for active work, and the archive serves as an audit trail of product decisions. Spec 001 (dashboard visual enhancements) was closed 2026-04-02 with 42 of 42 tasks completed.

**Merge discipline**: The window contains 10 merge commits (4.44% of total). The largest single merge introduced 29,763 differential lines — a feature branch of significant scope. PR-based merge rate is low (1 explicit PR merge), but the project compensates through AI-assisted code review and constitution-aware audit tooling, not through traditional PR volume.

**Release tags**: `total_tags = 0` remains the single most actionable governance gap. The project has shipped substantial capability across recognizable milestones (AI integration, comparison dashboard, schema 2.3.0) without a single semantic version tag. Adding `v0.1.0` through `v1.0.0` retroactively — or initiating the practice on the next delivery — would close the external release signal gap.

### Architecture & Technology

The technical fingerprint reflects a mature polyglot system:

| Signal | Detail |
|--------|--------|
| Languages | Python (backend), JavaScript/JSX (frontend), TypeScript (types), PowerShell (tooling), Shell (CI) |
| Framework | React 19 + Vite 8 (frontend), Click CLI + PyGithub (backend) |
| AI Integration | Anthropic Claude Haiku (optional summarization) |
| Build pipeline | Vite → `docs/` (GitHub Pages), Python spark CLI → `data/users/{user}/` |
| Automation | GitHub Actions weekly + manual dispatch |
| Config | `config/spark.yml` as single source of truth (enforced since 2026-04-02) |
| Governance | DevSpark framework (.devspark/), 21 agent/prompt shims |

The most significant architecture evolution in the April 2026 sprint was the shift to **user-scoped output paths** (`data/users/{username}/repositories.json`). Previously output was written to a flat `data/` root. The new structure enables multi-user generation with clean separation — a prerequisite for scaling from a personal analytics tool to a platform component.

`spark.yml` consolidation as single config source eliminates the "silent fallback" pattern that prior audits flagged. Configuration errors now surface immediately with actionable messaging rather than silently degrading to defaults.

---

## Change Patterns

The hotspot map separates generated artifacts from source code, consistent with Principle VI:

**Top source code hotspots (meaningful change signal):**

| File | Changes | Signal |
|------|---------|--------|
| `src/spark/unified_data_generator.py` | 28 | Active development; central pipeline integration point |
| `src/spark/fetcher.py` | 26 | API layer evolution; cache strategy refinements |
| `src/spark/cli.py` | 25 | CLI surface expanding with new commands and flags |
| `src/spark/unified_report_workflow.py` | 20 | Orchestration logic actively maintained |
| `frontend/src/App.jsx` | 19 | Root component absorbing routing/state complexity |
| `config/spark.yml` | 18 | Configuration surface growing with each feature |
| `src/spark/summarizer.py` | 14 | AI integration evolving (model updates, fallback logic) |
| `frontend/src/components/DrillDown/RepositoryDetail.jsx` | 11 | Drill-down detail view under active development |
| `src/spark/cache.py` | 11 | Cache layer refined across schema and strategy changes |

**Key observations:**

1. **`unified_data_generator.py` is the system's center of gravity** — 28 changes in 95 days signals this module shoulders the integration burden between API data, schema versioning, and output format. At this change rate, it is a refactoring candidate once the schema stabilizes.

2. **`fetcher.py` and `cli.py` are co-evolving** — both at 25–26 changes. The CLI expands the surface while the fetcher adapts to new data requirements. Both files carry size justification comments (834 and 767 LOC respectively), putting them in the MUST_JUSTIFY tier under Principle I.

3. **`config/spark.yml` at 18 changes** signals configuration-driven design succeeding: features are being added through config toggles rather than code paths — a positive extensibility signal.

4. **`frontend/src/App.jsx` at 19 changes** is moderately high for a root component. If routing logic or state management continues accreting, extracting a dedicated router and context provider would relieve the complexity.

5. **Generated artifact hotspots** (`output/reports/`, `docs/data/`, `output/*.svg`, `docs/*.html`) dominate the top 15 by raw change count (40–92 changes each). Per Principle VI, these are categorized as NOISE — generated artifact. They confirm the automated pipeline is running consistently, not that source files are unstable.

---

## Milestone Timeline

No semantic version tags exist in the repository. The following milestone table is reconstructed from major merge commits and feature boundary commits — it represents the release equivalent history even without formal tags:

| Date | Milestone | Lines Changed | Significance |
|------|-----------|--------------|-------------|
| 2025-12-28 | **Project inception** | — | First commit: spec analysis and remediation |
| 2025-12-28 | SVG visualizer + theme system | ~initial | Overview, heatmap, languages, streaks, fun, release SVGs |
| 2025-12-31 | AI-Powered Analysis v2.0.0 | 21,986 | Anthropic Claude Haiku integration, three-tier fallback |
| 2026-01-02 | **Repository Comparison Dashboard** | 29,763 | Side-by-side comparison, Recharts visualizations |
| 2026-01-03 | React ErrorBoundary | — | Resilience layer for frontend |
| 2026-01-18 | Unified pipeline + PowerShell automation | — | `spark unified` command, GitHub Actions integration |
| 2026-03-07 | Mobile-first UI redesign | 15,657 | Responsive layout, touch-optimized dashboard |
| 2026-03-14 | **Spec 001 validation closure** | 18,255 | PR #2 merged; test coverage gates enforced |
| 2026-03-28 | Commit statistics + attention insights | — | Spark score enhancements, markdown summary rendering |
| 2026-04-02 | **Dashboard visual enhancements (Spec 001)** | 16,054 | Contribution heatmap, activity timeline, dark mode, bus factor |
| 2026-04-02 | User-scoped output paths | — | Multi-user architecture prerequisite |
| 2026-04-02 | DevSpark migration from Spec Kit 1.5.1 | — | Governance framework upgrade |
| 2026-04-02 | Constitution v1.1.0 (CAP-2026-001, CAP-2026-002) | — | LOC thresholds + Generated Artifact Boundary enforced |

Velocity context: the three largest merges all occurred within the first 5 weeks. The project's architectural skeleton was assembled at high speed, and subsequent sprints have been hardening, enhancing, and governing that foundation.

---

## Constitution Alignment

Constitution v1.1.0 (amended 2026-04-02) | 6 Principles + Governance

| Principle | Evidence | Assessment |
|-----------|----------|------------|
| **I. Single Responsibility** | Module separation: fetcher, calculator, visualizer, ranker, summarizer, cache each with distinct responsibilities. `fetcher.py` (834 LOC) and `cli_handlers.py` (767 LOC) carry MUST_JUSTIFY annotations. | **Strong** — boundary violations documented and justified, not ignored |
| **II. Interface Stability** | `repositories.json` versioned at schema 2.3.0; breaking changes tracked in CHANGELOG; frontend contract documented in `frontend-repositories-json-guide.md` | **Strong** — schema versioning discipline evident |
| **III. Test Discipline** | 644 test files, 26 test-related commits, constitution-mandated >80% core module coverage, coverage gate in GitHub Actions | **Strong** — automated enforcement in CI |
| **IV. Observable Operations** | `--verbose` flag on CLI, stdout/stderr logging throughout, GitHub Actions logs on every run | **Strong** — no silent failures pattern is architecturally embedded |
| **V. Performant Architecture** | `spark unified` single-pass, pushed_at content-addressed cache, <5 min constitutionally mandated | **Good** — cache in active development (11 changes), no perf regression evidence |
| **VI. Generated Artifact Boundary** | `config/spark.yml` scan exclusions; `site-audit.ps1` reads exclusions dynamically; hotspot audit classifies generated paths as NOISE | **Strong** — principle is operational the same day it was ratified |
| **Governance** | Constitution history tracked, CAP process used for amendments, proposals archived with decision dates | **Strong** — governance is practiced, not aspirational |

**Overall alignment: HIGH.** The commit history does not contradict the constitution — it predates and independently validates it. The governance artifacts formalize patterns that were already emerging in the codebase.

---

*Generated by /devspark.repo-story | DevSpark — Adaptive System Life Cycle Development*
