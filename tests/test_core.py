import pytest

from fibonacci_kata.core import fibonacci


def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_fibonacci_values():
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(12) == 144


def test_fibonacci_large_values():
    assert fibonacci(100) == 354224848179261915075


def test_fibonacci_negative_input():
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci(-1)
