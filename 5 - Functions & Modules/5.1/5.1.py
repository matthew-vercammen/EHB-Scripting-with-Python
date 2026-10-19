# 5.1.1
def my_function():
    print("Proficiat, je hebt een functie geschreven")

my_function()

# 5.1.2
# def my_calc(a, b):
  #  print(a + b)

# my_calc(4,7)

# 5.1.3
def my_calc(a,b):
    return a + b

som = my_calc(67, 9)
print(som)

# 5.1.4
def my_arguments(x,y, *args):
    print(type(x))
    print(x)

    print(type(y))
    print(y)

    print(type(args))
    print(args)

my_arguments(5, 10, 200, 2, 4)

# 5.1.5
my_number = 10


def my_calculation(x):
    global my_number
    print(x * my_number)
    my_number = 100


my_calculation(10)

# 5.1.6
def regio(straat, huisnummer, gemeente, postcode):
    print("Uw straat is: " + straat)
    print("Uw huisnummer is: " + huisnummer)
    print("Uw gemeente is: " + gemeente)
    print("Uw postcode is: " + postcode)

straat = input("Wat is uw straat?")
huisnummer = input("Wat is uw huisnummer?")
gemeente = input("Wat is uw gemeente?")
postcode = input("Wat is uw postcode?")

regio(straat, huisnummer, gemeente, postcode)
