# Fibonacci TDD Kata

A Python project exploring the Fibonacci sequence using Test-Driven Development (TDD), from interactive notebook experimentation to a structured Python package.

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/)

## Installation

Clone the repository and install the dependencies:

```bash
uv sync --all-groups
```

## Usage

```python
from fibonacci_kata import fibonacci

print(fibonacci(10))  # 55
```

The function returns the nth Fibonacci number, starting with `fibonacci(0) = 0` and `fibonacci(1) = 1`.

Negative indices raise a `ValueError`.

## Tests

Run the test suite:

```bash
uv run pytest -v
```

Check code quality:

```bash
uv run ruff check .
```

Build the package:

```bash
uv build
```

## Interactive notebook

Launch the Marimo notebook:

```bash
uv run marimo edit notebooks/notebook.py
```

The notebook provides an interactive way to explore Fibonacci numbers.

## Continuous Integration

GitHub Actions automatically runs linting and tests on pushes and pull requests targeting the `master` branch.

## License

MIT
