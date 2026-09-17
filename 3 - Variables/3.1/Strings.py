from operator import concat

# # student string functions
# student = " I am a student"
#
# print(type(student))
#print(student.index("a"))
# print(student.count("a"))
# print(student.find("stu"))
# print(student.find("Stu"))
# print(student.lower())
# print(student.upper())
# print(student.startswith(" "))
# print(student.startswith("i"))
# print(student.endswith("t"))
# print(student.strip())
# print(student.strip("t"))
# print(len(student))


# Declare my_string
my_string = "Als een potvis in een pispot pist zit de pispot vol met potvispis."

# Print my_string second to last letter
print(my_string[-2])


# Re-declare my_string
my_string = "De koetsier poetst de postkoets met postkoetspoets."

# Count amount of "o" characters in my_string
print(my_string.count("o"))


# Re-declare my_string
my_string = "Als kakkerlakken in kattebakken kakken, heb je een kattebak vol met kakkerlakkenkak."

# Replace spaces with underscores in my_string
print(my_string.replace(" ", "_"))

# Declare strings
my_string1 = "Knappe kappers kappen knap,"
my_string2 = "maar de knecht van de knappe kapper kapt"
my_string3 = "nog knapper dan de knappe kapper kappen kan."

# Concat strings
print(my_string1 + " " + my_string2 + " " + my_string3)