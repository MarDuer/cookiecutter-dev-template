{% if cookiecutter.project_type == "python_cli" -%}
"""Main entry point for {{ cookiecutter.project_name }}."""

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
{%- endif %}
