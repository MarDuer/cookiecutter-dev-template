# Contributing to {{ cookiecutter.project_name }}

Thank you for your interest in contributing!

## Development Setup

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
1. Fork and clone the repository
2. Install dependencies:
   ```bash
   just install
   ```
3. Create a branch for your changes
4. Make your changes
5. Run tests and linting:
   ```bash
   just ci
   ```
6. Commit using conventional commits
7. Push and create a pull request

{%- elif cookiecutter.project_type == "c_tricore" -%}
1. Fork and clone the repository
2. Install build tools (SCons, HighTec GCC)
3. Create a branch for your changes
4. Make your changes
5. Build and test:
   ```bash
   just build
   just test
   just misra
   ```
6. Commit using conventional commits
7. Push and create a pull request

{%- endif %}

## Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `build`, `ci`, `perf`, `revert`

## Code Style

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
- Follow PEP 8
- Use type hints
- Write docstrings (Google style)
- Keep functions small and focused
- Write tests for new features

{%- elif cookiecutter.project_type == "c_tricore" -%}
- Follow MISRA-C:2012 guidelines
- Use consistent naming conventions
- Comment complex logic
- Write unit tests

{%- endif %}

## Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review from maintainers

## Questions?

Open an issue or contact the maintainers.
