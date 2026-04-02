# Data Contract: repositories.json Schema v2.3.0

**Feature**: 001-dashboard-visual-enhancements  
**Date**: 2026-04-02  
**Type**: JSON data contract between Python backend and React frontend

## Contract Summary

The `data/repositories.json` file is the sole data contract between the Python CLI backend and the React dashboard frontend. Schema v2.3.0 adds optional fields for activity calendar, commit volume metrics, and bus factor indicators. All additions are backward-compatible — the frontend MUST handle their absence.

## New Fields (v2.3.0 Additions)

### Profile-Level Fields

```json
{
  "profile": {
    "username": "markhazleton",
    "total_repositories": 50,
    "total_stars": 120,
    "total_forks": 35,
    "total_commits": 5000,
    "activity_calendar": {
      "2025-04-01": 3,
      "2025-04-02": 0,
      "2025-04-03": 7
    },
    "weekly_activity": [
      {
        "week": "2025-W14",
        "label": "Apr 1",
        "commits": 12,
        "active_repos": 4
      }
    ]
  }
}
```

### Per-Repository Fields

```json
{
  "repositories": [
    {
      "name": "example-repo",
      "total_additions": 15420,
      "total_deletions": 8230,
      "code_churn": 23650,
      "bus_factor": 2,
      "bus_factor_health": "warning",
      "contributor_stats": [
        {
          "login": "markhazleton",
          "commits": 180,
          "additions": 12000,
          "deletions": 6000
        },
        {
          "login": "contributor2",
          "commits": 45,
          "additions": 3420,
          "deletions": 2230
        }
      ]
    }
  ]
}
```

### Metadata Changes

```json
{
  "metadata": {
    "schema_version": "2.3.0",
    "schema_features": [
      "attention_metrics",
      "dependency_version_coverage",
      "activity_calendar",
      "commit_volume_stats",
      "bus_factor"
    ]
  }
}
```

## Backward Compatibility Rules

1. Frontend MUST check for field existence before accessing any v2.3.0 field
2. Missing `activity_calendar` → heatmap component renders empty state with message
3. Missing `weekly_activity` → timeline component renders empty state with message
4. Missing `total_additions`/`total_deletions` → display "Stats not available"
5. Missing `bus_factor` → display "N/A"
6. Missing `contributor_stats` → hide contributor breakdown section
7. Frontend MUST NOT crash or show errors when fed a v2.2.0 JSON file

## Producer (Python Backend)

- `unified_data_generator.py` is the sole producer
- New fields populated during Phase 3 (Assemble) using cached API responses
- `activity_calendar` sourced from `calculator.py` `commits_by_day` (already computed)
- `weekly_activity` derived from `activity_calendar` during assembly
- Commit volume from `repo.get_stats_code_frequency()` (cached)
- Bus factor from `repo.get_stats_contributors()` (cached)
- All new API calls subject to rate limit handling and cache invalidation via `pushed_at`

## Consumer (React Frontend)

- `metricsCalculator.js` transforms raw JSON into component-ready data
- Components access data through existing prop-drilling from `App.jsx`
- New components: `ContributionHeatmap.jsx`, `ActivityTimeline.jsx`, `ThemeToggle.jsx`
- ExportButton.jsx columns updated to include new fields
