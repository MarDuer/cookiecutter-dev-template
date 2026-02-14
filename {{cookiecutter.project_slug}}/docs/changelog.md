# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [{{ cookiecutter.version }}] - {{ "now" | strftime("%Y-%m-%d") }}

### Added
- Initial release
{% if cookiecutter.project_type == "python_cli" -%}
- CLI with init, run, and config commands
- Configuration management
- Structured logging
{%- elif cookiecutter.project_type == "python_library" -%}
- Core library functionality
- Configuration management
{%- elif cookiecutter.project_type == "c_tricore" -%}
- Cyclic handler pattern
- TriCore TC375 support
- MISRA-C:2012 compliance
{%- endif %}
