# ADR-0007: Pre-commit Strategy - Client vs Server

**Status:** Accepted

**Date:** 2026-02-14

**Deciders:** Template Authors

## Context

Code quality checks can run locally (pre-commit hooks) or on CI/CD servers. We need to balance developer experience with code quality enforcement.

## Decision

**Client-side (mandatory):**
- Commit message validation (commitizen)
- Branch name validation
- Basic file checks (trailing whitespace, YAML syntax)
- Ruff formatting and linting (auto-fix)
- isort (auto-fix)

**Client-side (optional via just commands):**
- mypy type checking
- pytest test suite

**Server-side (GitHub Actions):**
- All client-side checks
- Full test suite with coverage
- Type checking
- Security scanning
- Documentation builds

## Rationale

- **Fast feedback**: Auto-fix issues locally before commit
- **Developer freedom**: Heavy checks (tests, mypy) optional locally
- **Enforcement**: All checks run on CI/CD
- **Flexibility**: Developers can run `just ci` to simulate CI locally

## Consequences

### Positive

- Fast local commits (only essential checks)
- Developers can iterate quickly
- All code is validated on server
- Optional local validation available
- Auto-fix reduces manual work

### Negative

- Developers might push code that fails CI
- Need to maintain two check configurations
- Some duplication between local and CI

### Neutral

- Requires discipline to run optional checks
- CI provides safety net

## Alternatives Considered

### Alternative 1: All checks locally

Slow commits, frustrating developer experience.

### Alternative 2: No local checks

Fast commits, but many CI failures and wasted time.

### Alternative 3: Minimal local, minimal CI

Fast but risky, quality issues slip through.

## References

- [pre-commit Documentation](https://pre-commit.com/)
- [GitHub Actions](https://docs.github.com/en/actions)

## Notes

This strategy balances speed and quality. Developers can always run `just ci` to validate everything locally before pushing.
