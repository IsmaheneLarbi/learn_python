def fibonacci(n):
    """Returns the nth element of the fibonacci series."""
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 101):
    print(n, ":", fibonacci(n))
