def ask_information():
    info = {"Naam":"","Leeftijd":"", "Adres":""}

    info["Naam"] = input("Wat is uw naam? ")
    info["Leeftijd"] = input("Wat is uw leeftijd? ")
    info["Adres"] = input("Wat is uw adres? ")

    return info