import re

my_text = "Python is een scripting taal die je kan gebruiken voor network automation."

pattern = re.compile(r"^Python")
matches = pattern.findall(my_text)

if matches:
    print("Een match is gevonden.")
else:
    print("Er is geen match gevonden.")