import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest as py

    return


@app.cell
def _(O):
    #def Fibonacci (n):
    #    Fibonacci=[0,1]
    #   for k in range (2,n+1):
    #        Fibo_k = Fibonacci[k-1] + Fibonacci[k-2]
    #        Fibonacci.append(Fibo_k_k)
    #    return F[n]

    def Fibonacci (n):
        if n==0:
            return O
        elif n==1:
            return 1
        else:
            return Fibonacci(n-1) + Fibonacci(n-2)
    
        
    

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
