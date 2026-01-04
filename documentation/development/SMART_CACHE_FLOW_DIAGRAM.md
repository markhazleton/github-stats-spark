# Smart Cache Refresh Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    spark unified --user USERNAME                     │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    UnifiedDataGenerator.generate()                   │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                        ┌───────────────────────┐
                        │  --force-refresh?     │
                        └───────────────────────┘
                          │                   │
                         Yes                 No
                          │                   │
                          ▼                   ▼
              ┌───────────────────┐  ┌──────────────────────┐
              │  Clear ALL cache  │  │ Check data freshness │
              │  Full generation  │  │  repositories.json   │
              └───────────────────┘  └──────────────────────┘
                                              │
                                              ▼
                                    ┌──────────────────┐
                                    │ File exists?     │
                                    └──────────────────┘
                                      │              │
                                     No             Yes
                                      │              │
                                      │              ▼
                                      │    ┌──────────────────────┐
                                      │    │ Parse generated_at   │
                                      │    │ from metadata        │
                                      │    └──────────────────────┘
                                      │              │
                                      │              ▼
                                      │    ┌──────────────────────┐
                                      │    │ Age < 7 days?        │
                                      │    └──────────────────────┘
                                      │      │              │
                                      │     Yes            No
                                      │      │              │
                                      │      ▼              ▼
                  ┌───────────────────┤  RETURN       ┌──────────────────────┐
                  │  Full generation  │  existing     │ Selective Refresh    │
                  │  (No existing     │  data         │ _selective_cache_    │
                  │   data)           │  (Skip!)      │      refresh()       │
                  └───────────────────┘               └──────────────────────┘
                           │                                    │
                           │                                    ▼
                           │                          ┌──────────────────────┐
                           │                          │ Fetch repo list      │
                           │                          │ (lightweight)        │
                           │                          └──────────────────────┘
                           │                                    │
                           │                                    ▼
                           │                          ┌──────────────────────┐
                           │                          │ For each repository: │
                           │                          │  Compare pushed_at   │
                           │                          │  with generated_at   │
                           │                          └──────────────────────┘
                           │                                    │
                           │                                    ▼
                           │                          ┌──────────────────────┐
                           │                          │ Build list of repos  │
                           │                          │ needing refresh      │
                           │                          └──────────────────────┘
                           │                                    │
                           │                                    ▼
                           │                          ┌──────────────────────┐
                           │                          │ _apply_selective_    │
                           │                          │    cache_clear()     │
                           │                          └──────────────────────┘
                           │                                    │
                           │                                    ▼
                           │                          ┌──────────────────────┐
                           │                          │ For each repo in     │
                           │                          │ refresh list:        │
                           │                          │  Clear cache entries │
                           │                          └──────────────────────┘
                           │                                    │
                           └────────────────────────────────────┘
                                                      │
                                                      ▼
                            ┌───────────────────────────────────────┐
                            │  Proceed with generation workflow:    │
                            │  1. Fetch repositories                │
                            │  2. Analyze commits                   │
                            │  3. Rank repositories                 │
                            │  4. Generate AI summaries (optional)  │
                            │  5. Analyze tech stack                │
                            │  6. Save to repositories.json         │
                            └───────────────────────────────────────┘
                                                      │
                                                      ▼
                            ┌───────────────────────────────────────┐
                            │  COMPLETE: repositories.json updated  │
                            │  with new generated_at timestamp      │
                            └───────────────────────────────────────┘
```

## Cache Key Structure

```
commits_{username}_{repo_name}_{iso_week}.json
└──────┘ └───────┘ └─────────┘ └────────┘
   │        │          │            │
   │        │          │            └─ ISO week (e.g., 2026W01)
   │        │          └────────────── Repository name
   │        └───────────────────────── GitHub username
   └────────────────────────────────── Cache entry type
```

### Cache Entry Types
- `commits_*` - Basic commit list
- `commit_counts_*` - Time-windowed commit counts
- `commits_stats_*` - Detailed commit statistics
- `languages_*` - Language breakdown
- `readme_*` - README content
- `dependency_files_*` - Dependency manifests
- `repositories_*` - Repository metadata
- `user_profile_*` - User profile data

## Decision Tree

```
Is repositories.json < 7 days old?
├─ YES → Return existing data (instant response)
└─ NO  → Continue to next check

Is --force-refresh flag set?
├─ YES → Clear ALL cache, full regeneration
└─ NO  → Use smart cache refresh

For each repository:
  Has repository.pushed_at > repositories.json.generated_at?
  ├─ YES → Add to refresh list
  └─ NO  → Keep existing cache

Clear cache only for repositories in refresh list
Proceed with normal generation workflow
```

## Performance Comparison

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        Traditional Approach                               │
├──────────────────────────────────────────────────────────────────────────┤
│  Every run:                                                               │
│  • Fetch all 50 repositories          → 50 API calls                     │
│  • Fetch commits for each             → 50 API calls                     │
│  • Fetch languages for each           → 50 API calls                     │
│  • Fetch README for each              → 50 API calls                     │
│  • Fetch dependencies for each        → 50 API calls                     │
│  • Total API calls:                   → ~250 calls                       │
│  • Execution time:                    → ~5 minutes                       │
└──────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────┐
│                      Smart Cache Refresh (< 1 week)                       │
├──────────────────────────────────────────────────────────────────────────┤
│  • Check repositories.json age        → 0 API calls                      │
│  • Return existing data               → 0 API calls                      │
│  • Total API calls:                   → 0 calls                          │
│  • Execution time:                    → <1 second                        │
│  • Savings:                           → 100% API calls, 99.7% time       │
└──────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────┐
│              Smart Cache Refresh (>= 1 week, 5 repos changed)             │
├──────────────────────────────────────────────────────────────────────────┤
│  • Fetch lightweight repo list        → 1 API call                       │
│  • Identify 5 repos with new commits  → 0 API calls (cached)            │
│  • Clear cache for 5 repos only       → 0 API calls                     │
│  • Fetch data for 5 repos             → ~25 API calls                    │
│  • Use cache for 45 repos             → 0 API calls                     │
│  • Total API calls:                   → ~26 calls                        │
│  • Execution time:                    → ~30 seconds                      │
│  • Savings:                           → 90% API calls, 90% time          │
└──────────────────────────────────────────────────────────────────────────┘
```

## Example Scenarios

### Scenario 1: Daily Developer Workflow

```
Day 1 (Monday):      spark unified --user dev
                     → repositories.json created (2026-01-06 09:00:00)
                     → Full generation (5 minutes)

Day 2 (Tuesday):     spark unified --user dev
                     → Data age: 1 day < 7 days
                     → SKIP generation, return existing data (<1 second)

Day 3 (Wednesday):   spark unified --user dev
                     → Data age: 2 days < 7 days
                     → SKIP generation, return existing data (<1 second)

Day 8 (Next Monday): spark unified --user dev
                     → Data age: 7 days >= 7 days
                     → Smart refresh: 3 active repos updated
                     → Selective refresh (30 seconds)
                     → New repositories.json created (2026-01-13 09:00:00)
```

### Scenario 2: Weekly CI/CD Pipeline

```
Week 1 (2026W01):    GitHub Actions runs on Sunday
                     → No existing data
                     → Full generation (5 minutes)
                     → Commit: repositories.json

Week 2 (2026W02):    GitHub Actions runs on Sunday
                     → Data age: 7 days
                     → Smart refresh: 12 active repos
                     → Selective refresh (1 minute)
                     → Commit: updated repositories.json

Week 3 (2026W03):    GitHub Actions runs on Sunday
                     → Data age: 7 days
                     → Smart refresh: 8 active repos
                     → Selective refresh (45 seconds)
                     → Commit: updated repositories.json
```

### Scenario 3: Archived Project

```
Project last active: 2025-11-01
Last data generation: 2025-11-15

Current date: 2026-01-06
Run: spark unified --user archive

Check: Data age = 52 days >= 7 days
Fetch: 20 repositories
Compare push dates:
  • repo1.pushed_at: 2025-10-15 < 2025-11-15 → No refresh
  • repo2.pushed_at: 2025-10-20 < 2025-11-15 → No refresh
  • ... (all 20 repos have no new commits)

Result: 0 repositories need refresh
        Use existing cache for all repos
        Fast generation (10 seconds)
        Data confirms project is inactive
```
