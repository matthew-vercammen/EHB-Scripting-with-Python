import re

my_numbers = '''
Below you will find numbers and letters:

Contains numbers and letters:
00-a0-83-B1-c0-8E
2d-f4-83-89-DE-FC

Contains only numbers:
44:12:47:87:15:35
55:78:45:57:11:78

'''

pattern = re.compile(r"\d{1,2}")
matches = pattern.findall(my_numbers)

for match in matches:
    print(match)