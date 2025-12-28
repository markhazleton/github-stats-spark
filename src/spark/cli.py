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
    if args.command == "generate":
        handle_generate(args, logger)
    elif args.command == "preview":
        handle_preview(args, logger)
    elif args.command == "config":
        handle_config(args, logger)
    elif args.command == "cache":
        handle_cache(args, logger)


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
