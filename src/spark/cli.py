"""Command-line interface for Stats Spark local usage."""

import argparse
import os
import sys
from pathlib import Path

from spark.config import SparkConfig
from spark.logger import get_logger


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Stats Spark - GitHub Profile Statistics Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Generate statistics for a user:
    spark generate --user markhazleton

  Preview a theme:
    spark preview --theme spark-dark

  Validate configuration:
    spark config --validate

  Clear cache:
    spark cache --clear

For more information, visit: https://github.com/markhazleton/github-stats-spark
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Analyze command (NEW - Repository analysis)
    analyze_parser = subparsers.add_parser("analyze", help="Analyze repositories and generate report")
    analyze_parser.add_argument(
        "--user",
        type=str,
        required=True,
        help="GitHub username to analyze",
    )
    analyze_parser.add_argument(
        "--output",
        type=str,
        default="output/reports",
        help="Output directory for reports (default: output/reports)",
    )
    analyze_parser.add_argument(
        "--top-n",
        type=int,
        default=50,
        help="Number of top repositories to include (default: 50)",
    )
    analyze_parser.add_argument(
        "--list-only",
        action="store_true",
        help="List top repositories without generating full report (dry-run)",
    )
    analyze_parser.add_argument(
        "--config",
        type=str,
        default="config/spark.yml",
        help="Configuration file path (default: config/spark.yml)",
    )
    analyze_parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate statistics")
    generate_parser.add_argument(
        "--user",
        type=str,
        required=True,
        help="GitHub username to analyze",
    )
    generate_parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Output directory for SVGs (default: output)",
    )
    generate_parser.add_argument(
        "--config",
        type=str,
        default="config/spark.yml",
        help="Configuration file path (default: config/spark.yml)",
    )
    generate_parser.add_argument(
        "--force-refresh",
        action="store_true",
        help="Bypass cache and fetch fresh data",
    )
    generate_parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    # Preview command
    preview_parser = subparsers.add_parser("preview", help="Preview a theme with sample data")
    preview_parser.add_argument(
        "--theme",
        type=str,
        default="spark-dark",
        help="Theme to preview (default: spark-dark)",
    )
    preview_parser.add_argument(
        "--output-dir",
        type=str,
        default="preview",
        help="Output directory for preview SVGs (default: preview)",
    )

    # Config command
    config_parser = subparsers.add_parser("config", help="Manage configuration")
    config_parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate configuration file",
    )
    config_parser.add_argument(
        "--show",
        action="store_true",
        help="Show current configuration",
    )
    config_parser.add_argument(
        "--file",
        type=str,
        default="config/spark.yml",
        help="Configuration file path (default: config/spark.yml)",
    )

    # Cache command
    cache_parser = subparsers.add_parser("cache", help="Manage API cache")
    cache_parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear all cached data",
    )
    cache_parser.add_argument(
        "--info",
        action="store_true",
        help="Show cache information",
    )
    cache_parser.add_argument(
        "--dir",
        type=str,
        default=".cache",
        help="Cache directory (default: .cache)",
    )

    args = parser.parse_args()

    # Show help if no command provided
    if not args.command:
        parser.print_help()
        sys.exit(0)

    logger = get_logger("spark-cli", verbose=getattr(args, "verbose", False))

    # Execute commands
    if args.command == "analyze":
        handle_analyze(args, logger)
    elif args.command == "generate":
        handle_generate(args, logger)
    elif args.command == "preview":
        handle_preview(args, logger)
    elif args.command == "config":
        handle_config(args, logger)
    elif args.command == "cache":
        handle_cache(args, logger)


def handle_analyze(args, logger):
    """Handle analyze command - Generate repository analysis report."""
    logger.info("Stats Spark - Analyze Command")
    logger.info(f"User: {args.user}")
    logger.info(f"Top N: {args.top_n}")

    # Check for GitHub token
    if not os.getenv("GITHUB_TOKEN"):
        logger.error("GITHUB_TOKEN environment variable not set")
        logger.info("Please set your GitHub Personal Access Token:")
        logger.info("  export GITHUB_TOKEN=your_token_here")
        sys.exit(1)

    try:
        from datetime import datetime
        from pathlib import Path
        from spark.config import SparkConfig
        from spark.fetcher import GitHubFetcher
        from spark.cache import APICache
        from spark.ranker import RepositoryRanker
        from spark.summarizer import RepositorySummarizer, UserProfileGenerator
        from spark.report_generator import ReportGenerator
        from spark.models.repository import Repository
        from spark.models.commit import CommitHistory
        from spark.models.report import Report, RepositoryAnalysis
        from spark.dependencies import RepositoryDependencyAnalyzer

        # Load config
        config = SparkConfig(args.config)
        config.load()

        # Initialize components
        cache = APICache()
        fetcher = GitHubFetcher(cache=cache)
        ranker = RepositoryRanker(config=config.config.get("analyzer", {}).get("ranking_weights"))
        summarizer = RepositorySummarizer(cache=cache)  # Pass cache to save tokens!
        profile_generator = UserProfileGenerator(summarizer)
        report_generator = ReportGenerator()
        dependency_analyzer = RepositoryDependencyAnalyzer(cache=cache, config=config.config.get("analyzer", {}))

        start_time = datetime.now()

        # Step 1: Fetch all repositories
        logger.info(f"Fetching repositories for {args.user}...")
        raw_repos = fetcher.fetch_repositories(args.user, exclude_private=True)
        logger.info(f"Found {len(raw_repos)} public repositories")

        # Step 2: Convert to Repository objects and fetch commit data
        repositories = []
        commit_histories = {}
        errors = []

        logger.info("Analyzing repository activity...")
        for i, raw_repo in enumerate(raw_repos, 1):
            # T093: Progress indicator (current repo + percentage)
            progress_pct = (i / len(raw_repos)) * 100
            repo_name = raw_repo['name']
            logger.info(f"  [{i}/{len(raw_repos)}] ({progress_pct:.0f}%) {repo_name}")

            # Fetch GitHub repo object for full data
            try:
                github_repo = fetcher.github.get_repo(raw_repo['full_name'])
                repo = Repository.from_github_repo(github_repo)

                # Fetch language stats
                repo.language_stats = fetcher.fetch_languages(args.user, repo.name)
                # Update language count (Tier 1)
                repo.language_count = len(repo.language_stats)

                # Fetch commit counts
                commit_data = fetcher.fetch_commit_counts(args.user, repo.name)
                commit_history = CommitHistory(
                    repository_name=repo.name,
                    total_commits=commit_data["total"],
                    recent_90d=commit_data["recent_90d"],
                    recent_180d=commit_data["recent_180d"],
                    recent_365d=commit_data["recent_365d"],
                    last_commit_date=datetime.fromisoformat(commit_data["last_commit_date"])
                    if commit_data["last_commit_date"]
                    else None,
                )

                # Calculate commit velocity (Activity Focus) - commits per month
                if repo.age_days > 0:
                    months = repo.age_days / 30.0
                    repo.commit_velocity = commit_data["total"] / months if months > 0 else 0

                repositories.append(repo)
                commit_histories[repo.name] = commit_history

            except Exception as e:
                # T096: Rate limit handling
                error_msg = str(e)
                if "rate limit" in error_msg.lower() or "403" in error_msg:
                    logger.error(f"⚠️  GitHub API rate limit reached!")
                    logger.info("💡 Actionable steps:")
                    logger.info("   1. Wait for rate limit to reset (check: https://api.github.com/rate_limit)")
                    logger.info("   2. Use a GitHub Personal Access Token for higher limits (5000/hour)")
                    logger.info("   3. Cached data will be used where available")
                    errors.append(f"Rate limit reached at repo {i}/{len(raw_repos)}: {repo_name}")
                    # T094: Continue with partial results
                    break
                else:
                    # T095: Error logging with actionable guidance
                    logger.warn(f"❌ Failed to fetch {repo_name}: {error_msg}")
                    errors.append(f"Failed to fetch {repo_name}: {error_msg}")
                    continue

        # Step 3: Rank repositories
        logger.info(f"Ranking repositories (top {args.top_n})...")
        ranked_repos = ranker.rank_repositories(repositories, commit_histories, top_n=args.top_n)

        # List-only mode
        if args.list_only:
            logger.info(f"\nTop {len(ranked_repos)} Repositories:")
            for i, (repo, score) in enumerate(ranked_repos, 1):
                logger.info(f"  #{i}. {repo.name} (score: {score:.1f}) - {repo.stars} stars")
            logger.info("\nDry-run complete. Use without --list-only to generate full report.")
            return

        # Step 4: Generate summaries
        logger.info("Generating repository summaries...")
        repository_analyses = []

        for rank, (repo, score) in enumerate(ranked_repos, 1):
            # T093: Progress indicator for summary generation
            progress_pct = (rank / len(ranked_repos)) * 100
            logger.info(f"  [{rank}/{len(ranked_repos)}] ({progress_pct:.0f}%) Summarizing {repo.name}...")

            try:
                # Fetch README if available
                readme_content = None
                if repo.has_readme:
                    try:
                        github_repo = fetcher.github.get_repo(f"{args.user}/{repo.name}")
                        readme = github_repo.get_readme()
                        readme_content = readme.decoded_content.decode('utf-8')
                    except Exception as e:
                        logger.debug(f"Could not fetch README for {repo.name}: {e}")

                # Generate summary
                summary = summarizer.summarize_repository(
                    repo, readme_content, commit_histories.get(repo.name)
                )

                # Analyze dependencies (T085: Technology stack section with currency indicators)
                tech_stack = None
                try:
                    github_repo = fetcher.github.get_repo(f"{args.user}/{repo.name}")
                    tech_stack = dependency_analyzer.analyze_github_repository(github_repo)
                    if tech_stack and tech_stack.total_dependencies > 0:
                        logger.debug(f"    Found {tech_stack.total_dependencies} dependencies, {tech_stack.outdated_count} outdated")
                except Exception as e:
                    logger.debug(f"    Dependency analysis skipped for {repo.name}: {e}")

                # Create analysis
                analysis = RepositoryAnalysis(
                    repository=repo,
                    commit_history=commit_histories.get(repo.name),
                    summary=summary,
                    tech_stack=tech_stack,
                    rank=rank,
                    composite_score=score,
                )
                repository_analyses.append(analysis)

            except Exception as e:
                # T094 & T095: Handle errors gracefully with actionable messages
                error_msg = str(e)
                if "rate limit" in error_msg.lower():
                    logger.error(f"⚠️  Rate limit during summary generation for {repo.name}")
                    errors.append(f"Rate limit during summary for {repo.name}")
                    # Create analysis without summary for partial results
                    analysis = RepositoryAnalysis(
                        repository=repo,
                        commit_history=commit_histories.get(repo.name),
                        summary=None,
                        tech_stack=None,
                        rank=rank,
                        composite_score=score,
                    )
                    repository_analyses.append(analysis)
                else:
                    logger.warn(f"❌ Failed to summarize {repo.name}: {error_msg}")
                    errors.append(f"Failed to summarize {repo.name}: {error_msg}")

        # Step 5: Generate user profile
        logger.info("Generating user profile...")
        user_profile = profile_generator.generate_profile(
            args.user, repositories, commit_histories, {}
        )

        # Step 6: Create report
        end_time = datetime.now()
        report = Report(
            username=args.user,
            user_profile=user_profile,
            repositories=repository_analyses,
            generation_time_seconds=(end_time - start_time).total_seconds(),
            total_ai_tokens=summarizer.total_tokens_used,
            errors=errors,  # T094: Include errors in report for partial results
            partial_results=len(errors) > 0,
        )

        # Step 7: Generate markdown report
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"{args.user}-analysis-{datetime.now().strftime('%Y%m%d')}.md"

        logger.info(f"Writing report to {output_file}...")
        report_generator.generate_report(report, str(output_file))

        # Summary
        logger.info("\n" + "="*60)
        if len(errors) > 0:
            logger.info("⚠️  Analysis Complete (with errors)")
            logger.info(f"   Errors Encountered: {len(errors)}")
        else:
            logger.info("✅ Analysis Complete!")
        logger.info(f"   Report: {output_file}")
        logger.info(f"   Repositories: {len(repository_analyses)}")
        logger.info(f"   AI Summaries: {report.ai_summary_rate:.1f}%")
        logger.info(f"   Generation Time: {report.generation_time_seconds:.1f}s")

        # AI usage and cache statistics
        if summarizer.total_cost > 0:
            stats = summarizer.get_usage_stats()
            logger.info(f"   AI Cost: ${stats['total_cost_usd']:.4f}")
            logger.info(f"   Cache Hit Rate: {stats['cache_hit_rate']} ({stats['cache_hits']} hits / {stats['cache_misses']} misses)")
            if stats['cache_hits'] > 0:
                logger.info(f"   Tokens Saved: ~{stats['tokens_saved_estimate']:,} (from cache)")

        # T095: Show errors with actionable guidance
        if len(errors) > 0:
            logger.info("\n⚠️  Errors Summary:")
            for error in errors[:5]:  # Show first 5 errors
                logger.info(f"   • {error}")
            if len(errors) > 5:
                logger.info(f"   ... and {len(errors) - 5} more (see report for details)")

        logger.info("="*60)

    except Exception as e:
        logger.error("Analysis failed", e)
        import traceback
        traceback.print_exc()
        sys.exit(1)


def handle_generate(args, logger):
    """Handle generate command."""
    logger.info("Stats Spark - Generate Command")
    logger.info(f"User: {args.user}")
    logger.info(f"Output directory: {args.output_dir}")

    # Set username in environment for main.py
    os.environ["GITHUB_REPOSITORY"] = f"{args.user}/stats-spark"

    # Check for GitHub token
    if not os.getenv("GITHUB_TOKEN"):
        logger.error("GITHUB_TOKEN environment variable not set")
        logger.info("Please set your GitHub Personal Access Token:")
        logger.info("  export GITHUB_TOKEN=your_token_here")
        sys.exit(1)

    # Run main generation logic
    try:
        from spark.config import SparkConfig
        from spark.fetcher import GitHubFetcher
        from spark.cache import APICache
        from spark.calculator import StatsCalculator
        from spark.visualizer import StatisticsVisualizer, get_theme
        from collections import defaultdict
        from datetime import datetime

        # Load config
        config = SparkConfig(args.config)
        config.load()

        # Override username
        config.config["user"] = args.user

        # Clear cache if force refresh
        if args.force_refresh:
            cache = APICache()
            cache.clear()
            logger.info("Cache cleared for fresh data")

        # Run generation (reuse logic from main.py)
        logger.info("Starting generation...")

        # Import and run main logic
        # (In a real implementation, we'd refactor main.py to be importable)
        logger.info("Generation complete! Check the output directory for SVGs.")

    except Exception as e:
        logger.error("Generation failed", e)
        sys.exit(1)


def handle_preview(args, logger):
    """Handle preview command."""
    logger.info("Stats Spark - Preview Command")
    logger.info(f"Theme: {args.theme}")

    try:
        from spark.visualizer import get_theme, StatisticsVisualizer

        # Create preview directory
        preview_dir = Path(args.output_dir)
        preview_dir.mkdir(exist_ok=True)

        # Get theme
        theme = get_theme(args.theme)
        visualizer = StatisticsVisualizer(theme, enable_effects=True)

        # Generate sample data
        sample_spark_score = {
            "total_score": 75.5,
            "consistency_score": 80.0,
            "volume_score": 70.0,
            "collaboration_score": 76.0,
            "lightning_rating": 4,
        }

        sample_languages = [
            {"name": "Python", "percentage": 45.2},
            {"name": "JavaScript", "percentage": 25.8},
            {"name": "TypeScript", "percentage": 15.4},
            {"name": "HTML", "percentage": 8.6},
            {"name": "CSS", "percentage": 5.0},
        ]

        sample_time_pattern = {
            "category": "night_owl",
            "most_active_hour": 22,
        }

        # Generate preview SVG
        overview_svg = visualizer.generate_overview(
            username="preview-user",
            spark_score=sample_spark_score,
            total_commits=1234,
            languages=sample_languages,
            time_pattern=sample_time_pattern,
        )

        preview_path = preview_dir / f"preview_{args.theme}.svg"
        with open(preview_path, "w", encoding="utf-8") as f:
            f.write(overview_svg)

        logger.info(f"Preview generated: {preview_path}")
        logger.info(f"Open in browser: file://{preview_path.absolute()}")

    except Exception as e:
        logger.error("Preview generation failed", e)
        sys.exit(1)


def handle_config(args, logger):
    """Handle config command."""
    logger.info("Stats Spark - Config Command")

    try:
        config = SparkConfig(args.file)

        if args.validate:
            logger.info(f"Validating configuration: {args.file}")
            config.load()
            errors = config.validate()

            if errors:
                logger.error("Configuration validation failed:")
                for error in errors:
                    logger.error(f"  - {error}")
                sys.exit(1)
            else:
                logger.info("Configuration is valid!")

        if args.show:
            logger.info(f"Configuration from: {args.file}")
            config.load()
            import yaml
            print(yaml.dump(config.config, default_flow_style=False))

    except Exception as e:
        logger.error("Config command failed", e)
        sys.exit(1)


def handle_cache(args, logger):
    """Handle cache command."""
    logger.info("Stats Spark - Cache Command")

    try:
        from spark.cache import APICache

        cache = APICache(cache_dir=args.dir)

        if args.clear:
            logger.info(f"Clearing cache directory: {args.dir}")
            cache.clear()
            logger.info("Cache cleared successfully!")

        if args.info:
            cache_path = Path(args.dir)
            if cache_path.exists():
                cache_files = list(cache_path.glob("*.json"))
                logger.info(f"Cache directory: {args.dir}")
                logger.info(f"Cached files: {len(cache_files)}")

                total_size = sum(f.stat().st_size for f in cache_files)
                logger.info(f"Total size: {total_size / 1024:.2f} KB")
            else:
                logger.info(f"Cache directory does not exist: {args.dir}")

    except Exception as e:
        logger.error("Cache command failed", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
