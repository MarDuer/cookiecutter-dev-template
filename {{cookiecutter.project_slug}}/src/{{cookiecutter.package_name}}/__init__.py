{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
"""{{ cookiecutter.project_name }}."""

__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"
{%- endif %}
