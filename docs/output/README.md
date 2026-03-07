# Generated SVG Output

This directory contains the automatically generated SVG statistics visualizations.

## SVG Categories

- **overview.svg**: Comprehensive dashboard with Spark Score, commits, languages, and time patterns
- **heatmap.svg**: Commit frequency calendar visualization
- **languages.svg**: Programming language usage breakdown
- **release.svg**: Weekly/monthly release cadence sparklines
- **fun.svg**: Lightning Round Stats - fun facts and one-liners
- **streaks.svg**: Current and longest coding streaks

## Usage in Profile README

Embed these SVGs in your GitHub profile README using markdown:

```markdown
![GitHub Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Regeneration

SVGs are automatically regenerated daily at midnight UTC via GitHub Actions. You can also manually trigger the workflow from the Actions tab.

## Local Generation

To generate SVGs locally for testing:

```bash
python -m spark.cli generate --user YOUR_USERNAME
```

See `docs/embedding-guide.md` for detailed instructions and examples.
