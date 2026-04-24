# Contract: Portfolio Intelligence JSON Schema

**Feature**: `004-portfolio-intelligence` | **Date**: 2026-04-24
**Type**: Output data contract (repositories.json enrichment)
**Consumers**: markhazleton.com (site integration), React frontend dashboard

## Schema Addition to repositories.json

Each repository object in `data/repositories.json` gains the following fields:

```json
{
  "classification": "core",
  "signal_score": 87,
  "relevance": "high",
  "notes": "Actively maintained core system with 24 commits in the last 90 days",
  "portfolio_role": "CORE",
  "portfolio_signal": "HIGH",
  "portfolio_action": "FEATURE",
  "portfolio_positioning": "This repository represents the core system for spec-driven AI-assisted development."
}
```

## Field Definitions

| Field | Type | Required | Nullable | Description |
|-------|------|----------|----------|-------------|
| `classification` | string enum | Yes | No | Rule-based tier: `"core"` \| `"supporting"` \| `"archive"` |
| `signal_score` | integer | Yes | No | Portfolio signal strength 0–100 |
| `relevance` | string enum | Yes | No | `"high"` \| `"medium"` \| `"low"` (derived from classification) |
| `notes` | string | Yes | No | Human-readable context; min length 1 |
| `portfolio_role` | string enum | No | Yes | AI-assessed role: `"CORE"` \| `"SUPPORTING"` \| `"ARCHIVE"` or null |
| `portfolio_signal` | string enum | No | Yes | AI-assessed signal: `"HIGH"` \| `"MEDIUM"` \| `"LOW"` or null |
| `portfolio_action` | string enum | No | Yes | AI recommendation: `"FEATURE"` \| `"KEEP"` \| `"ARCHIVE"` \| `"CONSIDER_PRIVATE"` or null |
| `portfolio_positioning` | string | No | Yes | AI-generated positioning sentence or null |

## Invariants

1. `classification` is always present for non-forked public repositories
2. `signal_score` ∈ [0, 100]
3. `relevance` is derived deterministically: `core→high`, `supporting→medium`, `archive→low`
4. `notes` is never null or empty string
5. `portfolio_*` fields are null when no AI summary has been generated for the repository
6. `classification` (lowercase) and `portfolio_role` (UPPERCASE) use different casing conventions intentionally — they are independent fields from different systems

## Versioning

This schema extends the existing `repositories.json` format additively. No existing fields are removed or renamed. Consumers reading the pre-existing schema continue to work unchanged.

## Stability Commitment

- `classification`, `signal_score`, `relevance`, `notes`: **stable** — required by markhazleton.com integration (SC-004)
- `portfolio_*` fields: **best-effort** — depend on AI availability; consumers must handle null values

## Example Consumer Usage (JavaScript)

```js
// Render portfolio breakdown — works even if portfolio_* fields are null
const coreRepos = repos.filter(r => r.classification === 'core');
const signalSorted = [...repos].sort((a, b) => b.signal_score - a.signal_score);

// AI positioning line, with graceful fallback to notes
const displayText = repo.portfolio_positioning ?? repo.notes;
```
