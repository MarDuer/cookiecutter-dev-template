{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
"""Tests for configuration module."""

import os
import pytest
from {{ cookiecutter.package_name }}.config import Config, ConfigurationError


def test_config_init(temp_config_dir):
    """Test Config initialization."""
    config = Config(config_dir=temp_config_dir)
    assert config.config_dir == temp_config_dir


def test_load_yaml(config, sample_yaml_config):
    """Test loading YAML configuration."""
    data = config.load_yaml("test.yaml")
    assert data["key"] == "value"
    assert data["number"] == 42


def test_load_json(config, sample_json_config):
    """Test loading JSON configuration."""
    data = config.load_json("test.json")
    assert data["key"] == "value"
    assert data["number"] == 42


def test_load_yaml_missing_file(config):
    """Test loading non-existent YAML file."""
    with pytest.raises(ConfigurationError):
        config.load_yaml("missing.yaml")


def test_get_with_default(config):
    """Test getting value with default."""
    assert config.get("missing_key", "default") == "default"


def test_get_from_env(config, monkeypatch):
    """Test getting value from environment."""
    monkeypatch.setenv("TEST_KEY", "env_value")
    assert config.get("test_key") == "env_value"


def test_set_and_get(config):
    """Test setting and getting values."""
    config.set("test_key", "test_value")
    assert config.get("test_key") == "test_value"


@pytest.mark.parametrize("key,value", [
    ("string_key", "string_value"),
    ("int_key", 42),
    ("bool_key", True),
])
def test_set_various_types(config, key, value):
    """Test setting various value types."""
    config.set(key, value)
    assert config.get(key) == value
{%- endif %}
