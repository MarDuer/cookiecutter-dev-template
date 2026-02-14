# ADR-0002: Use Ruff and isort for Linting and Formatting

**Status:** Accepted

**Date:** 2026-02-14

**Deciders:** Template Authors

## Context

Python code quality requires linting and formatting tools. Traditional options include Black, Flake8, pylint, and isort. We need fast, comprehensive tools that work well together.

## Decision

Use **Ruff** for linting and formatting, plus **isort** for import sorting.

## Rationale

- **Ruff**: Extremely fast (10-100x faster than alternatives), replaces multiple tools (Flake8, Black, pyupgrade), written in Rust
- **isort**: Specialized import sorting, well-established, integrates with Ruff
- **Comprehensive**: Covers linting, formatting, and code modernization
- **Configurable**: Extensive rule sets (pycodestyle, pydocstyle, etc.)
- **Active**: Maintained by Astral, same team as uv

## Consequences

### Positive

- Single tool (ruff) replaces Black, Flake8, pyupgrade
- Extremely fast execution
- Consistent code style across projects
- Auto-fix capabilities
- Good VS Code integration

### Negative

- Ruff is relatively new (less mature than Black/Flake8)
- Some edge cases may differ from Black
- Requires both ruff and isort (not fully consolidated)

### Neutral

- Configuration in pyproject.toml
- Learning curve for ruff-specific rules

## Alternatives Considered

### Alternative 1: Black + Flake8 + isort

Traditional, well-tested, but slower and requires three separate tools.

### Alternative 2: Ruff only

Ruff can handle imports, but isort is more specialized and configurable for import sorting.

### Alternative 3: pylint

More comprehensive but significantly slower and more opinionated.

## References

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [isort Documentation](https://pycqa.github.io/isort/)

## Notes

Ruff's speed makes it ideal for pre-commit hooks and CI/CD pipelines. The combination with isort provides the best balance of speed and functionality.
