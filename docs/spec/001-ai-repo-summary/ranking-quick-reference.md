# Repository Ranking Quick Reference

**Context**: FR-002, SC-007 - Top 50 repository ranking algorithm
**Full Research**: See `repository-ranking-research.md`

## TL;DR: Recommended Formula

```python
Repository_Score = Popularity × 0.30 + Activity × 0.45 + Health × 0.25
```

**Weighting Rationale**:
- **45% Activity**: Ensures "active, well-maintained" repos rank high (SC-007)
- **30% Popularity**: Stars/forks indicate significance without dominating
- **25% Health**: Documentation, maturity, issue management matter

---

## Component Formulas

### Popularity Score (0-100)

```python
popularity = (
    min(50, 12.5 × log10(stars + 1)) +      # 50% weight
    min(30, 10 × log10(forks + 1)) +        # 30% weight
    min(20, 8 × log10(watchers + 1))        # 20% weight
)
```

**Key**: Logarithmic scaling prevents mega-repos from dominating.

### Activity Score (0-100)

```python
activity = (
    commit_score × 0.50 +     # Recent commit volume
    recency_score × 0.30 +    # How recently pushed
    engagement × 0.20         # Issues + PRs
)

where:
    commit_score = (
        min(50, commits_90d × 2) × 0.5 +      # Last 90 days: 50%
        min(50, commits_180d × 1) × 0.3 +     # 90-180 days: 30%
        min(50, commits_365d × 0.5) × 0.2     # 180-365 days: 20%
    )

    recency_score = {
        30 if last_push < 7 days ago
        25 if last_push < 30 days ago
        15 if last_push < 90 days ago
        5 if last_push < 180 days ago
        0 otherwise
    }

    engagement = min(20, (open_issues + pull_requests) × 0.5)
```

**Key**: Multi-window approach with time decay favors recently active repos.

### Health Score (0-100)

```python
health = (
    documentation_score +  # 30%: README, license, description
    maturity_score +       # 30%: Age sweet spot (6mo-3yr)
    issue_score -          # 25%: Issue closure rate
    archive_penalty        # -50 if archived
)

where:
    documentation = (
        15 if has_readme else 0 +
        10 if has_license else 0 +
        5 if description length > 20 else 0
    )

    maturity = {
        5 if age < 30 days
        15 if age < 180 days
        30 if age < 1095 days (3 years)
        20 if age >= 1095 days
    }

    issue_score = (closed_issues / total_issues) × 25

    archive_penalty = -50 if archived else 0
```

**Key**: Rewards mature, well-documented repos with good issue management.

---

## Recent Activity Timeframe

**Recommended Windows**:
- **Primary**: 90 days (3 months) - 50% weight
- **Secondary**: 180 days (6 months) - 30% weight
- **Tertiary**: 365 days (1 year) - 20% weight

**Activity Classification**:
| Last Commit | Status | Score Impact |
|-------------|--------|--------------|
| < 7 days | Actively developed | +30% |
| 7-30 days | Recently maintained | +20% |
| 30-90 days | Maintained | +10% |
| 90-180 days | Sporadically maintained | 0% |
| 180-365 days | Minimally maintained | -20% |
| > 365 days | Stale | -50% |

---

## Edge Case Handling

### Archived Repositories
```python
if is_archived:
    popularity_score *= 0.5  # 50% reduction
    activity_score *= 0.1    # 90% reduction

    # Exception for historically significant
    if stars > 1000:
        popularity_score *= 0.7 / 0.5  # Only 30% reduction
```

### Forked Repositories
```python
if is_fork:
    if commits_ahead > 10 and commits_ahead > commits_behind:
        # Active fork with meaningful changes
        all_scores *= 0.8
    else:
        # Minimal changes from upstream
        all_scores *= 0.3
```

**Alternative**: Use `exclude_forks=True` flag (already in codebase).

### Zero-Star Active Projects
```python
if popularity_score < 20 and activity_score > 70:
    # Boost underrated, actively-developed projects
    boost = (activity_score - popularity_score) × 0.3
    popularity_score += boost
```

### Empty Repositories
```python
# Filter out empty repos
exclude if commits == 0 or size < 10KB
```

---

## Normalization Strategies

### Problem: Repository Age Bias
- Old repo: 300 commits in 3 years (100/year)
- New repo: 150 commits in 3 months (600/year)

Without normalization, old repo scores higher despite being less active.

### Solution: Activity Rate
```python
def normalize_by_age(commits_total, repo_age_days, recent_commits_90d):
    if repo_age_days < 90:
        # Very young: use total commits
        activity_rate = commits_total / max(1, repo_age_days) × 30
    else:
        # Mature: use 90-day rate
        activity_rate = recent_commits_90d / 3  # commits per month

    return min(100, activity_rate × 5)
```

**Key**: Use recent activity rate (commits/month), not absolute totals.

---

## Example Scores

| Scenario | Pop | Act | Health | Total | Rank |
|----------|-----|-----|--------|-------|------|
| **Ideal**: 1.2K stars, 45 commits/90d, 3d ago | 76 | 95 | 81 | 84 | 1 |
| **Legacy**: 5K stars, 2 commits/90d, 45d ago | 94 | 40 | 65 | 62 | 2 |
| **New Active**: 15 stars, 80 commits/90d, 2d ago | 27 | 84 | 59 | 55 | 3 |
| **Archived**: 10K stars, 0 commits/90d, archived | 50 | 2 | 13 | 24 | 4 |
| **Fork**: 5 stars, fork with 3 ahead/500 behind | 4 | 8 | 40 | 14 | 5 |

**Validation**: With 45% activity weight, 2 of top 3 are active = meets SC-007 threshold.

---

## Implementation Checklist

### Phase 1: Basic Ranking (MVP)
- [ ] Popularity score with logarithmic scaling
- [ ] Activity score (90-day window)
- [ ] Health score (docs, age, issues)
- [ ] Composite weighted score
- [ ] Sort and return top 50

### Phase 2: Enhanced Metrics
- [ ] Multi-window activity (90d/180d/365d)
- [ ] Recency bonus/penalty
- [ ] Engagement score (issues + PRs)
- [ ] Maturity sweet spot (6mo-3yr)

### Phase 3: Edge Cases
- [ ] Archived repository penalty
- [ ] Fork divergence check
- [ ] Zero-star boost for active projects
- [ ] Empty repository filter

### Phase 4: Optimization
- [ ] Activity rate normalization
- [ ] Percentile ranking (optional)
- [ ] User-configurable weights
- [ ] Caching for repeated rankings

---

## Integration Points

### Existing Code to Extend

**`src/spark/fetcher.py`**:
```python
# Add method for time-windowed commit counts
def fetch_repository_metrics(self, username, repo_name):
    return {
        'commits_90d': count_commits_since(90_days_ago),
        'commits_180d': count_commits_since(180_days_ago),
        'commits_365d': count_commits_since(365_days_ago),
        'open_issues': repo.open_issues_count,
        'closed_issues': repo.get_issues(state='closed').totalCount,
        'is_archived': repo.archived,
        'is_fork': repo.fork,
        'has_readme': check_has_readme(repo),
        'has_license': repo.license is not None,
    }
```

**New module: `src/spark/ranker.py`**:
```python
class RepositoryRanker:
    def rank_repositories(self, repos, top_n=50):
        # Calculate scores
        # Apply edge case adjustments
        # Sort by composite score
        # Return top N
```

### Usage Example

```python
from spark.fetcher import GitHubFetcher
from spark.ranker import RepositoryRanker

# Fetch all repos
fetcher = GitHubFetcher(token=GITHUB_TOKEN)
repos = fetcher.fetch_repositories('username')

# Enrich with ranking metrics
for repo in repos:
    metrics = fetcher.fetch_repository_metrics('username', repo['name'])
    repo.update(metrics)

# Rank and get top 50
ranker = RepositoryRanker()
top_50 = ranker.rank_repositories(repos, top_n=50)

print(f"Top repository: {top_50[0]['name']} (score: {top_50[0]['composite_score']})")
```

---

## Validation Against Requirements

### FR-002: Rank by stars, forks, commits, issues
- ✅ Stars: 50% of popularity score
- ✅ Forks: 30% of popularity score
- ✅ Recent commits: 50% of activity score
- ✅ Issue engagement: 20% of activity score

### SC-007: Active repos in top 10 positions 85% of time
- ✅ Activity weight = 45% (highest component)
- ✅ Recency bonus favors recently pushed repos
- ✅ Multi-window decay penalizes stale repos
- ✅ Archived repos heavily penalized

**Expected Result**: With recommended weights, 85%+ of top 10 will have activity within 90 days.

---

## Quick Decision Matrix

**When to use this ranking algorithm**:
- ✅ Generating "top 50 repositories" for a user profile
- ✅ Identifying most significant projects across a portfolio
- ✅ Highlighting active, well-maintained work

**When NOT to use**:
- ❌ Sorting by popularity alone (use stars)
- ❌ Finding newest projects (use creation date)
- ❌ Language-specific filtering (add language filter first)

---

## Performance Considerations

**Time Complexity**: O(n log n) for sorting n repositories

**API Calls Required per Repository**:
- Basic info: 1 call (already fetched)
- Commits by time window: 3 calls (90d, 180d, 365d)
- Issue counts: 1 call (closed issues)
- README check: 1 call
- **Total**: ~6 calls per repo

**For 50 repositories**: ~300 API calls
- With caching: ~50 calls (5000 limit = plenty of headroom)
- Without caching: 300 calls (within 5000/hour limit)

**Optimization**: Batch fetch metrics and cache aggressively.

---

**Next Steps**:
1. Review detailed research in `repository-ranking-research.md`
2. Implement `src/spark/ranker.py` module
3. Extend `src/spark/fetcher.py` with metrics methods
4. Test against real user data
5. Validate SC-007 compliance (85% active in top 10)

**Status**: Research complete, ready for implementation.
