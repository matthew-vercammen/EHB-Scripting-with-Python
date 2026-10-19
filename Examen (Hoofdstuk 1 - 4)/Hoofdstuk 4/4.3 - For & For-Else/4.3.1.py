# declare my_numbers
my_numbers = [150, 125, 12, 6, 78, 30, 5, 12, 47, 1236]

# 1. Show every element in my_numbers using a for-loop
print("1.")
for number in my_numbers:
    print(number)
else:
    print()
# 2. Show every element in my_numbers + print text at the end
print("2.")

for number2 in my_numbers:
    print(number2)
else:
    print("Proficiat, uw for loop is met succes afgerond!")
    print()

# 3. Show every element in my_numbers using index
print("3.")

for index, item in enumerate(my_numbers):
    print(str(index) + " " + str(item))
else:
    print()

# 4. Divide every element in my_numbers by 3, then print
print("4.")

for number4 in my_numbers:
    print(number4/3)
else:
    print()

# 5. Add every element in my_numbers to new list my_new_numbers, then sort, then print
print("5.")

my_new_numbers = []

for number5 in my_numbers:
    my_new_numbers.append(number5)
else:
    my_new_numbers.sort()
    print(my_new_numbers)
    print()
