# Stats Spark ⚡

> Automated GitHub profile statistics generator with beautiful SVG visualizations

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

Stats Spark automatically analyzes your GitHub activity and generates stunning SVG visualizations that you can embed in your profile README. Get insights into your coding patterns, track your streaks, and showcase your Spark Score!

## ✨ Features

- **⚡ Spark Score**: Unique 0-100 metric combining consistency, volume, and collaboration
- **📊 Comprehensive Statistics**: Commits, languages, time patterns, and more
- **🎨 Beautiful Themes**: Dark, light, and custom themes with WCAG AA compliance
- **🤖 Fully Automated**: Runs daily via GitHub Actions at midnight UTC
- **🎯 Selective Output**: Choose which statistics to generate
- **🖥️ Local CLI**: Preview and test locally before deploying
- **♿ Accessible**: WCAG AA contrast compliance for all themes
- **🚀 Fast**: <5 minutes for 500 repositories with intelligent caching

## 🚀 Quick Start

### 1. Fork This Repository

Click the "Fork" button in the top right to create your own copy.

### 2. Enable GitHub Actions

1. Go to **Settings** → **Actions** → **General**
2. Select "Allow all actions and reusable workflows"
3. Click **Save**

### 3. Run the Workflow

1. Navigate to **Actions** tab
2. Select "Generate GitHub Statistics"
3. Click "Run workflow" → "Run workflow"
4. Wait 2-5 minutes for completion

### 4. Embed in Your Profile

Add to your profile README (`username/username/README.md`):

```markdown
![GitHub Stats](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)
```

**Replace `YOUR_USERNAME`** with your GitHub username!

Full instructions: [Getting Started Guide](docs/getting-started.md)

## 📊 Statistics Categories

Stats Spark generates 5 SVG categories:

| Category | Description | File |
|----------|-------------|------|
| **Overview** | Spark Score, commits, languages, time pattern | `overview.svg` |
| **Heatmap** | Commit frequency calendar | `heatmap.svg` |
| **Languages** | Programming language breakdown | `languages.svg` |
| **Fun Stats** ⚡ **ENHANCED** | 8 personality-driven achievements with emoji flair | `fun.svg` |
| **Streaks** | Current and longest coding streaks | `streaks.svg` |

### ⚡ Enhanced Fun Stats (New!)

The Fun Stats visualization now showcases **8 creative measurements** with personality:

- 🦉 **Coding Time Personality** - Night Owl, Early Bird, or Daytime Coder
- 🚀 **Commit Velocity** - From "Quality over Quantity" to "Commit Machine"
- 📚 **Repository Collection** - Achievement tiers from Focused to Collector
- 🌐 **Language Diversity** - Specialist to Polyglot Programmer
- ⭐ **Community Recognition** - Stars earned across all repositories
- 🏛️ **Account Longevity** - Experience badges from newcomer to veteran
- 💥 **Commit Milestones** - Total commits with achievement levels
- 🌙 **Pattern Personality** - Custom messages based on your coding style

## ⚡ Spark Score

The Spark Score is a 0-100 metric reflecting your GitHub activity:

**Formula**: `40% Consistency + 35% Volume + 25% Collaboration`

**Lightning Rating**: 1-5 bolts based on your score
- ⚡⚡⚡⚡⚡ (80-100): Exceptional
- ⚡⚡⚡⚡ (60-79): Strong
- ⚡⚡⚡ (40-59): Good
- ⚡⚡ (20-39): Growing
- ⚡ (0-19): Starting

## 🎨 Themes

- **spark-dark** (default): Dark theme with electric blue and gold
- **spark-light**: Light theme with WCAG AA colors
- **custom**: Define your own in `config/themes.yml`

See [Configuration Guide](docs/configuration.md) for theme customization.

## 💻 Local CLI

```bash
# Generate statistics
export GITHUB_TOKEN=your_token
spark generate --user YOUR_USERNAME

# Preview a theme
spark preview --theme spark-dark

# Validate config
spark config --validate
```

## 📚 Documentation

- [Getting Started Guide](docs/getting-started.md) - Complete setup instructions
- [Configuration Guide](docs/configuration.md) - All configuration options
- [Embedding Guide](docs/embedding-guide.md) - How to embed SVGs in README
- [API Reference](docs/api-reference.md) - Developer documentation for core modules

## 🔧 Troubleshooting

**Workflow fails?** Check Actions logs and verify GitHub Actions is enabled.

**SVGs don't display?** Verify URLs use correct username and files exist in `output/`.

**Rate limiting?** Workflow automatically handles with caching and retries.

See [Getting Started Guide](docs/getting-started.md) for more help.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue with details and reproduction steps
2. **Suggest Features**: Share ideas for new visualizations or improvements
3. **Submit Pull Requests**: Fix bugs or add features
4. **Improve Documentation**: Help make guides clearer
5. **Share Examples**: Show how you're using Stats Spark!

Please see [API Reference](docs/api-reference.md) for developer documentation.

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=spark --cov-report=html

# View coverage report
start htmlcov/index.html
```

Current test coverage: **52%** (core modules: 80%+)

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

## 🙏 Acknowledgments

- Built with [PyGithub](https://github.com/PyGithub/PyGithub)
- SVG generation with [svgwrite](https://github.com/mozman/svgwrite)

---

<div align="center">

**⚡ Powered by Stats Spark**

Illuminate your GitHub activity with beautiful statistics

[Get Started](docs/getting-started.md) • [Documentation](docs/) • [Report Issue](https://github.com/markhazleton/github-stats-spark/issues)

</div>
