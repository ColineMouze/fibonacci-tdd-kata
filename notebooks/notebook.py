import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    from fibonacci_kata import fibonacci

    return (fibonacci,)


@app.cell
def _():
    import marimo as mo

    slider = mo.ui.slider(0, 50, value=10, label="Indice n")
    slider
    return mo, slider


@app.cell
def _(fibonacci, mo, slider):
    mo.md(f"""
    ### Fibonacci\n\nfibonacci({slider.value}) = **{fibonacci(slider.value)}**
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
