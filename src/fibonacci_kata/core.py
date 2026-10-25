"""Core Fibonacci functionality."""


def fibonacci(n: int) -> int:
    """Return the nth number of the Fibonacci sequence."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b

    return a
