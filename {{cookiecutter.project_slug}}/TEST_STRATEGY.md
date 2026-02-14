# Test Strategy

This document outlines the testing approach for {{ cookiecutter.project_name }}.

## Testing Philosophy

- **Test early, test often**: Catch bugs before they reach production
- **Comprehensive coverage**: Aim for >80% code coverage
- **Fast feedback**: Tests should run quickly
- **Maintainable**: Tests should be easy to understand and update
- **Automated**: All tests run in CI/CD

## Test Pyramid

```
       /\
      /  \     E2E Tests (Few)
     /----\
    /      \   Integration Tests (Some)
   /--------\
  /          \ Unit Tests (Many)
 /____________\
```

### Unit Tests (Foundation)

**What:** Test individual functions, methods, and classes in isolation.

**Coverage:** 80%+ of codebase

**Tools:**
- pytest for test execution
- pytest-cov for coverage reporting
- pytest-mock for mocking dependencies

**Location:** `tests/test_*.py`

**Examples:**
```python
def test_config_loader():
    """Test configuration loading."""
    config = Config()
    assert config.get("key", "default") == "default"

@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
])
def test_process_various_inputs(input, expected):
    """Test multiple input cases."""
    assert process(input) == expected
```

**Run:**
```bash
just test           # All tests
just test-cov       # With coverage
```

{% if cookiecutter.use_integration_tests == "yes" -%}
### Integration Tests (Middle Layer)

**What:** Test interactions between components.

**Coverage:** Critical paths and integrations

**Tools:**
- pytest with integration markers
- Test fixtures for setup/teardown

**Location:** `tests/integration/`

**Examples:**
```python
@pytest.mark.integration
def test_full_workflow():
    """Test complete workflow."""
    config = Config()
    core = Core(config._config)
    result = core.process("test")
    assert result == "TEST"
```

**Run:**
```bash
uv run pytest -m integration
```
{%- endif %}

## Test Organization

### Directory Structure

```
tests/
├── __init__.py
├── conftest.py              # Shared fixtures
├── test_config.py           # Config tests
├── test_core.py             # Core logic tests
├── test_cli.py              # CLI tests
{% if cookiecutter.use_integration_tests == "yes" -%}
└── integration/             # Integration tests
    └── test_workflows.py
{%- endif %}
```

### Naming Conventions

- **Files:** `test_*.py`
- **Functions:** `test_<what>_<condition>()`
- **Classes:** `Test<Component>`
- **Fixtures:** Descriptive names (e.g., `temp_config_dir`)

## Test Fixtures

**Purpose:** Reusable test setup and teardown

**Location:** `tests/conftest.py`

**Example:**
```python
@pytest.fixture
def temp_config_dir(tmp_path):
    """Create temporary config directory."""
    config_dir = tmp_path / "etc"
    config_dir.mkdir()
    return config_dir
```

## Mocking Strategy

**When to mock:**
- External services (APIs, databases)
- File system operations (when appropriate)
- Time-dependent code
- Expensive operations

**Example:**
```python
def test_api_call(mocker):
    """Test API call with mocking."""
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"status": "ok"}
    mocker.patch("requests.get", return_value=mock_response)
    
    result = fetch_data()
    assert result["status"] == "ok"
```

## Coverage Requirements

### Thresholds

- **Overall:** 80% minimum (configurable in pyproject.toml)
- **Warning:** <80% generates warning
- **Failure:** <60% fails CI (configurable)

### Exclusions

Lines excluded from coverage:
- `pragma: no cover`
- `def __repr__`
- `raise AssertionError`
- `raise NotImplementedError`
- `if __name__ == .__main__.:`
- `if TYPE_CHECKING:`

### Coverage Reports

```bash
just test-cov       # Terminal + HTML report
open htmlcov/index.html  # View HTML report
```

## CI/CD Testing

### GitHub Actions

**test.yml workflow:**
- Runs on every push and PR
- Executes all tests
- Generates coverage report
- Posts coverage to PR comments
- Uploads to Codecov/Coveralls

**Caching:**
- uv cache
- pytest cache
- mypy cache

**Parallelization:**
- Uses pytest-xdist for parallel execution

## Test Types

### 1. Unit Tests

**Focus:** Individual functions/methods

**Characteristics:**
- Fast (<1ms per test)
- No external dependencies
- Isolated
- Deterministic

**Example:**
```python
def test_add():
    assert add(2, 3) == 5
```

### 2. Parametrized Tests

**Focus:** Multiple input scenarios

**Characteristics:**
- Tests same logic with different inputs
- Reduces code duplication
- Clear test cases

**Example:**
```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

### 3. Exception Tests

**Focus:** Error handling

**Example:**
```python
def test_invalid_input():
    with pytest.raises(ValueError, match="Invalid input"):
        process_data("invalid")
```

### 4. Fixture-Based Tests

**Focus:** Complex setup/teardown

**Example:**
```python
def test_with_database(db_session):
    """Test using database fixture."""
    user = User(name="Test")
    db_session.add(user)
    db_session.commit()
    assert user.id is not None
```

## Best Practices

### DO

✅ Write tests first (TDD) when possible
✅ Test one thing per test
✅ Use descriptive test names
✅ Keep tests simple and readable
✅ Use fixtures for common setup
✅ Mock external dependencies
✅ Test edge cases and error conditions
✅ Maintain tests alongside code

### DON'T

❌ Test implementation details
❌ Write flaky tests
❌ Ignore failing tests
❌ Skip tests without good reason
❌ Test third-party code
❌ Make tests dependent on each other
❌ Use sleep() for timing

## Running Tests

### Local Development

```bash
# All tests
just test

# With coverage
just test-cov

# Specific file
uv run pytest tests/test_config.py

# Specific test
uv run pytest tests/test_config.py::test_load_yaml

# With verbose output
uv run pytest -v

# Stop on first failure
uv run pytest -x

# Show print statements
uv run pytest -s
```

### CI/CD

Tests run automatically on:
- Every push to main/develop
- Every pull request
- Scheduled daily runs

## Debugging Tests

### Failed Test

```bash
# Run with verbose output
uv run pytest -v tests/test_failing.py

# Drop into debugger on failure
uv run pytest --pdb

# Show local variables
uv run pytest -l
```

### Coverage Gaps

```bash
# Generate coverage report
just test-cov

# View HTML report
open htmlcov/index.html

# Find untested lines
uv run pytest --cov --cov-report=term-missing
```

## Performance Testing

{% if cookiecutter.use_profiling == "yes" -%}
**Tool:** pytest-benchmark

**Example:**
```python
def test_performance(benchmark):
    """Benchmark function performance."""
    result = benchmark(expensive_function, arg1, arg2)
    assert result is not None
```

**Run:**
```bash
uv run pytest --benchmark-only
```
{%- else -%}
Performance testing can be added with pytest-benchmark if needed.
{%- endif %}

## Test Maintenance

### Regular Tasks

- **Weekly:** Review coverage reports
- **Monthly:** Update test dependencies
- **Per PR:** Ensure new code has tests
- **Per release:** Run full test suite

### Updating Tests

When code changes:
1. Update affected tests
2. Add tests for new functionality
3. Remove tests for deleted code
4. Verify coverage hasn't decreased

## Continuous Improvement

### Metrics to Track

- Test count
- Coverage percentage
- Test execution time
- Flaky test rate
- Bug escape rate

### Goals

- Maintain >80% coverage
- Keep test suite under 1 minute
- Zero flaky tests
- All PRs include tests

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [Testing Best Practices](https://docs.python-guide.org/writing/tests/)

## Questions?

For questions about testing strategy, open an issue or contact the maintainers.
