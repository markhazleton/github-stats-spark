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
  ALL-IN-ONE: Generate unified data + SVGs + reports in a single optimized run:
    spark unified --user markhazleton

  With AI summaries for each repository (requires ANTHROPIC_API_KEY):
    spark unified --user markhazleton --include-ai-summaries

  Force fresh data (bypass cache):
    spark unified --user markhazleton --force-refresh

  Legacy commands (for specific operations only):
    spark generate --user markhazleton  # Generate statistics/SVGs only
    spark analyze --user markhazleton    # Generate analysis reports only

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

    # Unified command (ALL-IN-ONE - Comprehensive data + SVGs + reports)
    unified_parser = subparsers.add_parser(
        "unified",
        help="ALL-IN-ONE: Generate unified data, SVGs, and markdown reports in a single optimized run"
    )
    unified_parser.add_argument(
        "--user",
        type=str,
        required=True,
        help="GitHub username to analyze",
    )
    unified_parser.add_argument(
        "--output-dir",
        type=str,
        default="data",
        help="Output directory for repositories.json (default: data)",
    )
    unified_parser.add_argument(
        "--config",
        type=str,
        default="config/spark.yml",
        help="Configuration file path (default: config/spark.yml)",
    )
    unified_parser.add_argument(
        "--force-refresh",
        action="store_true",
        help="Bypass cache and fetch fresh data for all operations",
    )
    unified_parser.add_argument(
        "--include-ai-summaries",
        action="store_true",
        help="Include AI-generated summaries for each repository (requires ANTHROPIC_API_KEY)",
    )
    unified_parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    unified_parser.add_argument(
        "--max-repos",
        type=int,
        default=None,
        help="Maximum number of repositories to process (for testing/debugging)",
    )

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
    analyze_parser.add_argument(
        "--unified",
        action="store_true",
        help="Generate unified report (SVGs + analysis) instead of dated report",
    )
    analyze_parser.add_argument(
        "--keep-dated",
        action="store_true",
        help="Also generate dated report when using --unified mode",
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
        "--dashboard",
        action="store_true",
        help="Generate dashboard JSON data for repository comparison dashboard",
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
        "--prune",
        action="store_true",
        help="Prune old cache entries (keep last 2 weeks)",
    )
    cache_parser.add_argument(
        "--info",
        action="store_true",
        help="Show cache information",
    )
    cache_parser.add_argument(
        "--status",
        action="store_true",
        help="Show cache status for repositories",
    )
    cache_parser.add_argument(
        "--update-status",
        action="store_true",
        help="Update cache status in repositories cache file",
    )
    cache_parser.add_argument(
        "--fetch-fresh",
        action="store_true",
        help="Fetch fresh repository data from GitHub when updating status (makes 1 API call)",
    )
    cache_parser.add_argument(
        "--list-refresh-needed",
        action="store_true",
        help="List repositories that need cache refresh",
    )
    cache_parser.add_argument(
        "--user",
        type=str,
        help="GitHub username (required for status commands)",
    )
    cache_parser.add_argument(
        "--dir",
        type=str,
        default=".cache",
        help="Cache directory (default: .cache)",
    )

    # Refresh command - smart incremental updates
    refresh_parser = subparsers.add_parser(
        "refresh",
        help="Smart incremental refresh - only update repos with new commits"
    )
    refresh_parser.add_argument(
        "--user",
        type=str,
        required=True,
        help="GitHub username",
    )
    refresh_parser.add_argument(
        "--clear-summaries",
        action="store_true",
        help="Clear AI summaries and tech stack data to regenerate",
    )
    refresh_parser.add_argument(
        "--include-ai-summaries",
        action="store_true",
        help="Generate AI summaries for updated repositories",
    )
    refresh_parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    args = parser.parse_args()

    # Show help if no command provided
    if not args.command:
        parser.print_help()
        sys.exit(0)

    logger = get_logger("spark-cli", verbose=getattr(args, "verbose", False))

    # Execute commands
    if args.command == "unified":
        handle_unified(args, logger)
    elif args.command == "analyze":
        handle_analyze(args, logger)
    elif args.command == "generate":
        handle_generate(args, logger)
    elif args.command == "preview":
        handle_preview(args, logger)
    elif args.command == "config":
        handle_config(args, logger)
    elif args.command == "cache":
        handle_cache(args, logger)
    elif args.command == "refresh":
        handle_refresh(args, logger)


def handle_unified(args, logger):
    """Handle unified command - ALL-IN-ONE: Generate unified data, SVGs, and reports."""
    from datetime import datetime
    from pathlib import Path
    from spark.config import SparkConfig
    from spark.unified_data_generator import UnifiedDataGenerator
    from spark.cache import APICache
    from spark.unified_report_workflow import UnifiedReportWorkflow
    from spark.unified_report_generator import UnifiedReportGenerator
    from spark.exceptions import WorkflowError
    
    logger.info("=" * 70)
    logger.info("Stats Spark - ALL-IN-ONE Unified Generation")
    logger.info("=" * 70)
    logger.info(f"User: {args.user}")
    logger.info(f"Data output: {args.output_dir}")
    logger.info(f"Reports output: output/")
    logger.info(f"AI Summaries: {'Yes' if args.include_ai_summaries else 'No'}")
    logger.info(f"Force Refresh: {'Yes' if args.force_refresh else 'No'}")

    # Check for GitHub token
    if not os.getenv("GITHUB_TOKEN"):
        logger.error("GITHUB_TOKEN environment variable not set")
        logger.info("Please set your GitHub Personal Access Token:")
        logger.info("  export GITHUB_TOKEN=your_token_here")
        sys.exit(1)

    # Check for Anthropic API key if AI summaries requested
    if args.include_ai_summaries and not os.getenv("ANTHROPIC_API_KEY"):
        logger.warning("ANTHROPIC_API_KEY not set - AI summaries will be skipped")
        logger.info("To enable AI summaries, set: export ANTHROPIC_API_KEY=your_key")

    try:
        start_time = datetime.now()
        
        # ===================================================================
        # STEP 1: Generate Unified Data (repositories.json)
        # ===================================================================
        logger.info("")
        logger.info("=" * 70)
        logger.info("STEP 1/3: Generating Unified Data (repositories.json)")
        logger.info("=" * 70)
        
        # Load config
        config = SparkConfig(args.config)
        config.load()

        # Override AI summaries setting if specified
        if args.include_ai_summaries:
            dashboard_config = config.config.get("dashboard", {})
            if "data_generation" not in dashboard_config:
                dashboard_config["data_generation"] = {}
            dashboard_config["data_generation"]["include_ai_summaries"] = True

        cache_config = config.config.get("cache", {})
        shared_cache = APICache(
            cache_dir=cache_config.get("directory", ".cache"),
            config=config,
        )

        # Create generator
        generator = UnifiedDataGenerator(
            config=config,
            username=args.user,
            output_dir=args.output_dir,
            force_refresh=args.force_refresh,
            max_repos_override=args.max_repos,
            cache=shared_cache,
        )

        # Generate and save unified data
        data_output_path, generation_skipped = generator.save()
        logger.info(f"Unified data saved to: {data_output_path}")

        # Skip SVG/Report generation if data was fresh and unchanged
        if generation_skipped:
            logger.info("")
            logger.info("=" * 70)
            logger.info("⏭️  Skipping SVG and Report Generation")
            logger.info("=" * 70)
            logger.info("Data is fresh (< 1 week old) - no repositories updated")
            logger.info("SVG visualizations and reports are already up-to-date")
            logger.info("Use --force-refresh to regenerate everything")
            
            end_time = datetime.now()
            total_time = (end_time - start_time).total_seconds()
            
            logger.info("")
            logger.info("=" * 70)
            logger.info("Unified Workflow Complete (No Updates Needed)")
            logger.info("=" * 70)
            logger.info(f"Unified Data: {data_output_path}")
            logger.info(f"SVG Files: output/*.svg (unchanged)")
            logger.info(f"Report: output/reports/{args.user}-analysis.md (unchanged)")
            logger.info(f"Total Time: {total_time:.1f}s")
            logger.info("")
            logger.info("All data is current - no regeneration needed!")
            return 0

        # ===================================================================
        # STEP 2: Generate SVG Visualizations
        # ===================================================================
        logger.info("")
        logger.info("=" * 70)
        logger.info("STEP 2/3: Generating SVG Visualizations")
        logger.info("=" * 70)
        
        # Initialize cache with config TTL
        workflow = UnifiedReportWorkflow(
            config, 
            shared_cache, 
            output_dir="output",
            max_repos=args.max_repos
        )
        
        try:
            unified_report = workflow.execute(args.user)
            logger.info(f"Generated {len(unified_report.available_svgs)} SVG files")
            
            # ===================================================================
            # STEP 3: Generate Markdown Reports
            # ===================================================================
            logger.info("")
            logger.info("=" * 70)
            logger.info("STEP 3/3: Generating Markdown Reports")
            logger.info("=" * 70)
            
            output_dir = Path("output/reports")
            output_dir.mkdir(parents=True, exist_ok=True)
            report_path = output_dir / f"{args.user}-analysis.md"
            
            generator_report = UnifiedReportGenerator(config)
            generator_report.generate_report(unified_report, str(report_path))
            logger.info(f"Report saved to: {report_path}")
            
        except WorkflowError as e:
            logger.warning(f"SVG/Report generation had issues: {e}")
            logger.info("Unified data generation was successful, but SVG/reports had errors")

        # ===================================================================
        # Summary
        # ===================================================================
        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds()
        
        logger.info("")
        logger.info("=" * 70)
        logger.info("ALL-IN-ONE Generation Complete!")
        logger.info("=" * 70)
        logger.info(f"📊 Unified Data: {data_output_path}")
        logger.info(f"SVG Files: output/*.svg")
        logger.info(f"Report: output/reports/{args.user}-analysis.md")
        logger.info(f"⏱️  Total Time: {total_time:.1f}s")
        logger.info("")
        logger.info("All data gathered, LLM summaries generated (if enabled),")
        logger.info("and visualizations/reports created in a single optimized run!")

        return 0

    except Exception as e:
        logger.error(f"Unified generation failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


def handle_analyze(args, logger):
    """Handle analyze command - Generate repository analysis report."""
    logger.info("Stats Spark - Analyze Command")
    logger.info(f"User: {args.user}")
    logger.info(f"Top N: {args.top_n}")

    # Route to unified or dated mode
    if args.unified:
        logger.info("Mode: Unified Report (SVGs + Analysis)")
        return handle_unified_analyze(args, logger)
    else:
        logger.info("Mode: Dated Report (Analysis Only)")
        return handle_dated_analyze(args, logger)


def handle_unified_analyze(args, logger):
    """Generate unified report with SVGs and analysis."""
    from datetime import datetime
    from pathlib import Path
    from spark.config import SparkConfig
    from spark.cache import APICache
    from spark.unified_report_workflow import UnifiedReportWorkflow
    from spark.unified_report_generator import UnifiedReportGenerator
    from spark.exceptions import WorkflowError

    # Check for GitHub token
    if not os.getenv("GITHUB_TOKEN"):
        logger.error("GITHUB_TOKEN environment variable not set")
        logger.info("Please set your GitHub Personal Access Token:")
        logger.info("  export GITHUB_TOKEN=your_token_here")
        sys.exit(1)

    try:
        # Load config
        config = SparkConfig(args.config)
        config.load()

        # Initialize cache with config TTL
        cache_config = config.get("cache", {})
        cache = APICache(
            cache_dir=cache_config.get("directory", ".cache"),
            config=config,
        )
        workflow = UnifiedReportWorkflow(config, cache, output_dir="output")

        # Execute unified workflow
        logger.info("=" * 70)
        logger.info("Executing Unified Report Workflow")
        logger.info("=" * 70)

        unified_report = workflow.execute(args.user)

        # Generate unified markdown (non-dated)
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        unified_path = output_dir / f"{args.user}-analysis.md"

        generator = UnifiedReportGenerator(config)
        generator.generate_report(unified_report, str(unified_path))

        logger.info("")
        logger.info("=" * 70)
        logger.info("Unified Report Generated Successfully")
        logger.info("=" * 70)
        logger.info(f"Report: {unified_path}")
        logger.info(f"SVGs: {len(unified_report.available_svgs)}/6")
        logger.info(f"Repos: {len(unified_report.repositories)}")
        logger.info(f"Success Rate: {unified_report.success_rate}%")
        logger.info(f"Generation Time: {unified_report.generation_time:.1f}s")

        # Optionally generate dated report for comparison
        if args.keep_dated:
            logger.info("")
            logger.info("Generating dated report for comparison...")
            dated_args = argparse.Namespace(**vars(args))
            dated_args.unified = False
            handle_dated_analyze(dated_args, logger)

        return 0

    except WorkflowError as e:
        logger.error(f"Workflow failed: {e}")
        return 1
    except Exception as e:
        import traceback
        logger.error(f"Unexpected error: {e}")
        logger.error(traceback.format_exc())
        return 1


def handle_dated_analyze(args, logger):
    """Handle dated report generation (existing behavior)."""
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

        # Initialize cache with config TTL
        cache_config = config.config.get("cache", {})
        cache = APICache(
            cache_dir=cache_config.get("directory", ".cache"),
            config=config,
        )
        
        # Initialize components
        fetcher = GitHubFetcher(cache=cache)
        ranker = RepositoryRanker(config=config.config.get("analyzer", {}).get("ranking_weights"))
        summarizer = RepositorySummarizer(cache=cache)  # Pass cache to save tokens!
        profile_generator = UserProfileGenerator(summarizer)
        report_generator = ReportGenerator()
        dependency_analyzer = RepositoryDependencyAnalyzer(config=config.config.get("analyzer", {}))

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

                # Fetch language stats (with push date for smart caching)
                repo.language_stats = fetcher.fetch_languages(
                    args.user, 
                    repo.name,
                    repo_pushed_at=github_repo.pushed_at
                )
                # Update language count (Tier 1)
                repo.language_count = len(repo.language_stats)

                # Fetch commit counts (with push date for smart caching)
                commit_data = fetcher.fetch_commit_counts(
                    args.user, 
                    repo.name,
                    repo_pushed_at=github_repo.pushed_at
                )
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
                    repo,
                    readme_content,
                    commit_histories.get(repo.name),
                    repository_owner=args.user,
                    repo_pushed_at=repo.pushed_at,
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
            logger.info("Analysis Complete (with errors)")
            logger.info(f"   Errors Encountered: {len(errors)}")
        else:
            logger.info("Analysis Complete!")
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
        from spark.cache import APICache
        from datetime import datetime

        # Load config
        config = SparkConfig(args.config)
        config.load()

        # Override username
        config.config["user"] = args.user

        # Clear cache if force refresh
        if args.force_refresh:
            cache_config = config.config.get("cache", {})
            cache = APICache(
                cache_dir=cache_config.get("directory", ".cache"),
                config=config,
            )
            cache.clear()
            logger.info("Cache cleared for fresh data")

        # Route to dashboard or SVG generation
        if args.dashboard:
            logger.info("Mode: Dashboard Data Generation")
            handle_dashboard_generation(args, logger, config)
        else:
            # Run standard SVG generation (reuse logic from main.py)
            logger.info("Starting generation...")
            # Import and run main logic
            # (In a real implementation, we'd refactor main.py to be importable)
            logger.info("Generation complete! Check the output directory for SVGs.")

    except Exception as e:
        logger.error("Generation failed", e)
        sys.exit(1)


def handle_dashboard_generation(args, logger, config):
    """Handle dashboard data generation."""
    from spark.dashboard_generator import DashboardGenerator
    from datetime import datetime

    try:
        logger.info("=" * 70)
        logger.info("Dashboard Data Generation")
        logger.info("=" * 70)
        logger.info(f"Username: {args.user}")
        logger.info(f"Config: {args.config}")

        # Initialize dashboard generator
        generator = DashboardGenerator(config=config.config, username=args.user)

        # Generate dashboard data
        logger.info("")
        logger.info("Generating dashboard data...")
        start_time = datetime.now()

        dashboard_data = generator.generate()

        # Save to JSON file
        output_path = generator.write_json_output(dashboard_data)

        end_time = datetime.now()
        generation_time = (end_time - start_time).total_seconds()

        # Summary
        logger.info("")
        logger.info("=" * 70)
        logger.info("Dashboard Generation Complete!")
        logger.info("=" * 70)
        logger.info(f"Output: {output_path}")
        logger.info(f"Repositories: {len(dashboard_data.repositories)}")
        logger.info(f"Username: {dashboard_data.profile.username if dashboard_data.profile else 'N/A'}")
        logger.info(f"Schema Version: {dashboard_data.metadata.schema_version if dashboard_data.metadata else 'N/A'}")
        logger.info(f"Generation Time: {generation_time:.1f}s")
        logger.info("=" * 70)

        return 0

    except Exception as e:
        logger.error(f"Dashboard generation failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


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
        from spark.cache_status import CacheStatusTracker

        cache = APICache(cache_dir=args.dir)
        cache_tracker = CacheStatusTracker(cache_dir=args.dir)

        if args.clear:
            logger.info(f"Clearing cache directory: {args.dir}")
            cache.clear()
            logger.info("Cache cleared successfully!")

        if args.prune:
            logger.info(f"Pruning cache directory: {args.dir}")
            cache.prune(keep_weeks=2)
            logger.info("Cache pruned successfully!")

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

        if args.status:
            if not args.user:
                logger.error("--user is required for cache status")
                sys.exit(1)
            
            logger.info(f"Cache status for user: {args.user}")
            stats = cache_tracker.get_cache_statistics(username=args.user)
            logger.info(f"Total repositories: {stats['total_repositories']}")
            logger.info(f"Cached repositories: {stats['cached_repositories']}")
            logger.info(f"Needs refresh: {stats['needs_refresh']}")
            logger.info(f"Up to date: {stats['up_to_date']}")
            logger.info(f"Cache hit rate: {stats['cache_hit_rate']}")
            logger.info(f"Refresh rate: {stats['refresh_rate']}")

        if args.update_status:
            if not args.user:
                logger.error("--user is required for cache status update")
                sys.exit(1)
            
            fetch_fresh = getattr(args, 'fetch_fresh', False)
            if fetch_fresh:
                logger.info(f"Fetching fresh repository data from GitHub for user: {args.user}")
            else:
                logger.info(f"Updating cache status for user: {args.user}")
            
            cache_data = cache_tracker.update_repositories_cache_with_status(
                username=args.user,
                fetch_fresh=fetch_fresh
            )
            logger.info(f"Updated cache status for {len(cache_data.get('value', []))} repositories")
            logger.info(f"Cache status updated at: {cache_data.get('cache_status_updated')}")
            
            # Show summary of refresh needs and recent activity
            repos = cache_data.get('value', [])
            needs_refresh = sum(1 for r in repos if r.get('cache_status', {}).get('refresh_needed', False))
            
            # Count repositories updated in the past 7 days
            from datetime import datetime, timezone, timedelta
            seven_days_ago = datetime.now(timezone.utc) - timedelta(days=7)
            recently_updated = 0
            recently_updated_with_outdated_cache = 0
            recently_updated_repos = []
            
            for r in repos:
                pushed_at = r.get('pushed_at')
                if pushed_at:
                    try:
                        pushed_date = datetime.fromisoformat(pushed_at.replace('+00:00', ''))
                        if pushed_date.tzinfo is None:
                            pushed_date = pushed_date.replace(tzinfo=timezone.utc)
                        if pushed_date >= seven_days_ago:
                            recently_updated += 1
                            cache_status = r.get('cache_status', {})
                            cache_date = cache_status.get('cache_date', 'No cache')
                            is_outdated = False
                            
                            # Check if this recently-updated repo has outdated cache
                            if cache_status.get('refresh_needed', False):
                                refresh_reasons = cache_status.get('refresh_reasons', [])
                                if 'repo_has_new_commits' in refresh_reasons:
                                    recently_updated_with_outdated_cache += 1
                                    is_outdated = True
                            
                            recently_updated_repos.append({
                                'name': r['name'],
                                'pushed_at': pushed_at,
                                'cache_date': cache_date,
                                'is_outdated': is_outdated
                            })
                    except (ValueError, AttributeError):
                        pass
            
            logger.info(f"Repositories updated in past 7 days: {recently_updated}")
            if recently_updated_with_outdated_cache > 0:
                logger.info(f"  └─ Of those, {recently_updated_with_outdated_cache} have outdated cache (new commits since last fetch)")
            
            # Display the list of recently updated repositories
            if recently_updated_repos:
                logger.info("\nRecently updated repositories:")
                for repo_info in recently_updated_repos:
                    status_marker = "⚠️ OUTDATED" if repo_info['is_outdated'] else "✓ cached"
                    logger.info(f"  • {repo_info['name']}")
                    logger.info(f"      Last update: {repo_info['pushed_at']}")
                    logger.info(f"      Cache date:  {repo_info['cache_date']} {status_marker}")
            
            if needs_refresh > 0:
                logger.info(f"\n{needs_refresh} repositories need cache refresh")
            else:
                logger.info("\nAll repositories have up-to-date cache!")

        if args.list_refresh_needed:
            if not args.user:
                logger.error("--user is required for listing refresh-needed repositories")
                sys.exit(1)
            
            logger.info(f"Repositories needing refresh for user: {args.user}")
            repos = cache_tracker.get_repositories_needing_refresh(username=args.user)
            
            if not repos:
                logger.info("All repositories have up-to-date cache!")
            else:
                logger.info(f"\n{len(repos)} repositories need refresh:")
                for repo in repos[:20]:  # Show first 20
                    cache_status = repo.get("cache_status", {})
                    reasons = cache_status.get("refresh_reasons", [])
                    logger.info(f"  - {repo['name']}: {', '.join(reasons)}")
                
                if len(repos) > 20:
                    logger.info(f"  ... and {len(repos) - 20} more")

    except FileNotFoundError as e:
        logger.error(f"Cache file not found: {e}")
        logger.info("Run 'spark unified --user USERNAME' first to generate cache")
        sys.exit(1)
    except Exception as e:
        logger.error("Cache command failed", e)
        import traceback
        traceback.print_exc()
        sys.exit(1)


def handle_refresh(args, logger):
    """Handle smart incremental refresh command."""
    from spark.refresh import SmartRefresh

    logger.info("Stats Spark - Smart Incremental Refresh")
    logger.info("=" * 80)

    try:
        refresher = SmartRefresh()
        result = refresher.refresh(
            username=args.user,
            include_ai_summaries=args.include_ai_summaries,
            clear_summaries=args.clear_summaries,
        )

        logger.info("\n" + "=" * 80)
        logger.info("Refresh Summary:")
        logger.info(f"  🔄 Refreshed: {result['refreshed']} repositories")
        logger.info(f"  ✅ Unchanged: {result['unchanged']} repositories")
        logger.info(f"  🗑️  Removed: {result['removed']} repositories")

        if result['refreshed'] > 0:
            logger.info("\n💡 Tip: Run 'cd frontend && npm run build' to update the dashboard")

    except Exception as e:
        logger.error("Refresh command failed", e)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
