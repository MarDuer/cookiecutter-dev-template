{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
# Multi-stage build for {{ cookiecutter.project_name }}

# Builder stage
FROM python:{{ cookiecutter.python_version }}-slim AS builder

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.toml ./
COPY src ./src

# Install dependencies
RUN uv venv && \
    uv pip install --no-cache -e .

# Runtime stage
FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

{% if cookiecutter.project_type == "python_cli" -%}
# Set entrypoint
ENTRYPOINT ["{{ cookiecutter.package_name }}"]
CMD ["--help"]
{%- else -%}
# Default command
CMD ["python", "-m", "{{ cookiecutter.package_name }}"]
{%- endif %}

# Health check (optional)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import {{ cookiecutter.package_name }}" || exit 1

# Labels
LABEL maintainer="{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>" \
      version="{{ cookiecutter.version }}" \
      description="{{ cookiecutter.project_short_description }}"
{%- endif %}
