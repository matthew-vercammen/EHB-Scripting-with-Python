# Ask user to input values
num1 = input("Geef het eerste getal in: ")
num2 = input("Geef het tweede getal in: ")
operator = input("Geef de bewerking (+, -, * of /) in: ")

# convert inputs to floats
num1 = float(num1)
num2 = float(num2)

# if, elif & else statements
if operator == "+":
    result = num1 + num2
    print("Het resultaat is: ", result)
elif operator == "-":
    result = num1 - num2
    print("Het resultaat is: ", result)
elif operator == "*":
    result = num1 * num2
    print("Het resultaat is: ", result)
elif operator == "/":
    result = num1 / num2
    print("Het resultaat is: ", result)
else:
    print("Sorry! Er is iets fout gegaan!")
