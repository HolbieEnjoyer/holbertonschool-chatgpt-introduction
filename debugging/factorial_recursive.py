#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given integer using recursion.

    Parameters:
        n (int): The integer for which factorial is to be calculated.

    Returns:
        int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Extracting the command line argument and calculating factorial
f = factorial(int(sys.argv[1]))
print(f)
