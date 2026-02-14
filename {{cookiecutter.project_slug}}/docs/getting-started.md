# Getting Started

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
## Prerequisites

- Python {{ cookiecutter.python_version }}+
- uv (Python package manager)

## Installation

### Using uv (recommended)

```bash
uv pip install {{ cookiecutter.package_name }}
```

### From source

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
just install
```

{% if cookiecutter.project_type == "python_cli" -%}
## Basic Usage

### Initialize a project

```bash
{{ cookiecutter.package_name }} init my-project
```

### Run the application

```bash
{{ cookiecutter.package_name }} run
```

### View configuration

```bash
{{ cookiecutter.package_name }} config
```
{%- endif %}

## Configuration

Create a `.env` file in your project root:

```bash
cp .env.template .env
```

Edit the `.env` file with your settings.

{%- elif cookiecutter.project_type == "c_tricore" -%}
## Prerequisites

- HighTec Free GCC toolchain for TriCore
- SCons build system
- Python 3.10+ (for build tools)

## Installation

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
```

## Building

```bash
# Debug build
just build

# Release build
just build-release
```

## Running Tests

```bash
just test
```
{%- endif %}

## Next Steps

- Read the [Architecture](architecture.md) documentation
- Check out [Examples](examples.md)
- Review [Contributing](contributing.md) guidelines
