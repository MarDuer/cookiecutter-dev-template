# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Overview

Welcome to the documentation for {{ cookiecutter.project_name }}.

{% if cookiecutter.project_type == "python_cli" -%}
This is a command-line tool that provides the following features:

- Configuration management
- Structured logging
- Extensible command system
{%- elif cookiecutter.project_type == "python_library" -%}
This is a Python library that provides:

- Clean API
- Type hints
- Comprehensive documentation
{%- elif cookiecutter.project_type == "c_tricore" -%}
This is an embedded C project for Infineon TriCore TC375 that provides:

- Cyclic handler pattern
- MISRA-C:2012 compliance
- Production-ready structure
{%- endif %}

## Quick Links

- [Getting Started](getting-started.md) - Installation and first steps
- [Architecture](architecture.md) - System design and patterns
{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
- [API Reference](api.md) - Detailed API documentation
{%- endif %}
- [Examples](examples.md) - Usage examples
- [Contributing](contributing.md) - How to contribute

## License

This project is licensed under the {{ cookiecutter.license }} License.
