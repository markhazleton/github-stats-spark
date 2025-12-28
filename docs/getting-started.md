# Getting Started with Stats Spark

Welcome to Stats Spark! This guide will help you set up automated GitHub statistics generation for your profile.

## Prerequisites

Before you begin, ensure you have:

- A GitHub account
- A repository for your GitHub profile (username/username)
- Basic familiarity with GitHub Actions

## Quick Start (5 Minutes)

### Step 1: Fork the Repository

1. Visit the Stats Spark repository: `https://github.com/markhazleton/github-stats-spark`
2. Click the "Fork" button in the top right
3. Select your account as the destination

### Step 2: Enable GitHub Actions

1. Go to your forked repository
2. Navigate to **Settings** → **Actions** → **General**
3. Ensure "Allow all actions and reusable workflows" is selected
4. Click **Save**

### Step 3: Configure Your Username

The system will auto-detect your username from the repository, but you can customize it:

1. Edit `config/spark.yml` in your fork
2. Set `user: your-github-username` (or leave as `auto`)
3. Commit the change

### Step 4: Trigger the Workflow

#### Option A: Wait for Automatic Run
- The workflow runs automatically at midnight UTC daily
- Check back tomorrow to see your stats!

#### Option B: Manual Trigger (Recommended for First Run)
1. Go to **Actions** tab in your repository
2. Select "Generate GitHub Statistics" workflow
3. Click "Run workflow" → "Run workflow"
4. Wait 2-5 minutes for completion

### Step 5: Verify Generation

1. Check the **Actions** tab for workflow status
2. Once complete, navigate to `output/` directory
3. You should see 5 SVG files:
   - `overview.svg` - Comprehensive dashboard
   - `heatmap.svg` - Commit activity calendar
   - `languages.svg` - Programming language breakdown
   - `release.svg` - Release cadence sparklines (weekly/monthly repo diversity)
   - `fun.svg` - Fun facts and stats
   - `streaks.svg` - Coding streaks

### Step 6: Embed in Your Profile

Add these lines to your profile README (`username/username/README.md`):

```markdown
## GitHub Statistics

![GitHub Stats Overview](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/overview.svg)

![Language Breakdown](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/languages.svg)

![Coding Streaks](https://raw.githubusercontent.com/YOUR_USERNAME/github-stats-spark/main/output/streaks.svg)
```

**Important**: Replace `YOUR_USERNAME` with your actual GitHub username!

## Troubleshooting

### Workflow Fails with "Authentication Failed"

The `GITHUB_TOKEN` is automatically provided by GitHub Actions. If you see authentication errors:
- Check that GitHub Actions is enabled in your repository settings
- Ensure you haven't modified the workflow file to remove the token

### No SVGs Generated

1. Check workflow logs in the Actions tab for errors
2. Verify you have public repositories with commits
3. Ensure `config/spark.yml` is valid YAML

### SVGs Don't Display in Profile README

1. Verify the URLs use your correct username
2. Check that the workflow has committed SVGs to the `output/` directory
3. Ensure your profile repository is public
4. Try hard-refreshing your browser (Ctrl+F5 / Cmd+Shift+R)

### Rate Limiting Issues

If you have many repositories (>100):
- The workflow automatically handles rate limiting with retries
- You may need to wait a few minutes between runs
- Check the workflow logs for "Rate limit exceeded" messages

## Next Steps

- **Customize Themes**: See [Configuration Guide](configuration.md)
- **Selective Statistics**: Enable/disable specific SVG categories
- **Local Testing**: Use the CLI to preview changes before deploying

## Support

- **Issues**: Report bugs at [GitHub Issues](https://github.com/markhazleton/github-stats-spark/issues)
- **Documentation**: Full docs at [docs/](.)
- **Examples**: See [assets/examples/markhazleton/](../assets/examples/markhazleton/)

---

**Ready to shine?** ⚡ Let Stats Spark illuminate your GitHub activity!
