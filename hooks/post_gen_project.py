#!/usr/bin/env python3
"""Post-generation hook for cookiecutter template."""
import os
import shutil
import subprocess
import sys
from pathlib import Path

project_type = "{{ cookiecutter.project_type }}"
use_devcontainer = "{{ cookiecutter.use_devcontainer }}"

print("🔧 Running post-generation setup...")

# Remove files based on project type
if project_type == "c_tricore":
    # Remove Python package files but keep build tools
    files_to_remove = [
        "src/{{ cookiecutter.package_name }}",
        "tests/test_cli.py",
        "tests/test_config.py",
        "tests/test_core.py",
        "tests/conftest.py",
        "docs/api.md",
    ]
    for item in files_to_remove:
        path = Path(item)
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            print(f"  ✓ Removed {item}")

elif project_type in ["python_cli", "python_library"]:
    # Remove C-specific files
    files_to_remove = [
        "SConstruct",
        "linker",
        "startup",
        "scripts/misra_check.sh",
    ]
    for item in files_to_remove:
        path = Path(item)
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            print(f"  ✓ Removed {item}")

# Remove devcontainer if not needed
if use_devcontainer == "no":
    devcontainer_dir = Path(".devcontainer")
    if devcontainer_dir.exists():
        shutil.rmtree(devcontainer_dir)
        print("  ✓ Removed .devcontainer")

# Initialize git repository
try:
    subprocess.run(["git", "init"], check=True, capture_output=True)
    print("  ✓ Initialized git repository")
except subprocess.CalledProcessError:
    print("  ⚠ Failed to initialize git repository")

# Initialize Git LFS
try:
    subprocess.run(["git", "lfs", "install"], check=True, capture_output=True)
    print("  ✓ Initialized Git LFS")
except (subprocess.CalledProcessError, FileNotFoundError):
    print("  ⚠ Git LFS not found. Install it from: https://git-lfs.github.com/")

# Set git commit template
try:
    subprocess.run(
        ["git", "config", "commit.template", ".gitmessage"],
        check=True,
        capture_output=True
    )
    print("  ✓ Set git commit template")
except subprocess.CalledProcessError:
    print("  ⚠ Failed to set git commit template")

# Setup Python environment for all project types
print("\n📦 Setting up Python environment...")

# Check if uv is available
try:
    subprocess.run(["uv", "--version"], check=True, capture_output=True)
except (subprocess.CalledProcessError, FileNotFoundError):
    print("  ⚠ uv not found. Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh")
    print("  Skipping virtual environment setup")
    sys.exit(0)

# Create virtual environment
try:
    subprocess.run(["uv", "venv"], check=True)
    print("  ✓ Created virtual environment")
except subprocess.CalledProcessError:
    print("  ⚠ Failed to create virtual environment")

# Install dependencies based on project type
if project_type in ["python_cli", "python_library"]:
    try:
        subprocess.run(
            ["uv", "pip", "install", "-e", ".[dev,test,docs]"],
            check=True
        )
        print("  ✓ Installed dependencies")
    except subprocess.CalledProcessError:
        print("  ⚠ Failed to install dependencies")

    # Install pre-commit hooks
    try:
        subprocess.run(
            ["uv", "run", "pre-commit", "install"],
            check=True,
            capture_output=True
        )
        print("  ✓ Installed pre-commit hooks")
    except subprocess.CalledProcessError:
        print("  ⚠ Failed to install pre-commit hooks")

elif project_type == "c_tricore":
    # Install SCons and development tools for C projects
    try:
        subprocess.run(
            ["uv", "pip", "install", "scons", "cppcheck"],
            check=True
        )
        print("  ✓ Installed SCons and build tools")
    except subprocess.CalledProcessError:
        print("  ⚠ Failed to install build tools")

    # Install pre-commit hooks
    try:
        subprocess.run(
            ["uv", "run", "pre-commit", "install"],
            check=True,
            capture_output=True
        )
        print("  ✓ Installed pre-commit hooks")
    except subprocess.CalledProcessError:
        print("  ⚠ Failed to install pre-commit hooks")

print("\n✨ Project setup complete!")
print("\nNext steps:")
if project_type in ["python_cli", "python_library"]:
    print("  1. Review and customize .env file")
    print("  2. Run tests: just test")
    print("  3. View docs: just docs-serve")
elif project_type == "c_tricore":
    print("  1. Configure toolchain paths")
    print("  2. Build project: just build")
    print("  3. Run tests: just test")
