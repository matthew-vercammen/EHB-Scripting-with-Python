# var my_dict
from string.templatelib import convert

my_dict = {"Vendor":"Cisco", "Device":"3750", "Ports":"24", "IOS":"13"}

# commands
print("Commands:")

print(type(my_dict))

print(len(my_dict))

del my_dict["Ports"]
print(my_dict)

my_dict["RAM"] = 256
print(my_dict)

print("Vendor" in my_dict)
print("vendor" in my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict.pop('Device')
print(my_dict)

my_dict.update({"Speed":"1Gb"})
print(my_dict)

print()

# vars
scripting_languages = {1:"python", 2:"ruby", 3:"javascript", 4:"PHP", 5:"perl"}
ide_programs = {"ide_atom":"atom", "ide_vs":"visual_studio", "ide_pv":"py_dev", "ide_pc":"pyCharm"}

# show data types
print("1.")

print(type(scripting_languages))
print(type(ide_programs))

print()

# show values "javascript" & "py_dev" using []
print("2.")

print(scripting_languages[3])
print(ide_programs["ide_pv"])

print()

# show values "python" & "pyCharm" using get
print("3.")

print(scripting_languages.get(1))
print(ide_programs.get("ide_pc"))

print()

# change value of key 4 in scripting_languages to "Bash"
print("4.")

scripting_languages[4] = "Bash"
print(scripting_languages)

print()

# create new item with key "ide_rm" & value "rubeMine" in ide_programs
print("5.")

ide_programs.update({"ide_rm":"rubeMine"})
print(ide_programs)

print()

# remove "visual_studio" from ide_programs using del
print("6.")

del ide_programs["ide_vs"]
print(ide_programs)

print()

# remove "perl" from scripting_languages using pop
print("7.")

scripting_languages.pop(5)
print(scripting_languages)

print()

# save scripting_languages values to new var scripting_values, then convert to list
print("8.")

scripting_values = scripting_languages.values()
print(scripting_values)
print(type(scripting_values))

scripting_values = list(scripting_values)
print(type(scripting_values))

print()

# save ide_programs keys to new var program_keys, then convert to list
print("9.")

program_keys = ide_programs.keys()
print(program_keys)
print(type(program_keys))

program_keys = list(program_keys)
print(type(program_keys))