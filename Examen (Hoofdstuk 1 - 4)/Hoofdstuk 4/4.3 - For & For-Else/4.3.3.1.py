# Er is een list "network_devices" met meerdere dictionaries
# ELKE ITEM van de list heeft een dictionary met twee keys name & status met elk hun eigen value
# In totaal zijn er 5 dictionaries met elk hun eigen key/value
network_devices = [
    {"name": "Router 1", "status": "Up"},
    {"name": "Switch 1", "status": "Down"},
    {"name": "Firewall 1", "status": "Down"},
    {"name": "Server 1", "status": "Up"},
    {"name": "Switch 2", "status": "Down"}
]

# Maak gebruik van een loop om doorheen elke item te gaan van network_devices
for device in network_devices:

    # Vervolledig de print statement met de "name" van elk apparaat
    # BVB: Status van apparaat: Router 1
    print("Status van apparaat: " + device["name"])

    # Check de status van elk apparaat, maak een onderscheid tussen Up en Down.
    # Indien de status UP is
    if device["status"] == "Up":
        print("Apparaat: " + device["name"] + " is operationaal. Er zijn geen acties nodig.")
        print()

    # Indien de status DOWN is
    elif device["status"] == "Down":
        # Vervolledig de print statement met de "name" van elk apparaat
        print("Apparaat: " + device["name"] +  " is niet operationaal. Enkele acties zijn nodig.")
        print()

        # Zorg dat de status van het apparaat op UP wordt geplaatst
        device["status"] = "Up"

    # Geef een foutboodschap in het geval de status niet UP of DOWN is
    else:
        print("Status is ongekend.")
        print()

# Als laatste toon je nu de naam van het apparaat en zijn status
# Als resultaat moeten alle apparaten een status UP hebben
print("De status van alle apparaten:")
for device in network_devices:
    print("Naam apparaat: " + device["name"])
    print("Status apparaat: " + device["status"])