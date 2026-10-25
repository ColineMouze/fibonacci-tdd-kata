import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_kata import fibonacci

    return fibonacci, mo, plt


@app.cell
def _(mo):
    n = mo.ui.slider(start=0, stop=20, value=10, label="Fobonacci index")
    n
    return (n,)


@app.cell
def _(fibonacci, mo, n):
    result = fibonacci(n.value)

    mo.md(f"Fibonacci({n.value}) = **{result}**")
    return


@app.cell
def _(fibonacci, n, plt):
    indices = list(range(n.value + 1))
    values = [fibonacci(i) for i in indices]

    fig, ax = plt.subplots()
    ax.plot(indices, values, marker="o")
    ax.set_title("Fibonacci sequence")
    ax.set_xlabel("Index n")
    ax.set_ylabel("Fibonacci(n)")
    ax.grid(True)

    fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
