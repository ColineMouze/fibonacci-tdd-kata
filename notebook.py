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
    """Return the nth number of the Fibonacci sequence.

    The Fibonacci sequence is defined by:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n >= 2.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


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
    slider = marimo.ui.slider(0, 30, value=10)
    slider
    return (slider,)


@app.cell
def _(marimo, slider):
    marimo.md(f"fibonacci({slider.value}) = {fibonacci(slider.value)}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
