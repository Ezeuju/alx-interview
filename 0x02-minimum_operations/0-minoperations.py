#!/usr/bin/python3
"""
Defines a function that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
        exactly n H characters in the file."""
    sumfactors = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            sumfactors += i
        else:
            i += 1
    return sumfactors + n if n > 1 else sumfactors
