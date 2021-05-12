# def factorial(n):
#     assert n >= 0 and int(n) == n, 'The number must be positive integer only'
#     if n in [0, 1]:
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(10))

# Fibonacci number - Recursion

# def fibonacci(n):
#     assert n >= 0 and int(n) == n, 'The number must be positive integer only'
#     if n in [0, 1]:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(-7))

"""How to find sum of digit of a positive integer
number using recursion?
"""
#  Recursive case - the flow


def sumofDigits(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumofDigits(int(n/10))


print(sumofDigits(13))
