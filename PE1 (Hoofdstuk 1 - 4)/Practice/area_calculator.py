"""
Read a shape and its measurements from input.

The shape is one of these three words:
 - rectangle - next two lines are width and height
 - triangle - next two lines are base and height
 - circle - next line is the radius

Print the area with two decimal places: "Area: [result]"

Triangle area = base × height / 2.
Circle area = pi × radius × radius.
"""

import math

# Read the shape
shape = input().strip().lower()
area = 0.00


# Read measurements and calculate area
if shape == "rectangle":
    base = float(input())
    height = float(input())

    area = base * height
elif shape == "triangle":
    base = float(input())
    height = float(input())

    area = (base * height) / 2
elif shape == "circle":
    radius = float(input())

    area = math.pi * radius * radius
else:
    print("Error")

# Print the area
print("Area: " + format(area, ".2f"))