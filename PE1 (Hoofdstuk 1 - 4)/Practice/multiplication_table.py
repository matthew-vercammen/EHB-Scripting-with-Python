"""
Read a number from input.

Print its multiplication table from 1 to 10.
Each line should look like this: [number] x [i] = [result]
"""

# Read the number
n = int(input())

# Print multiplication table
i = 1

while i <= 10:
    result = n * i
    print(str(n) + " x " + str(i) + " = " + str(result))
    i += 1