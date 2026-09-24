# Define var
my_dict = {"Vendor":"Cisco", "Device":"3750", "Ports":"24", "IOS":"13"}

# Functions
print(type(my_dict))
print()

print(len(my_dict))
print()

del my_dict["Ports"]
print(my_dict)
print()

my_dict["RAM"] = 256
print(my_dict)
print()

print("Vendor" in my_dict)
print("vendor" in my_dict)
print()

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print()

my_dict.pop('Device')
print(my_dict)
print()

my_dict.update({"Speed" : "1Gb"})
print(my_dict)

