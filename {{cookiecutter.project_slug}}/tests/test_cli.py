{% if cookiecutter.project_type == "python_cli" -%}
"""Tests for CLI module."""

from unittest.mock import MagicMock, patch

from {{ cookiecutter.package_name }}.cli import cmd_config, cmd_init, cmd_run, main


def test_cmd_init(tmp_path, capsys):
    """Test init command."""
    args = MagicMock(path=str(tmp_path / "new_project"))
    result = cmd_init(args)
    assert result == 0
    assert (tmp_path / "new_project").exists()
    captured = capsys.readouterr()
    assert "Initialized" in captured.out


def test_cmd_run(capsys):
    """Test run command."""
    args = MagicMock(input="test")
    result = cmd_run(args)
    assert result == 0
    captured = capsys.readouterr()
    assert "TEST" in captured.out


def test_cmd_config(capsys):
    """Test config command without key."""
    args = MagicMock(key=None)
    result = cmd_config(args)
    assert result == 0
    captured = capsys.readouterr()
    assert "Configuration" in captured.out


def test_cmd_config_with_key(capsys, monkeypatch):
    """Test config command with specific key."""
    monkeypatch.setenv("TEST_KEY", "test_value")
    args = MagicMock(key="test_key")
    result = cmd_config(args)
    assert result == 0
    captured = capsys.readouterr()
    assert "test_key" in captured.out


def test_main_no_command(capsys):
    """Test main with no command."""
    with patch("sys.argv", ["{{ cookiecutter.package_name }}"]):
        result = main()
        assert result == 1


def test_main_init_command(tmp_path):
    """Test main with init command."""
    with patch("sys.argv", ["{{ cookiecutter.package_name }}", "init", str(tmp_path / "test")]):
        result = main()
        assert result == 0


def test_main_run_command():
    """Test main with run command."""
    with patch("sys.argv", ["{{ cookiecutter.package_name }}", "run", "hello"]):
        result = main()
        assert result == 0
{%- endif %}
