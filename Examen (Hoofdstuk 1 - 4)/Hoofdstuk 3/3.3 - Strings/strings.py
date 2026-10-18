# var
student = " I am a student"

# commands
print(type(student))
print(student.index("a"))
print(student.count("a"))
print(student.find("stu"))
print(student.find("Stu"))
print(student.lower())
print(student.upper())
print(student.startswith(" "))
print(student.startswith("i"))
print(student.endswith("t"))
print(student.strip())
print(student.strip("t"))
print(len(student))
print()

# print second to last character
my_string = "Als een potvis in een pispot pist zit de pispot vol met potvispis."
print(my_string[-1])
print()

# count "o" characters
my_string = "De koetsier poetst de postkoets met postkoetspoets."
print(my_string.count("o"))
print()

# replace spaces with underscores
my_string = "Als kakkerlakken in kattebakken kakken, heb je een kattebak vol met kakkerlakkak."
print(my_string.replace(" ", "_"))
print()

# concatenate
my_string1 = "Knappe kappers kappen knap,"
my_string2 = "maar de knecht van de knappe kapper kapt"
my_string3 = "nog knapper dan de knappe kapper kappen kan."
print(my_string1 + " " + my_string2 + " " + my_string3)