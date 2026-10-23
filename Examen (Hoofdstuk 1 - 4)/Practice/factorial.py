"""
Read a number from input.
Create a function that calculates the factorial of that number.

The factorial of N means: multiply all numbers from 1 to N together.
Example: factorial of 5 = 1 × 2 × 3 × 4 × 5 = 120

The factorial of 0 is 1.

Print the result like this: [n]! = [result]
"""

# Create a function for factorial
def factorial(n):
    # Return the factorial of n
    fac = 1
    i = 1

    while i <= n:
        fac *= i
        i += 1

    return fac

# Read input and print result
num = int(input())
print(str(num) + "! = " + str(factorial(num)))
