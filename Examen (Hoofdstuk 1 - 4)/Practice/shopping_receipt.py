"""
Your program reads three lines:
- Item name
- Price (a number like 1.50)
- Quantity (a whole number like 3)

Print exactly these 4 lines:
Item: [item]
Price: $[price] (always two decimal places, like 1.50)
Quantity: [quantity]
Total: $[total] (price times quantity, two decimal places)
"""

# Read input
item = input().strip()
price = float(input())
quantity = int(input())

# Calculate total
total = float(quantity * price)

# Print the receipt
print("Item: " + item)
print("Price: $" + format(price, ".2f"))
print("Quantity: " + str(quantity))
print("Total: $" + format(total, ".2f"))
