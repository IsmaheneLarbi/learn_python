fibonacci_cache = {}

def fibonacci(n):
    # If value cached, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # compute the nth term
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # cache the newly calculated value then return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 1001):
    print(n, ":", fibonacci(n))
