# ADR-0006: Use Hatchling as Build Backend

**Status:** Accepted

**Date:** 2026-02-14

**Deciders:** Template Authors

## Context

Python projects need a PEP 517-compliant build backend to create distributable packages. Options include setuptools, hatchling, flit, and poetry-core.

## Decision

Use **hatchling** as the build backend.

## Rationale

- **Modern**: Built for PEP 517/518 standards
- **Simple**: Minimal configuration needed
- **Fast**: Quick builds
- **No setup.py**: Pure pyproject.toml configuration
- **Good defaults**: Sensible behavior out of the box
- **Maintained**: Part of the Hatch project ecosystem

## Consequences

### Positive

- Clean pyproject.toml configuration
- No legacy setup.py needed
- Fast build times
- Good integration with modern tools
- Simple to understand

### Negative

- Less feature-rich than setuptools
- Smaller community than setuptools
- Fewer advanced build options

### Neutral

- Configuration in pyproject.toml
- Works seamlessly with uv

## Alternatives Considered

### Alternative 1: setuptools

Most widely used, but more complex configuration and legacy baggage.

### Alternative 2: flit

Very simple, but limited features for complex projects.

### Alternative 3: poetry-core

Good, but tied to poetry ecosystem.

## References

- [Hatchling Documentation](https://hatch.pypa.io/latest/)
- [PEP 517](https://peps.python.org/pep-0517/)
- [PEP 518](https://peps.python.org/pep-0518/)

## Notes

Hatchling provides a modern, simple build backend that works well with uv and follows Python packaging standards.
