#!/usr/bin/env python3
"""Pre-generation hook for cookiecutter template validation."""
import re
import sys

project_slug = "{{ cookiecutter.project_slug }}"
python_version = "{{ cookiecutter.python_version }}"
project_type = "{{ cookiecutter.project_type }}"

# Validate project slug based on project type
if project_type in ["python_cli", "python_library"]:
    # Python projects need valid Python module names
    if not re.match(r"^[a-z][a-z0-9_]*$", project_slug):
        print(f"ERROR: '{project_slug}' is not a valid Python module name.")
        print("Must start with a letter and contain only lowercase letters, numbers, and underscores.")
        sys.exit(1)
elif project_type == "c_tricore":
    # C projects need valid C identifiers (allow uppercase)
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", project_slug):
        print(f"ERROR: '{project_slug}' is not a valid C identifier.")
        print("Must start with a letter and contain only letters, numbers, and underscores.")
        sys.exit(1)

# Validate Python version for Python projects
if project_type in ["python_cli", "python_library"]:
    valid_versions = ["3.10", "3.11", "3.12", "3.13", "3.14"]
    if python_version not in valid_versions:
        print(f"ERROR: Python version '{python_version}' is not supported.")
        print(f"Supported versions: {', '.join(valid_versions)}")
        sys.exit(1)

print(f"✓ Validation passed for project: {project_slug}")
