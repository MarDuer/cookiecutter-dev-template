# Integration Testing Guide

This document describes how to test the cookiecutter template to ensure all features work correctly.

## Test Matrix

| Project Type | Python Version | Optional Features | Platform |
|--------------|----------------|-------------------|----------|
| python_cli   | 3.12          | None              | Linux    |
| python_cli   | 3.14          | async, pydantic   | Linux    |
| python_library | 3.12        | None              | Linux    |
| c_tricore    | N/A           | N/A               | Linux    |

## Automated Testing

Run the integration test script:

```bash
./scripts/test_template.sh
```

This script will:
1. Generate projects with different configurations
2. Verify file structure
3. Run tests in generated projects
4. Check documentation builds
5. Verify Docker builds
6. Clean up test projects

## Manual Testing Checklist

### 1. Template Generation

- [ ] Generate Python CLI project
- [ ] Generate Python Library project
- [ ] Generate C/TriCore project
- [ ] Verify all files are created
- [ ] Check cookiecutter variable substitution

### 2. Python CLI Project

```bash
uvx --python 3.14 cookiecutter . --no-input project_type=python_cli
cd my_project
```

- [ ] Virtual environment created (`.venv/`)
- [ ] Dependencies installed
- [ ] Pre-commit hooks installed
- [ ] Git repository initialized

**Run Commands:**
- [ ] `just test` - All tests pass
- [ ] `just lint` - No linting errors
- [ ] `just typecheck` - No type errors
- [ ] `just format` - Code formatted
- [ ] `just docs-serve` - Documentation serves
- [ ] `just docs-build` - Documentation builds
- [ ] `just ci` - All CI checks pass
- [ ] `just docker-build` - Docker image builds
- [ ] `just docker-run` - Container runs

**CLI Commands:**
- [ ] `uv run my_project --help` - Shows help
- [ ] `uv run my_project init test` - Creates directory
- [ ] `uv run my_project run "hello"` - Processes input
- [ ] `uv run my_project config` - Shows configuration

**Git Operations:**
- [ ] Make a change
- [ ] `git add .`
- [ ] `git commit` - Pre-commit hooks run
- [ ] Commit message template appears

**VS Code:**
- [ ] Open in VS Code
- [ ] Extensions recommended
- [ ] Tasks available (Ctrl+Shift+B)
- [ ] Debugging works (F5)

### 3. Python Library Project

```bash
uvx --python 3.14 cookiecutter . --no-input project_type=python_library
cd my_library
```

- [ ] `just test` - Tests pass
- [ ] `just lint` - No errors
- [ ] `just docs-serve` - Documentation works
- [ ] Import library: `uv run python -c "import my_library"`

### 4. C/TriCore Project

```bash
uvx --python 3.14 cookiecutter . --no-input project_type=c_tricore
cd my_tricore_project
```

**Note:** Requires HighTec GCC toolchain installed

- [ ] `just build` - Project builds (if toolchain available)
- [ ] `just misra` - MISRA check runs
- [ ] `just docs-serve` - Documentation works
- [ ] Verify file structure:
  - [ ] `src/*.c` and `src/*.h` exist
  - [ ] `startup/` directory exists
  - [ ] `linker/tc375_link.ld` exists
  - [ ] `SConstruct` exists

### 5. Optional Features

**Async Support:**
```bash
uvx --python 3.14 cookiecutter . --no-input use_async=yes
```
- [ ] Async code present in generated project
- [ ] pytest-asyncio installed
- [ ] Tests pass

**Pydantic Support:**
```bash
uvx --python 3.14 cookiecutter . --no-input use_pydantic=yes
```
- [ ] Pydantic installed
- [ ] Validation examples present

**Devcontainer:**
```bash
uvx --python 3.14 cookiecutter . --no-input use_devcontainer=yes
```
- [ ] `.devcontainer/devcontainer.json` exists
- [ ] Can open in VS Code Remote Containers

### 6. GitHub Actions

Push generated project to GitHub and verify:

- [ ] Test workflow runs
- [ ] Linting workflow runs
- [ ] Pre-commit workflow runs
- [ ] Documentation deploys to GitHub Pages
- [ ] Docker workflow builds image
- [ ] Dependabot creates PRs
- [ ] CodeQL scans code

### 7. Documentation

- [ ] All documentation pages render correctly
- [ ] API documentation auto-generates
- [ ] Mermaid diagrams render
- [ ] Search works
- [ ] Navigation works
- [ ] Mobile responsive

### 8. Coverage

- [ ] Coverage report generates
- [ ] HTML report viewable
- [ ] Coverage meets threshold (>80%)
- [ ] Coverage badge in README

### 9. Docker

- [ ] `docker build -t test .` - Builds successfully
- [ ] `docker run test` - Runs correctly
- [ ] `docker-compose up` - Services start
- [ ] Image size reasonable (<500MB)

### 10. Cross-Platform

**Windows (WSL2):**
- [ ] Template generates
- [ ] `scripts/setup_windows.ps1` installs just
- [ ] All commands work

**macOS:**
- [ ] Template generates
- [ ] All commands work

**Linux:**
- [ ] Template generates
- [ ] All commands work

## Common Issues

### Issue: uv not found
**Solution:** Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Issue: just not found
**Solution:** Run `scripts/setup_windows.ps1` (Windows) or install just

### Issue: Pre-commit hooks fail
**Solution:** Run `just format` to auto-fix issues

### Issue: Tests fail
**Solution:** Check test output, verify dependencies installed

### Issue: Docker build fails
**Solution:** Check Dockerfile, verify base image available

## Performance Benchmarks

Expected performance:

- Template generation: <5 seconds
- Dependency installation: <30 seconds
- Test suite: <10 seconds
- Documentation build: <5 seconds
- Docker build: <2 minutes

## Regression Testing

After template changes:

1. Run full test suite
2. Generate all project types
3. Verify no breaking changes
4. Update version if needed
5. Update CHANGELOG.md

## Continuous Integration

The template itself should be tested:

- [ ] Cookiecutter JSON validates
- [ ] Jinja2 templates render
- [ ] Hooks execute without errors
- [ ] Generated projects pass CI

## Success Criteria

Template is ready for release when:

- ✅ All project types generate successfully
- ✅ All tests pass in generated projects
- ✅ Documentation builds and deploys
- ✅ Docker images build and run
- ✅ CI/CD pipelines work
- ✅ Cross-platform compatibility verified
- ✅ No critical bugs or issues

## Reporting Issues

If you find issues during testing:

1. Note the exact steps to reproduce
2. Include error messages
3. Specify platform and versions
4. Open an issue on GitHub
5. Tag with `bug` or `testing` label

## Test Results

Document test results:

```
Date: YYYY-MM-DD
Tester: Name
Platform: OS/Version
Python: Version

Results:
- Python CLI: ✅ Pass
- Python Library: ✅ Pass
- C/TriCore: ✅ Pass
- Docker: ✅ Pass
- Documentation: ✅ Pass
- CI/CD: ✅ Pass

Issues Found: None

Notes: All tests passed successfully
```
