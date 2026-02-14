{% if cookiecutter.project_type == "python_cli" -%}
"""Command-line interface for {{ cookiecutter.project_name }}."""

import argparse
import logging
import sys
from pathlib import Path

from . import __version__
from .config import Config
from .core import Core

logger = logging.getLogger(__name__)


def cmd_init(args: argparse.Namespace) -> int:
    """Initialize project.

    Args:
        args: Command arguments.

    Returns:
        Exit code.
    """
    logger.info(f"Initializing project in: {args.path}")
    path = Path(args.path)
    path.mkdir(parents=True, exist_ok=True)
    print(f"✓ Initialized project in {path}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Run main application.

    Args:
        args: Command arguments.

    Returns:
        Exit code.
    """
    config = Config()
    core = Core(config._config)

    logger.info("Running application")
    result = core.process(args.input or "hello world")
    print(f"Result: {result}")
    return 0


def cmd_config(args: argparse.Namespace) -> int:
    """Show configuration.

    Args:
        args: Command arguments.

    Returns:
        Exit code.
    """
    config = Config()

    if args.key:
        value = config.get(args.key)
        print(f"{args.key}: {value}")
    else:
        print("Configuration:")
        print(f"  LOG_LEVEL: {config.get('LOG_LEVEL', 'INFO')}")
        print(f"  DEBUG: {config.get('DEBUG', 'false')}")
        print(f"  APP_NAME: {config.get('APP_NAME', '{{ cookiecutter.project_name }}')}")

    return 0


def main() -> int:
    """Main entry point.

    Returns:
        Exit code.
    """
    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.package_name }}",
        description="{{ cookiecutter.project_short_description }}",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize project")
    init_parser.add_argument("path", nargs="?", default=".", help="Project path")

    # run command
    run_parser = subparsers.add_parser("run", help="Run application")
    run_parser.add_argument("input", nargs="?", help="Input data")

    # config command
    config_parser = subparsers.add_parser("config", help="Show configuration")
    config_parser.add_argument("key", nargs="?", help="Configuration key")

    args = parser.parse_args()

    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    if not args.command:
        parser.print_help()
        return 1

    # Execute command
    commands = {
        "init": cmd_init,
        "run": cmd_run,
        "config": cmd_config,
    }

    try:
        return commands[args.command](args)
    except Exception as e:
        logger.exception("Command failed")
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
{%- endif %}
