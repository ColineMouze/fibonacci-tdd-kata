import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest as py

    return


@app.function
#def Fibonacci (n):
#    Fibonacci=[0,1]
#   for k in range (2,n+1):
#        Fibo_k = Fibonacci[k-1] + Fibonacci[k-2]
#        Fibonacci.append(Fibo_k_k)
#    return F[n]

def Fibonacci (n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


@app.function
def test_Fiboinit():
    assert Fibonacci(0) == 0
    assert Fibonacci(1) == 1
    return


@app.function
def test_Fibo():
    assert Fibonacci(2) == 1
    assert Fibonacci(4) == 3
    assert Fibonacci(12) == 144
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
