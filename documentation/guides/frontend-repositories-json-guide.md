# Front-End Guide to Consuming `repositories.json`

**Schema Version:** 2.2.0  
**Generator:** `unified_data_generator` (via `spark unified`)  
**Stack:** React 19 + Vite 8 + Chart.js 4 + Dexie (IndexedDB)

This guide covers every field in `data/repositories.json`, the data-fetching pipeline, and how the dashboard components consume the data. Code excerpts are taken directly from the live codebase.

---

## Table of Contents

1. [How repositories.json Is Generated](#1-how-repositoriesjson-is-generated)
2. [Top-Level Schema](#2-top-level-schema)
3. [Profile Object](#3-profile-object)
4. [Metadata Object](#4-metadata-object)
5. [Repository Object — Complete Field Reference](#5-repository-object--complete-field-reference)
6. [Data Fetching Pipeline](#6-data-fetching-pipeline)
7. [Offline-First Caching with Dexie](#7-offline-first-caching-with-dexie)
8. [Hook: useRepositoryData](#8-hook-userepositorydata)
9. [Hook: useTableSort](#9-hook-usetablesort)
10. [Components That Consume the Data](#10-components-that-consume-the-data)
11. [Metrics Calculator Service](#11-metrics-calculator-service)
12. [Rendering AI Summaries as Markdown](#12-rendering-ai-summaries-as-markdown)
13. [Attention Metrics and the Needs-Attention View](#13-attention-metrics-and-the-needs-attention-view)
14. [Dependency Enrichment and Version Coverage](#14-dependency-enrichment-and-version-coverage)
15. [Pull Request and Security Signals](#15-pull-request-and-security-signals)
16. [Export Functionality (CSV / JSON)](#16-export-functionality-csv--json)
17. [URL Routing and View Switching](#17-url-routing-and-view-switching)
18. [Build and Deployment](#18-build-and-deployment)

---

## 1. How `repositories.json` Is Generated

The Python CLI command that produces the JSON is:

```bash
spark unified --user markhazleton --include-ai-summaries --verbose
```

This single command runs the full pipeline:

1. **GitHubFetcher** — Authenticates with `GITHUB_TOKEN`, fetches all public repositories, applies `pushed_at`-based content-addressed cache.
2. **StatsCalculator** — Computes Spark Score (40% consistency + 35% volume + 25% collaboration), streak detection, time patterns.
3. **RepositoryRanker** — Calculates `composite_score` (30% popularity + 45% activity + 25% health) and assigns `rank`.
4. **RepositoryDependencyAnalyzer** — Parses manifest files, performs live registry lookups (npm, PyPI, RubyGems, NuGet), resolves current/latest versions, calculates currency scores.
5. **Attention Scorer** — Computes `attention_score` from security (35%), PRs (25%), staleness (25%), dependencies (15%).
6. **RepositorySummarizer** — Claude Haiku 3.5 AI summaries with three-tier fallback.
7. **UnifiedDataGenerator** — Assembles everything into `data/repositories.json`.

The frontend build (`npm run build`) then copies `data/` into `docs/data/` for GitHub Pages.

---

## 2. Top-Level Schema

```jsonc
{
  "profile": { /* user profile */ },
  "repositories": [ /* array of repository objects */ ],
  "metadata": { /* generation metadata */ }
}
```

The frontend validates this structure in `dataService.js`:

```js
if (!data || typeof data !== "object") {
  throw new Error("Invalid dashboard data: expected object");
}
if (!Array.isArray(data.repositories)) {
  throw new Error("Invalid dashboard data: repositories must be an array");
}
```

---

## 3. Profile Object

```jsonc
{
  "profile": {
    "username": "markhazleton",
    "total_repositories": 37,
    "total_stars": 18,
    "total_forks": 7,
    "total_commits": 3746
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `username` | `string` | GitHub username |
| `total_repositories` | `int` | Count of public repositories analyzed |
| `total_stars` | `int` | Sum of stars across all repos |
| `total_forks` | `int` | Sum of forks across all repos |
| `total_commits` | `int` | Sum of commits across all repos |

**Frontend usage:** Passed as `profile` prop to `StatCards` and `DashboardView`.

---

## 4. Metadata Object

```jsonc
{
  "metadata": {
    "generated_at": "2026-03-29T14:59:19.515118+00:00",
    "schema_version": "2.2.0",
    "generator": "unified_data_generator",
    "schema_features": ["attention_metrics", "dependency_version_coverage"],
    "attention_formula_version": "1.0"
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `generated_at` | `ISO 8601` | UTC timestamp of when the data was produced |
| `schema_version` | `string` | Semantic version of the JSON schema |
| `generator` | `string` | Name of the generator module |
| `schema_features` | `string[]` | Feature flags indicating which enrichments are present |
| `attention_formula_version` | `string` | Version of the attention scoring algorithm |

**Frontend usage:** `generated_at` is displayed in the footer via `App.jsx`:

```js
const formatGeneratedAt = (timestamp) => {
  if (!timestamp) return "Unknown";
  const parsed = new Date(timestamp);
  if (Number.isNaN(parsed.getTime())) return "Unknown";
  return parsed.toLocaleString();
};
```

Use `schema_features` to feature-gate UI sections:

```js
const hasAttention = data.metadata?.schema_features?.includes("attention_metrics");
```

---

## 5. Repository Object — Complete Field Reference

Every entry in the `repositories[]` array has the fields below. All fields are present for every repository unless noted as optional.

### 5.1 Identity & Metadata

| Field | Type | Example | Description |
|-------|------|---------|-------------|
| `name` | `string` | `"github-stats-spark"` | Repository name |
| `description` | `string\|null` | `"A GitHub Stats..."` | Repository description |
| `url` | `string` | `"https://github.com/..."` | GitHub URL |
| `homepage` | `string\|null` | `"https://markhazleton.github.io/..."` | Custom homepage URL |
| `has_pages` | `bool` | `true` | Whether GitHub Pages is enabled |
| `pages_url` | `string\|null` | `"https://..."` | GitHub Pages URL |
| `website_url` | `string\|null` | `"https://..."` | Resolved website (homepage or pages_url) |
| `language` | `string\|null` | `"Python"` | Primary language |
| `language_stats` | `object` | `{"Python": 50000, "JS": 20000}` | Language byte counts |
| `languages` | `object` | `{}` | Alias for language_stats |
| `language_count` | `int` | `5` | Number of languages |
| `size_kb` | `int` | `11937` | Repository size in KB |
| `is_fork` | `bool` | `false` | Whether the repo is a fork |
| `is_private` | `bool` | `false` | Always `false` (private repos are excluded) |
| `is_archived` | `bool` | `false` | Whether the repo is archived |
| `age_days` | `int` | `90` | Days since creation |

### 5.2 Popularity

| Field | Type | Description |
|-------|------|-------------|
| `stars` | `int` | Star count |
| `forks` | `int` | Fork count |
| `watchers` | `int` | Watcher count |
| `open_issues` | `int` | Open issue count (when present) |

### 5.3 Timestamps

| Field | Type | Description |
|-------|------|-------------|
| `created_at` | `ISO 8601` | Repository creation timestamp |
| `updated_at` | `ISO 8601` | Last update timestamp |
| `pushed_at` | `ISO 8601` | Last push timestamp |
| `days_since_last_push` | `int` | Computed staleness (0 = pushed today) |

### 5.4 Commit History

Nested under `commit_history`:

```jsonc
{
  "commit_history": {
    "repository_name": "github-stats-spark",
    "total_commits": 199,
    "recent_90d": 183,
    "recent_180d": 199,
    "recent_365d": 199,
    "last_commit_date": "2026-03-29T02:11:35+00:00",
    "first_commit_date": "2025-12-28T17:48:33+00:00",
    "patterns": ["highly_active", "recently_updated", "accelerating"],
    "commit_frequency": 61.0,
    "consistency_score": 0,
    "activity_rate": 2.033,
    "days_since_last_commit": 0
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `total_commits` | `int` | Lifetime commit count |
| `recent_90d` | `int` | Commits in last 90 days |
| `recent_180d` | `int` | Commits in last 180 days |
| `recent_365d` | `int` | Commits in last 365 days |
| `first_commit_date` | `ISO 8601` | Date of first commit |
| `last_commit_date` | `ISO 8601` | Date of most recent commit |
| `patterns` | `string[]` | Activity pattern tags (e.g., `"highly_active"`, `"accelerating"`, `"declining"`) |
| `commit_frequency` | `float` | Commits per month |
| `consistency_score` | `int` | 0-100 regularity score |
| `activity_rate` | `float` | Commits per day (recent window) |
| `days_since_last_commit` | `int` | Staleness indicator |

**Frontend access pattern** (used across all components):

```js
const totalCommits = repo.commit_history?.total_commits || repo.total_commits || 0;
const recent90d = repo.commit_history?.recent_90d || repo.recent_commits_90d || 0;
const lastCommit = repo.commit_history?.last_commit_date || repo.last_commit_date;
```

### 5.5 Commit Metrics

Nested under `commit_metrics`:

```jsonc
{
  "commit_metrics": {
    "avg_size": 12266.16,
    "total_commits": 199,
    "largest_commit": {
      "sha": "5a6925327c...",
      "date": "2026-01-04T14:38:58+00:00",
      "size": 282812,
      "files_changed": 141406,
      "lines_added": 2654,
      "lines_deleted": 138752
    },
    "smallest_commit": {
      "sha": "1838276400...",
      "date": "2026-01-02T21:06:22+00:00",
      "size": 2,
      "files_changed": 1,
      "lines_added": 1,
      "lines_deleted": 0
    },
    "commit_size_distribution": {
      "min": 0, "q1": 269, "median": 1972, "q3": 10993, "max": 282812
    }
  }
}
```

**Top-level aliases** (maintained for backwards compatibility):

| Field | Type | Notes |
|-------|------|-------|
| `avg_commit_size` | `float` | Same as `commit_metrics.avg_size` |
| `largest_commit` | `object` | Same as `commit_metrics.largest_commit` |
| `smallest_commit` | `object` | Same as `commit_metrics.smallest_commit` |
| `commit_velocity` | `float` | Commits per month |
| `total_commits` | `int` | Same as `commit_history.total_commits` |
| `recent_commits_90d` | `int` | Same as `commit_history.recent_90d` |
| `first_commit_date` | `ISO 8601` | Same as `commit_history.first_commit_date` |
| `last_commit_date` | `ISO 8601` | Same as `commit_history.last_commit_date` |

### 5.6 AI Summary

Nested under `summary`:

```jsonc
{
  "summary": {
    "text": "# Stats Spark - Technical Analysis\n\n## Executive Summary\n...",
    "ai_generated": true,
    "generation_method": "claude-haiku-4-5",
    "generated_at": "2026-03-29T07:57:08.184230",
    "model_used": "claude-haiku-4-5",
    "tokens_used": 3272,
    "confidence_score": 90
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `text` | `string` | Full markdown-formatted summary |
| `ai_generated` | `bool` | `true` if Claude, `false` if fallback |
| `generation_method` | `string` | `"claude-haiku-4-5"`, `"readme_extraction"`, or `"metadata_only"` |
| `generated_at` | `ISO 8601` | When the summary was produced |
| `model_used` | `string\|null` | AI model identifier |
| `tokens_used` | `int\|null` | Token count for cost tracking |
| `confidence_score` | `int\|null` | 0-100 confidence from the AI model |

**Top-level alias:** `ai_summary` contains the same text as `summary.text`.

### 5.7 Quality Indicators

| Field | Type | Description |
|-------|------|-------------|
| `has_readme` | `bool` | README present |
| `has_license` | `bool` | License file present |
| `has_ci_cd` | `bool` | CI/CD workflow detected |
| `has_tests` | `bool` | Test directory/files detected |
| `has_docs` | `bool` | Documentation detected |

### 5.8 Ranking

| Field | Type | Description |
|-------|------|-------------|
| `rank` | `int` | Position in composite score ranking (1 = best) |
| `composite_score` | `float` | 0-100 Spark Score: 45% activity + 30% popularity + 25% health |

### 5.9 Technology Stack

Nested under `tech_stack`:

```jsonc
{
  "tech_stack": {
    "repository_name": "github-stats-spark",
    "languages": {},
    "frameworks": [],
    "dependencies": [ /* DependencyInfo objects */ ],
    "version_info": {},
    "dependency_file_type": "requirements.txt",
    "currency_score": 69,
    "outdated_count": 9,
    "total_dependencies": 10,
    "known_versions_count": 10,
    "resolved_latest_versions_count": 10,
    "unknown_versions_count": 0,
    "primary_language": null,
    "language_diversity": 0,
    "outdated_percentage": 90.0,
    "version_coverage_percentage": 100.0,
    "latest_version_coverage_percentage": 100.0
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `frameworks` | `string[]` | Detected frameworks |
| `dependencies` | `DependencyInfo[]` | Enriched dependency list (see §14) |
| `dependency_file_type` | `string` | Manifest file type (`"requirements.txt"`, `"package.json"`, etc.) |
| `currency_score` | `int` | 0-100 overall dependency freshness |
| `outdated_count` | `int` | Number of outdated dependencies |
| `total_dependencies` | `int` | Total dependencies tracked |
| `known_versions_count` | `int` | Dependencies with concrete current version |
| `resolved_latest_versions_count` | `int` | Dependencies with registry-resolved latest version |
| `unknown_versions_count` | `int` | Dependencies without resolvable version |
| `outdated_percentage` | `float` | Percentage of deps that are outdated |
| `version_coverage_percentage` | `float` | Percentage of deps with known current version |
| `latest_version_coverage_percentage` | `float` | Percentage of deps with registry-resolved latest version |

### 5.10 Pull Request Summary

Nested under `pull_request_summary`:

```jsonc
{
  "pull_request_summary": {
    "availability": "available",
    "reason": "none",
    "has_open_pull_requests": false,
    "total_open": 0,
    "draft_count": 0,
    "review_requested_count": 0,
    "oldest_open_age_days": null,
    "source": "rest.pulls.list"
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `availability` | `string` | `"available"`, `"partial"`, or `"unavailable"` |
| `reason` | `string` | `"none"` if available, or reason like `"permission_denied"` |
| `has_open_pull_requests` | `bool` | Quick check flag |
| `total_open` | `int` | Open PR count |
| `draft_count` | `int` | Draft PRs |
| `review_requested_count` | `int` | PRs awaiting review |
| `oldest_open_age_days` | `int\|null` | Age of the oldest open PR |
| `source` | `string` | API endpoint used |

### 5.11 Security Summary

Nested under `security_summary`:

```jsonc
{
  "security_summary": {
    "availability": "partial",
    "reason": "permission_denied",
    "overall_state": "clear",
    "feature_status": {
      "advanced_security": "unknown",
      "secret_scanning": "unknown",
      "secret_scanning_push_protection": "unknown",
      "dependency_alerts": "unavailable",
      "automated_security_fixes": "unavailable"
    },
    "active_alert_counts": {
      "total_open": 0,
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0
    },
    "sources": ["rest.repos.get", "rest.dependabot.alerts"]
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `availability` | `string` | `"available"`, `"partial"`, `"unavailable"` |
| `overall_state` | `string` | `"clear"` or `"alerts_detected"` |
| `feature_status` | `object` | Per-feature enablement (`"enabled"`, `"disabled"`, `"unknown"`) |
| `active_alert_counts.total_open` | `int` | Total open security alerts |
| `active_alert_counts.critical` | `int` | Critical severity count |
| `active_alert_counts.high` | `int` | High severity count |
| `active_alert_counts.medium` | `int` | Medium severity count |
| `active_alert_counts.low` | `int` | Low severity count |

### 5.12 Attention Metrics

Nested under `attention_metrics`:

```jsonc
{
  "attention_score": 6.5,
  "attention_rank": 28,
  "attention_metrics": {
    "score": 6.5,
    "tier": "healthy",
    "needs_attention": false,
    "reasons": ["dependencies"],
    "components": {
      "pull_requests": {
        "score": 0.0,
        "availability": "available",
        "reason": "none",
        "total_open": 0,
        "draft_count": 0,
        "review_requested_count": 0,
        "oldest_open_age_days": null
      },
      "security": {
        "score": 10.0,
        "availability": "partial",
        "reason": "permission_denied",
        "overall_state": "clear",
        "active_alert_counts": { "total_open": 0, "critical": 0, "high": 0, "medium": 0, "low": 0 }
      },
      "staleness": {
        "score": 0.0,
        "days_since_last_push": 0,
        "recent_commits_90d": 183,
        "open_issues": 0
      },
      "dependencies": {
        "score": 20.2,
        "total_dependencies": 10,
        "outdated_count": 9,
        "outdated_percentage": 90.0,
        "currency_score": 69,
        "version_coverage_percentage": 100.0,
        "latest_version_coverage_percentage": 100.0,
        "unknown_versions_count": 0
      }
    }
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `attention_score` | `float` | 0-100 composite maintenance urgency score |
| `attention_rank` | `int` | Global rank (1 = needs most attention) |
| `attention_metrics.tier` | `string` | `"critical"`, `"elevated"`, `"watch"`, or `"healthy"` |
| `attention_metrics.needs_attention` | `bool` | Quick flag — `true` for critical/elevated |
| `attention_metrics.reasons` | `string[]` | Contributing factors |
| `attention_metrics.components.*` | `object` | Per-dimension breakdown with individual scores |

### 5.13 Screenshot

Nested under `screenshot` (optional — only present for repos with GitHub Pages):

```jsonc
{
  "screenshot": {
    "path": "output/screenshots/github-stats-spark.png",
    "url": "https://markhazleton.github.io/github-stats-spark/",
    "captured_at": "2026-03-07T22:07:36.952941+00:00",
    "width": 1280,
    "height": 720,
    "file_size_kb": 60.94
  }
}
```

---

## 6. Data Fetching Pipeline

`dataService.js` implements a cache-first strategy with network fallback:

```js
import { offlineStorage } from "./offlineStorage";

export async function fetchDashboardData({
  useCache = true,
  forceRefresh = false,
  maxRetries = 3,
  retryDelay = 2000,
  cacheBust = true,
  user,
} = {}) {
  const baseUrl = getDataBaseUrl(); // DEV: "/data", PROD: "{BASE_URL}data"
  const selectedUser = getSelectedUser(user);
  const cacheToken = cacheBust ? `?v=${Date.now()}` : "";
  const url = `${baseUrl}/${getRepositoriesPath(selectedUser)}${cacheToken}`;

  // 1. Try IndexedDB cache first
  if (useCache && !forceRefresh) {
    const cachedData = await offlineStorage.get(cacheKey);
    if (cachedData) return { ...cachedData, _fromCache: true };
  }

  // 2. Fetch from network with timeout + retries
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 30_000);
    const response = await fetch(url, { cache: "no-store", signal: controller.signal });
    const data = await response.json();
    // Validate shape
    // Cache fresh data
    await offlineStorage.set(cacheKey, data, "2.0.0");
    return { ...data, _fromCache: false };
  }

  // 3. Fall back to stale cache
  const stale = await offlineStorage.get(cacheKey);
  if (stale) return { ...stale, _fromCache: true, _stale: true };

  throw new Error("Failed to load data");
}
```

**Key details:**

- Uses a `?v=` cache-bust query parameter to avoid browser caching.
- Requests use `cache: "no-store"` to bypass HTTP cache.
- 30-second timeout per attempt, 3 retries with 2-second delay.
- Returns `_fromCache: true` and `_stale: true` flags for UI indicators.

**Environment-based URLs:**
- Development: `/data/repositories.json`
- Production (GitHub Pages): `/github-stats-spark/data/repositories.json`

**Multi-user support:** A `?user=username` query parameter selects `users/{username}/repositories.json`.

---

## 7. Offline-First Caching with Dexie

`offlineStorage.js` wraps IndexedDB via Dexie.js:

```js
import Dexie from "dexie";

const db = new Dexie("GitHubStatsSpark");
db.version(1).stores({ cache: "key, data, version, timestamp" });

export const offlineStorage = {
  async get(key) { /* returns data if found */ },
  async set(key, data, version) { /* upserts into IndexedDB */ },
  async clear() { /* clears all cached data */ },
};
```

The `App.jsx` force-refresh button clears the cache:

```js
const handleForceRefresh = async () => {
  await clearCache();
  await refetch({ forceRefresh: true, cacheBust: true });
};
```

---

## 8. Hook: `useRepositoryData`

The primary data hook in `hooks/useRepositoryData.js`:

```js
export default function useRepositoryData() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async (options = {}) => {
    setLoading(true);
    setError(null);
    const dashboardData = await fetchDashboardData({
      useCache: options.useCache ?? false,
      forceRefresh: options.forceRefresh ?? true,
      cacheBust: options.cacheBust ?? true,
    });
    setData(dashboardData);
  };

  useEffect(() => { fetchData(); }, []);

  return { data, loading, error, refetch: fetchData };
}
```

**Usage in App.jsx:**

```jsx
const { data, loading, error, refetch } = useRepositoryData();
// data.profile, data.repositories, data.metadata are now available
```

---

## 9. Hook: `useTableSort`

`hooks/useTableSort.js` provides sorting and filtering for the table view:

```js
const {
  sortedData: processedRepositories,
  sortKey,
  sortOrder,
  filterLanguage,
  handleSort,
  handleFilterChange,
  clearFilter,
} = useTableSort(data?.repositories || [], "stars", "desc");
```

**Supported sort keys and their nested-field resolution:**

| Sort Key | Resolution Path |
|----------|-----------------|
| `name` | `repo.name` |
| `language` | `repo.language` |
| `stars` | `repo.stars` |
| `composite_score` | `repo.composite_score` |
| `commit_count` / `commits` | `repo.commit_history.total_commits` |
| `first_commit_date` | `repo.commit_history.first_commit_date` |
| `last_commit_date` | `repo.commit_history.last_commit_date` |
| `avg_commit_size` | `repo.commit_metrics.avg_size` |
| `largest_commit` | `repo.commit_metrics.largest_commit.size` |
| `smallest_commit` | `repo.commit_metrics.smallest_commit.size` |
| `signal_status` | Custom comparator using `pull_request_summary` + `security_summary` |
| `updated` | `repo.updated_at` |

---

## 10. Components That Consume the Data

### 10.1 App.jsx — Root Component

Manages three views via URL hash routing:

| Hash | View | Component |
|------|------|-----------|
| (none) / `#table` | Dashboard | `RepositoryTable` |
| `#visualizations` | Charts | `DashboardView` (lazy) |
| `#attention` | Maintenance | `AttentionView` (lazy) |

Props passed to child components:

```jsx
<RepositoryTable
  repositories={processedRepositories}
  sortKey={sortKey}
  sortOrder={sortOrder}
  onSort={handleSort}
  onRowClick={handleRepoClick}
/>

<DashboardView
  repositories={data.repositories}
  profile={data.profile}
  onRepoClick={handleRepoClick}
/>

<AttentionView
  repositories={data.repositories}
  onRepoClick={handleRepoClick}
/>
```

### 10.2 RepositoryTable / TableRow

Each `TableRow` renders these columns:

| Column | Source |
|--------|--------|
| Repository Name | `repo.name` |
| Language | `repo.language` |
| Signals (PR + Security) | `repo.pull_request_summary`, `repo.security_summary` |
| First Commit | `repo.commit_history.first_commit_date` |
| Last Commit | `repo.commit_history.last_commit_date` |
| Total Commits | `repo.commit_history.total_commits` |
| Stars | `repo.stars` |
| Spark Score | `repo.composite_score` |

**Signal pills** show PR and security status with color coding:

```jsx
const pullRequestLabel =
  pullRequestSummary.availability === "available"
    ? `PR ${openPullRequests}`
    : "PR n/a";

let securityLabel = "SEC n/a";
if (securitySummary.availability === "available") {
  securityLabel = securityAlerts > 0 ? `SEC ${securityAlerts}` : "SEC clear";
}
```

### 10.3 StatCards

Summary cards using data from across the entire repository list:

```js
const totalRepos = repositories.length;
const totalCommits = repositories.reduce(
  (sum, r) => sum + (r.commit_history?.total_commits || r.total_commits || 0), 0
);
const languages = [...new Set(repositories.map(r => r.language).filter(Boolean))];
const avgScore = repositories.reduce((sum, r) => sum + (r.composite_score || 0), 0) / totalRepos;
const activeRepos = repositories.filter(r => (r.commit_history?.recent_90d || 0) > 0).length;
const totalOpenPRs = repositories.reduce(
  (sum, r) => sum + (r.pull_request_summary?.availability === "available"
    ? r.pull_request_summary.total_open || 0 : 0), 0
);
const totalSecurityAlerts = repositories.reduce(
  (sum, r) => sum + (r.security_summary?.availability === "available"
    ? r.security_summary.active_alert_counts?.total_open || 0 : 0), 0
);
```

Cards displayed:
1. **Repositories** — total count
2. **Total Commits** — sum with "N active in 90d" sublabel
3. **Languages** — unique language count
4. **Avg Spark Score** — mean composite_score
5. **Open Pull Requests** — total across all repos
6. **Security Alerts** — total with availability note

### 10.4 DashboardView

Renders four Chart.js visualizations:

1. **Spark Score Bar Chart** — Repos sorted by `composite_score` desc
2. **Language Distribution Pie** — Doughnut chart from language counts
3. **Activity Scatter Plot** — x=`age_days`, y=`total_commits`, size=`composite_score`
4. **Recent Activity Bar Chart** — Top 15 repos by `recent_commits_90d`
5. **Health Chart** — Stacked horizontal bars for quality indicators (`has_readme`, `has_license`, `has_ci_cd`, `has_tests`, `has_docs`)

### 10.5 RepositoryDetail (Drill-Down Modal)

Opened when a user clicks a repository name. Consumes virtually every field in the repository object. Organized into collapsible sections:

| Section | Key Fields Used |
|---------|----------------|
| Quick Stats Bar | `stars`, `forks`, `watchers`, `open_issues`, `rank` |
| Summary | `summary.text` (rendered as Markdown), `summary.ai_generated`, `summary.model_used`, `summary.confidence_score` |
| Website Preview | `screenshot.path`, `screenshot.url`, `screenshot.captured_at`, `screenshot.file_size_kb`, `website_url` |
| Repository Info | `language`, `created_at`, `updated_at`, `pushed_at`, `days_since_last_push`, `age_days`, `size_kb`, `url`, `website_url`, `has_pages`, `pages_url` |
| Quality Indicators | `has_readme`, `has_license`, `has_ci_cd`, `has_tests`, `has_docs`, `is_archived`, `is_fork` |
| Languages | `language_stats`, `language_count` |
| Repository Signals | `pull_request_summary.*`, `security_summary.*` |
| Commit Activity | `commit_history.*` |
| Commit Metrics | `commit_metrics.avg_size`, `commit_metrics.largest_commit`, `commit_metrics.smallest_commit` |
| Activity Metrics | `contributors_count`, `release_count`, `latest_release_date` |
| Ranking | `rank`, `composite_score` |
| Technology Stack | `tech_stack.frameworks`, `tech_stack.dependencies[]`, `tech_stack.currency_score`, `tech_stack.known_versions_count`, `tech_stack.version_coverage_percentage`, `tech_stack.resolved_latest_versions_count`, `tech_stack.latest_version_coverage_percentage` |

**Gesture support:** The modal supports swipe-to-dismiss (down), swipe-left/right for next/previous repo, and keyboard navigation (Escape, Arrow keys).

---

## 11. Metrics Calculator Service

`services/metricsCalculator.js` provides reusable formatting and transformation utilities:

### Formatters

```js
formatDate("2026-01-15T10:30:00Z")          // "Jan 15, 2026"
formatDate("2026-01-15T10:30:00Z", "long")   // "January 15, 2026"
formatDate("2026-01-15T10:30:00Z", "relative") // "2 months ago"

formatCommitSize(12266.16)     // "12,266.2"
formatNumber(1234567)          // "1.2M"
formatNumber(1234)             // "1.2K"
```

### Chart Transformers

```js
// For bar charts
transformForBarChart(repositories, "totalCommits")
// → [{ name, value, language, fullData }] sorted desc, max 50

// For scatter plots
transformForScatterPlot(repositories, "totalCommits", "avgCommitSize")
// → [{ name, x, y, language, fullData }]

// For line graphs
transformForLineGraph(repositories, "lastCommitDate")
// → [{ name, value, date, language, fullData }] sorted by date
```

### Metric ID Mapping

The `getMetricValue(repo, metricId)` function resolves metric IDs to nested fields:

| Metric ID | Resolution |
|-----------|------------|
| `totalCommits` | `commit_history.total_commits` |
| `avgCommitSize` | `commit_metrics.avg_size` |
| `largestCommit` | `commit_metrics.largest_commit.size` |
| `smallestCommit` | `commit_metrics.smallest_commit.size` |
| `firstCommitDate` | `commit_history.first_commit_date` (as timestamp) |
| `lastCommitDate` | `commit_history.last_commit_date` (as timestamp) |

---

## 12. Rendering AI Summaries as Markdown

The `MarkdownContent` component renders the `summary.text` field as rich HTML:

```jsx
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function MarkdownContent({ content, className = "" }) {
  if (!content) return null;
  return (
    <div className={mergedClassName}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: ({ ...props }) => (
            <a {...props} target="_blank" rel="noopener noreferrer" />
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
```

**Dependencies:** `react-markdown` ^10.1.0, `remark-gfm` ^4.0.1

**Usage in RepositoryDetail:**

```jsx
<MarkdownContent content={repository.summary.text} className={styles.summaryText} />
```

**Features:**
- GitHub Flavored Markdown (tables, strikethrough, autolinks, task lists)
- External links open in new tab with `noopener noreferrer`
- Styled via CSS module `MarkdownContent.module.css`

---

## 13. Attention Metrics and the Needs-Attention View

The `AttentionView` component (`components/Attention/AttentionView.jsx`) ranks repositories by maintenance urgency.

### Data Extraction

```js
const rankedRepositories = useMemo(() => {
  return [...repositories]
    .filter((repo) => repo.attention_metrics)  // Only repos with attention data
    .sort((a, b) => (b.attention_score || 0) - (a.attention_score || 0));
}, [repositories]);
```

### Summary Cards

```js
const summary = useMemo(() => {
  const needsAttention = rankedRepositories.filter(r => r.attention_metrics?.needs_attention);
  const critical = needsAttention.filter(r => r.attention_metrics?.tier === "critical");
  const securityBacklog = rankedRepositories.filter(
    r => (r.security_summary?.active_alert_counts?.total_open || 0) > 0
  );
  const stale = rankedRepositories.filter(r => (r.days_since_last_push || 0) >= 90);
  return { total: needsAttention.length, critical: critical.length, securityBacklog: securityBacklog.length, stale: stale.length };
}, [rankedRepositories]);
```

### Table Columns

| Column | Source |
|--------|--------|
| Rank | `repo.attention_rank` |
| Repository | `repo.name`, `repo.language` |
| Tier | `repo.attention_metrics.tier` → badge class (`critical`, `elevated`, `watch`, `healthy`) |
| Score | `repo.attention_score` (formatted to 1 decimal) |
| PRs | `repo.attention_metrics.components.pull_requests.total_open` |
| Alerts | `repo.attention_metrics.components.security.active_alert_counts.total_open` |
| Stale | `repo.days_since_last_push` |
| Deps | `repo.attention_metrics.components.dependencies.outdated_count` / `total_dependencies` |

### Score Formula (displayed in explainer sidebar)

| Component | Weight | Source |
|-----------|--------|--------|
| Security | 35% | Critical/high alerts weighted heavily |
| Pull Requests | 25% | Backlog count, age, review load |
| Staleness | 25% | Days since last push |
| Dependencies | 15% | Outdated packages, version coverage gaps |

### Feature Gating

When attention data is absent (pre-2.2.0 schema), the component shows an empty state:

```jsx
if (rankedRepositories.length === 0) {
  return (
    <div className={styles.emptyState}>
      <h3>No attention signals available</h3>
      <p>Generate repositories.json with schema 2.2.0 or later...</p>
    </div>
  );
}
```

---

## 14. Dependency Enrichment and Version Coverage

Each dependency in `tech_stack.dependencies[]` has the following enriched fields:

```jsonc
{
  "name": "PyGithub",
  "current_version": "2.1.1",
  "latest_version": "2.9.0",
  "ecosystem": "pypi",
  "versions_behind": 0,
  "is_outdated": true,
  "status": "minor_outdated",
  "version_requirement": "2.1.1,<3.0.0",
  "current_version_known": true,
  "latest_version_status": "resolved",
  "latest_version_source": "pypi",
  "source_file": "requirements.txt"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | `string` | Package name |
| `current_version` | `string` | Installed/declared version |
| `latest_version` | `string` | Latest version from registry |
| `ecosystem` | `string` | Package ecosystem (`"pypi"`, `"npm"`, `"rubygems"`, `"nuget"`) |
| `versions_behind` | `int` | Major versions behind (deprecated; use `status`) |
| `is_outdated` | `bool` | Whether dependency is behind latest |
| `status` | `string` | `"current"`, `"minor_outdated"`, `"major_outdated"`, `"unknown"` |
| `version_requirement` | `string\|null` | Raw version constraint from manifest |
| `current_version_known` | `bool` | Whether a concrete version was resolved |
| `latest_version_status` | `string` | `"resolved"`, `"not_found"`, `"lookup_failed"` |
| `latest_version_source` | `string\|null` | Registry name |
| `source_file` | `string\|null` | Manifest file (e.g., `"requirements.txt"`, `"package.json"`) |

### Frontend Consumption in RepositoryDetail

Dependencies are sorted by priority and limited to 8:

```js
const dependencyStatusPriority = {
  major_outdated: 0, minor_outdated: 1, unknown: 2, current: 3,
};

const topDependencies = [...(repository.tech_stack?.dependencies || [])]
  .sort((a, b) => {
    const aPriority = dependencyStatusPriority[a.status] ?? 99;
    const bPriority = dependencyStatusPriority[b.status] ?? 99;
    if (aPriority !== bPriority) return aPriority - bPriority;
    return a.name.localeCompare(b.name);
  })
  .slice(0, 8);
```

Each dependency renders with a colored badge and version info:

```jsx
<span className={getDependencyBadgeClass(dependency.status)}>
  {dependency.status.replace(/_/g, " ")}
</span>
<div className={styles.dependencyMeta}>
  {dependency.current_version_known
    ? `${dependency.current_version}${dependency.latest_version ? ` -> ${dependency.latest_version}` : ""}`
    : dependency.version_requirement || dependency.current_version}
</div>
<div className={styles.dependencyAux}>
  {dependency.source_file || dependency.ecosystem}
</div>
```

**Coverage metrics** are shown as fractions with percentages:

```jsx
<dt>Known Versions</dt>
<dd>{known_versions_count}/{total_dependencies} ({version_coverage_percentage}%)</dd>

<dt>Registry Coverage</dt>
<dd>{resolved_latest_versions_count}/{total_dependencies} ({latest_version_coverage_percentage}%)</dd>
```

---

## 15. Pull Request and Security Signals

### Pattern for Availability-Aware Access

Both PR and security data may be `"available"`, `"partial"`, or `"unavailable"`. Always check `availability` before rendering counts:

```js
// Safe PR access
const getOpenPRs = (repo) =>
  repo.pull_request_summary?.availability === "available"
    ? repo.pull_request_summary.total_open || 0
    : 0;

// Safe security access
const getAlerts = (repo) =>
  repo.security_summary?.availability === "available"
    ? repo.security_summary.active_alert_counts?.total_open || 0
    : 0;
```

### TableRow Signal Pills

```jsx
<span className={`${styles.signalPill} ${
  pullRequestSummary.availability !== "available"
    ? styles.signalPillMuted     // Gray for unavailable
    : openPullRequests > 0
      ? styles.signalPillWarning // Yellow for open PRs
      : styles.signalPillSuccess // Green for clear
}`}>
  {pullRequestLabel}
</span>
```

### RepositoryDetail Breakdown

The Signals section renders:
- **PR availability badge** (green/yellow/red)
- **Open PR count**, draft count, review-requested count
- **Oldest open PR age** in days
- **Security overall state** badge (`"clear"` = green, `"alerts_detected"` = red)
- **Alert counts** broken down by severity: Critical | High | Medium | Low
- **Feature status** per security feature (advanced_security, secret_scanning, etc.)

---

## 16. Export Functionality (CSV / JSON)

The `ExportButton` component generates client-side exports:

### CSV Columns Exported

```js
const columns = [
  { key: "name", label: "Repository Name" },
  { key: "language", label: "Language" },
  { key: "stars", label: "Stars" },
  { key: "forks", label: "Forks" },
  { key: "watchers", label: "Watchers" },
  { key: "open_issues", label: "Open Issues" },
  { key: "created_at", label: "Created At" },
  { key: "updated_at", label: "Last Updated" },
  { key: "commit_history.total_commits", label: "Total Commits" },
  { key: "commit_history.recent_90d", label: "Commits (90d)" },
  { key: "commit_history.recent_180d", label: "Commits (180d)" },
  { key: "commit_history.recent_365d", label: "Commits (365d)" },
  { key: "commit_history.first_commit_date", label: "First Commit" },
  { key: "commit_history.last_commit_date", label: "Last Commit" },
  { key: "commit_metrics.avg_size", label: "Avg Commit Size" },
  { key: "commit_metrics.largest_commit.size", label: "Largest Commit" },
  { key: "commit_metrics.smallest_commit.size", label: "Smallest Commit" },
  { key: "commit_velocity", label: "Commit Velocity" },
  { key: "age_days", label: "Age (days)" },
  { key: "days_since_last_push", label: "Days Since Push" },
  { key: "has_readme", label: "Has README" },
  { key: "has_license", label: "Has License" },
  { key: "has_ci_cd", label: "Has CI/CD" },
  { key: "has_tests", label: "Has Tests" },
  { key: "pull_request_summary.availability", label: "PR Data Availability" },
  { key: "pull_request_summary.total_open", label: "Open Pull Requests" },
  { key: "pull_request_summary.draft_count", label: "Draft Pull Requests" },
  { key: "pull_request_summary.review_requested_count", label: "PRs Awaiting Review" },
  { key: "security_summary.availability", label: "Security Data Availability" },
  { key: "security_summary.overall_state", label: "Security Overall State" },
  { key: "security_summary.active_alert_counts.total_open", label: "Open Security Alerts" },
  { key: "security_summary.active_alert_counts.critical", label: "Critical Alerts" },
  { key: "security_summary.active_alert_counts.high", label: "High Alerts" },
];
```

Nested fields are resolved using a dot-path helper:

```js
const getNestedValue = (obj, path) => {
  return path.split(".").reduce((acc, part) => acc?.[part], obj);
};
```

---

## 17. URL Routing and View Switching

The app uses URL hash routing (`window.location.hash`):

```js
// Read initial view from URL
const getInitialView = () => {
  const hash = window.location.hash.slice(1);
  if (hash === "visualizations") return "visualizations";
  if (hash === "attention") return "attention";
  return "table";
};

// Update URL on view change
const handleViewChange = (view) => {
  setCurrentView(view);
  if (view === "visualizations") { window.location.hash = "visualizations"; return; }
  if (view === "attention") { window.location.hash = "attention"; return; }
  window.location.hash = "";
};

// Listen for browser back/forward
useEffect(() => {
  const handleHashChange = () => {
    const hash = window.location.hash.slice(1);
    if (hash === "visualizations") setCurrentView("visualizations");
    else if (hash === "attention") setCurrentView("attention");
    else setCurrentView("table");
  };
  window.addEventListener("hashchange", handleHashChange);
  return () => window.removeEventListener("hashchange", handleHashChange);
}, []);
```

**Direct links:**
- `https://example.com/` → Dashboard table
- `https://example.com/#visualizations` → Charts
- `https://example.com/#attention` → Needs attention

---

## 18. Build and Deployment

### Development

```bash
cd frontend
npm install
npm run dev
# → http://localhost:5173
# Fetches from /data/repositories.json (requires data/ in project root)
```

### Production Build

```bash
cd frontend
npm run build
# 1. prebuild: clean + lint + format check
# 2. vite build → outputs to ../docs/
# 3. postbuild: copies data/ and output/ into docs/
```

Vite config (`vite.config.js`):
- Base path: `/github-stats-spark/` (for GitHub Pages)
- Output: `../docs/`
- Path alias: `@` → `./src`

### GitHub Actions Weekly Workflow

1. Python generates `data/repositories.json`
2. Frontend `npm run build` produces `docs/`
3. `data/` and `output/` are copied into `docs/`
4. CI commits all generated files with `[skip ci]`

### npm Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `react` | ^19.2.4 | UI framework |
| `react-dom` | ^19.2.4 | DOM rendering |
| `chart.js` | ^4.5.1 | Chart rendering engine |
| `react-chartjs-2` | ^5.3.1 | React Chart.js wrapper |
| `dexie` | ^4.4.1 | IndexedDB wrapper for offline caching |
| `react-markdown` | ^10.1.0 | Markdown rendering for AI summaries |
| `remark-gfm` | ^4.0.1 | GitHub Flavored Markdown plugin |
| `@use-gesture/react` | ^10.3.1 | Touch gesture support |
| `react-modal-sheet` | ^5.6.0 | Mobile bottom sheet |
| `prop-types` | ^15.8.1 | Runtime type checking |
| `web-vitals` | ^5.2.0 | Performance metrics |
| `workbox-window` | ^7.4.0 | Service worker management |
