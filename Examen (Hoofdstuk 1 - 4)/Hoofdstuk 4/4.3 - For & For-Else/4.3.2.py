# Declare my_list_numbers
my_list_numbers = [1, 3, 4, 8, 9, 5 ,9 ,2, 4 ,3, 2, 5]

# 1. Show every item in list, multiplying by 2 if it's 5
print("1.")

for number in my_list_numbers:
    if number != 5:
        print(number)
        continue
    else:
        print(number*2)
else:
    print()

# Declare my_x & my_y
my_x = [2, 4, 6, 8, 10]
my_y = [1, 3, 5 ,7]

# 2. Iterate through my_x, multiplying every element by every element from my_y
print("2.")

for x in my_x:
    for y in my_y:
        print(x*y)
else:
    print()

# Declare dict_cisco
dict_cisco = {'ports' : 24, 'os' : '18.1X1', 'device' : '9600'}

# 3. Print every key-value pair
print("3.")

for key, value in dict_cisco.items():
    print(key + " = " + str(value))
