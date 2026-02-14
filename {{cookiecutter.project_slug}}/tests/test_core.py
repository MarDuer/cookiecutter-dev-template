{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
"""Tests for core module."""

import pytest

from {{ cookiecutter.package_name }}.core import Core


@pytest.fixture
def core():
    """Create Core instance."""
    return Core(config={"test": "value"})


def test_core_init(core):
    """Test Core initialization."""
    assert core.config == {"test": "value"}


def test_process(core):
    """Test data processing."""
    result = core.process("hello")
    assert result == "HELLO"


@pytest.mark.parametrize("input_data,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("test123", "TEST123"),
    ("", ""),
])
def test_process_various_inputs(core, input_data, expected):
    """Test processing various inputs."""
    assert core.process(input_data) == expected
{%- endif %}
