# Git Workflow Reference

## Current State

- **Branch**: `develop`
- **Commit**: `505ce19` - "feat: implement critical path for cookiecutter template"
- **Files**: 46 files committed
- **Lines**: 2,373 insertions

## Testing the Template

### 1. Generate a Test Project

```bash
# From the template directory
cd /home/markus/JustForFun/cookiecutter-dev-template
cookiecutter .
```

### 2. Test the Generated Project

```bash
cd <your-generated-project>

# Run tests
just test

# Check linting
just lint

# View docs
just docs-serve

# Try CLI
uv run <package-name> --help
```

### 3. Report Issues

If you find issues, note them down and we'll fix them in the next iteration.

## After Testing

### If Everything Works ✅

```bash
# Switch back to template directory
cd /home/markus/JustForFun/cookiecutter-dev-template

# Continue development on develop branch
git checkout develop

# We can then continue with:
# - GitHub Actions workflows
# - VS Code configuration
# - C/TriCore variant
# - etc.
```

### If Issues Found ❌

```bash
# Switch back to template directory
cd /home/markus/JustForFun/cookiecutter-dev-template

# Stay on develop branch
git checkout develop

# We'll fix issues and make new commits
git add <fixed-files>
git commit -m "fix: <description of fix>"
```

## Branch Strategy

- **`develop`**: Active development branch (current)
- **`main`**: Stable releases (empty for now)

When the template is fully tested and working:
```bash
git checkout main
git merge develop
git tag v0.1.0
```

## Quick Commands

```bash
# Check current branch
git branch

# View commit history
git log --oneline

# See what changed
git show HEAD

# View file tree
git ls-tree -r HEAD --name-only

# Check status
git status
```

## Rollback (if needed)

If something goes wrong during testing:

```bash
# Discard uncommitted changes
git checkout .

# Reset to last commit
git reset --hard HEAD

# Go back to specific commit
git reset --hard 505ce19
```

## Next Steps After Testing

1. **Test the template** - Generate a project and verify all features work
2. **Report findings** - Note any issues or improvements
3. **Continue development** - Add remaining features (GitHub Actions, VS Code, C/TriCore)
4. **Iterate** - Fix issues, add features, test again
5. **Release** - Merge to main when stable

## Contact Points

- Template directory: `/home/markus/JustForFun/cookiecutter-dev-template`
- Documentation: `QUICKSTART.md`, `CRITICAL_PATH_SUMMARY.md`
- Progress tracking: `IMPLEMENTATION_PROGRESS.md`
