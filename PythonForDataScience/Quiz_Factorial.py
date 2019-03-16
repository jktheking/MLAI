# Given a number ‘n’, output its factorial using reduce().
# Note: Make sure you handle the edge case of zero. As you know, 0! = 1

from functools import reduce
n = 4

def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda fact, i: fact*i, range(1, n+1))
print(factorial(0))
print(factorial(4))