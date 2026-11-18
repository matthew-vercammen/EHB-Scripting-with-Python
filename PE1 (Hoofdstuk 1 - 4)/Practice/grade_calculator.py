"""
Read a score from input (0 to 100).

Print the letter grade:
90 or more: A
80 to 89: B
70 to 79: C
60 to 69: D
Below 60: F
"""

# Read the score
score = int(input())

# Print the grade
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")