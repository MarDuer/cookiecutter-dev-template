---
name: Bug Report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

## Bug Description

<!-- A clear and concise description of what the bug is -->

## Steps to Reproduce

1. 
2. 
3. 
4. 

## Expected Behavior

<!-- What you expected to happen -->

## Actual Behavior

<!-- What actually happened -->

## Environment

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
- **Python version:** 
- **Package version:** 
- **OS:** 
- **Installation method:** (pip, uv, source)
{%- elif cookiecutter.project_type == "c_tricore" -%}
- **Toolchain version:** 
- **Target:** 
- **OS:** 
{%- endif %}

## Additional Context

<!-- Add any other context about the problem here -->

## Possible Solution

<!-- Optional: suggest a fix or reason for the bug -->

## Logs/Screenshots

<!-- If applicable, add logs or screenshots to help explain your problem -->

```
<!-- Paste relevant logs here -->
```
