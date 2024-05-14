#!/usr/bin/python3
import sys

# Define a function to calculate the factorial of a given number 'n'
def factorial(n):
    # Base case: If n is 0, factorial is 1
    if n == 0:
        return 1
    else:
        # Recursive case: Multiply n with the factorial of (n-1)
        return n * factorial(n-1)

# Get the input from the command line argument and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the factorial
print(f)
