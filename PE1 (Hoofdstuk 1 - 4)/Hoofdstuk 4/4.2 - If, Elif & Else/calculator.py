# 4.2.1

# ask user to input 2 numbers + operator
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
operator = input("Operator (+, -, *, /): ")
result = 0

# if statement for +
if operator == "+":
    result = num1 + num2
    print(result)
# elif statement for -
elif operator == "-":
    result = num1 - num2
    print(result)
# elif statement for *
elif operator == "*":
    result = num1 * num2
    print(result)
# elif statement for /
elif operator == "/":
    result = num1 / num2
    print(result)
# else statement
else:
    print("Incorrect input for operator.")

