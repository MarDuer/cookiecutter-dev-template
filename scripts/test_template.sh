#!/bin/bash
# Automated integration testing for cookiecutter template

set -e

echo "🧪 Starting Template Integration Tests"
echo "======================================"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counter
TESTS_PASSED=0
TESTS_FAILED=0

# Test function
test_project() {
    local project_type=$1
    local project_name=$2
    
    echo ""
    echo "${YELLOW}Testing: $project_type${NC}"
    echo "-----------------------------------"
    
    # Generate project
    echo "Generating project..."
    uvx --python 3.14 cookiecutter . --no-input \
        project_name="$project_name" \
        project_type="$project_type" || {
        echo "${RED}✗ Failed to generate project${NC}"
        ((TESTS_FAILED++))
        return 1
    }
    
    cd "$project_name" || return 1
    
    # Check file structure
    echo "Checking file structure..."
    if [ "$project_type" = "c_tricore" ]; then
        [ -f "SConstruct" ] || { echo "${RED}✗ SConstruct missing${NC}"; ((TESTS_FAILED++)); cd ..; return 1; }
        [ -d "src" ] || { echo "${RED}✗ src/ missing${NC}"; ((TESTS_FAILED++)); cd ..; return 1; }
        [ -d "startup" ] || { echo "${RED}✗ startup/ missing${NC}"; ((TESTS_FAILED++)); cd ..; return 1; }
        [ -d "linker" ] || { echo "${RED}✗ linker/ missing${NC}"; ((TESTS_FAILED++)); cd ..; return 1; }
    else
        [ -f "pyproject.toml" ] || { echo "${RED}✗ pyproject.toml missing${NC}"; ((TESTS_FAILED++)); cd ..; return 1; }
        [ -f "justfile" ] || { echo "${RED}✗ justfile missing${NC}"; ((TESTS_FAILED++)); cd ..; return 1; }
        [ -d "src" ] || { echo "${RED}✗ src/ missing${NC}"; ((TESTS_FAILED++)); cd ..; return 1; }
        [ -d "tests" ] || { echo "${RED}✗ tests/ missing${NC}"; ((TESTS_FAILED++)); cd ..; return 1; }
        [ -d "docs" ] || { echo "${RED}✗ docs/ missing${NC}"; ((TESTS_FAILED++)); cd ..; return 1; }
    fi
    
    echo "${GREEN}✓ File structure correct${NC}"
    ((TESTS_PASSED++))
    
    # Test Python projects
    if [ "$project_type" != "c_tricore" ]; then
        echo "Installing dependencies..."
        just install > /dev/null 2>&1 || {
            echo "${RED}✗ Failed to install dependencies${NC}"
            ((TESTS_FAILED++))
            cd ..
            return 1
        }
        echo "${GREEN}✓ Dependencies installed${NC}"
        ((TESTS_PASSED++))
        
        echo "Running tests..."
        just test > /dev/null 2>&1 || {
            echo "${RED}✗ Tests failed${NC}"
            ((TESTS_FAILED++))
            cd ..
            return 1
        }
        echo "${GREEN}✓ Tests passed${NC}"
        ((TESTS_PASSED++))
        
        echo "Running linting..."
        just lint > /dev/null 2>&1 || {
            echo "${RED}✗ Linting failed${NC}"
            ((TESTS_FAILED++))
            cd ..
            return 1
        }
        echo "${GREEN}✓ Linting passed${NC}"
        ((TESTS_PASSED++))
        
        echo "Building documentation..."
        just docs-build > /dev/null 2>&1 || {
            echo "${RED}✗ Documentation build failed${NC}"
            ((TESTS_FAILED++))
            cd ..
            return 1
        }
        echo "${GREEN}✓ Documentation built${NC}"
        ((TESTS_PASSED++))
    fi
    
    cd ..
    echo "${GREEN}✓ All tests passed for $project_type${NC}"
    
    return 0
}

# Clean up function
cleanup() {
    echo ""
    echo "Cleaning up test projects..."
    rm -rf test_cli test_library test_tricore
    echo "Cleanup complete"
}

# Trap cleanup on exit
trap cleanup EXIT

# Run tests
echo ""
echo "Test 1: Python CLI Project"
test_project "python_cli" "test_cli"

echo ""
echo "Test 2: Python Library Project"
test_project "python_library" "test_library"

echo ""
echo "Test 3: C/TriCore Project"
test_project "c_tricore" "test_tricore"

# Summary
echo ""
echo "======================================"
echo "Test Summary"
echo "======================================"
echo "${GREEN}Passed: $TESTS_PASSED${NC}"
echo "${RED}Failed: $TESTS_FAILED${NC}"
echo ""

if [ $TESTS_FAILED -eq 0 ]; then
    echo "${GREEN}🎉 All tests passed!${NC}"
    exit 0
else
    echo "${RED}❌ Some tests failed${NC}"
    exit 1
fi
