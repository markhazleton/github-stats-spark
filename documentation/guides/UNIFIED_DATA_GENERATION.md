# Unified Data Generation

## Overview

The `spark unified` command generates a comprehensive `repositories.json` file that merges data from all CLI commands (`generate`, `analyze`, `dashboard`) into a single, feature-rich dataset optimized for frontend consumption.

## What's Included

The unified data generator combines:

### 1. **Repository Metadata** (from `generate`)
- Basic repository information (name, description, URL)
- Languages and language statistics
- Repository attributes (stars, forks, watchers, open issues)
- Repository flags (archived, fork, has_readme, has_license, etc.)

### 2. **Commit Analysis** (from `analyze`)
- Detailed commit history (total, recent 90d/180d/365d)
- Commit velocity (commits per month)
- First and last commit dates
- Contributor counts

### 3. **Repository Ranking** (from `analyze`)
- Composite ranking score
- Repository rank (1-based)
- Calculated based on configurable weights

### 4. **Tech Stack Analysis** (from `analyze`)
- Framework detection
- Dependency analysis
- Outdated dependency detection
- Currency score (0-100)
- Dependency file types

### 5. **AI Summaries** (optional, from `analyze`)
- AI-generated repository summaries
- Generation method and confidence scores
- Model information and token usage

### 6. **User Profile** (from `dashboard`)
- Username and avatar
- Public repository count
- Total commits, stars, forks
- Bio, company, location, blog
- Social links

### 7. **Metadata**
- Generation timestamp
- Schema version (2.0.0)
- Repository count
- Data source information
- Generation time
- Cache hit rate
- Error tracking
- Feature flags

## Usage

### Basic Usage

```bash
# Generate unified data for a user
spark unified --user markhazleton

# Output: data/repositories.json
```

### With AI Summaries

```bash
# Include AI-generated summaries (requires Anthropic API key)
spark unified --user markhazleton --include-ai-summaries

# Set API key
export ANTHROPIC_API_KEY=your_key_here
```

### Custom Output Directory

```bash
# Specify custom output directory
spark unified --user markhazleton --output-dir custom/path
```

### Force Refresh

```bash
# Bypass cache and fetch fresh data
spark unified --user markhazleton --force-refresh
```

### Verbose Mode

```bash
# Enable detailed logging
spark unified --user markhazleton --verbose
```

## Configuration

The unified generator uses settings from `config/spark.yml`:

```yaml
# Dashboard configuration (used by unified generator)
dashboard:
  enabled: true
  data_generation:
    max_repositories: 200        # Limit number of repositories
    max_commits_per_repo: 100    # Commits to fetch per repo
    include_ai_summaries: false  # Enable AI summaries
    include_commit_metrics: true
    include_language_stats: true

# Analyzer configuration (used for ranking)
analyzer:
  top_repositories: 50  # Number of repositories to rank
  ranking_weights:
    stars_weight: 0.20
    commit_frequency_weight: 0.25
    recency_weight: 0.15
    # ... more weights
```

## Output Schema

The generated `repositories.json` has the following structure:

```json
{
  "repositories": [
    {
      "name": "repo-name",
      "description": "Repository description",
      "url": "https://github.com/user/repo",
      "language": "Python",
      "created_at": "2023-01-01T00:00:00+00:00",
      "updated_at": "2024-01-01T00:00:00+00:00",
      "pushed_at": "2024-01-01T00:00:00+00:00",
      
      "stars": 100,
      "forks": 25,
      "watchers": 50,
      "open_issues": 5,
      "size_kb": 5000,
      
      "is_archived": false,
      "is_fork": false,
      "has_readme": true,
      "has_license": true,
      "has_ci_cd": true,
      "has_tests": true,
      "has_docs": true,
      
      "language_stats": {
        "Python": 50000,
        "JavaScript": 30000
      },
      "language_count": 2,
      
      "age_days": 365,
      "days_since_last_push": 7,
      "commit_velocity": 15.5,
      "contributors_count": 10,
      "release_count": 5,
      "latest_release_date": "2024-01-01T00:00:00+00:00",
      
      "rank": 1,
      "composite_score": 85.5,
      
      "commit_history": {
        "total_commits": 500,
        "recent_90d": 50,
        "recent_180d": 100,
        "recent_365d": 200,
        "last_commit_date": "2024-01-01T00:00:00+00:00",
        "first_commit_date": "2023-01-01T00:00:00+00:00"
      },
      
      "tech_stack": {
        "frameworks": ["Django", "React"],
        "dependencies": [
          {
            "name": "django",
            "current_version": "4.2.0",
            "latest_version": "5.0.0",
            "ecosystem": "pypi",
            "versions_behind": 1,
            "is_outdated": true,
            "status": "major_outdated"
          }
        ],
        "dependency_file_type": "requirements.txt",
        "total_dependencies": 25,
        "outdated_count": 5,
        "outdated_percentage": 20.0,
        "currency_score": 75
      },
      
      "summary": {
        "text": "AI-generated repository summary...",
        "ai_generated": true,
        "generation_method": "claude-haiku",
        "confidence_score": 85,
        "model_used": "claude-haiku-3.5"
      }
    }
  ],
  
  "profile": {
    "username": "markhazleton",
    "avatar_url": "https://avatars.githubusercontent.com/...",
    "public_repos_count": 48,
    "profile_url": "https://github.com/markhazleton",
    "total_commits": 5000,
    "total_stars": 250,
    "total_forks": 75,
    "bio": "Software Engineer",
    "company": "Company Name",
    "location": "City, State",
    "blog": "https://blog.example.com",
    "twitter_username": "username"
  },
  
  "metadata": {
    "generated_at": "2024-01-01T12:00:00",
    "schema_version": "2.0.0",
    "repository_count": 48,
    "data_source": "GitHub API",
    "generation_time_seconds": 45.5,
    "cache_hit_rate": "75% (30/40)",
    "errors": null,
    "partial_results": false,
    "features": {
      "commit_metrics": true,
      "tech_stack_analysis": true,
      "ai_summaries": false,
      "ranking": true
    },
    "ai_usage": {
      "total_tokens": 15000,
      "total_cost_usd": 0.05,
      "cache_hits": 10,
      "cache_misses": 5,
      "cache_hit_rate": "66.7%"
    }
  }
}
```

## Features

### Comprehensive Data
- All attributes from generate, analyze, and dashboard commands
- Single source of truth for frontend applications
- Consistent data structure across all repositories

### Performance Optimization
- Caching support (bypass with `--force-refresh`)
- Rate limit handling
- Partial results on errors
- Configurable repository and commit limits

### Quality Indicators
- Repository ranking and scoring
- Tech stack currency scores
- Dependency status tracking
- Activity metrics

### Error Handling
- Graceful degradation on API errors
- Error tracking in metadata
- Partial results support
- Rate limit detection

## Frontend Integration

The unified data is optimized for frontend consumption:

### Loading Data

```javascript
// Fetch the unified data
const response = await fetch('/data/repositories.json');
const data = await response.json();

// Access repositories
const repos = data.repositories;
const profile = data.profile;
const metadata = data.metadata;
```

### Filtering and Sorting

```javascript
// Filter by language
const pythonRepos = repos.filter(r => r.language === 'Python');

// Sort by ranking
const topRanked = repos
  .filter(r => r.rank !== null)
  .sort((a, b) => a.rank - b.rank);

// Sort by stars
const mostStarred = repos
  .sort((a, b) => b.stars - a.stars);

// Filter by tech stack currency
const wellMaintained = repos
  .filter(r => r.tech_stack?.currency_score >= 80);
```

### Display Components

```javascript
// Repository card with all data
function RepositoryCard({ repo }) {
  return (
    <div className="repo-card">
      <h3>{repo.name}</h3>
      <p>{repo.description}</p>
      
      <div className="stats">
        <span>⭐ {repo.stars}</span>
        <span>🔀 {repo.forks}</span>
        <span>💻 {repo.language}</span>
      </div>
      
      {repo.rank && (
        <div className="ranking">
          Rank #{repo.rank} (Score: {repo.composite_score})
        </div>
      )}
      
      {repo.commit_history && (
        <div className="activity">
          {repo.commit_history.total_commits} commits
          ({repo.commit_history.recent_90d} in last 90 days)
        </div>
      )}
      
      {repo.tech_stack && (
        <div className="tech-stack">
          <div>Dependencies: {repo.tech_stack.total_dependencies}</div>
          <div>Currency: {repo.tech_stack.currency_score}/100</div>
          {repo.tech_stack.outdated_count > 0 && (
            <div className="warning">
              {repo.tech_stack.outdated_count} outdated
            </div>
          )}
        </div>
      )}
      
      {repo.summary && (
        <div className="summary">
          {repo.summary.text}
          {repo.summary.ai_generated && (
            <span className="ai-badge">AI Generated</span>
          )}
        </div>
      )}
    </div>
  );
}
```

## Testing

Run the test script to verify the unified generator:

```bash
# PowerShell
.\test-unified-data.ps1

# Bash
./test-unified-data.sh
```

The test script will:
1. Display command help
2. Generate unified data for a test user
3. Verify output file creation
4. Parse and display data summary
5. Show sample repository data

## Comparison with Other Commands

| Feature | `unified` | `generate` | `analyze` | `dashboard` |
|---------|-----------|------------|-----------|-------------|
| Repository metadata | ✅ | ✅ | ✅ | ✅ |
| Commit metrics | ✅ | ❌ | ✅ | ✅ |
| Repository ranking | ✅ | ❌ | ✅ | ❌ |
| Tech stack analysis | ✅ | ❌ | ✅ | ❌ |
| AI summaries | ✅ (opt) | ❌ | ✅ | ❌ |
| User profile | ✅ | ❌ | ✅ | ✅ |
| Single JSON output | ✅ | ❌ | ❌ | ✅ |
| Frontend optimized | ✅ | ❌ | ❌ | ✅ |

## Performance Tips

1. **Use caching**: Don't use `--force-refresh` unless needed
2. **Limit repositories**: Configure `max_repositories` for faster generation
3. **Skip AI summaries**: Only use `--include-ai-summaries` when needed
4. **Monitor rate limits**: GitHub API has rate limits (5000/hour with token)
5. **Incremental updates**: Cache prevents re-fetching unchanged data

## Troubleshooting

### Rate Limit Errors

```bash
# GitHub API rate limit reached
# Solution: Wait for reset or use token with higher limits
curl https://api.github.com/rate_limit

# Check when rate limit resets
```

### Missing Data

```bash
# Some repositories missing data
# Solution: Check metadata.errors for specific failures
jq '.metadata.errors' data/repositories.json
```

### Large File Size

```bash
# Output file too large
# Solution: Reduce max_repositories or disable AI summaries

# Edit config/spark.yml
dashboard:
  data_generation:
    max_repositories: 50  # Reduce from 200
    include_ai_summaries: false
```

### Slow Generation

```bash
# Taking too long to generate
# Solution: Reduce commits per repo or use cache

# Edit config/spark.yml
dashboard:
  data_generation:
    max_commits_per_repo: 50  # Reduce from 100
```

## Next Steps

1. **Use the data**: Import `data/repositories.json` in your frontend
2. **Customize**: Edit `config/spark.yml` to adjust settings
3. **Automate**: Set up scheduled generation (GitHub Actions)
4. **Enhance**: Add custom attributes to the UnifiedDataGenerator

## API Reference

See [unified_data_generator.py](../src/spark/unified_data_generator.py) for the full implementation.

Key classes:
- `UnifiedDataGenerator`: Main generator class
- `generate()`: Generate unified data
- `save()`: Save to JSON file
- `_build_unified_repo_data()`: Build repository data structure
