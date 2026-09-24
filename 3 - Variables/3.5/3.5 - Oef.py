print("1.")
# Declare vars
scripting_languages = {1:"python", 2:"ruby", 3:"javascript", 4:"PHP", 5:"perl"}
ide_programs = {"ide_atom":"atom", "ide_vs":"visual studio", "ide_pv":"py_dev", "ide_pc":"pyCharm"}

# Show vars class
print(type(scripting_languages))
print(type(ide_programs))
print()

print("2.")
# Show values using []
print(scripting_languages[3])
print(ide_programs["ide_pv"])
print()

print("3.")
# Show values using get()
print(scripting_languages.get(1))
print(ide_programs.get("ide_pc"))
print()

print("4.")
# Update scripting_languages key 4
scripting_languages.update({4:"Bash"})
print(scripting_languages)
print()

print("5.")
# Create new item in ide_programs
ide_programs["ide_rm"] = "rubeMine"
print(ide_programs)
print()

print("6.")
# Remove key+value from ide_programs using del
del ide_programs["ide_vs"]
print(ide_programs)
print()

print("7.")
# Remove key+value from scripting_languages using pop
scripting_languages.pop(5)
print(scripting_languages)
print()

print("8.")
# Create new var
scripting_values = scripting_languages.values()

# Print scripting_values
print(scripting_values)

# Print type of scripting_values
print(type(scripting_values))

# Change scripting_values type
scripting_values = list(scripting_languages.values())
print(type(scripting_values))
print()

print("9.")
# Create new var
program_keys = ide_programs.keys()
print(program_keys)

# Show program_keys class
print(type(program_keys))

# Convert program_keys class to list
program_keys = list(ide_programs.keys())
print(type(program_keys))

