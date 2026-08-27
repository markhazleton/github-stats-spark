# Stats Spark Documentation

Complete documentation for Stats Spark - GitHub profile statistics and analysis generator.

## Documentation Ownership

All project documentation lives in this `.documentation/` tree, consolidating user-facing guides, API reference, and framework planning artifacts.

Approved README exceptions are linked here so contributors have a single entry point:

- `frontend/README.md` for frontend contributor workflow details
- `frontend/public/README.md` for static asset metadata
- `docs/README.md` for deployed-site output metadata
- `output/README.md` for generated SVG output metadata

## 📚 Quick Navigation

### Getting Started

- **[Getting Started Guide](guides/getting-started.md)** - Complete setup instructions for GitHub Actions
- **[Quick Start: Unified Command](quickstart/QUICKSTART_UNIFIED.md)** - All-in-one command for local development
- **[Configuration Guide](guides/configuration.md)** - All configuration options and customization

### User Guides

- **[Analyze Command Guide](guides/analyze-command.md)** - AI-powered repository analysis
- **[Embedding Guide](guides/embedding-guide.md)** - How to embed SVGs in your profile
- **[Unified Pipeline Guide](guides/unified-pipeline.md)** - Schema 2.3.0 output contract and generation flow

### Reference

- **[API Reference](api/api-reference.md)** - Developer documentation for core modules
- **[Architecture Overview](architecture/README.md)** - System design and data flow
- **[Changelog](CHANGELOG.md)** - Version history and release notes
- **[Testing](guides/TESTING.md)** - Test coverage and quality metrics
- **[Fix Score Remediation Prompt](copilot/prompts/fix-score-remediation.md)** - Copilot prompt for resolving score blockers
- **[Constitution](memory/constitution.md)** - Non-negotiable project principles
- **[Feature Specs](specs/)** - Feature specifications and task plans

## 🎯 Common Tasks

### First Time Setup

1. Read [Getting Started Guide](guides/getting-started.md)
2. Fork the repository
3. Enable GitHub Actions
4. Trigger your first workflow run

### Local Development

1. Follow [Quick Start: Unified Command](quickstart/QUICKSTART_UNIFIED.md)
2. Set environment variables (`GITHUB_TOKEN`, optional `ANTHROPIC_API_KEY`)
3. Run `spark unified --user YOUR_USERNAME`

### Customization

- **Themes**: Edit `config/themes.yml` - See [Configuration Guide](guides/configuration.md)
- **Repository Limits**: Configure in `config/spark.yml`
- **Output Selection**: Use CLI flags to generate specific visualizations

### Troubleshooting

- **Workflow Issues**: Check Actions logs and [Getting Started Guide](guides/getting-started.md#troubleshooting)
- **SVG Display**: Verify URLs and clear browser cache
- **Rate Limits**: Workflow handles automatically with smart caching
- **AI Summaries**: Check `ANTHROPIC_API_KEY` is set correctly

## 📊 Dashboard Integration

The React dashboard automatically builds from your generated data:

1. Run `spark unified --user YOUR_USERNAME` to generate `data/repositories.json`
2. Dashboard automatically updates on GitHub Pages: `https://YOUR_USERNAME.github.io/github-stats-spark/`
3. Mobile-first responsive design with touch-optimized interactions and markdown-rendered repository summaries
4. Includes a dedicated Needs Attention view powered by `attention_score`, `attention_rank`, and `attention_metrics`
5. Dependency coverage and latest-version visibility come directly from enriched `tech_stack` fields
6. See [Dashboard Build Pipeline](architecture/DASHBOARD_BUILD_PIPELINE.md) for technical details

## 🔧 For Developers

### Module Documentation

See [API Reference](api/api-reference.md) for detailed documentation:

- **Core Modules**: `fetcher`, `calculator`, `visualizer`, `cache`, `config`
- **Analysis**: `ranker`, `summarizer`, `unified_report_workflow`
- **CLI**: Command-line interface and workflow orchestration

### Architecture

- [Architecture Overview](architecture/README.md) - System design and component interaction
- [Dashboard Build Pipeline](architecture/DASHBOARD_BUILD_PIPELINE.md) - Frontend build process

### Testing

See [TESTING.md](guides/TESTING.md) for:

- Running test suite with pytest
- Coverage reports (52% overall, 80%+ core modules)
- Test organization and fixtures

### Contributing

- Follow [Getting Started Guide](guides/getting-started.md) for development setup
- Run tests before submitting PRs: `pytest --cov=spark`
- Maintain or improve coverage on modified modules
- Update documentation for new features

## 🌟 Key Features

### Smart Caching

- **Change-Based**: Only updates repositories with new commits
- **Metadata Refresh**: Updates stars/forks in 2.1s when no changes
- **400x Faster**: Typical daily checks with no updates
- **Commit-Safe Visuals**: Release cadence, heatmap, streaks, and fun stats now fall back cleanly across cached commit shapes instead of rendering empty states
- See [Changelog](CHANGELOG.md) for implementation details

### AI Integration

- **Claude Haiku**: Fast, cost-effective AI summaries
- **97%+ Success Rate**: Robust with three-tier fallback
- **Optional**: Works without API key using README extraction

### Visualizations

- **6 SVG Categories**: Overview, heatmap, languages, streaks, fun stats, release cadence
- **Themes**: Dark, light, and custom with WCAG AA accessibility
- **Embed Anywhere**: Use in profile READMEs, project documentation, websites
- **Release Cadence Semantics**: Weekly and monthly diversity represent unique repositories touched per period

## 📖 Documentation Standards

All documentation in this project:

- ✅ Matches actual code behavior
- ✅ Uses current command syntax
- ✅ Includes working examples
- ✅ Updated with code changes

**No work-in-progress docs** - only production-ready guides and references.

## 🔗 External Resources

- **[Main README](../README.md)** - Project overview and quick start
- **[GitHub Repository](https://github.com/MakeBoldSolutions/github-stats-spark)** - Source code
- **[Sample Dashboard](https://makeboldsolutions.github.io/github-stats-spark/)** - Live demo
- **[Issues](https://github.com/MakeBoldSolutions/github-stats-spark/issues)** - Bug reports and feature requests

---

**Need help?** Check the relevant guide above or [open an issue](https://github.com/MakeBoldSolutions/github-stats-spark/issues).
