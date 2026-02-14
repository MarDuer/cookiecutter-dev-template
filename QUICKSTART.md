# Quick Start Guide - Testing the Template

## Prerequisites

```bash
# Install uv (includes uvx)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Generate a Test Project

```bash
# Using uvx (recommended - no need to install cookiecutter)
uvx --python 3.14 cookiecutter /home/markus/JustForFun/cookiecutter-dev-template

# Or if you have cookiecutter installed
cd /home/markus/JustForFun/cookiecutter-dev-template
cookiecutter .
```

### Example Inputs

When prompted, use these values for testing:

```
project_name: My Test Tool
project_slug: my_test_tool (auto-generated)
package_name: my_test_tool (auto-generated)
project_short_description: A test CLI tool
author_name: Your Name
author_email: your.email@example.com
github_username: yourusername
project_type: python_cli
python_version: 3.12
license: MIT
use_async: no
use_pydantic: no
use_profiling: no
use_integration_tests: no
use_devcontainer: no
use_stale_bot: no
use_pypi_deployment: yes
coverage_service: codecov
package_index: pypi
publishing_approval: manual
version: 0.1.0
```

## Verify the Generated Project

```bash
cd my_test_tool

# Check structure
ls -la

# Verify Python environment was created
ls -la .venv

# Run tests
just test

# Check linting
just lint

# View documentation
just docs-serve
# Open http://127.0.0.1:8000 in browser

# Try the CLI
uv run my_test_tool --help
uv run my_test_tool init test-project
uv run my_test_tool run "hello world"
uv run my_test_tool config
```

## Expected Output

### Directory Structure
```
my_test_tool/
├── .github/          (empty for now)
├── .venv/            ✓ Created by post-gen hook
├── docs/             ✓ Complete documentation
├── etc/              ✓ Config files
├── scripts/          ✓ Helper scripts
├── src/              ✓ Source code
│   └── my_test_tool/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── config.py
│       ├── core.py
│       └── exceptions.py
├── tests/            ✓ Test suite
├── .cz.toml          ✓ Commitizen config
├── .editorconfig     ✓ Editor config
├── .env.template     ✓ Environment template
├── .gitignore        ✓ Git ignore
├── .gitmessage       ✓ Commit template
├── .pre-commit-config.yaml  ✓ Pre-commit hooks
├── justfile          ✓ Task automation
├── LICENSE           ✓ MIT License
├── mkdocs.yml        ✓ Docs config
├── pyproject.toml    ✓ Python config
├── README.md         ✓ Project README
└── uv.toml           ✓ UV config
```

### Test Output
```bash
$ just test
============================= test session starts ==============================
collected 15 items

tests/test_cli.py ........                                               [ 53%]
tests/test_config.py .....                                               [ 86%]
tests/test_core.py ..                                                    [100%]

---------- coverage: platform linux, python 3.12.0 -----------
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
src/my_test_tool/__init__.py            3      0   100%
src/my_test_tool/cli.py                50      2    96%   45-46
src/my_test_tool/config.py             35      1    97%   67
src/my_test_tool/core.py               12      0   100%
src/my_test_tool/exceptions.py          6      0   100%
-----------------------------------------------------------------
TOTAL                                 106      3    97%

============================== 15 passed in 0.45s ===============================
```

### CLI Output
```bash
$ uv run my_test_tool --help
usage: my_test_tool [-h] [--version] [-v] {init,run,config} ...

A test CLI tool

positional arguments:
  {init,run,config}  Available commands
    init             Initialize project
    run              Run application
    config           Show configuration

options:
  -h, --help         show this help message and exit
  --version          show program's version number and exit
  -v, --verbose      Enable verbose output

$ uv run my_test_tool run "hello world"
Result: HELLO WORLD
```

## Troubleshooting

### uv not found
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# Restart terminal
```

### Pre-commit hooks not installed
```bash
uv run pre-commit install
```

### Tests failing
```bash
# Reinstall dependencies
just install

# Run with verbose output
just test -v
```

## Next Steps

1. **Customize the generated project**
   - Edit `.env` file
   - Modify `src/my_test_tool/core.py`
   - Add your business logic

2. **Make a commit**
   ```bash
   git add .
   git commit
   # The commit template will guide you
   ```

3. **Build documentation**
   ```bash
   just docs-build
   # Output in site/
   ```

4. **Run all CI checks**
   ```bash
   just ci
   ```

## Success Criteria

✅ Project generates without errors
✅ Virtual environment is created
✅ Dependencies are installed
✅ All tests pass
✅ Documentation builds successfully
✅ CLI commands work
✅ Pre-commit hooks are installed

If all of these work, the template is functioning correctly!
