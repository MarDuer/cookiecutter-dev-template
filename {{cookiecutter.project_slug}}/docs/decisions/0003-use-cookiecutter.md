# ADR-0003: Use Cookiecutter for Template Customization

**Status:** Accepted

**Date:** 2026-02-14

**Deciders:** Template Authors

## Context

We need a way to create customizable project templates that can generate different types of projects (Python CLI, Library, C/TriCore) with various optional features.

## Decision

Use **Cookiecutter** as the template engine.

## Rationale

- **Mature**: Well-established tool with large community
- **Flexible**: Jinja2 templating allows complex conditionals
- **Hooks**: Pre/post-generation hooks for automation
- **Cross-platform**: Works on Windows, Linux, macOS
- **Language-agnostic**: Can template any file type
- **Interactive**: Prompts users for configuration

## Consequences

### Positive

- Proven, stable templating solution
- Rich ecosystem of existing templates
- Good documentation and community support
- Powerful Jinja2 templating
- Automation via hooks

### Negative

- Jinja2 syntax can be verbose
- Some edge cases with file naming
- Requires Python to run

### Neutral

- Configuration in cookiecutter.json
- Learning curve for Jinja2 templating

## Alternatives Considered

### Alternative 1: Copier

Modern alternative with better update support, but smaller community and less mature.

### Alternative 2: Yeoman

JavaScript-based, more complex, not Python-native.

### Alternative 3: Custom scripts

More control but requires maintaining custom tooling.

## References

- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

## Notes

Cookiecutter's maturity and Python-native approach make it the best choice for a Python-focused template with multi-language support.
