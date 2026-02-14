{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
# API Reference

::: {{ cookiecutter.package_name }}
    options:
      show_root_heading: true
      show_source: true
{%- endif %}
