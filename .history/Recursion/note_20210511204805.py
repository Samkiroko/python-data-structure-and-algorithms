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


# def sumofDigits(n):
#     assert n >= 0 and int(n) == n, 'The number must be positive integer only'
#     if n == 0:
#         return 0
#     else:
#         return int(n % 10) + sumofDigits(int(n/10))


# print(sumofDigits(13))

# power of the number using Recursion

#  Step 1 : Recursive case - the flow
#  x**n = x*x**n-1

# def power(x, n):
#   return x * x**n-1

def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp-1)


print(power(2, 4))
