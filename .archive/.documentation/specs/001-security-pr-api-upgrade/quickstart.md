# Quickstart

This quickstart describes how to validate the feature after implementation is complete.

## 1. Install dependencies

```powershell
pip install -r requirements.txt
pip install -e .
```

If dashboard consumers are updated for the new fields:

```powershell
Set-Location frontend
npm install
Set-Location ..
```

## 2. Generate unified data with the current baseline behavior

```powershell
spark unified --user markhazleton --verbose
```

Validate that:

- `data/repositories.json` is generated successfully.
- Every included repository record contains `pull_request_summary`.
- Every included repository record contains `security_summary`.
- Repositories without visible security access still emit `security_summary.availability = "partial"` or `"unavailable"` instead of missing the field.
- Private repositories remain excluded before any PR or security enrichment fields are assembled.

## 3. Validate explicit API-version behavior

Run the same generation flow with the implementation's explicit `2026-03-10` request path enabled.

Expected result:

- Repository generation still succeeds.
- Pull request summaries do not rely on deprecated `merge_commit_sha` or singular `assignee` fields.
- Repository parsing does not depend on deprecated `has_downloads`.
- Logs or generated metadata surface the current staged API-upgrade decision and any fallback state.

## 4. Verify caching and force-refresh behavior

Run the generator twice against an unchanged account.

Expected result:

- The second run should avoid unnecessary refresh work for unchanged repositories.
- Pull request and security summaries should follow the same `pushed_at`-keyed cache/refresh strategy as the rest of repository assembly, without TTL-driven refreshes.

Then validate force refresh:

```powershell
spark unified --user markhazleton --verbose --force-refresh
```

Expected result:

- Enrichment data is refreshed regardless of cache presence.

## 5. Run targeted tests

```powershell
pytest tests/unit tests/integration
```

If the dashboard consumes the new fields:

```powershell
Set-Location frontend
npm test
Set-Location ..
```

## 6. Confirm rollout gates

The feature is ready to move from staged support to default `2026-03-10` usage only if all of the following are true:

- Standard runs for fewer than 500 repositories remain under the project runtime budget.
- If the runtime budget is exceeded, the run surfaces mitigation guidance or explicit budget-exceeded reporting.
- Partial and unavailable states are explicit and logged.
- Contract consumers tolerate the schema bump from `2.0.0` to `2.1.0`.
- No existing parser still depends on documented deprecated fields removed in `2026-03-10`.
