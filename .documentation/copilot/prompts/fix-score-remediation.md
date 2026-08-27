# Fix Score Remediation Prompt

Use this prompt with GitHub Copilot when the repository needs an implementation pass to remove issues that prevent a perfect evaluation score.

Prompt file:

- `.github/prompts/devspark.fix-score.prompt.md`

## Intent

The prompt tells Copilot to:

- Inspect the latest generated repository data, screenshot audit, and DevSpark audit reports.
- Identify the concrete score blockers.
- Fix root causes in source code, config, docs, workflows, or dependency manifests.
- Regenerate stats and dashboard artifacts through supported commands.
- Run backend, frontend, lint, format, build, and audit gates.
- Report remaining blockers as either fixable defects or accepted external limitations.

## Recommended Use

Run the prompt from the repository root after stats have been generated:

```text
/devspark.fix-score
```

Optional scoped examples:

```text
/devspark.fix-score Focus on screenshot_audit failures for MakeBoldSolutions.
/devspark.fix-score Focus on frontend build and npm audit blockers.
/devspark.fix-score Use .documentation/copilot/audit/2026-05-12_results.md as the baseline.
```

## Guardrails

The prompt explicitly prevents Copilot from hiding issues by weakening checks or manually editing generated outputs. Generated files must be refreshed through the Stats Spark pipeline and dashboard build commands.
