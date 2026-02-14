{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path
from {{ cookiecutter.package_name }}.config import Config


@pytest.fixture
def temp_config_dir(tmp_path):
    """Create temporary config directory."""
    config_dir = tmp_path / "etc"
    config_dir.mkdir()
    return config_dir


@pytest.fixture
def sample_yaml_config(temp_config_dir):
    """Create sample YAML config file."""
    config_file = temp_config_dir / "test.yaml"
    config_file.write_text("key: value\nnumber: 42\n")
    return config_file


@pytest.fixture
def sample_json_config(temp_config_dir):
    """Create sample JSON config file."""
    config_file = temp_config_dir / "test.json"
    config_file.write_text('{"key": "value", "number": 42}')
    return config_file


@pytest.fixture
def config(temp_config_dir):
    """Create Config instance with temp directory."""
    return Config(config_dir=temp_config_dir)
{%- endif %}
