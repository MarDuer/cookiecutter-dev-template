# ADR-0005: Use MkDocs Material for Documentation

**Status:** Accepted

**Date:** 2026-02-14

**Deciders:** Template Authors

## Context

Projects need comprehensive documentation that is easy to write, beautiful to read, and simple to deploy. Options include Sphinx, MkDocs, Docusaurus, and GitBook.

## Decision

Use **MkDocs with Material theme** for documentation.

## Rationale

- **Simple**: Markdown-based, easy to write
- **Beautiful**: Material theme is modern and professional
- **Fast**: Quick builds and live reload
- **Features**: Search, navigation, code highlighting, Mermaid diagrams
- **Python-native**: Integrates well with Python projects
- **mkdocstrings**: Auto-generates API docs from docstrings
- **GitHub Pages**: Easy deployment

## Consequences

### Positive

- Beautiful, professional documentation
- Easy to write (Markdown)
- Fast build times
- Excellent search functionality
- Mobile-responsive
- Mermaid diagram support
- Auto-generated API documentation

### Negative

- Less extensible than Sphinx
- Smaller plugin ecosystem than Sphinx
- Material theme has many options (can be overwhelming)

### Neutral

- Configuration in mkdocs.yml
- Google docstring style for API docs

## Alternatives Considered

### Alternative 1: Sphinx

More powerful, but complex configuration, reStructuredText is harder to write.

### Alternative 2: Docusaurus

Modern, React-based, but JavaScript-centric and heavier.

### Alternative 3: GitBook

Beautiful, but commercial product with limitations.

## References

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [mkdocstrings](https://mkdocstrings.github.io/)

## Notes

MkDocs Material provides the best balance of simplicity, beauty, and functionality for Python projects. The Material theme is widely adopted and actively maintained.
