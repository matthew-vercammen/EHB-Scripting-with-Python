# Er is een list "network_devices" met dictionaries
# ELKE ITEM in de dictionary heeft drie keys name, status & size met elk hun eigen value
# In totaal zijn er 6 dictionaries met elk hun eigen key/value
network_packets = [
    {"source": "192.168.1.1", "destination": "192.168.1.20", "size": 1500},
    {"source": "123.47.36.9", "destination": "23.178.65.2", "size": 900},
    {"source": "192.168.1.1", "destination": "192.168.1.42", "size": 1200},
    {"source": "94.123.5.7", "destination": "184.14.23.1", "size": 800},
    {"source": "192.168.1.2", "destination": "192.168.1.47", "size": 700},
    {"source": "192.168.1.2", "destination": "168.4.1.7", "size": 700},
]

# Onderstaande variabelen gaan we gebruiken om het aantal pakketten op te tellen
# Aantal pakketten met grootte boven de 1000
large_packets = 0
# Aantal pakketten bedoelt voor intern verkeer
internal_traffic = 0
# Aantal pakketten bedoelt voor extern verkeer
external_traffic = 0

# Vervolledig en maak gebruik van een loop om doorheen elk pakket te gaan van network_packets
for packet in network_packets:
    # Geef een beschrijving op van elk pakket
    print("Packet met als source: " + str(packet["source"]))
    print("Packet met als destination: " + str(packet["destination"]))
    print("Packet met als packet-size: " + str(packet["size"]))

    # Check en geef een melding indien de packet-size groter is dan 1000
    if packet["size"] > 1000:
        print("Packet-size is groter dan 1000.")
        # Nadien moet je bijhouden hoeveel packets er groter zijn dan 1000. Maak gebruik van de variabele "large_packets".
        large_packets += 1

    # Check en bekijk of de source EN destionation starten met "192.168.1.". Dit is voor intern verkeer
    if str(packet["source"]).startswith("192.168.1.") and str(packet["destination"]).startswith("192.168.1."):
        print("Dit is intern verkeer.\n")
        # Nadien moet je bijhouden hoeveel packets er bedoeld zijn voor intern verkeer. Maak gebruik van de variabele "internal_traffic".
        internal_traffic += 1
    # Indien het niet match dan is dit verkeer bedoeld voor extern verkeer.
    else:
        print("Dit is extern verkeer.\n")
        # Nadien moet je bijhouden hoeveel packets er bedoeld zijn voor extern verkeer. Maak gebruik van de variabele "external_traffic".
        external_traffic += 1

# Toon op het scherm een overzicht van alle pakketten met de variabele large_packets, internal_traffic en external_traffic
print("Overzicht:")
print("Aantal large packets: " + str(large_packets))
print("Aantal internal traffic packets: " + str(internal_traffic))
print("Aantal external traffic packets: " + str(external_traffic))
