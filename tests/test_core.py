
from fibonacci_kata.core import fibonacci


def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_fibonacci_values():
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(12) == 144


def _(marimo):
    slider = marimo.ui.slider(0, 50, value=10)
    return (slider,)


def _(marimo, slider):
    marimo.md(f"fibonacci({slider.value}) = {fibonacci(slider.value)}")


def test_fibonacci_large_values():
    assert fibonacci(100) == 354224848179261915075