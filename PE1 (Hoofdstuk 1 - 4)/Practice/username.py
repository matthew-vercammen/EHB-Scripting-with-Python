"""
Read a first name and a last name from input.

Create a username by joining the two names together in lowercase (no space between them).

Print these two lines:

Username: [username]
Initials: [first letter of first name][first letter of last name] (in uppercase)
"""

# Read input
first_name = input().strip()
last_name = input().strip()

# Create username (lowercase, no space)
username = (first_name + last_name).lower()

# Create initials (uppercase first letters)
initials = (first_name[0] + last_name[0]).upper()

# Print results
print("Username: " + username)
print("Initials: " + initials)