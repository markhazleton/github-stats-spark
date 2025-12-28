# Configuration Guide

Stats Spark is highly customizable through YAML configuration files. This guide covers all available options.

## Configuration Files

- **`config/spark.yml`**: Main configuration file
- **`config/themes.yml`**: Custom theme definitions

## Main Configuration (`spark.yml`)

### User Settings

```yaml
# GitHub username to analyze
# Use "auto" to detect from GITHUB_REPOSITORY environment variable
user: auto
```

**Options**:
- `auto`: Auto-detect from repository name (recommended for GitHub Actions)
- `your-username`: Specific GitHub username

### Statistics Configuration

```yaml
stats:
  # Enabled statistics categories
  enabled:
    - overview    # Comprehensive dashboard with Spark Score
    - heatmap     # Commit frequency calendar
    - languages   # Programming language breakdown
    - fun         # Lightning Round Stats
    - streaks     # Coding and learning streaks

  # Thresholds for categorization
  thresholds:
    graveyard_months: 6        # Months of inactivity → inactive
    starter_commits: 50        # Commits threshold for "starter"
    power_user_commits: 1000   # Commits threshold for "power user"
    night_owl_hours: [22, 23, 0, 1, 2, 3, 4]
    early_bird_hours: [5, 6, 7, 8, 9]
```

**Available Categories**:
- `overview`: Main dashboard with Spark Score, commits, languages, time pattern
- `heatmap`: GitHub-style contribution heatmap
- `languages`: Bar chart of programming languages
- `fun`: Fun facts and one-liners
- `streaks`: Current and longest coding streaks

**Tip**: Disable categories you don't want by removing them from the `enabled` list.

### Visualization Configuration

```yaml
visualization:
  # Theme selection
  theme: spark-dark  # Options: spark-dark, spark-light, custom theme name

  # Visual style
  style: electric    # Options: electric, minimal, detailed

  # Visual effects
  effects:
    glow: true       # Enable glow effects
    animations: false # Animations (not supported in GitHub READMEs)
    gradient: true   # Gradient fills
```

**Built-in Themes**:
- `spark-dark`: Dark theme with electric blue primary and gold accents (default)
- `spark-light`: Light theme with WCAG AA compliant colors

**Custom Themes**: Define in `config/themes.yml` (see below)

### Branding Configuration

```yaml
branding:
  show_logo: true             # Show Stats Spark logo
  show_powered_by: true       # Show "Powered by Stats Spark" footer
  custom_footer: ""           # Custom footer text (optional)
```

### Cache Configuration

```yaml
cache:
  enabled: true               # Enable API response caching
  ttl_hours: 6                # Cache time-to-live (hours)
  directory: .cache           # Cache directory
```

**Note**: Caching significantly reduces GitHub API calls. Keep enabled unless debugging.

### Repository Limits

```yaml
repositories:
  max_count: 500              # Maximum repositories to process
  exclude_private: true       # Exclude private repos (required)
  exclude_forks: false        # Exclude forked repositories
```

**Important**: `exclude_private: true` is required per project constitution. Private repositories are never included in statistics.

## Custom Themes (`themes.yml`)

Define your own color schemes:

```yaml
custom_themes:
  # Ocean theme example
  ocean:
    colors:
      primary: "#06B6D4"      # Cyan
      accent: "#8B5CF6"       # Purple
      background: "#0C4A6E"   # Deep blue
      text: "#E0F2FE"         # Light cyan
      border: "#075985"       # Medium blue

    effects:
      glow: true
      gradient: true
      animations: false
```

### Theme Color Properties

- **primary**: Main elements (bars, graphs, headers)
- **accent**: Highlights, special elements, Spark Score
- **background**: SVG background color
- **text**: All text elements
- **border**: Borders, dividers, grid lines

### WCAG AA Compliance

Ensure your custom themes meet WCAG AA contrast ratio (4.5:1 minimum) between text and background:

**Good Examples**:
- Dark background `#0D1117` + Light text `#C9D1D9` ✅
- Light background `#FFFFFF` + Dark text `#1F2937` ✅

**Bad Examples**:
- Light background `#FFFFFF` + Light text `#D1D5DB` ❌
- Dark background `#000000` + Dark text `#333333` ❌

### Using Custom Themes

1. Define theme in `config/themes.yml`
2. Set `visualization.theme` in `spark.yml` to your theme name
3. Run generation to apply

Example:
```yaml
# In spark.yml
visualization:
  theme: ocean  # Use the ocean theme from themes.yml
```

## Environment Variables

Stats Spark reads these environment variables:

- **`GITHUB_TOKEN`**: GitHub Personal Access Token (required)
- **`GITHUB_REPOSITORY`**: Repository name for auto-detection (auto-provided by Actions)

## Example Configurations

### Minimal Configuration (Only Overview)

```yaml
user: auto
stats:
  enabled:
    - overview
visualization:
  theme: spark-dark
```

### Maximum Configuration (All Features)

```yaml
user: markhazleton
stats:
  enabled:
    - overview
    - heatmap
    - languages
    - fun
    - streaks
  thresholds:
    graveyard_months: 3
    starter_commits: 100
    power_user_commits: 2000
visualization:
  theme: spark-dark
  effects:
    glow: true
    gradient: true
cache:
  enabled: true
  ttl_hours: 12
repositories:
  max_count: 1000
  exclude_forks: true
```

### Performance-Optimized Configuration

```yaml
user: auto
stats:
  enabled:
    - overview
    - languages
visualization:
  theme: spark-dark
  effects:
    glow: false  # Disable for simpler SVGs
cache:
  enabled: true
  ttl_hours: 24  # Cache longer
repositories:
  max_count: 100  # Process fewer repos
  exclude_forks: true
```

## Validation

Validate your configuration before deploying:

```bash
# Using CLI
spark config --validate --file config/spark.yml

# Using Python
python -c "from spark.config import SparkConfig; c = SparkConfig(); c.load(); print(c.validate())"
```

## Tips

1. **Start Simple**: Begin with default configuration and customize gradually
2. **Test Locally**: Use `spark preview --theme your-theme` to preview changes
3. **Performance**: Reduce `max_count` if workflow takes too long
4. **Caching**: Increase `ttl_hours` if your activity doesn't change frequently
5. **Selective Output**: Disable unused categories to speed up generation

## Next Steps

- [Getting Started Guide](getting-started.md)
- [Embedding Guide](embedding-guide.md)
- [Theme Examples](../config/themes.yml)
