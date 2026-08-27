---
description: Diagnose and fix the repository issues preventing a perfect evaluation score
---

# Fix Score Remediation

You are working in the `github-stats-spark` repository. Your goal is to identify, fix, and verify the concrete issues that prevent this repository from reaching a perfect evaluation score.

Use this as an implementation prompt, not a report-only prompt. Make code, configuration, documentation, or generated-artifact changes when they are justified by evidence from the repo.

## Inputs

Optional user context:

```text
$ARGUMENTS
```

If `$ARGUMENTS` mentions a specific user, repo, score category, audit file, or failing gate, prioritize that scope. Otherwise use the current default user from `config/spark.yml`.

## Required Context

Read these files before making changes:

- `.github/copilot-instructions.md`
- `.documentation/memory/constitution.md`
- `config/spark.yml`
- Latest audit report under `.documentation/copilot/audit/`
- `data/users/<default-user>/repositories.json`
- `output/users/<default-user>/reports/screenshot-audit.md`, if it exists
- `frontend/package.json`
- `requirements.txt`
- `requirements-dev.txt`

Use generated data as evidence, but do not hand-edit generated JSON, SVG, screenshots, or `docs/` outputs except by rerunning the project generators.

## Scoring Inputs To Account For

Build an issue list from every applicable scoring input. Account for inputs that
are low, false, missing, stale, unavailable, or contradicted by audit output.

Repository attention score, where lower is better:

- Formula: `pull_requests * 0.25 + security * 0.35 + staleness * 0.25 + dependencies * 0.15`.
- Repository-level fields: `attention_score`, `attention_rank`, `attention_metrics.score`, `attention_metrics.tier`, `attention_metrics.needs_attention`, and `attention_metrics.reasons`.
- Pull request inputs: `attention_metrics.components.pull_requests.score`, `availability`, `reason`, `total_open`, `draft_count`, `review_requested_count`, and `oldest_open_age_days`.
- Security inputs: `attention_metrics.components.security.score`, `availability`, `reason`, `overall_state`, plus `active_alert_counts.total_open`, `critical`, `high`, `medium`, and `low`.
- Staleness inputs: `attention_metrics.components.staleness.score`, `days_since_last_push`, `recent_commits_90d`, and `open_issues`. Repos with open issues and zero recent commits receive extra pressure.
- Dependency inputs: `attention_metrics.components.dependencies.score`, `total_dependencies`, `outdated_count`, `outdated_percentage`, `currency_score`, `version_coverage_percentage`, `latest_version_coverage_percentage`, and `unknown_versions_count`.
- Dependency record inputs: for every dependency in `tech_stack.dependencies`, account for `name`, `source_file`, `ecosystem`, `current_version`, `version_requirement`, `current_version_known`, `latest_version`, `latest_version_status`, `latest_version_source`, `versions_behind`, `is_outdated`, and `status`.

Repository composite ranking score, where higher is better:

- Formula: `popularity * 0.30 + activity * 0.45 + health * 0.25`, using the weights in `config/spark.yml`.
- Popularity inputs: `stars`, `forks`, and `watchers`.
- Activity inputs: `commit_history.total_commits`, `recent_90d`, `recent_180d`, `recent_365d`, `last_commit_date`, `pushed_at`, and `days_since_last_push`.
- Health inputs: `has_readme`, `age_days`, total commits, `open_issues`, recent 90-day commits, `stars`, `forks`, and fork/star ratio.
- Edge-case inputs: `is_archived`, `is_fork`, `fork_info.commits_ahead`, `fork_info.commits_behind`, `is_private`, missing `pushed_at`, and very small `size_kb`.

Profile Spark Score, where higher is better:

- Formula: `consistency * 0.40 + volume * 0.35 + collaboration * 0.25`.
- Consistency inputs: commit timestamps, weekly commit counts, variance, and active-week coverage.
- Volume inputs: total commit count.
- Collaboration inputs: repository `stars`, `forks`, `watchers`, and profile `followers`.

Quality, community, README, website, and audit inputs:

- Repository quality flags: `has_readme`, `has_license`, `has_ci_cd`, `has_tests`, and `has_docs`.
- Community health fields, if generated: `has_discussions`, `has_contributing`, `has_code_of_conduct`, `has_security_policy`, `topics`, `issue_close_ratio`, `release_count`, `latest_release_tag`, and `latest_release_date`.
- README quality fields, if generated: `readme_quality_score.score`, `length`, `has_headings`, `has_code_blocks`, `has_images`, and `has_install_section`. Inspect the README directly for links because links contribute to the score even when the cached summary does not expose a `has_links` flag.
- Website fields: `homepage`, `website_url`, `pages_url`, `has_pages`, `homepage_status`, `homepage_response_ms`, and `screenshot_audit.status`, `flags`, `url`, and image diagnostics.
- Diagnostics fields: `diagnostics_summary.availability`, `reason`, `issues.total_open`, `issues.stale_over_30d`, `issues.stale_over_90d`, `actions.recent_runs`, `actions.failure_count`, `actions.last_run_status`, `actions.last_run_conclusion`, `security.dependabot.*`, and `security.code_scanning.*`.
- Latest DevSpark/site-audit findings under `.documentation/copilot/audit/`.
- Verification gates: `npm audit`, `pip-audit`, lint, format, tests, frontend build, dashboard postbuild, and screenshot audit.
- Any stale TODO/task-ID comments or constitution violations.

If a field appears in scoring code but is missing from generated dashboard data,
inspect the matching cache category or per-repository detail JSON before deciding
it is not a blocker.

Treat external downtime differently from fixable repo defects. If a website is intentionally offline or a third-party service is unavailable, document it as an accepted external limitation instead of forcing a fake pass.

## Remediation Rules

1. Do not hide issues by weakening scoring, removing checks, deleting findings, or editing generated artifacts directly.
2. Fix root causes in source code, configuration, dependency manifests, docs, or workflow scripts.
3. Preserve public-only repository processing and generated-artifact boundaries from the constitution.
4. Keep changes small and targeted. Avoid broad refactors unless the issue cannot be fixed safely without one.
5. When a score cannot reach perfect because the data reflects real external state, add a concise explanation in the relevant report or documentation and keep the evaluator honest.
6. If dependency updates are needed, update lockfiles and verify build/test compatibility.

## Expected Workflow

1. Run `git status --short` and note existing changes.
2. Identify the top score blockers and map each blocker to a file, generated data field, or audit finding.
3. Make the smallest source changes that address fixable blockers.
4. Regenerate stats through the supported pipeline, for example:

   ```powershell
   $env:GITHUB_TOKEN = gh auth token
   .\run-spark.ps1 -Screenshots -Verbose -HeartbeatSeconds 30
   ```

5. Rebuild dashboard artifacts:

   ```powershell
   cd frontend
   npx vite build
   npm run postbuild
   ```

6. Run verification:

   ```powershell
   .\.venv\Scripts\python.exe -m pytest
   cd frontend
   npx vitest run
   npm run lint
   npm run format:check
   npm audit --audit-level=high
   ```

   If a required tool is missing, install it in the project-local environment and rerun the gate.

## Final Response Requirements

Return:

- Score blockers found
- Fixes made, with file paths
- Generated artifacts refreshed
- Verification commands and results
- Remaining non-perfect-score reasons, if any, clearly separated into fixable versus external/accepted limitations
