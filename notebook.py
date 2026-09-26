import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo
    import pytest as py


    return (marimo,)


@app.function
def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    """Return the nth number of the Fibonacci sequence."""
    return a


@app.function
def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    return


@app.function
def test_fibonacci_values():
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(12) == 144
    return


@app.cell
def _(marimo):
    slider = marimo.ui.slider(0, 50, value=10)
    slider
    return (slider,)


@app.cell
def _(marimo, slider):
    marimo.md(f"fibonacci({slider.value}) = {fibonacci(slider.value)}")
    return


@app.function
def test_fibonacci_large_values():
    assert fibonacci(100) == 354224848179261915075


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
