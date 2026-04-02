# Data Model: Dashboard Visual Enhancements

**Feature**: 001-dashboard-visual-enhancements  
**Date**: 2026-04-02

## Entity Overview

This feature adds new fields to the existing `repositories.json` schema and introduces computation-only entities in the frontend. No new database tables or persistent stores are created.

## New Fields on Existing Entities

### `repositories.json` — Top-Level Profile Enhancement

Add `activity_calendar` to the profile/root level (aggregated across all repositories):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `activity_calendar` | `Dict[str, int]` | Optional | Map of `"YYYY-MM-DD"` → commit count across all repos. Already computed by `calculator.py` as `commits_by_day`. |
| `weekly_activity` | `List[Dict]` | Optional | Array of `{week: "YYYY-Wnn", commits: int, active_repos: int}` for trailing 52 weeks. Derived from `activity_calendar` + repo `pushed_at`. |

### `repositories.json` — Per-Repository Additions

Add to each repository object:

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `total_additions` | `int \| null` | Optional | `null` | Total lines added across all time, from `stats/code_frequency`. |
| `total_deletions` | `int \| null` | Optional | `null` | Total lines deleted across all time, from `stats/code_frequency`. |
| `code_churn` | `int \| null` | Optional | `null` | `total_additions + abs(total_deletions)` |
| `bus_factor` | `int \| null` | Optional | `null` | Minimum contributors for 50% of commits. |
| `bus_factor_health` | `string \| null` | Optional | `null` | One of: `"critical"` (1), `"warning"` (2), `"healthy"` (3+). |
| `contributor_stats` | `List[Dict] \| null` | Optional | `null` | Array of `{login: str, commits: int, additions: int, deletions: int}`, sorted by commits desc. Top 10 only. |

### Schema Version

Increment from `2.2.0` to `2.3.0`. New fields are optional — frontend must handle their absence gracefully.

Schema features array gains: `"activity_calendar"`, `"commit_volume_stats"`, `"bus_factor"`.

## Frontend Computation-Only Entities

These are not persisted — they exist only in React component state, derived from `repositories.json` data:

### DailyCommitCount (for Heatmap)

```
{
  date: string       // "YYYY-MM-DD"
  count: number      // commit count for that day
  intensity: number  // 0-4 scale (0 = none, 4 = highest quartile)
}
```

Derived from `activity_calendar` in `metricsCalculator.js`. Intensity levels calculated by quartile distribution of non-zero days.

### WeeklyActivityPoint (for Timeline)

```
{
  week: string       // "YYYY-Wnn" ISO week
  label: string      // "Jan 1" human-readable week start
  commits: number
  activeRepos: number
}
```

Derived from `weekly_activity` in `metricsCalculator.js`.

### ThemePreference (for Dark Mode)

```
{
  theme: "light" | "dark" | "system"
  resolvedTheme: "light" | "dark"  // actual applied theme
}
```

Stored in `localStorage` under key `spark-theme`. React context provides `theme`, `resolvedTheme`, and `toggleTheme()`.

## Relationships

```
repositories.json (root)
├── profile
│   ├── activity_calendar: Dict[date → count]      # NEW
│   └── weekly_activity: List[WeeklyActivityPoint]  # NEW
├── repositories[]
│   ├── (existing fields...)
│   ├── total_additions: int                        # NEW
│   ├── total_deletions: int                        # NEW
│   ├── code_churn: int                             # NEW
│   ├── bus_factor: int                             # NEW
│   ├── bus_factor_health: string                   # NEW
│   └── contributor_stats: List[ContributorEntry]   # NEW
└── metadata
    ├── schema_version: "2.3.0"                     # CHANGED
    └── schema_features: [... + 3 new]              # CHANGED
```

## Validation Rules

- `activity_calendar` keys must be valid ISO dates in `YYYY-MM-DD` format
- `activity_calendar` values must be non-negative integers
- `bus_factor` must be >= 1 when present
- `bus_factor_health` must be one of: `"critical"`, `"warning"`, `"healthy"`, or `null`
- `total_additions` and `total_deletions` must be non-negative when present
- `contributor_stats` entries must have non-negative `commits`, `additions`, `deletions`
- `weekly_activity` must be ordered chronologically
- Frontend must treat all new fields as optional (backward compatibility with schema 2.2.0)

## State Transitions

No state machine applies — all new data is computed once during `spark unified` and consumed read-only by the frontend.

The only stateful element is `ThemePreference`, which transitions:
- `"system"` → user clicks toggle → `"dark"` → clicks again → `"light"` → clicks again → `"system"`
