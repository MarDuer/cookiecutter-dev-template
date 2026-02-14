{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
"""Custom exceptions for {{ cookiecutter.project_name }}."""


class {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}Error(Exception):
    """Base exception for {{ cookiecutter.project_name }}."""


class ConfigurationError({{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}Error):
    """Configuration related errors."""


class ValidationError({{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}Error):
    """Data validation errors."""
{%- endif %}
