# ADR-0004: Use Just for Task Automation

**Status:** Accepted

**Date:** 2026-02-14

**Deciders:** Template Authors

## Context

Projects need a task runner for common operations (testing, linting, building, documentation). Options include Make, npm scripts, task, and just.

## Decision

Use **just** as the task automation tool.

## Rationale

- **Simple**: Easy-to-read syntax, no Make quirks
- **Cross-platform**: Works on Windows, Linux, macOS
- **Modern**: Built for modern development workflows
- **Fast**: Written in Rust, minimal overhead
- **Flexible**: Supports parameters, dependencies, and conditionals
- **Self-documenting**: `just --list` shows all commands

## Consequences

### Positive

- Clean, readable justfile syntax
- No tab vs space issues (unlike Make)
- Built-in command listing
- Cross-platform without workarounds
- Easy to learn

### Negative

- Less ubiquitous than Make
- Requires installation (not system default)
- Smaller community than Make

### Neutral

- New tool for developers familiar with Make
- Configuration in justfile

## Alternatives Considered

### Alternative 1: Make

Universal, but has quirks (tabs, platform differences), harder to read.

### Alternative 2: npm scripts

JavaScript-centric, requires Node.js, not ideal for Python/C projects.

### Alternative 3: task (go-task)

Similar to just, but less adoption and Go-based.

## References

- [just Documentation](https://github.com/casey/just)
- [just vs Make](https://github.com/casey/just#what-are-the-idiosyncrasies-of-make-that-just-avoids)

## Notes

just's simplicity and cross-platform support make it ideal for modern development. We provide a PowerShell script for Windows installation.
