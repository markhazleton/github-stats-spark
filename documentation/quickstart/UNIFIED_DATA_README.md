# Unified Data Generation - Implementation Summary

## What Was Created

A new comprehensive data generation system that merges all spark CLI commands (generate, analyze, dashboard) into a single unified `repositories.json` file with all attributes needed by the frontend.

## Files Created

### 1. **Core Module**
- **src/spark/unified_data_generator.py** (600+ lines)
  - `UnifiedDataGenerator` class
  - Combines data from all CLI commands
  - Comprehensive repository analysis
  - Support for AI summaries, tech stack analysis, ranking
  - Performance optimized with caching

### 2. **CLI Integration**
- **Updated: src/spark/cli.py**
  - Added new `unified` command
  - `handle_unified()` function
  - Updated help text and examples

### 3. **Documentation**
- **documentation/guides/UNIFIED_DATA_GENERATION.md** (500+ lines)
  - Complete usage guide
  - Configuration documentation
  - Output schema specification
  - Frontend integration examples
  - Troubleshooting guide

### 4. **Test Scripts**
- **test-unified-data.ps1** - PowerShell test script
- **test-unified-data.sh** - Bash test script

## Usage

### Basic Command

```bash
# Generate unified data for a user
spark unified --user markhazleton

# Output: data/repositories.json with comprehensive data
```

### With Options

```bash
# Include AI summaries (requires Anthropic API key)
spark unified --user markhazleton --include-ai-summaries

# Force refresh (bypass cache)
spark unified --user markhazleton --force-refresh

# Custom output directory
spark unified --user markhazleton --output-dir custom/path

# Verbose logging
spark unified --user markhazleton --verbose
```

## What Data Is Included

The unified `repositories.json` contains:

### Repository Data
- ✅ Basic metadata (name, description, URL, dates)
- ✅ Repository stats (stars, forks, watchers, issues)
- ✅ Repository attributes (archived, fork, readme, license, CI/CD, tests, docs)
- ✅ Language statistics and counts
- ✅ Activity metrics (age, last push, commit velocity, contributors, releases)

### Commit Analysis
- ✅ Total commits
- ✅ Recent activity (90d, 180d, 365d)
- ✅ First and last commit dates
- ✅ Commit velocity (commits per month)

### Repository Ranking
- ✅ Composite ranking score
- ✅ Repository rank (1-based)
- ✅ Configurable ranking weights

### Tech Stack Analysis (Optional)
- ✅ Framework detection
- ✅ Dependency analysis
- ✅ Outdated dependency detection
- ✅ Currency score (0-100)
- ✅ Dependency file types

### AI Summaries (Optional)
- ✅ AI-generated repository summaries
- ✅ Generation method and confidence scores
- ✅ Model information and token usage

### User Profile
- ✅ Username, avatar, bio
- ✅ Public repository count
- ✅ Total commits, stars, forks
- ✅ Company, location, blog
- ✅ Social links

### Metadata
- ✅ Generation timestamp
- ✅ Schema version (2.0.0)
- ✅ Repository count
- ✅ Generation time
- ✅ Cache statistics
- ✅ Error tracking
- ✅ Feature flags

## Output Schema

```json
{
  "repositories": [
    {
      "name": "repo-name",
      "description": "...",
      "url": "...",
      "language": "Python",
      "stars": 100,
      "forks": 25,
      "rank": 1,
      "composite_score": 85.5,
      "commit_history": {
        "total_commits": 500,
        "recent_90d": 50,
        "recent_180d": 100,
        "recent_365d": 200
      },
      "tech_stack": {
        "frameworks": ["Django"],
        "total_dependencies": 25,
        "outdated_count": 5,
        "currency_score": 75
      },
      "summary": {
        "text": "AI summary...",
        "ai_generated": true
      }
    }
  ],
  "profile": {
    "username": "markhazleton",
    "public_repos_count": 48,
    "total_commits": 5000,
    "total_stars": 250
  },
  "metadata": {
    "generated_at": "2024-01-01T12:00:00",
    "schema_version": "2.0.0",
    "repository_count": 48,
    "generation_time_seconds": 45.5
  }
}
```

## Configuration

Edit `config/spark.yml`:

```yaml
dashboard:
  enabled: true
  data_generation:
    max_repositories: 200        # Limit repositories
    max_commits_per_repo: 100    # Commits per repo
    include_ai_summaries: false  # Enable AI summaries

analyzer:
  top_repositories: 50           # Number to rank
  ranking_weights:
    stars_weight: 0.20
    commit_frequency_weight: 0.25
    # ... more weights
```

## Testing

```bash
# PowerShell
.\test-unified-data.ps1

# Bash
./test-unified-data.sh
```

The test will:
1. Display help
2. Generate unified data
3. Verify output file
4. Show data summary

## Frontend Integration

```javascript
// Load the unified data
const response = await fetch('/data/repositories.json');
const data = await response.json();

// Use the data
const repos = data.repositories;
const profile = data.profile;

// Filter and sort
const topRanked = repos
  .filter(r => r.rank !== null)
  .sort((a, b) => a.rank - b.rank);

const pythonRepos = repos.filter(r => r.language === 'Python');
```

## Benefits

### For Developers
- ✅ Single source of truth
- ✅ All data in one place
- ✅ Consistent structure
- ✅ Well-documented schema
- ✅ Easy to use

### For Frontend
- ✅ Single API call
- ✅ Rich data for displays
- ✅ No need to merge data
- ✅ Frontend-optimized structure
- ✅ Type-safe with schema

### Performance
- ✅ Caching support
- ✅ Rate limit handling
- ✅ Partial results on errors
- ✅ Configurable limits
- ✅ Progress tracking

## Next Steps

1. **Set GitHub Token**
   ```bash
   export GITHUB_TOKEN=your_token_here
   ```

2. **Generate Data**
   ```bash
   spark unified --user markhazleton
   ```

3. **Use in Frontend**
   - Import `data/repositories.json`
   - Build dashboards, charts, cards
   - Filter, sort, and display

4. **Optional: Add AI Summaries**
   ```bash
   export ANTHROPIC_API_KEY=your_key_here
   spark unified --user markhazleton --include-ai-summaries
   ```

5. **Automate**
   - Set up GitHub Actions
   - Schedule daily/weekly updates
   - Auto-commit updated data

## Comparison with Previous Approach

| Aspect | Before | After (Unified) |
|--------|--------|----------------|
| Commands needed | 3 (generate, analyze, dashboard) | 1 (unified) |
| Data files | Multiple | Single JSON |
| Data consistency | Manual merging | Automatic |
| Frontend integration | Complex | Simple |
| Maintenance | Multiple codebases | Single generator |
| Performance | 3 separate runs | 1 optimized run |

## Technical Details

### Architecture
- Inherits from all existing generators
- Reuses fetchers, rankers, analyzers
- Combines data in memory
- Single output pass

### Data Flow
1. Fetch repositories (GitHubFetcher)
2. Analyze commits (StatsCalculator)
3. Rank repositories (RepositoryRanker)
4. Analyze tech stack (DependencyAnalyzer)
5. Generate summaries (RepositorySummarizer, optional)
6. Build unified structure
7. Write JSON output

### Performance Features
- API caching (reduce API calls)
- Rate limit detection
- Error handling and recovery
- Configurable limits
- Progress logging

## Support

See full documentation:
- [Unified Data Generation Guide](documentation/guides/UNIFIED_DATA_GENERATION.md)
- [API Reference](src/spark/unified_data_generator.py)

## Success Criteria ✅

- [x] Merges all CLI commands data
- [x] Single comprehensive JSON output
- [x] All repository attributes included
- [x] Frontend-optimized structure
- [x] Well-documented and tested
- [x] Performance optimized
- [x] Error handling
- [x] Configurable
