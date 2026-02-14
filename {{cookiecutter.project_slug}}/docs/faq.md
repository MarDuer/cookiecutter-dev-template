# Frequently Asked Questions

## General

### What is {{ cookiecutter.project_name }}?

{{ cookiecutter.project_short_description }}

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
### What Python versions are supported?

Python {{ cookiecutter.python_version }} and above.

### How do I report a bug?

Please open an issue on [GitHub](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues).

{%- elif cookiecutter.project_type == "c_tricore" -%}
### What toolchain is required?

HighTec Free GCC toolchain for TriCore TC375.

### Is this MISRA-C compliant?

Yes, the code follows MISRA-C:2012 guidelines.

{%- endif %}

## Contributing

### How can I contribute?

See the [Contributing](contributing.md) guide for details.

### What is the development workflow?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request
