"""Main entry point for Stats Spark GitHub Actions workflow."""

import os
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

from spark.config import SparkConfig
from spark.fetcher import GitHubFetcher
from spark.cache import APICache
from spark.logger import get_logger
from spark.calculator import StatsCalculator
from spark.visualizer import StatisticsVisualizer, get_theme


def main():
    """Main execution function for automated statistics generation.

    Supports two modes:
    - Default: Generate SVG statistics (original workflow)
    - SPARK_COMMAND=analyze: Generate repository analysis report (new workflow)
    """
    logger = get_logger("spark-main", verbose=True)

    # T097: Support analyze command for GitHub Actions
    command = os.getenv("SPARK_COMMAND", "generate").lower()

    if command == "analyze":
        # Delegate to analyze workflow
        from spark.cli import handle_analyze
        from argparse import Namespace

        # Create args namespace from environment variables
        args = Namespace(
            user=os.getenv("SPARK_USER") or None,
            output=os.getenv("SPARK_OUTPUT", "output/reports"),
            top_n=int(os.getenv("SPARK_TOP_N", "50")),
            list_only=os.getenv("SPARK_LIST_ONLY", "").lower() == "true",
            config=os.getenv("SPARK_CONFIG", "config/spark.yml"),
            verbose=os.getenv("SPARK_VERBOSE", "").lower() == "true",
        )

        # Auto-detect user from GITHUB_REPOSITORY if not provided
        if not args.user:
            repo = os.getenv("GITHUB_REPOSITORY", "")
            if "/" in repo:
                args.user = repo.split("/")[0]

        if not args.user:
            logger.error("Could not determine username. Set SPARK_USER environment variable")
            sys.exit(1)

        logger.info(f"Running analyze command for user: {args.user}")
        handle_analyze(args, logger)
        return

    try:
        logger.info("Stats Spark - GitHub Statistics Generator")
        logger.info("=" * 50)

        # Load configuration
        logger.info("Loading configuration...")
        config = SparkConfig("config/spark.yml")
        config.load()

        # Validate configuration
        errors = config.validate()
        if errors:
            logger.error("Configuration validation failed:")
            for error in errors:
                logger.error(f"  - {error}")
            sys.exit(1)

        logger.info("Configuration loaded successfully")

        # Get username (auto-detect or from config)
        username = config.get_user()
        if not username or username == "auto":
            logger.error("Could not determine username. Set 'user' in spark.yml or GITHUB_REPOSITORY environment variable")
            sys.exit(1)

        logger.info(f"Generating statistics for user: {username}")

        # Check for GitHub token
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            logger.error("GITHUB_TOKEN environment variable not set")
            sys.exit(1)

        # Initialize cache
        cache_config = config.get("cache", {})
        cache_enabled = cache_config.get("enabled", True)
        cache_ttl = cache_config.get("ttl_hours", 6)
        cache_dir = cache_config.get("directory", ".cache")

        cache = APICache(cache_dir=cache_dir, ttl_hours=cache_ttl) if cache_enabled else None
        logger.info(f"Cache: {'enabled' if cache_enabled else 'disabled'} (TTL: {cache_ttl}h)")

        # Initialize GitHub fetcher
        repo_config = config.get("repositories", {})
        max_repos = repo_config.get("max_count", 500)

        logger.info("Initializing GitHub API client...")
        fetcher = GitHubFetcher(token=github_token, cache=cache, max_repos=max_repos)

        # Check rate limit status
        rate_limit = fetcher.get_rate_limit_status()
        logger.info(f"GitHub API Rate Limit: {rate_limit['remaining']}/{rate_limit['limit']} remaining")

        # Fetch user profile
        logger.info("Fetching user profile...")
        try:
            profile = fetcher.fetch_user_profile(username)
            logger.info(f"User: {profile['name']} ({profile['username']})")
            logger.info(f"Public repositories: {profile['public_repos']}")
        except Exception as e:
            logger.error("Failed to fetch user profile", e)
            sys.exit(1)

        # Fetch repositories
        logger.info("Fetching repositories...")
        exclude_private = repo_config.get("exclude_private", True)
        exclude_forks = repo_config.get("exclude_forks", False)

        try:
            repositories = fetcher.fetch_repositories(
                username,
                exclude_private=exclude_private,
                exclude_forks=exclude_forks,
            )
            logger.info(f"Fetched {len(repositories)} repositories")
        except Exception as e:
            logger.error("Failed to fetch repositories", e)
            sys.exit(1)

        # Initialize statistics calculator
        logger.info("Initializing statistics calculator...")
        calculator = StatsCalculator(profile, repositories)

        # Fetch commits and languages for each repository
        logger.info("Fetching commits and languages for repositories...")
        all_commits = []
        commits_by_date = defaultdict(int)

        for i, repo in enumerate(repositories):
            repo_name = repo["name"]

            # Progress indicator
            if (i + 1) % 10 == 0:
                logger.info(f"Processing repository {i + 1}/{len(repositories)}: {repo_name}")

            try:
                # Fetch commits for this repository
                commits = fetcher.fetch_commits(username, repo_name, max_commits=200)
                all_commits.extend(commits)

                # Count commits by date for heatmap
                for commit in commits:
                    if commit.get("date"):
                        date = datetime.fromisoformat(commit["date"].replace("Z", "+00:00"))
                        date_key = date.strftime("%Y-%m-%d")
                        commits_by_date[date_key] += 1

                # Add commits to calculator
                calculator.add_commits(commits)

                # Fetch languages for this repository
                languages = fetcher.fetch_languages(username, repo_name)
                calculator.add_languages(languages)

            except Exception as e:
                logger.debug(f"Skipping repository {repo_name}: {e}")
                continue

        logger.info(f"Fetched {len(all_commits)} total commits across {len(repositories)} repositories")

        # Handle edge case: no commits
        if len(all_commits) == 0:
            logger.warn("No commits found for user. Generating minimal statistics.")

        # Calculate statistics
        logger.info("Calculating statistics...")

        spark_score = calculator.calculate_spark_score()
        logger.info(f"Spark Score: {spark_score['total_score']}/100 (⚡ {spark_score['lightning_rating']} bolts)")

        time_patterns = calculator.analyze_time_patterns()
        logger.info(f"Time Pattern: {time_patterns['category']}")

        languages = calculator.aggregate_languages()
        if languages:
            top_lang = languages[0]
            logger.info(f"Top Language: {top_lang['name']} ({top_lang['percentage']}%)")

        streaks = calculator.calculate_streaks()
        logger.info(f"Current Streak: {streaks['current_streak']} days, Longest: {streaks['longest_streak']} days")

        release_cadence = calculator.calculate_release_cadence()
        logger.info(
            "Weekly repo diversity peak: %s repos"
            % release_cadence.get("max_weekly", 0)
        )

        # Get enabled statistics categories
        enabled_stats = config.get_enabled_stats()
        logger.info(f"Enabled statistics: {', '.join(enabled_stats)}")

        # Initialize visualizer with theme
        theme_name = config.get_theme()
        logger.info(f"Using theme: {theme_name}")

        theme = get_theme(theme_name, config.themes_config)
        enable_effects = config.get("visualization.effects.glow", True)
        visualizer = StatisticsVisualizer(theme, enable_effects)

        # Prepare output directory
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        # Generate SVG visualizations
        logger.info("Generating SVG visualizations...")

        # Overview
        if "overview" in enabled_stats:
            logger.info("Generating overview.svg...")
            overview_svg = visualizer.generate_overview(
                username=username,
                spark_score=spark_score,
                total_commits=len(all_commits),
                languages=languages[:5],  # Top 5 languages
                time_pattern=time_patterns,
            )

            overview_path = output_dir / "overview.svg"
            with open(overview_path, "w", encoding="utf-8") as f:
                f.write(overview_svg)
            logger.info(f"Created: {overview_path}")

        # Heatmap
        if "heatmap" in enabled_stats:
            logger.info("Generating heatmap.svg...")
            heatmap_svg = visualizer.generate_heatmap(
                commits_by_date=commits_by_date,
                username=username,
            )

            heatmap_path = output_dir / "heatmap.svg"
            with open(heatmap_path, "w", encoding="utf-8") as f:
                f.write(heatmap_svg)
            logger.info(f"Created: {heatmap_path}")

        # Languages
        if "languages" in enabled_stats:
            logger.info("Generating languages.svg...")
            languages_svg = visualizer.generate_languages(
                languages=languages,
                username=username,
            )

            languages_path = output_dir / "languages.svg"
            with open(languages_path, "w", encoding="utf-8") as f:
                f.write(languages_svg)
            logger.info(f"Created: {languages_path}")

        # Fun Stats
        if "fun" in enabled_stats:
            logger.info("Generating fun.svg...")

            # Prepare fun stats
            account_age_days = 0
            if profile.get("created_at"):
                created_at = datetime.fromisoformat(profile["created_at"].replace("Z", "+00:00"))
                account_age_days = (datetime.now(created_at.tzinfo) - created_at).days

            # Calculate total stars across all repositories
            total_stars = sum(repo.get("stars", 0) for repo in repositories)

            # Calculate average commits per day
            avg_commits_per_day = 0
            if account_age_days > 0:
                avg_commits_per_day = len(all_commits) / account_age_days

            fun_stats = {
                "most_active_hour": time_patterns.get("most_active_hour", "Unknown"),
                "pattern": time_patterns.get("category", "Unknown"),
                "total_repos": len(repositories),
                "account_age_days": account_age_days,
                "total_commits": len(all_commits),
                "languages_count": len(languages),
                "total_stars": total_stars,
                "avg_commits_per_day": avg_commits_per_day,
            }

            fun_svg = visualizer.generate_fun_stats(
                stats=fun_stats,
                username=username,
            )

            fun_path = output_dir / "fun.svg"
            with open(fun_path, "w", encoding="utf-8") as f:
                f.write(fun_svg)
            logger.info(f"Created: {fun_path}")

        # Streaks
        if "streaks" in enabled_stats:
            logger.info("Generating streaks.svg...")
            streaks_svg = visualizer.generate_streaks(
                streaks=streaks,
                username=username,
            )

            streaks_path = output_dir / "streaks.svg"
            with open(streaks_path, "w", encoding="utf-8") as f:
                f.write(streaks_svg)
            logger.info(f"Created: {streaks_path}")

        # Release cadence sparklines
        if "release" in enabled_stats:
            logger.info("Generating release.svg...")
            release_svg = visualizer.generate_release_cadence(
                cadence=release_cadence,
                username=username,
            )

            release_path = output_dir / "release.svg"
            with open(release_path, "w", encoding="utf-8") as f:
                f.write(release_svg)
            logger.info(f"Created: {release_path}")

        # Final rate limit check
        final_rate_limit = fetcher.get_rate_limit_status()
        logger.info(f"Final API Rate Limit: {final_rate_limit['remaining']}/{final_rate_limit['limit']} remaining")
        logger.info(f"API calls used: {final_rate_limit['used']}")

        logger.info("=" * 50)
        logger.info("Stats Spark execution complete successfully!")
        logger.info(f"Generated {len(enabled_stats)} SVG visualizations in {output_dir}")

    except Exception as e:
        logger.error("Fatal error during execution", e)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
