{% if cookiecutter.project_type == "c_tricore" -%}
#!/bin/bash
# MISRA-C:2012 compliance check using Cppcheck

echo "Running MISRA-C:2012 compliance check..."

cppcheck \
    --addon=misra \
    --enable=all \
    --suppress=missingIncludeSystem \
    --inline-suppr \
    --std=c11 \
    -I src \
    -I startup \
    src/*.c startup/*.c

echo "MISRA check complete!"
{%- endif %}
