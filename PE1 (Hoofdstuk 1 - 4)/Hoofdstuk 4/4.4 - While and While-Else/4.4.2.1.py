# Dictionary network_settings met enkele keys en lege values
from ipaddress import ip_address

network_settings = {
    "IP Address": "",
    "Subnet Mask": "",
    "Gateway": "",
    "DNS Server": ""
}


# Menu optie die we aan de gebruiker laten zien in de while conditie
menu = """
Network Configuration Menu:
1. Configureer IP Address
2. Configureer Subnet Mask
3. Configureer Gateway
4. Configureer DNS Server
5. Show Current Configuration
6. Exit
"""

# Maak een boolean aan die je zal gebruiken voor je while conditie
exit_bool = True

# Vervolledig de while conditie met het gebruik van de exit_bool
while exit_bool:

    # Laat de gebruiker telkens opnieuw het keuzemenu zien
    print(menu)

    # De gebruiker moet een keuze ingeven op basis van het nummer 1,2,3,4,5,6
    choice = input("Geef je keuze in van 1 tot 6: ")

    # Elke optie in het menu zal een bepaalde actie uitvoeren. Zorg voor een structuur waarbij elke keuze wordt nagegaan

    # Bij keuze 1:
    # - Ga je aan de gebruiker vragen om een IP adres in te geven
    # - Je gaat het IP-adres opslagen in de variabele network_settings met de juiste key
    # - Geef aan de gebruiker de boodschap dat het IP adres is opgeslagen
    if choice == "1":
        ip = input("Geef het IP-adres in: ")
        network_settings["IP Address"] = ip

        print("Het IP-adres is met succes opgeslagen!")
    # Bij keuze 2:
    # - Ga je aan de gebruiker vragen om een subnet-mask adres in te geven
    # - Je gaat het subnet-mask opslagen in de variabele network_settings met de juiste key
    # - Geef aan de gebruiker de boodschap dat het subnet-mask adres is opgeslagen
    elif choice == "2":
        mask = input("Geef het subnet-mask adres in: ")
        network_settings["Subnet Mask"] = mask

        print("Het subnet-mask adres is met succes opgeslagen!")
    # Bij keuze 3:
    # - Ga je aan de gebruiker vragen om een gateway adres in te geven
    # - Je gaat het gateway-adres opslagen in de variabele network_settings met de juiste key
    # - Geef aan de gebruiker de boodschap dat het gateway adres is opgeslagen
    elif choice == "3":
        gateway = input("Geef het gateway-adres in: ")
        network_settings["Gateway"] = gateway

        print("Het gateway-adres is met succes opgeslagen!")
    # Bij keuze 4:
    # - Ga je aan de gebruiker vragen om een DNS adres in te geven
    # - Je gaat het DNS adres opslagen in de variabele network_settings met de juiste key
    # - Geef aan de gebruiker de boodschap dat het DNS adres is opgeslagen
    elif choice == "4":
        dns = input("Geef het DNS-adres in: ")
        network_settings["DNS Server"] = dns

        print("Het DNS-adres is met succes opgeslagen!")
    # Bij keuze 5:
    # - Ga je aan de gebruiker alle network configuratie settings tonen op het scherm
    # - Zorg voor een manier dat je doorheen de dictionary kan gaan waar bij elke key en value wordt overlopen
    elif choice == "5":
        print("Huidige netwerk-configuratie:")

        for key in network_settings:
            print(key + ": " + network_settings[key])
    # Bij keuze 6:
    # - Het programma stopt. Zorg ervoor dat de while conditie niet meer matcht
    elif choice == "6":
        exit_bool = False
    # Bij keuze ongekend:
    # - Geef de gebruiker de boodschap dat er geen correct keuze is gemaakt
    else:
        print("Ongeldige keuze.")
        print()
