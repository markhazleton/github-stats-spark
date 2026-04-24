# Data Model: Portfolio Intelligence System

**Feature**: `004-portfolio-intelligence` | **Date**: 2026-04-24

## New Entities

### ClassificationResult

Produced by `RepositoryClassifier.classify()`. Injected into each `repo_dict` entry during assembly.

| Field | Type | Values | Source |
|-------|------|--------|--------|
| `classification` | string | `"core"` \| `"supporting"` \| `"archive"` | Rule-based engine (priority-ordered thresholds) or `config/portfolio.yml` override |
| `signal_score` | integer | 0–100 | Equal-weight formula: recency(33%) + volume(33%) + tier_score(34%) |
| `relevance` | string | `"high"` \| `"medium"` \| `"low"` | Derived: core→high, supporting→medium, archive→low |
| `notes` | string | any | Config override verbatim; else auto-generated phrase |

### ClassificationConfig (config/portfolio.yml)

```yaml
repos:
  devspark: core
  TailwindSpark: core
  PromptSpark.Chat: core
  BootstrapSpark: supporting
  "*": archive          # wildcard default for all unspecified repos
```

Valid tier values: `core`, `supporting`, `archive` (case-insensitive on load)

## Extended Entities

### Repository (models/repository.py additions)

No changes to the Python dataclass. Classification fields live only in the output `repo_dict` (computed during assembly, not stored in the GitHub API response model).

### repo_dict (unified_data_generator.py output)

New keys added to each repository entry in `data/repositories.json`:

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

Note: `classification`/`signal_score`/`relevance`/`notes` = rule-based (deterministic). `portfolio_role`/`portfolio_signal`/`portfolio_action`/`portfolio_positioning` = AI informational (from summarizer, may be null).

## Classification Rules

Priority-ordered (first match wins, applied after config overrides):

```
IF pushed_at ≤ 90 days ago
   AND commits_90d ≥ 5
   AND (has_tests OR has_ci_cd)
THEN classification = "core"

ELSE IF pushed_at ≤ 365 days ago
     OR commits_90d ≥ 1
THEN classification = "supporting"

ELSE classification = "archive"
```

Config overrides are applied BEFORE these rules. Wildcard `"*"` sets the default tier for repos not explicitly named.

## Signal Score Formula

```
recency_score  = max(0, 100 - (days_since_push / 365 * 100))
volume_score   = min(100, commits_90d / 30 * 100)
tier_score     = { core: 100, supporting: 60, archive: 20 }

signal_score   = round((recency_score + volume_score + tier_score) / 3)
```

All three inputs normalized to 0–100 before averaging. Volume ceiling: 30 commits/90d = 100.

## Auto-Generated Notes Templates

| Classification | commits_90d | Generated Note |
|----------------|-------------|----------------|
| core | ≥10 | "Actively maintained core system with {n} commits in the last 90 days" |
| core | <10 | "Core system in the portfolio; maintained with focused recent activity" |
| supporting | ≥1 | "Supporting project with recent updates" |
| supporting | 0 | "Supporting project; periodically maintained" |
| archive | any | "Historical project; no longer actively maintained" |

## Visualization Data Shapes

### PortfolioBreakdown (frontend + SVG)

```json
{
  "core": { "count": 4, "percentage": 25.0 },
  "supporting": { "count": 6, "percentage": 37.5 },
  "archive": { "count": 6, "percentage": 37.5 }
}
```

Derived from: `repos.filter(r => !r.is_fork).groupBy(r => r.classification)`

### SignalDistribution (frontend + SVG)

```json
[
  { "name": "devspark", "signal_score": 95, "classification": "core" },
  { "name": "TailwindSpark", "signal_score": 82, "classification": "core" },
  ...
]
```

Sorted by `signal_score` descending. Top N repos (configurable, default 20).

## State Transitions

```
[no classification]
       ↓  (first data generation run with config/portfolio.yml present)
[classified: core | supporting | archive]
       ↓  (config/portfolio.yml updated)
[reclassified on next generation run]
       ↓  (repo pushed → cache invalidated → data regenerated)
[reclassified with updated activity data]
```

## Validation Rules

- `classification` MUST be one of `"core"`, `"supporting"`, `"archive"`
- `signal_score` MUST be an integer in range [0, 100]
- `relevance` MUST match classification: core↔high, supporting↔medium, archive↔low
- `notes` MUST be a non-empty string
- Every non-forked public repo MUST have all four fields (SC-003)
