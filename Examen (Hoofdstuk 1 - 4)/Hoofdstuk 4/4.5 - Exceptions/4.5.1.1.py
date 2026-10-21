my_string = "2"
my_integer = 2

try:
    print(my_string + my_integer)
except TypeError:
    print("Error: cannot concatenate an integer")