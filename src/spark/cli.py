"""Command-line interface for Stats Spark local usage."""

import argparse
import sys

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


def main():
    """Main CLI entry point."""
    parser = build_main_parser()

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


if __name__ == "__main__":
    main()
