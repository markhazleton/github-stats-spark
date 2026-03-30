# Repository Story: github-stats-spark

> Generated 2026-03-28 | Window: 12 months (covers full 90-day history) | Scope: full

## Executive Summary

This repository is a dual-stack GitHub analytics product that combines a Python analysis pipeline with a React dashboard and generated publishing artifacts. The technology footprint and file activity indicate a system that ingests repository data, computes statistics, and publishes visual/report outputs. Evidence includes active Python (`.py`), JavaScript/TypeScript (`.js`, `.jsx`, `.ts`), and workflow automation artifacts, with committed outputs under `output/`, `data/`, and `docs/`.

The project reached meaningful delivery scale quickly: 201 total commits across 2 contributors in a 90-day span (first commit: 2025-12-28, latest commit: 2026-03-28). Contributor distribution is concentrated but collaborative, with 144 commits (Lead Architect) and 57 commits (Developer A). This is a high activity level for an early-stage product and suggests rapid iteration from inception to feature-rich delivery.

Velocity was front-loaded and then normalized. Monthly commit volume moved from 33 (2025-12) to 113 (2026-01), then down to 18 (2026-02), and up to 37 (2026-03). The January peak is consistent with initial architecture and feature assembly, while February and March indicate a transition into consolidation and follow-on enhancements.

Governance signals are mixed but improving. Merge activity exists (10 merge commits, 4.98% of commits), but explicit PR-style merge evidence is limited (`merged_pr_count = 1`). Commit message standardization is partial (50 conventional commits, 24.88% adoption), and the repository currently has no release tags (`total_tags = 0`), which limits externally visible release milestone discipline.

Delivery evidence is strong despite no tags: the commit log shows major feature merges, sustained README evolution (14 README commits), and recurring generated outputs. In business terms, this is a fast-moving, implementation-heavy phase with clear product momentum and an opportunity to harden release/process maturity.

## Technical Analysis

### Development Velocity

Commit trend shows a launch spike then stabilization: 33 commits in 2025-12, 113 in 2026-01, 18 in 2026-02, and 37 in 2026-03 (201 total). January accounts for 56.22% of all commits, indicating concentrated build-out.

Code volume is substantial: 609,197 lines added and 508,715 deleted in-window. The churn ratio is 0.835 ($508,715 / 609,197$), which indicates high rewrite/refactor pressure rather than strictly additive greenfield coding. In practical terms, this pattern usually reflects rapid refinement, generated artifact turnover, and architectural evolution happening concurrently.

No `--compare-baseline` override was requested, so baseline delta analysis was not applied beyond month-by-month trend observation.

### Contributor Dynamics

Contributor census is a two-person team throughout the observed period: Lead Architect (144 commits) and Developer A (57 commits). Bus factor concentration is material: the top contributor owns 71.64% of commits ($144 / 201$), leaving 28.36% to the second contributor.

Monthly participation indicates continuity rather than episodic contribution. Both roles are active each month: Dec (21/12), Jan (90/23), Feb (9/9), Mar (24/13). This suggests no abrupt team contraction, but leadership concentration remains a delivery risk if unmitigated.

### Quality Signals

Testing investment appears high by file inventory and moderate by commit-topic frequency. `test_file_count` is 630 and estimated source files are 123, giving a test-to-source ratio of 5.12:1. Test-related commit subjects account for 22 commits, indicating ongoing but not dominant test-focused change flow.

Commit hygiene is partially standardized. Conventional commits are 50 of 201 (24.88%), with 1 clearly informal commit in the measured set. Average commit subject length is 62.29 characters, generally long enough to be descriptive. Conventional prefix diversity is low (3 distinct prefixes: `feat`, `fix`, `docs`), implying room to improve semantic granularity (for example `refactor`, `test`, `chore`, `ci`).

### Governance & Process Maturity

Merge commit percentage is 4.98% (10 of 201), which signals some branch-based integration but not strong evidence of a strict PR-gated workflow. The context metric `merged_pr_count = 1` reinforces that explicit PR merge labeling is limited or inconsistently represented in commit subjects.

Tag discipline is currently absent (`total_tags = 0`), so release cadence is not externally codified through semantic tags. This is the largest governance maturity gap for downstream stakeholders who rely on stable release checkpoints.

Branch strategy signals show occasional large integrations (`largest_merges` include changesets up to 29,763 lines across 135 files), suggesting feature-branch aggregation does occur. The process would be more auditable with consistent PR metadata and tagged release anchors.

### Architecture & Technology

Technical signals confirm a polyglot repository with Python, JavaScript, TypeScript, PowerShell, shell, and Markdown present. This aligns with a backend analytics + frontend dashboard + automation toolchain architecture.

Configuration maturity is selective: GitHub Actions are present (`has_github_actions = true`), while Dockerfile, root `package.json`, and `pyproject.toml` are absent. The repo appears to rely on mixed Python packaging and frontend-local tooling rather than a single root orchestrator.

Hotspot concentration (especially in generated outputs and publishing artifacts) indicates a pipeline-centric architecture where regeneration and publication are first-class operations. This is efficient for continuous publishing but can inflate churn noise unless generated files are partitioned cleanly from source review paths.

## Change Patterns

Top 5 most-modified files:

1. `output/fun.svg` (85 changes)
2. `output/reports/markhazleton-analysis.md` (84)
3. `data/repositories.json` (80)
4. `docs/data/repositories.json` (68)
5. `docs/index.html` (62)

Interpretation:

- The top hotspots are predominantly generated or publish-surface artifacts, which implies frequent full-pipeline regeneration.
- This supports fast feedback for output quality, but it can obscure source-level intent during code review.
- Source hotspots such as `src/spark/unified_data_generator.py` (25), `src/spark/cli.py` (25), and `src/spark/fetcher.py` (22) indicate core orchestration and ingestion logic as active complexity centers.

Directory-level concentration (from hotspot aggregation):

- `docs`: 586
- `output`: 362
- `src`: 113
- `data`: 80
- `frontend`: 64
- `.cache`: 42

This pattern suggests deployment/output surfaces account for most file-touch volume, while core application logic remains active but comparatively less noisy.

## Milestone Timeline

No tagged milestones were found (`milestones.tags` is empty; `total_tags = 0`), so a release-tag timeline cannot be constructed for this period.

## Constitution Alignment

Constitution file detected at `.documentation/memory/constitution.md`; alignment assessment based on commit-history signals:

Strong alignment signals:

- Fail-fast/observability intent is supported by active workflow/config and frequent operational commits (including CI/build-classified subjects: 60).
- Single-responsibility architecture appears directionally aligned with modular hotspots in `src/spark/` (`fetcher`, `cli`, `unified_*` modules updated independently).
- Documentation governance appears active (14 README commits, dedicated documentation artifact activity).

Partial or weak alignment signals:

- Process maturity is below constitution ambition in release governance: no semantic tags despite sustained delivery.
- Commit convention adoption (24.88%) is below what would be expected for highly observable governance at scale.
- Large generated-artifact churn can make quality and determinism auditing harder unless review boundaries are enforced.

Not directly verifiable from commit metadata alone:

- Private repository exclusion correctness and WCAG compliance cannot be fully proven by history metrics alone; they require targeted validation runs and output audits.

Overall alignment: medium. Architectural and delivery behavior generally supports constitutional direction, while release governance and commit-process discipline are the main gaps.

## Value Proposition: The Developer Portfolio Problem

### The Pain Point

A working developer accumulates repositories the way a workshop accumulates projects — prototypes, experiments, client work, side ideas, abandoned starts, and genuine portfolio pieces all live side by side. GitHub profiles surface none of this context. A visitor sees a flat list of repository names sorted by last push date, and the developer themselves loses track of which projects are stale, which have open security alerts, and which ones actually represent their best work.

Existing tools don't solve this. **github-readme-stats** (the most popular alternative) generates static SVG badges showing star counts, commit totals, and top languages — vanity metrics that tell a viewer nothing about what a developer actually built or whether any of it is maintained. Profile README generators are one-time cosmetic templates. External platforms like CodersRank or GitRoll require surrendering data to third-party services and offer no self-hosted, embeddable output.

The gap is clear: no existing tool transforms a GitHub account into an **intelligible, self-maintaining portfolio** that a developer can use to understand their own work and present it to others.

### How Stats Spark Solves It

Stats Spark treats a GitHub profile as a body of work that deserves curation — and then automates that curation entirely.

**1. AI-Generated Project Summaries That Explain What You Built**

Every repository gets a technical summary written by Claude Haiku, drawing from the README, commit patterns, language distribution, and dependency graph. A three-tier fallback chain (AI → README extraction → metadata template) ensures 97%+ coverage even for repos with no documentation. The result: a visitor (or the developer themselves) can understand what each project does without reading source code.

This matters most for the developer with 30-50+ repositories. Those dormant-but-interesting projects — the CLI tool from two years ago, the prototype API, the experiment with a new framework — become discoverable again because each one has a clear, generated description of its purpose and technical approach.

**2. Maintenance Triage That Surfaces What Needs Attention**

The "Needs Attention" dashboard ranks every repository by a composite maintenance score (35% security alerts, 25% open PR backlog, 25% staleness, 15% dependency drift) and assigns a tier: Critical, Elevated, Watch, or Healthy. Summary cards show total critical repos, security backlog, and stale project counts at a glance.

For a developer managing many repositories, this is the difference between "I should probably check on things" and a prioritized action list. The staleness signal alone (days since last push, recent 90-day commit count) prevents projects from silently rotting.

**3. Composite Ranking That Tells Your Story**

The repository ranker uses a weighted algorithm (30% popularity + 45% activity with multi-window time decay + 25% health signals) to surface a developer's most significant active work. Time-decay windows ensure that a project with 5 commits this month ranks above a project with 500 commits two years ago. Archived repos and forks are automatically penalized so the ranking reflects original, maintained work.

Combined with the Spark Score (40% consistency + 35% volume + 25% collaboration), a viewer gets a genuine signal about a developer's working patterns — not just "this person made 3,000 commits" but "this person contributes consistently, maintains their projects, and works across multiple technologies."

**4. Zero-Maintenance, Self-Hosted, Free**

The entire pipeline runs on a weekly GitHub Actions schedule. No external service, no subscription, no manual updates. Generated artifacts (SVGs, JSON data, interactive dashboard) deploy to GitHub Pages automatically. A developer sets it up once and gets a living, always-current portfolio that costs nothing to operate.

### Unique Differentiators vs. Existing Tools

| Capability | Stats Spark | github-readme-stats | CodersRank / GitRoll | Manual Portfolio |
|---|---|---|---|---|
| AI-generated project summaries | ✅ Claude Haiku with 3-tier fallback | ❌ | ❌ | ❌ (manual writing) |
| Maintenance triage (security, staleness, PRs) | ✅ Tiered scoring system | ❌ | Partial | ❌ |
| Time-decay activity ranking | ✅ Multi-window (90d/180d/365d) | ❌ (all-time totals only) | Partial | ❌ |
| Interactive drill-down dashboard | ✅ Mobile-first, WCAG AA | ❌ (static SVGs only) | ✅ (third-party hosted) | ❌ |
| Repository comparison (up to 5) | ✅ Side-by-side with diff visualization | ❌ | Partial | ❌ |
| Self-hosted on GitHub Pages | ✅ Zero cost | N/A (embed only) | ❌ (external platform) | ✅ (manual effort) |
| Automated weekly refresh | ✅ GitHub Actions | ✅ (on-demand embed) | ✅ | ❌ |
| Deterministic scoring algorithm | ✅ Spark Score (open formula) | ❌ | ❌ (proprietary) | N/A |
| Dependency health tracking | ✅ Currency score + outdated count | ❌ | ❌ | ❌ |
| Technology diversity analysis | ✅ Polyglot tracking across repos | ✅ (top languages only) | ✅ | ❌ |

### The Core Value

Stats Spark's unique position is that it is the only tool that combines **AI-powered content understanding** (what did you build?), **maintenance intelligence** (what needs your attention?), and **activity-weighted ranking** (what represents your best current work?) into a single, free, self-hosted pipeline. It turns a GitHub account from a flat list of repository names into a curated, always-current developer portfolio with genuine analytical depth.

For the developer with dozens of repositories and various ideas they want to keep current, Stats Spark answers the three questions that no other tool addresses together: *What have I built? What's falling behind? What should I showcase?*

---
*Generated by /speckit.repo-story | Spec Kit Spark - Adaptive System Life Cycle Development*
