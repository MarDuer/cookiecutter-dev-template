# Contributing to {{ cookiecutter.project_name }}

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/{{ cookiecutter.project_slug }}
   cd {{ cookiecutter.project_slug }}
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
   ```

## Development Setup

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
### Prerequisites

- Python {{ cookiecutter.python_version }}+
- [uv](https://github.com/astral-sh/uv) package manager
- [just](https://github.com/casey/just) command runner

### Installation

```bash
just install
just test  # Verify installation
```

{%- elif cookiecutter.project_type == "c_tricore" -%}
### Prerequisites

- HighTec Free GCC toolchain for TriCore
- SCons build system
- Python 3.10+ (for build tools)

### Installation

```bash
just build
just test
```

{%- endif %}

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
```bash
just format    # Format code
just lint      # Check linting
just typecheck # Type checking
just test      # Run tests
```

{%- elif cookiecutter.project_type == "c_tricore" -%}
```bash
just build     # Build project
just test      # Run tests
just misra     # Check MISRA compliance
```

{%- endif %}

### 3. Commit Changes

We use [Conventional Commits](https://www.conventionalcommits.org/):

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `build`, `ci`, `perf`, `revert`

### 4. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Coding Standards

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
- Follow PEP 8 (enforced by ruff)
- Use type hints for all functions
- Write docstrings (Google style)
- Maximum line length: 100 characters

{%- elif cookiecutter.project_type == "c_tricore" -%}
- Follow MISRA-C:2012 guidelines
- Use consistent naming conventions
- Maximum line length: 120 characters
- Comment complex logic

{%- endif %}

## Testing

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
- Place tests in `tests/` directory
- Name test files `test_*.py`
- Aim for >80% code coverage

```bash
just test       # Run all tests
just test-cov   # Run with coverage
```

{%- elif cookiecutter.project_type == "c_tricore" -%}
- Tests can be added using Unity or other C test frameworks
- Place tests in `tests/` directory

```bash
just build      # Build project
just misra      # Run MISRA checks
```

{%- endif %}

## Documentation

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
```bash
just docs-serve  # Serve locally
just docs-build  # Build static site
```

{%- endif %}

- Update `README.md` for user-facing changes
- Update `docs/` for detailed documentation
- Add examples to `docs/examples.md`

## Pull Request Process

1. Ensure all checks pass
2. Fill out PR template completely
3. Request review from maintainers
4. Address feedback
5. Maintainers will merge when approved

## Questions?

- Open an issue
- Contact maintainers at {{ cookiecutter.author_email }}

## License

By contributing, you agree that your contributions will be licensed under the {{ cookiecutter.license }} License.
