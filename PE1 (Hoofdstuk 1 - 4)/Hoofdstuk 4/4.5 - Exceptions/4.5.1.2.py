my_number_zero = 0
my_number_ten = 2

try:
    print(my_number_ten / my_number_zero)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
finally:
    print(type(my_number_zero))
    print(type(my_number_ten))