# User input voor de geheime code
my_lower = input("Wat is je secret voor kleine letters? ")
my_upper = input("Wat is je secret voor hoofdletters? ")
my_digit = input("Wat is je secret voor getallen? ")

# Check de lengte van de input
if len(my_lower) + len(my_upper) + len(my_digit) < 8:
    print("De lengte van de geheime code is te kort")
else:
    # Check voor kleine letters
    if my_lower.islower():
        # Check voor hoofdletters
        if my_upper.isupper():
            # Check voor getallen
            if my_digit.isdigit():
                # Indien alles OK is dan is de code geldig
                print("De code is geldig.")

                my_code = set(my_lower + my_upper + my_digit)
                print(my_code)
            else:
                print("Je getallen zijn niet geldig.")
        else:
            print("Je hoofdletters zijn niet geldig.")
    else:
        print("Je kleine letters zijn niet geldig.")