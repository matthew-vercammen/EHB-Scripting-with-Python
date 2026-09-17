# Declare vars
my_combo = ["EHB", "Cisco", 2020, "switCHing"]
my_numbers = [100, 2020, 5, 103]

# List functions | line 5-34
print(type(my_combo))
print(type(my_numbers))

print(min(my_numbers))
print(max(my_numbers))
# print(min(my_combo))

my_numbers.sort()
print(my_numbers)

my_combo.append("router")
print(my_combo)
print(len(my_combo))

del my_combo[3]
print(my_combo)

my_combo.pop(0)
print(my_combo)

my_combo.remove("Cisco")
print(my_combo)

# my_combo.remove("RoUter")

my_combo.insert(1, "Cisco")
print(my_combo)

print(len(my_combo))
# End of list functions

# Declare my_vendor
my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]

# Delete item with index 3
my_vendor.pop(3)
print(my_vendor)
print()

# Show index 2
print(my_vendor[2])
print()

# Append "Ruckus"
my_vendor.append("Ruckus")
print(my_vendor)
print()

# Show index of "Huawei"
print(my_vendor.index("Huawei"))
print()

# Add "Nokia" at index 2
my_vendor.insert(2, "Nokia")
print(my_vendor)
print()

# Sort my_vendor
my_vendor.sort()
print(my_vendor)
print()

# Declare my_number
my_number = [100, 1000, 50, 53, 10, 123, 789]

# Show my_number min and max values
print(min(my_number))
print(max(my_number))
print()

# Declare my_vendor2
my_vendor2 = ["Fortinet", "Arbor", "Aruba", "Checkpoint"]

# Add my_vendor2 to my_vendor
my_vendor.extend(my_vendor2)
print(my_vendor)
