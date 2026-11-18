# 1.
my_number = 0

# While loop
while my_number < 10:
    print("Uw nummer is: " + str(my_number))
    my_number += 1
# Print statement after while loop completes
else:
    print("Proficiat, je hebt 10 bereikt!")
    print()

# 2.
my_number = 0

# While loop goes until my_number reaches 100
while my_number < 100:
    my_number += 10

    # checks if my_number is 50, if so -> prints statement
    if my_number == 50:
        print("Je zit reeds in de helft, nog 50 te gaan!")
        continue

    print("Je getal zit op: " + str(my_number))

