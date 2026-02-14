{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
# API Reference

This page provides detailed API documentation for {{ cookiecutter.project_name }}.

## Core Module

::: {{ cookiecutter.package_name }}.core
    options:
      show_root_heading: true
      show_source: true
      heading_level: 3

## Configuration

::: {{ cookiecutter.package_name }}.config
    options:
      show_root_heading: true
      show_source: true
      heading_level: 3

## CLI Interface

::: {{ cookiecutter.package_name }}.cli
    options:
      show_root_heading: true
      show_source: true
      heading_level: 3

## Exceptions

::: {{ cookiecutter.package_name }}.exceptions
    options:
      show_root_heading: true
      show_source: true
      heading_level: 3

## Usage Examples

### Basic Usage

```python
from {{ cookiecutter.package_name }} import process

# Process some data
result = process("input data")
print(result)
```

### Configuration Management

```python
from {{ cookiecutter.package_name }}.config import Config

# Initialize configuration
config = Config()

# Set values
config.set("key", "value")

# Get values
value = config.get("key")
```

### Error Handling

```python
from {{ cookiecutter.package_name }} import process
from {{ cookiecutter.package_name }}.exceptions import ValidationError

try:
    result = process(invalid_data)
except ValidationError as e:
    print(f"Validation failed: {e}")
```
{%- endif %}
