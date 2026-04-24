"""Command-line interface for Stats Spark local usage."""

import argparse
import os
import sys

import github

from spark.cli_argument_builders import build_main_parser
from spark.cli_handlers import (
    handle_analyze,
    handle_cache,
    handle_config,
    handle_generate,
    handle_preview,
    handle_refresh,
    handle_unified,
)
from spark.logger import get_logger


def _configure_github_api_logging(logger) -> None:
    """Enable per-request GitHub API logging when explicitly requested."""
    raw_flag = os.getenv("SPARK_LOG_GITHUB_API_CALLS", "")
    enabled = raw_flag.strip().lower() in {"1", "true", "yes", "on"}
    if not enabled:
        return

    try:
        github.enable_console_debug_logging()
        logger.info("GitHub API request logging enabled (SPARK_LOG_GITHUB_API_CALLS)")
    except Exception as exc:
        logger.warning(f"Failed to enable GitHub API request logging: {exc}")


def main():
    """Main CLI entry point."""
    parser = build_main_parser()

    args = parser.parse_args()

    # Show help if no command provided
    if not args.command:
        parser.print_help()
        sys.exit(0)

    logger = get_logger("spark-cli", verbose=getattr(args, "verbose", False))
    _configure_github_api_logging(logger)

    # Execute commands
    result = None
    if args.command == "unified":
        result = handle_unified(args, logger)
    elif args.command == "analyze":
        result = handle_analyze(args, logger)
    elif args.command == "generate":
        result = handle_generate(args, logger)
    elif args.command == "preview":
        result = handle_preview(args, logger)
    elif args.command == "config":
        result = handle_config(args, logger)
    elif args.command == "cache":
        result = handle_cache(args, logger)
    elif args.command == "refresh":
        result = handle_refresh(args, logger)

    if isinstance(result, int) and result != 0:
        sys.exit(result)


if __name__ == "__main__":
    main()
