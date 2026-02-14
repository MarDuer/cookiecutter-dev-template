# Python/C Multi-Language Development Template

A comprehensive, production-ready cookiecutter template for developing Python packages/tools and C embedded projects using modern tooling, best practices, and automation.

## Features

### Core Technologies
- **uv** - Fast Python package manager
- **Cookiecutter** - Template customization
- **Just** - Task automation
- **Pre-commit** - Code quality hooks
- **GitHub Actions** - CI/CD pipelines
- **MkDocs Material** - Beautiful documentation
- **Commitizen** - Conventional commits and versioning

### Python Projects
- Ruff (linting/formatting), isort, mypy (type checking), pytest (testing)
- Blueprint CLI tool with argparse (init/run/config subcommands)
- Hybrid library + CLI architecture
- .env file support with priority handling
- Structured logging with YAML configuration
- Comprehensive test examples with fixtures, mocking, parametrize
- Optional: async/await, Pydantic validation, profiling

### C/TriCore Projects
- SCons build system for Infineon TriCore TC375
- Cyclic handler pattern (ModuleName_Init/ReInit/Hdl)
- HighTec Free GCC toolchain
- Linker script with TC375 memory map
- Startup code with trap handlers
- GPIO example
- Unity test framework
- MISRA-C:2012 compliance with Cppcheck

## Quick Start

### Prerequisites

- Python 3.10+
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [uv](https://github.com/astral-sh/uv) (for Python projects)

### Create a New Project

```bash
# Install cookiecutter
pip install cookiecutter

# Generate project from template
cookiecutter https://github.com/{{ cookiecutter.github_username }}/python-package-template

# Or from local template
cookiecutter /path/to/python-package-template
```

Follow the prompts to customize your project.

### Post-Generation

The template automatically:
- Initializes git repository
- Creates virtual environment (Python projects)
- Installs dependencies
- Sets up pre-commit hooks

## Project Types

### Python CLI
Command-line tool with:
- Subcommands (init, run, config)
- Configuration management
- Structured logging

### Python Library
Reusable Python package with:
- Clean API
- Type hints
- Comprehensive documentation

### C/TriCore Embedded
Embedded C project for TriCore TC375 with:
- Cyclic handler pattern
- MISRA-C compliance
- Production-ready structure

## Configuration Options

- **Project type**: Python CLI, Python library, or C/TriCore
- **Python version**: 3.10, 3.11, 3.12, 3.13, 3.14
- **License**: MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, Proprietary
- **Optional features**: Async, Pydantic, profiling, integration tests, devcontainer
- **Coverage service**: Codecov, Coveralls, both, or none
- **Package index**: PyPI, self-hosted, or both

## Development

See [IMPLEMENTATION_PROGRESS.md](IMPLEMENTATION_PROGRESS.md) for current status.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please read the contributing guidelines first.
