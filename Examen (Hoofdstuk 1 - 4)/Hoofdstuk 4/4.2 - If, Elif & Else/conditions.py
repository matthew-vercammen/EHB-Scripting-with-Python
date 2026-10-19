# 4.2.2

# 4.2.2.1
# ask user for input and place into var
my_answer = input("Waarvoor gebruik je Internet Explorer? ")

# check my_answer length
if len(my_answer) >= 20:
    print("Your answer was: " + my_answer)
# else statement
else:
    print("Error: your answer is less than 20 characters.")

#4.2.2.2
# var check_me
check_me = "Netmiko Al Van Gehoord?"

# check_me if statement with two conditions
if "A" in check_me and check_me.count("o") >= 3:
    print("Gevonden")
else:
    print("Neen nog niet gehoord")

# 4.2.2.3
# var my_ending
my_ending = "Eindigt deze zin nu op een uitroepteken ?!"

# my_ending if statement using endswith()
if my_ending.endswith("!"):
    print("Yes!")
else:
    print("No.")

# 4.2.2.4
# var my_vendors
my_vendors = {1: "Cisco", 2: "Huawei", 3: "Juniper", 4: "Ruckus"}

# check whether value for key "4" contains "c"
if 4 in my_vendors and "c" in my_vendors[4]:
    print("Gevonden")
else:
    print("Niet gevonden")