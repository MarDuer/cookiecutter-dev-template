# ADR-0001: Use uv for Python Package Management

**Status:** Accepted

**Date:** 2026-02-14

**Deciders:** Template Authors

## Context

Python package management has several options: pip, poetry, pipenv, pdm, and uv. We need a fast, reliable package manager that supports modern Python workflows and integrates well with CI/CD.

## Decision

Use **uv** as the primary Python package manager for this template.

## Rationale

- **Speed**: uv is written in Rust and is 10-100x faster than pip
- **Modern**: Built for Python 3.10+ with modern features
- **Standards-compliant**: Uses pyproject.toml and follows PEP standards
- **Integrated**: Handles venv creation, dependency resolution, and installation
- **Active development**: Maintained by Astral (creators of ruff)
- **Simple**: Single tool replaces pip, pip-tools, virtualenv

## Consequences

### Positive

- Extremely fast dependency installation
- Simplified toolchain (one tool for multiple tasks)
- Better dependency resolution
- Native support in GitHub Actions
- Cross-platform compatibility

### Negative

- Relatively new tool (less mature than pip)
- Smaller community compared to pip/poetry
- Requires users to install uv

### Neutral

- Users familiar with pip need to learn uv commands
- Configuration in uv.toml and pyproject.toml

## Alternatives Considered

### Alternative 1: pip + pip-tools

Traditional approach, widely known, but slow and requires multiple tools.

### Alternative 2: Poetry

Popular, feature-rich, but slower than uv and more opinionated about project structure.

### Alternative 3: PDM

Modern and fast, but less adoption than poetry and uv.

## References

- [uv Documentation](https://github.com/astral-sh/uv)
- [uv Performance Benchmarks](https://astral.sh/blog/uv)

## Notes

uv is rapidly becoming the standard for modern Python projects and is recommended by many in the Python community.
