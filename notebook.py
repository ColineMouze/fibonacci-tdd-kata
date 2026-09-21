import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest as py


    return


@app.function
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)


@app.function
def test_Fiboinit():
    assert Fibonacci(0) == 0
    assert Fibonacci(1) == 1
    return


@app.function
def test_Fibo():
    assert Fibonacci(3) == 2
    assert Fibonacci(4) == 3
    assert Fibonacci(12) == 144
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
