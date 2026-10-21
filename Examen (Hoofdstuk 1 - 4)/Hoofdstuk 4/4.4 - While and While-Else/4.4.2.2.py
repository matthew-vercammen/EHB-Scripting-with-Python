# Menu voor de gebruiker om een keuze te maken
menu = """
Firewall Rule Menu:
Add - Toevoegen Firewall Rule
Del -  Verwijderen Firewall Rule
Overzicht - Overzicht Firewall Rules
Exit - Programme afslsuiten
"""

# Maak een list met de volgende naam "firewall_rules"
firewall_rules = []

# Je vraagt aan de gebruiker om een keuze in te geven: Add, Del, Overzicht, Exit
# Elke keuze heeft een bepaalde actie
# Keuzemenu wordt steeds opnieuw gegeven. Het programma stopt van zodra de gebruiker "Exit" heeft ingegeven.
exit_bool = True

while exit_bool:
    print(menu)
    choice = input("Maak een keuze: ").capitalize()

    # Keuze Add
    # - Hier ga je een firewall regel toevoegen aan de list firewall_rules
    # - Elke firewall regel die je toevoegt aan de list is een dictionary met volgende gegevens:
        # Key Name -> Value Naam van de firewall regel
        # Key SourceIP -> Value Source IP adres
        # Key DestinationIP -> Value Destination IP adres
        # Key SourcePort -> Value Source port adres
        # Key DestinationPort -> Value Destination port adres
    # - Opgelet elke firewall regel is UNIEK op basis van de naam. Doe het onderstaande:
    #       Zorg voor een controle dat er geen meerdere firewall regels bij zitten met dezelfde naam
    #       Geef een foutboodschap aan de gebruiker indien deze een firewall regel wilt toevoegen met dezelfde naam
    #       Vraag aan de gebruiker om een nieuwe naam in te geven (deze naam moet je ook controleren!)
    if choice == "Add":
        rule = {"Name": "", "SourceIP": "", "DestinationIP": "", "SourcePort": "", "DestinationPort": ""}

        name = ""
        name_check = True

        # Ask for name and check if it is unique
        while name_check:
            name = input("Wat is de naam van de firewall regel? ")

            # Assume the name will be unique (otherwise the first time will cause an endless loop bc no dictionaries exist yet)
            name_check = False

            # Loop through every dictionary in the list
            for rule_dict in firewall_rules:
                # Check if a matching value exists already
                if rule_dict["Name"] == name:
                    print("Een regel met deze naam bestaat al. Gelieve een andere naam in te geven.")
                    name_check = True
                    break
        else:
            rule["Name"] = name

        rule["SourceIP"] = input("Wat is het source IP-adres? ")
        rule["DestinationIP"] = input("Wat is het destination IP-adres? ")
        rule["SourcePort"] = input("Wat is de source port? ")
        rule["DestinationPort"] = input("Wat is de destination port? ")

        firewall_rules.append(rule)
    # Keuze Del
    # - Hier ga je een firewall regel verwijderen uit de list van firewall_rules
    # - Ga doorheen elke firewall rule en controleer de naam
        # Geef een foutboodschap aan de gebruiker indien de naam niet is gevonden
        # Geef een boodschap aan de gebruiker indien de naam is gevonden
    elif choice == "Del":
        delete_bool = True

        while delete_bool:
            to_delete = input("Geef de naam van de regel die je wil verwijderen: ")

            for rule in firewall_rules:
                if rule["Name"] == to_delete:
                    del rule
                    print("Regel verwijderd.")
                    delete_bool = False
                    break
            else:
                print("Regel niet gevonden. Controleer de naam.")
    # Keuze Overzicht
    # - Geef een overzicht van alle firewall regels aan de gebruiker
    elif choice == "Overzicht":
        print("------------------------------")
        for rule in firewall_rules:
            for key in rule:
                print(key + ": " + rule[key])

            print()
    # Keuze Exit
    # - Geef een boodschap aan de gebruiker en het programma wordt nadien afgesloten
    elif choice == "Exit":
        print("Het programma wordt afgesloten.")
        exit_bool = False
    # bij ongeldige input
    else:
        print("Ongeldige keuze.")