"""
The first line of input is a count (how many numbers will follow).
The next lines each have one number.

Add all the numbers together and print the sum: "Sum: [total]"
"""

# Read count
n = int(input())

# Read numbers and calculate sum
i = 1
number = int
total = 0

while i <= n:
    number = int(input())
    total += number
    i += 1

# Print the sum
print("Sum: " + str(total))