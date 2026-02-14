{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
"""Core business logic for {{ cookiecutter.project_name }}."""

import logging
from typing import Any

logger = logging.getLogger(__name__)


class Core:
    """Core application logic."""

    def __init__(self, config: dict[str, Any]) -> None:
        """Initialize core logic.

        Args:
            config: Configuration dictionary.
        """
        self.config = config
        logger.info("Core initialized")

    def process(self, data: str) -> str:
        """Process data.

        Args:
            data: Input data to process.

        Returns:
            Processed data.
        """
        logger.debug(f"Processing: {data}")
        result = data.upper()
        logger.info("Processing complete")
        return result
{%- endif %}
