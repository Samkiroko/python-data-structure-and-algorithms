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

# def power(base, exp):
#     assert exp >= 0 and int(
#         exp) == exp, "The exponent must be positive integer"
#     if exp == 0:
#         return 1
#     if exp == 1:
#         return base
#     return base * power(base, exp-1)


# print(power(2, 4))

# def gcd(a, b):
#     assert int(a) == a and int(b) == b, 'the number must be an integer'
#     if a < 0:
#         a = -1 * a
#     elif b < 0:
#         b = -1 * b
#     if b == 0:
#         return a
#     elif a < 0:
#         return
#     return gcd(b, a % b)


# print(gcd(60, 48))


# def computeGCD(x, y):

#     if x > y:
#         small = y
#     else:
#         small = x
#     for i in range(1, small+1):
#         if((x % i == 0) and (y % i == 0)):
#             gcd = i

#     return gcd


# a = 60
# b = 48

# # prints 12
# print("The gcd of 60 and 48 is : ", end="")
# print(computeGCD(60, 48))

#####
# How to covert a number from decimal to binary using recursion

# def decimalToBinary(n):
#     assert int(n) == n, "The parameter must be an integer only!"
#     if n == 0:
#         return 0
#     else:
#         return n % 2 + 10 * decimalToBinary(int(n/2))


# print(decimalToBinary(13))
