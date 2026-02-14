{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
"""Configuration management for {{ cookiecutter.project_name }}."""

import json
import logging
import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

from .exceptions import ConfigurationError

logger = logging.getLogger(__name__)


class Config:
    """Configuration loader with priority: .env-private > .env > environment > config files."""

    def __init__(self, config_dir: Path | None = None) -> None:
        """Initialize configuration.

        Args:
            config_dir: Directory containing configuration files. Defaults to etc/.
        """
        self.config_dir = config_dir or Path("etc")
        self._config: dict[str, Any] = {}
        self._load_env_files()

    def _load_env_files(self) -> None:
        """Load .env files with priority."""
        env_private = Path(".env-private")
        env_file = Path(".env")

        if env_private.exists():
            load_dotenv(env_private, override=True)
            logger.debug("Loaded .env-private")

        if env_file.exists():
            load_dotenv(env_file, override=False)
            logger.debug("Loaded .env")

    def load_yaml(self, filename: str) -> dict[str, Any]:
        """Load YAML configuration file.

        Args:
            filename: Name of YAML file in config directory.

        Returns:
            Configuration dictionary.

        Raises:
            ConfigurationError: If file cannot be loaded.
        """
        path = self.config_dir / filename
        try:
            with open(path) as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            raise ConfigurationError(f"Failed to load {path}: {e}") from e

    def load_json(self, filename: str) -> dict[str, Any]:
        """Load JSON configuration file.

        Args:
            filename: Name of JSON file in config directory.

        Returns:
            Configuration dictionary.

        Raises:
            ConfigurationError: If file cannot be loaded.
        """
        path = self.config_dir / filename
        try:
            with open(path) as f:
                return json.load(f)
        except Exception as e:
            raise ConfigurationError(f"Failed to load {path}: {e}") from e

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value with environment variable priority.

        Args:
            key: Configuration key.
            default: Default value if key not found.

        Returns:
            Configuration value.
        """
        return os.getenv(key.upper(), self._config.get(key, default))

    def set(self, key: str, value: Any) -> None:
        """Set configuration value.

        Args:
            key: Configuration key.
            value: Configuration value.
        """
        self._config[key] = value
{%- endif %}
