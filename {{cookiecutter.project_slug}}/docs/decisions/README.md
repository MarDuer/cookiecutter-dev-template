# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for {{ cookiecutter.project_name }}.

## What is an ADR?

An Architecture Decision Record (ADR) captures an important architectural decision made along with its context and consequences.

## Format

We use a simple format with the following sections:
- **Status**: Proposed, Accepted, Deprecated, Superseded
- **Date**: When the decision was made
- **Context**: The issue or problem being addressed
- **Decision**: What was decided
- **Rationale**: Why this decision was made
- **Consequences**: Positive, negative, and neutral outcomes
- **Alternatives**: Other options that were considered

## Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [0000](0000-template.md) | ADR Template | Template | - |
| [0001](0001-use-uv-for-package-management.md) | Use uv for Python Package Management | Accepted | 2026-02-14 |
| [0002](0002-use-ruff-and-isort.md) | Use Ruff and isort for Linting | Accepted | 2026-02-14 |
| [0003](0003-use-cookiecutter.md) | Use Cookiecutter for Templates | Accepted | 2026-02-14 |
| [0004](0004-use-just-for-task-automation.md) | Use Just for Task Automation | Accepted | 2026-02-14 |
| [0005](0005-use-mkdocs-material.md) | Use MkDocs Material for Documentation | Accepted | 2026-02-14 |
| [0006](0006-use-hatchling-build-backend.md) | Use Hatchling as Build Backend | Accepted | 2026-02-14 |
| [0007](0007-precommit-strategy.md) | Pre-commit Strategy (Client vs Server) | Accepted | 2026-02-14 |
| [0008](0008-modern-type-hints.md) | Modern Python Type Hints (3.10+) | Accepted | 2026-02-14 |

## Creating New ADRs

1. Copy `0000-template.md`
2. Rename with next number: `NNNN-short-title.md`
3. Fill in all sections
4. Update this index
5. Link from relevant documentation

## References

- [ADR GitHub Organization](https://adr.github.io/)
- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
