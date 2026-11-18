# vars
my_tuple = ()
my_tuple_int = (9)
my_tuple_int2 = (1, 2, 9)
my_tuple_str = ("EHB")

# commands
print("Commands:")

print(type(my_tuple))
print(type(my_tuple_int))
print((type(my_tuple_int2)))
print(type(my_tuple_str))

# my_tuple_int2.add(5) -- error - can't add items to a tuple
# print(my_tuple_int2)

print(len(my_tuple_int2))

print(5 in my_tuple_int2)
print(2 in my_tuple_int2)

del my_tuple_int2
# print(my_tuple_int2) -- error - my_tuple_int2 is not defined anymore

print()

# add items to my_tuble and show length, fist items, last item & index of "SD-WAN"
print("1.")

my_tuple = ("Routing", "Switching", "SD-WAN", "BGP", "Loadbalancing", "Cybersecurity")

print(len(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.index("SD-WAN"))
