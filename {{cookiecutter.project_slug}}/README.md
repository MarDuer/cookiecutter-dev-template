# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Project Information

- **Author**: {{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})
- **License**: {{ cookiecutter.license }}
- **Version**: {{ cookiecutter.version }}
{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
- **Python Version**: {{ cookiecutter.python_version }}+
{%- endif %}

## Quick Start

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
```bash
# Install dependencies
just install

# Run tests
just test

# View documentation
just docs-serve
```
{%- elif cookiecutter.project_type == "c_tricore" -%}
```bash
# Build project
scons

# Run tests
scons test
```
{%- endif %}

## Features

{% if cookiecutter.project_type == "python_cli" -%}
- Command-line interface with subcommands
- Configuration management (.env, YAML, JSON, TOML)
- Structured logging
{%- elif cookiecutter.project_type == "python_library" -%}
- Python library with comprehensive API
- Type hints and documentation
{%- elif cookiecutter.project_type == "c_tricore" -%}
- TriCore TC375 embedded project
- Cyclic handler pattern
- MISRA-C:2012 compliant
{%- endif %}
{% if cookiecutter.use_async == "yes" -%}
- Async/await support
{%- endif %}
{% if cookiecutter.use_pydantic == "yes" -%}
- Pydantic data validation
{%- endif %}

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

This project is licensed under the {{ cookiecutter.license }} License.
