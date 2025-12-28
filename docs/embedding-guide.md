# Embedding Guide

This guide shows you how to embed Stats Spark visualizations in your GitHub profile README and other markdown files.

## Basic Embedding

### Profile README

Add statistics to your GitHub profile README (`username/username/README.md`):

```markdown
## My GitHub Statistics

![GitHub Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)
```

**Replace `YOUR_USERNAME`** with your actual GitHub username!

## All Statistics Categories

### Overview Dashboard

Comprehensive view with Spark Score, commits, languages, and time pattern:

```markdown
![GitHub Stats Overview](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)
```

### Commit Heatmap

GitHub-style contribution calendar:

```markdown
![Commit Activity](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/heatmap.svg)
```

### Language Breakdown

Programming languages used:

```markdown
![Top Languages](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/languages.svg)
```

### Release Cadence

Weekly and monthly repo diversity sparklines:

```markdown
![Release Cadence](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/release.svg)
```

### Fun Stats

Lightning round facts and one-liners:

```markdown
![Fun Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/fun.svg)
```

### Coding Streaks

Current and longest streaks:

```markdown
![Coding Streaks](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/streaks.svg)
```

## Layout Examples

### Side-by-Side Layout

Display two statistics side-by-side:

```markdown
<div align="center">
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg" width="49%" />
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/languages.svg" width="49%" />
</div>
```

### Stacked Layout

All statistics in a vertical stack:

```markdown
## GitHub Statistics

![Overview](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)

![Languages](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/languages.svg)

![Streaks](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/streaks.svg)
```

### Grid Layout

2x2 grid of statistics:

```markdown
<div align="center">
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg" width="49%" />
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/heatmap.svg" width="49%" />
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/languages.svg" width="49%" />
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/streaks.svg" width="49%" />
</div>
```

## Advanced Embedding

### Custom Sizes

Resize SVGs using HTML:

```markdown
<img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg" width="600" />
```

### Links

Make SVGs clickable:

```markdown
[![GitHub Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)](https://github.com/YOUR_USERNAME/github-stats-spark)
```

### Centered Layout

Center statistics on the page:

```markdown
<div align="center">
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg" />
</div>
```

### With Headers

Add section headers:

```markdown
## ⚡ GitHub Statistics

![Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)

## 📊 Language Breakdown

![Languages](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/languages.svg)

## 🔥 Coding Streaks

![Streaks](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/streaks.svg)
```

## Real Example: markhazleton

Here's how [markhazleton](https://github.com/markhazleton) embeds Stats Spark:

```markdown
## My GitHub Activity

<div align="center">
  <img src="https://raw.githubusercontent.com/markhazleton/github-stats-spark/main/output/overview.svg" width="800" />
</div>

### Language Breakdown & Streaks

<div align="center">
  <img src="https://raw.githubusercontent.com/markhazleton/github-stats-spark/main/output/languages.svg" width="45%" />
  <img src="https://raw.githubusercontent.com/markhazleton/github-stats-spark/main/output/streaks.svg" width="45%" />
</div>
```

## Troubleshooting

### SVGs Not Displaying

1. **Check URL**: Ensure `YOUR_USERNAME` is replaced with your actual username
2. **Branch Name**: Verify branch is `main` (not `master`)
3. **File Path**: Confirm SVGs exist in `output/` directory
4. **Public Repository**: Profile repository must be public
5. **Cache**: Try hard refresh (Ctrl+F5 / Cmd+Shift+R)

### SVGs Look Blurry

GitHub may cache old versions:
1. Add a cache-busting parameter: `?v=2`
2. Wait 5-10 minutes for GitHub's cache to update
3. Clear your browser cache

### SVGs Don't Update

The workflow runs daily at midnight UTC:
1. Manually trigger from Actions tab for immediate update
2. Check workflow logs for errors
3. Verify the workflow committed new SVGs

### Wrong Theme

1. Check `config/spark.yml` for `theme:` setting
2. Re-run workflow after changing theme
3. Verify custom themes are defined in `config/themes.yml`

## Best Practices

1. **Use Raw URLs**: Always use `raw.githubusercontent.com` URLs
2. **Responsive Sizing**: Use percentage widths for responsive layouts
3. **Minimize Count**: Don't embed all 5 categories - choose 2-3 most relevant
4. **Update Frequency**: Daily updates are sufficient for most users
5. **Theme Consistency**: Match theme to your profile README style

## Markdown Templates

### Minimal Profile

```markdown
# Hi, I'm [Your Name] 👋

![GitHub Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)

## About Me
[Your bio here]
```

### Comprehensive Profile

```markdown
# Hi, I'm [Your Name] 👋

## 🚀 About Me
[Your bio]

## ⚡ GitHub Statistics

<div align="center">
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg" width="800" />
</div>

## 📊 Activity Details

<div align="center">
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/languages.svg" width="48%" />
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/streaks.svg" width="48%" />
</div>

## 📫 How to Reach Me
[Contact info]
```

## Next Steps

- [Configuration Guide](configuration.md) - Customize themes and settings
- [Getting Started](getting-started.md) - Initial setup
- [Example Outputs](../assets/examples/markhazleton/) - See real examples

---

**Questions?** Open an [issue](https://github.com/markhazleton/github-stats-spark/issues) or check the [docs](.).
