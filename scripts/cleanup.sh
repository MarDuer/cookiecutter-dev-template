#!/bin/bash
# Clean up all untracked files and directories (cookiecutter artifacts, test projects, etc.)

echo "🧹 Cleaning up template directory..."
echo ""
echo "This will remove all untracked files and directories."
echo "Files in .gitignore will be removed."
echo ""

# Show what will be removed
echo "Files/directories to be removed:"
git clean -ndx
echo ""

read -p "Continue? (y/N) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Remove all untracked files and directories, including ignored ones
    git clean -fdx
    echo "✓ Cleanup complete!"
else
    echo "Cleanup cancelled."
fi
