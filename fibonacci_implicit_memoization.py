from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    """Returns the nth element of the fibonacci series."""
    # check that the input is an integer
    if type(n) != int:
        raise TypeError("n must be a positive int.")
    if n < 1:
        raise ValueError("n must be a positive int.")
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 1001):
#     print(n, ":", fibonacci(n))

for n in range(1, 51):
    # the growth of a fibonacci series is of the golden ratio.
    print(fibonacci(n+1) / fibonacci(n))
# fibonacci("3")
