# def factorial(n):
#     assert n >= 0 and int(n) == n, 'The number must be positive integer only'
#     if n in [0, 1]:
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(10))

# Fibonacci number - Recursion

def fibonacci(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(8))
