# Maak gebruik van onderstaande list met verschillende dictionary items voor het maken van de oefening
my_routers = [
    {"Hostname":"Router 1", "MGMT_IP_Adres":"10.10.10.1", "Banner":"", "username":"ehbadmin", "Password":"Test123"},
    {"Hostname":"Router 2", "MGMT_IP_Adres":"10.10.10.2", "Banner":"", "username":"ehbroot", "Password":"Test456"},
    {"Hostname":"Router 3", "MGMT_IP_Adres":"10.10.10.3", "Banner":"", "username":"ehbadmin", "Password":"Test789"},
    {"Hostname":"Router 4", "MGMT_IP_Adres":"10.10.10.4", "Banner":"", "username":"ehbroot", "Password":"Test0973"}
]

# STAP 1
# -----------------------------------------------------------------------------------
# Je geeft de gebruiker een keuzemenu met volgende acties
# - Connecteren op een router       -> Zie uitleg STAP 2 - Connecteren op een router
# - Overzicht routers               -> Zie uitleg STAP 6 - Overzicht routers
# - Script stoppen                  -> Zie uitleg STAP 7 - Het script stopt


# STAP 2 - Connecteren op een router
# -----------------------------------------------------------------------------------
# Maak een variabele aan "my_connect_router" waar je de functie "connect_to_router" zal OPROEPEN en je geeft de variabele my_routers mee als parameter

# Je maakt een functie aan "connect_to_router" met een parameter, binnenin deze functie doe je het volgende:
    # Bij het connecteren op een router vraag je aan de gebruiker om een IP adres in te geven
    # Doe een controle om na te gaan of het IP adres bestaat aan de hand van de parameter die je meegeeft met de functie
    # Als het IP adres BESTAAT, dan vraag je nadien aan de gebruiker om een username en paswoord in te geven
    # Als de username en paswoord overeenkomen, dan heb je een succesvolle verbinding met de router
    # Bij een succesvolle verbinding, stuur je het IP adres terug van de router aan de gebruiker
    # Bij een niet succesvolle verbinding, stuur je een boolean False terug aan de gebruiker
    # Als het IP adres NIET BESTAAT, dan stuur je een False terug

    # TIP
    #--------------------------------------------------------------------------------
    # Je moet gebruik maken van de variabele my_routers die je meestuurt in de functie connect_to_router
    # Aan de hand van het ingegeven IP Adres kan je alle keys/valus terugvinden van de ITEM in de LIST
    # HIER STOPT DE FUNCTIE


# Indien de variabele "my_connect_router" (die je eerder hebt aangemaakt) een IP adres is (die wordt teruggestuurd vanuit functie connect_to_router), voer je het volgende uit
        # Geef aan de gebruiker de boodschap dat de connectie met de router is geslaagd.
        # Je geeft de gebruiker een nieuw keuzemenu met volgende acties
        # 1 - Configureren van de hostname            -> Zie uitleg STAP 3 - Configureren van de hostname
        # 2 - Configureren van de banner              -> Zie uitleg STAP 4 - Configureren van de banner
        # 3 - Verbreek de connectie met de router     -> Zie uitleg STAP 5 - Verbreek de connectie met de router

# Indien de variabele "my_connect_router" False is (die wordt teruggestuurd vanuit functie connect_to_router), voer je het volgende uit
    # De connectie naar het apparaat wordt verbroken
    # Je geeft de gebruiker terug het keuzemenu van STAP 1


# STAP 3 - Configureren van de hostname
# -----------------------------------------------------------------------------------
# Maak een variabele "my_hostname" aan waar je de functie "configure_hostname" zal OPROEPEN

# Maak een functie aan "configure_hostname" zonder gebruik van parameters, binnenin deze functie doe je het volgende:
    # Je vraagt aan de gebruiker om een hostname in te geven
    # Deze hostname stuur je terug
    # HIER STOPT DE FUNCTIE

# Zorg nadien dat de dictionary (waarmee je een CONNECTIE hebt gemaakt) wordt aangepast met de nieuwe hostname.

# TIP
# --------------------------------------------------------------------------------
# Je maakt gebruik van het IP adres die wordt teruggestuurd om een MATCH te kunnen vinden


# STAP 4 - Configureren van de banner
# -----------------------------------------------------------------------------------
# Maak een variabele "my_banner" aan waar je de functie "configure_banner" zal OPROEPEN

# Maak een functie aan "configure_banner" zonder gebruik van parameters, binnenin deze functie doe je het volgende:
    # Je vraagt aan de gebruiker om een banner in te geven
    # Deze banner stuur je terug
    # HIER STOPT DE FUNCTIE

# Zorg nadien dat de dictionary (waarmee je een CONNECTIE hebt gemaakt) wordt aangepast met de nieuwe banner.

# TIP
# --------------------------------------------------------------------------------
# Je maakt gebruik van het IP adres die wordt teruggestuurd om een MATCH te kunnen vinden


# STAP 5 - Verbreek de connectie met de router
# -----------------------------------------------------------------------------------
# Zorg ervoor dat de connectie wordt verbroken met de router
# Je geeft de gebruiker terug het keuzemenu van STAP 1


# STAP 6 - Overzicht routers
# -----------------------------------------------------------------------------------
# Maak een functie aan "overview_routers"
# Binnen deze functie moet je alle routers aflopen en toon je al hun gegevens op het scherm
# DENKVRAAG: Moet je parameters meesturen ja of neen?
# HIER STOPT DE FUNCTIE


# STAP 7 - Programma stopt
# -----------------------------------------------------------------------------------
# Maak een functie aan "stop_program"
# Zorg dat binnenin deze functie het script stopt
# DENKVRAAG: Moet je parameters meesturen ja of neen?
# HIER STOPT DE FUNCTIE