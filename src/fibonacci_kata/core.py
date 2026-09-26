def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    """Return the nth number of the Fibonacci sequence."""
    return a