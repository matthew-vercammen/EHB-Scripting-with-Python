# vars
my_combo = ["EHB", "Cisco", 2020, "switCHing"]
my_numbers = [100, 2020, 5, 103]

my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]
my_number = [100, 1000, 50, 53, 10, 123, 789]
my_vendor_2 = ["Fortinet", "Arbor", "Aruba", "Checkpoint"]

# commands
print(type(my_combo))
print(type(my_numbers))
print()

print(min(my_numbers))
print(max(my_numbers))
# print(min(my_combo)) -- error (can't use in list with mix of int & str)
print()

my_numbers.sort()
print(my_numbers)
print()

my_combo.append("router")
print(my_combo)
print()

print(len(my_combo))
print()

del my_combo[3]
print(my_combo)
print()

my_combo.pop(0)
print(my_combo)
print()

my_combo.remove("Cisco")
print(my_combo)
print()

# my_combo.remove("RoUter") -- error (can't remove entry that doesn't exist - case-sensitive)

my_combo.insert(1, "Cisco")
print(my_combo)
print()

print(len(my_combo))
print()

# remove index 3 from my_vendor
print("1.")
del my_vendor[3]
print(my_vendor)
print()

# show index 2
print("2.")
print(my_vendor[2])
print()

# append "Ruckus" to my_vendor
print("3.")
my_vendor.append("Ruckus")
print(my_vendor)
print()

# show index of "Huawei"
print("4.")
print(my_vendor.index("Huawei"))
print()

# add "Nokia" to index 2
print("5.")
my_vendor.insert(2, "Nokia")
print(my_vendor)
print()

# sort my_vendor
print("6.")
my_vendor.sort()
print(my_vendor)
print()

# show min and max of my_number
print("7.")
print(min(my_vendor))
print(max(my_vendor))
print()

# add my_vendor_2 to my_vendor
print("8.")
my_vendor.extend(my_vendor_2)
print(my_vendor)