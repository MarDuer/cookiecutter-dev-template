# Troubleshooting

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
## Installation Issues

### uv not found

Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Import errors

Ensure you've installed the package:

```bash
just install
```

## Runtime Issues

### Configuration not loading

Check that your `.env` file exists and is in the correct location.

### Tests failing

Run tests with verbose output:

```bash
just test -v
```

{%- elif cookiecutter.project_type == "c_tricore" -%}
## Build Issues

### Toolchain not found

Ensure HighTec GCC is installed and in your PATH.

### Linker errors

Check the linker script for correct memory addresses.

## Runtime Issues

### Module not initializing

Verify that `ModuleName_Init()` is called before the main loop.

{%- endif %}

## Getting Help

If you can't find a solution here:

1. Check [GitHub Issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)
2. Open a new issue with details
3. Contact the maintainers
