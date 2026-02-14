# ADR-0008: Modern Python Type Hints (3.10+ Syntax)

**Status:** Accepted

**Date:** 2026-02-14

**Deciders:** Template Authors

## Context

Python type hints have evolved. Python 3.10+ introduced modern syntax (`dict[str, int]` instead of `Dict[str, int]`, `X | None` instead of `Optional[X]`).

## Decision

Use **modern Python 3.10+ type hint syntax** throughout the template.

**Examples:**
- `dict[str, Any]` instead of `Dict[str, Any]`
- `list[str]` instead of `List[str]`
- `X | None` instead of `Optional[X]`
- `X | Y` instead of `Union[X, Y]`

## Rationale

- **Cleaner**: More readable, less imports
- **Standard**: PEP 604 (Python 3.10+) is now standard
- **Future-proof**: This is the direction Python is moving
- **Consistent**: Matches modern Python style guides
- **Simpler**: No need to import from typing for basic types

## Consequences

### Positive

- Cleaner, more readable code
- Fewer imports from typing module
- Follows modern Python standards
- Better IDE support

### Negative

- Requires Python 3.10+ (not compatible with 3.9 and earlier)
- Developers from older Python versions need to learn new syntax

### Neutral

- Template targets Python 3.10+ anyway
- Ruff enforces this with UP rules

## Alternatives Considered

### Alternative 1: Legacy typing syntax

Compatible with older Python, but verbose and outdated.

### Alternative 2: Mix of old and new

Inconsistent and confusing.

## References

- [PEP 604 - Union Types](https://peps.python.org/pep-0604/)
- [PEP 585 - Type Hinting Generics](https://peps.python.org/pep-0585/)

## Notes

Since the template targets Python 3.10+, using modern syntax is the right choice. Ruff's UP rules help enforce this automatically.
