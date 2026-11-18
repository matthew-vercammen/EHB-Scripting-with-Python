# vars
my_list = [5, 10, 15, 15, 10, 5]

my_set = {5, 10, 15, 15, 10, 5}
my_set2 = {5, 10, 20}

# commands
print("Commands:")

print(type(my_list))
print(type(my_set))
print(type(my_set2))

print(my_list)
print(my_set)
print(my_set2)

print(set(my_list))

print(len(my_set))

print(100 in my_set)
print(100 not in my_set)
print(5 in my_set)

my_set.add(20)
print(my_set)

my_set.remove(5)
print(my_set)

my_set.add(20)
print(my_set)

print(my_set.intersection(my_set2))

print(my_set.difference(my_set2))

print(my_set2.difference(my_set))

# create new list & new set, then create another set from list
print("1.")

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_set3 = {6, 8, 2, 4, 12, 10}

my_new_set = set(my_list2)
print(my_new_set)

print()

# show overlap between my_set3 & my_new_set
print("2.")

print(my_set3.difference(my_new_set))

print()

# show length of my_set3
print("3.")

print(len(my_set3))

print()

# create new set, convert to frozenset, then (try to) add new item
print("4.")

my_set4 = {10, 20, 30, 40, 50, 50, 20}
print(my_set4)

my_frozenset = frozenset(my_set4)
print(my_frozenset)

# my_frozenset[5] = 100 -- error because new items can't be added to frozensets
# print(my_frozenset)