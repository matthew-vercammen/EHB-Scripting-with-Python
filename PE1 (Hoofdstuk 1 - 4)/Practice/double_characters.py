""""
Double every character in a word.

Instructions:
1. Read one line of text from input.
2. Print the line with every character repeated twice, in the same order.

Example: abc becomes aabbcc.
"""

text = input("Input: ")
output = ""

for letter in text:
    output += letter
    output += letter
else:
    print(output)