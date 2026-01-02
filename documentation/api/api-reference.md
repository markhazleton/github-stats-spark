# API Reference

**Stats Spark** - GitHub Profile Statistics Generator

This document provides detailed API documentation for the core modules of Stats Spark.

---

## Core Modules

### `spark.config.SparkConfig`

Configuration management class for loading and validating Stats Spark settings.

#### Constructor

```python
SparkConfig(config_path: str = "config/spark.yml")
```

**Parameters:**
- `config_path` (str): Path to YAML configuration file. Defaults to `config/spark.yml`.

**Raises:**
- `FileNotFoundError`: If configuration file doesn't exist
- `ValueError`: If configuration is invalid or missing required fields

#### Methods

##### `load() -> Dict[str, Any]`

Load and parse configuration from YAML file.

**Returns:**
- `Dict[str, Any]`: Parsed configuration dictionary

**Example:**
```python
config = SparkConfig("config/spark.yml")
settings = config.load()
print(settings["user"])  # "auto" or username
```

##### `validate() -> bool`

Validate configuration structure and values.

**Returns:**
- `bool`: True if valid, raises ValueError otherwise

**Validation checks:**
- Required fields present (user, stats, visualization, cache, repositories)
- Theme exists (built-in or in themes.yml)
- Enabled statistics are valid categories
- Repository limits are positive integers
- Cache TTL is positive

**Example:**
```python
config = SparkConfig()
if config.validate():
    print("Configuration is valid")
```

##### `get_theme() -> Theme`

Get theme instance based on configuration.

**Returns:**
- `Theme`: Instance of SparkDarkTheme, SparkLightTheme, or CustomTheme

**Example:**
```python
config = SparkConfig()
theme = config.get_theme()
print(theme.primary_color)  # "#0EA5E9" for spark-dark
```

##### `get(key: str, default: Any = None) -> Any`

Get configuration value by dotted key path.

**Parameters:**
- `key` (str): Dotted path to config value (e.g., "stats.enabled")
- `default` (Any): Default value if key not found

**Returns:**
- `Any`: Configuration value or default

**Example:**
```python
config = SparkConfig()
enabled_stats = config.get("stats.enabled", [])
max_repos = config.get("repositories.max_count", 500)
```

---

### `spark.calculator.StatsCalculator`

Statistics calculation engine for GitHub activity analysis.

#### Constructor

```python
StatsCalculator(profile: Dict[str, Any], repositories: List[Dict[str, Any]])
```

**Parameters:**
- `profile` (Dict): User profile data from GitHub API
  - `username` (str): GitHub username
  - `public_repos` (int): Number of public repositories
  - `followers` (int): Follower count
- `repositories` (List[Dict]): List of repository data
  - Each repo contains: `name`, `stars`, `forks`, `watchers`

**Example:**
```python
profile = {
    "username": "markhazleton",
    "public_repos": 50,
    "followers": 100
}
repositories = [
    {"name": "repo1", "stars": 150, "forks": 20, "watchers": 30}
]
calculator = StatsCalculator(profile, repositories)
```

#### Methods

##### `add_commits(commits: List[Dict[str, Any]]) -> None`

Add commit data for analysis.

**Parameters:**
- `commits` (List[Dict]): Commit data with fields:
  - `sha` (str): Commit hash
  - `date` (str): ISO format timestamp
  - `message` (str): Commit message

**Example:**
```python
commits = [
    {"sha": "abc123", "date": "2025-12-28T10:00:00Z", "message": "Fix bug"}
]
calculator.add_commits(commits)
```

##### `add_languages(languages: Dict[str, int]) -> None`

Add language statistics from repositories.

**Parameters:**
- `languages` (Dict[str, int]): Language names to byte counts

**Example:**
```python
calculator.add_languages({"Python": 5000, "JavaScript": 3000})
```

##### `calculate_spark_score() -> Dict[str, Any]`

Calculate overall Spark Score (0-100 scale).

**Formula:**
- 40% Consistency (commit regularity)
- 35% Volume (commit count with logarithmic scaling)
- 25% Collaboration (stars, forks, followers, watchers)

**Returns:**
- `Dict[str, Any]` with fields:
  - `total_score` (float): Overall score (0-100)
  - `consistency_score` (float): Consistency component (0-100)
  - `volume_score` (float): Volume component (0-100)
  - `collaboration_score` (float): Collaboration component (0-100)
  - `lightning_rating` (int): Rating as lightning bolts (1-5)

**Example:**
```python
score = calculator.calculate_spark_score()
print(f"Score: {score['total_score']}")  # e.g., 78.5
print(f"Rating: {'⚡' * score['lightning_rating']}")  # ⚡⚡⚡⚡
```

##### `calculate_lightning_rating(score: float) -> int`

Map score to lightning bolt rating.

**Parameters:**
- `score` (float): Score value (0-100)

**Returns:**
- `int`: Lightning bolts (1-5)

**Thresholds:**
- 5 bolts: score >= 80
- 4 bolts: score >= 60
- 3 bolts: score >= 40
- 2 bolts: score >= 20
- 1 bolt: score < 20

**Example:**
```python
rating = calculator.calculate_lightning_rating(85)  # 5
```

##### `analyze_time_patterns() -> Dict[str, Any]`

Analyze commit time distribution and categorize coding pattern.

**Returns:**
- `Dict[str, Any]` with fields:
  - `hour_distribution` (Dict[int, int]): Commits per hour (0-23)
  - `category` (str): "night_owl", "early_bird", or "balanced"
  - `most_active_hour` (int): Hour with most commits

**Categories:**
- **Night Owl**: Majority of commits between 22:00-4:00
- **Early Bird**: Majority of commits between 5:00-9:00
- **Balanced**: Even distribution throughout day

**Example:**
```python
patterns = calculator.analyze_time_patterns()
print(patterns["category"])  # "night_owl"
print(patterns["most_active_hour"])  # 23
```

##### `aggregate_languages() -> List[Dict[str, Any]]`

Calculate language percentages and group into top 10 + "Other".

**Returns:**
- `List[Dict[str, Any]]`: Sorted by percentage descending
  - `name` (str): Language name
  - `bytes` (int): Total bytes
  - `percentage` (float): Percentage of total

**Features:**
- Groups languages beyond top 9 into "Other"
- Sorts by bytes (highest first)
- Percentages sum to 100%

**Example:**
```python
languages = calculator.aggregate_languages()
for lang in languages[:3]:
    print(f"{lang['name']}: {lang['percentage']:.1f}%")
# Python: 45.2%
# JavaScript: 30.1%
# HTML: 15.8%
```

##### `calculate_streaks() -> Dict[str, Any]`

Calculate coding streaks and learning patterns.

**Returns:**
- `Dict[str, Any]` with fields:
  - `current_streak` (int): Consecutive days with commits (from today backwards)
  - `longest_streak` (int): Longest streak in history
  - `learning_streak` (int): Days working with new languages

**Example:**
```python
streaks = calculator.calculate_streaks()
print(f"Current streak: {streaks['current_streak']} days")
print(f"Longest streak: {streaks['longest_streak']} days")
```

##### `calculate_release_cadence(weeks: int = 12, months: int = 12) -> Dict[str, Any]`

Compute weekly and monthly unique repository touchpoints for cadence sparklines.

**Parameters:**
- `weeks` (int): Number of trailing weeks to summarize
- `months` (int): Number of trailing months to summarize

**Returns:**
- `Dict[str, Any]` with fields:
  - `weekly` (List[Dict]): Ordered list of week labels and repo counts
  - `monthly` (List[Dict]): Ordered list of month labels and repo counts
  - `max_weekly` / `max_monthly` (int): Peak repo counts for scaling
  - `unique_repos` (int): Unique repositories touched in the sampled periods

**Example:**
```python
cadence = calculator.calculate_release_cadence()
print(cadence["weekly"][-1])  # {'label': 'W08', 'repos': 5, ...}
```

---

### `spark.visualizer.StatisticsVisualizer`

SVG visualization generator for GitHub statistics.

#### Constructor

```python
StatisticsVisualizer(theme: Theme, enable_effects: bool = True)
```

**Parameters:**
- `theme` (Theme): Theme instance (SparkDarkTheme, SparkLightTheme, CustomTheme)
- `enable_effects` (bool): Enable visual effects (glow, gradients). Defaults to True.

**Example:**
```python
from spark.themes.spark_dark import SparkDarkTheme

theme = SparkDarkTheme()
visualizer = StatisticsVisualizer(theme, enable_effects=True)
```

#### Methods

##### `generate_overview(...) -> str`

Generate overview SVG with Spark Score and key metrics.

**Parameters:**
- `username` (str): GitHub username
- `spark_score` (Dict): Spark Score data from calculator
- `total_commits` (int): Total commit count
- `languages` (List[Dict]): Top languages (up to 5 displayed)
- `time_pattern` (Dict): Time pattern analysis

**Returns:**
- `str`: SVG content as XML string

**Dimensions:** 800×400 pixels

**Layout:**
- Spark Score circle with lightning bolts
- Component scores (consistency, volume, collaboration)
- Top 4 languages with horizontal bars
- Time pattern badge (Night Owl/Early Bird/Balanced)
- "Powered by Stats Spark" footer

**Example:**
```python
svg = visualizer.generate_overview(
    username="markhazleton",
    spark_score={"total_score": 78.5, "lightning_rating": 4, ...},
    total_commits=1250,
    languages=[{"name": "Python", "percentage": 45.2}, ...],
    time_pattern={"category": "night_owl", "most_active_hour": 23}
)
with open("output/overview.svg", "w") as f:
    f.write(svg)
```

##### `generate_heatmap(...) -> str`

Generate commit frequency heatmap (GitHub-style calendar).

**Parameters:**
- `username` (str): GitHub username
- `commits_by_date` (Dict[str, int]): Date (YYYY-MM-DD) to commit count

**Returns:**
- `str`: SVG content

**Dimensions:** 900×200 pixels

**Features:**
- 52 weeks × 7 days grid
- Color intensity based on commit frequency
- Month labels
- Tooltips with date and count

**Example:**
```python
commits_by_date = {
    "2025-12-28": 5,
    "2025-12-27": 3,
    # ...
}
svg = visualizer.generate_heatmap("markhazleton", commits_by_date)
```

##### `generate_languages(...) -> str`

Generate language breakdown bar chart.

**Parameters:**
- `username` (str): GitHub username
- `languages` (List[Dict]): Language data with name, bytes, percentage

**Returns:**
- `str`: SVG content

**Dimensions:** 600×400 pixels

**Features:**
- Top 10 languages as horizontal bars
- Percentage labels
- Color-coded bars from theme
- "Other" grouping for remaining languages

**Example:**
```python
svg = visualizer.generate_languages("markhazleton", languages)
```

##### `generate_release_cadence(...) -> str`

Generate paired weekly/monthly repo diversity sparklines.

**Parameters:**
- `username` (str): GitHub username label
- `cadence` (Dict[str, Any]): Output from `calculate_release_cadence`

**Returns:**
- `str`: SVG content (900×420 pixels)

**Features:**
- Two side-by-side panels (weekly + monthly)
- Sparkline with area fill and peak indicators
- Tooltips describing repo count per period

**Example:**
```python
cadence = calculator.calculate_release_cadence()
svg = visualizer.generate_release_cadence(cadence, "markhazleton")
```

##### `generate_fun_stats(...) -> str`

Generate "Lightning Round Stats" one-liners.

**Parameters:**
- `username` (str): GitHub username
- `stats` (Dict[str, Any]): Fun statistics
  - `most_active_hour` (int)
  - `coding_pattern` (str)
  - `total_repos` (int)
  - `account_age_days` (int)

**Returns:**
- `str`: SVG content

**Dimensions:** 600×300 pixels

**Example:**
```python
fun_stats = {
    "most_active_hour": 23,
    "coding_pattern": "Night Owl",
    "total_repos": 50,
    "account_age_days": 1825
}
svg = visualizer.generate_fun_stats("markhazleton", fun_stats)
```

##### `generate_streaks(...) -> str`

Generate coding streaks visualization.

**Parameters:**
- `username` (str): GitHub username
- `current_streak` (int): Current streak in days
- `longest_streak` (int): Longest streak in days

**Returns:**
- `str`: SVG content

**Dimensions:** 600×250 pixels

**Example:**
```python
svg = visualizer.generate_streaks(
    username="markhazleton",
    current_streak=15,
    longest_streak=45
)
```

---

### `spark.fetcher.GitHubFetcher`

GitHub API client with rate limiting and caching.

#### Constructor

```python
GitHubFetcher(token: str, cache: Optional[APICache] = None)
```

**Parameters:**
- `token` (str): GitHub Personal Access Token
- `cache` (Optional[APICache]): Cache instance for API responses

**Raises:**
- `ValueError`: If token is empty or invalid

**Example:**
```python
from spark.fetcher import GitHubFetcher
from spark.cache import APICache

cache = APICache(cache_dir=".cache")
fetcher = GitHubFetcher(token=os.environ["GITHUB_TOKEN"], cache=cache)
```

#### Methods

##### `fetch_user_profile(username: str) -> Dict[str, Any]`

Fetch user profile data.

**Parameters:**
- `username` (str): GitHub username

**Returns:**
- `Dict[str, Any]`: User profile with public_repos, followers, created_at, etc.

**Caching:** 6 hours by default

**Example:**
```python
profile = fetcher.fetch_user_profile("markhazleton")
print(profile["public_repos"])
```

##### `fetch_repositories(username: str, max_count: int = 500) -> List[Dict[str, Any]]`

Fetch user repositories with pagination.

**Parameters:**
- `username` (str): GitHub username
- `max_count` (int): Maximum repositories to fetch. Defaults to 500.

**Returns:**
- `List[Dict[str, Any]]`: Repository data with name, stars, forks, watchers

**Features:**
- Automatic pagination
- Rate limiting with exponential backoff
- Excludes private repos (per privacy requirements)

**Example:**
```python
repos = fetcher.fetch_repositories("markhazleton", max_count=100)
for repo in repos[:5]:
    print(f"{repo['name']}: {repo['stars']} stars")
```

##### `fetch_commits(repo_name: str, username: str, max_count: int = 100) -> List[Dict[str, Any]]`

Fetch commits for a repository.

**Parameters:**
- `repo_name` (str): Repository name
- `username` (str): Repository owner
- `max_count` (int): Maximum commits to fetch. Defaults to 100.

**Returns:**
- `List[Dict[str, Any]]`: Commit data with sha, date, message

**Example:**
```python
commits = fetcher.fetch_commits("stats-spark", "markhazleton")
```

##### `fetch_languages(repo_name: str, username: str) -> Dict[str, int]`

Fetch language statistics for a repository.

**Parameters:**
- `repo_name` (str): Repository name
- `username` (str): Repository owner

**Returns:**
- `Dict[str, int]`: Language names to byte counts

**Example:**
```python
languages = fetcher.fetch_languages("stats-spark", "markhazleton")
print(languages)  # {"Python": 5000, "HTML": 300}
```

---

### `spark.cache.APICache`

File-based caching system for API responses.

#### Constructor

```python
APICache(cache_dir: str = ".cache", ttl_hours: int = 6)
```

**Parameters:**
- `cache_dir` (str): Directory for cache files. Defaults to `.cache`.
- `ttl_hours` (int): Time-to-live in hours. Defaults to 6.

**Example:**
```python
cache = APICache(cache_dir=".cache", ttl_hours=6)
```

#### Methods

##### `get(key: str) -> Optional[Any]`

Retrieve cached value if not expired.

**Parameters:**
- `key` (str): Cache key

**Returns:**
- `Optional[Any]`: Cached value or None if expired/missing

**Example:**
```python
data = cache.get("user:markhazleton:profile")
```

##### `set(key: str, value: Any) -> None`

Store value in cache with current timestamp.

**Parameters:**
- `key` (str): Cache key
- `value` (Any): Data to cache (must be JSON-serializable)

**Example:**
```python
cache.set("user:markhazleton:profile", profile_data)
```

##### `is_expired(key: str) -> bool`

Check if cache entry is expired.

**Parameters:**
- `key` (str): Cache key

**Returns:**
- `bool`: True if expired or doesn't exist

**Example:**
```python
if cache.is_expired("user:markhazleton:profile"):
    # Fetch fresh data
```

##### `clear() -> None`

Clear all cached data.

**Example:**
```python
cache.clear()
```

---

### `spark.themes.Theme`

Abstract base class for theme implementations.

#### Properties

All themes must implement these properties:

- `name` (str): Theme name
- `primary_color` (str): Primary color (hex)
- `accent_color` (str): Accent color (hex)
- `background_color` (str): Background color (hex)
- `text_color` (str): Text color (hex)
- `border_color` (str): Border color (hex)
- `effects` (Dict[str, bool]): Visual effects flags
  - `glow` (bool): Enable glow effects
  - `gradient` (bool): Enable gradients
  - `animations` (bool): Enable animations (not supported in GitHub)

#### Built-in Themes

##### `SparkDarkTheme`

Default dark theme with electric blue and gold accents.

```python
from spark.themes.spark_dark import SparkDarkTheme

theme = SparkDarkTheme()
print(theme.primary_color)  # "#0EA5E9" (Sky Blue)
print(theme.accent_color)   # "#FCD34D" (Gold)
```

##### `SparkLightTheme`

Light theme with WCAG AA compliant contrast ratios.

```python
from spark.themes.spark_light import SparkLightTheme

theme = SparkLightTheme()
print(theme.primary_color)  # "#0284C7" (Dark Blue)
print(theme.background_color)  # "#FFFFFF" (White)
```

##### `CustomTheme`

Load user-defined themes from `config/themes.yml`.

```python
from spark.themes.custom import CustomTheme

theme = CustomTheme("ocean")  # Load "ocean" theme from themes.yml
```

---

## Command Line Interface

### `spark generate`

Generate statistics locally.

```bash
spark generate --user USERNAME [options]
```

**Options:**
- `--user USERNAME`: GitHub username (required)
- `--output-dir DIR`: Output directory (default: `output/`)
- `--config FILE`: Config file path (default: `config/spark.yml`)
- `--force-refresh`: Bypass cache
- `--verbose`: Enable verbose logging

**Example:**
```bash
export GITHUB_TOKEN=ghp_xxxx
spark generate --user markhazleton --verbose
```

### `spark preview`

Preview theme with sample data.

```bash
spark preview --theme THEME [options]
```

**Options:**
- `--theme THEME`: Theme name (default: `spark-dark`)
- `--output-dir DIR`: Preview output directory (default: `preview/`)

**Example:**
```bash
spark preview --theme ocean
```

### `spark config`

Manage configuration.

```bash
spark config [options]
```

**Options:**
- `--validate`: Validate configuration
- `--show`: Display current configuration
- `--file FILE`: Config file path

**Example:**
```bash
spark config --validate --file config/spark.yml
```

### `spark cache`

Manage cache.

```bash
spark cache [options]
```

**Options:**
- `--clear`: Clear all cached data
- `--info`: Show cache information
- `--dir DIR`: Cache directory

**Example:**
```bash
spark cache --clear
spark cache --info --dir .cache
```

---

## Error Handling

All modules follow consistent error handling patterns:

### Common Exceptions

- `FileNotFoundError`: Configuration or cache files missing
- `ValueError`: Invalid configuration or input data
- `requests.exceptions.HTTPError`: GitHub API errors
- `RateLimitError`: GitHub API rate limit exceeded (custom exception)

### Example Error Handling

```python
from spark.config import SparkConfig
from spark.fetcher import GitHubFetcher

try:
    config = SparkConfig("config/spark.yml")
    config.validate()

    fetcher = GitHubFetcher(token=os.environ["GITHUB_TOKEN"])
    profile = fetcher.fetch_user_profile("markhazleton")

except FileNotFoundError as e:
    print(f"Configuration file not found: {e}")
except ValueError as e:
    print(f"Invalid configuration: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Type Hints

All modules use Python type hints for better IDE support:

```python
from typing import Dict, List, Any, Optional

def calculate_spark_score(self) -> Dict[str, Any]: ...
def fetch_repositories(self, username: str, max_count: int = 500) -> List[Dict[str, Any]]: ...
def get(self, key: str) -> Optional[Any]: ...
```

---

## Testing

### Unit Tests

Run unit tests with pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=spark --cov-report=html

# Run specific test file
pytest tests/unit/test_calculator.py

# Run specific test class
pytest tests/unit/test_calculator.py::TestSparkScore

# Verbose output
pytest -v
```

### Test Fixtures

Sample test data is available in `tests/fixtures/`:

- `sample_user_data.json`: Mock GitHub user profile
- `sample_config.yml`: Test configuration

---

## License

MIT License - see [LICENSE](../LICENSE) file for details.

---

## Additional Resources

- [Getting Started Guide](../guides/getting-started.md)
- [Configuration Reference](../guides/configuration.md)
- [Embedding Guide](../guides/embedding-guide.md)
- [Project README](../../README.md)
