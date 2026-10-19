#Input examen score opvragen
exam_score = int(input("Geef de examenscore in (0-100): "))

if exam_score < 0 or exam_score > 100:
    print("Foute ingave. De score moet tussen 0 en 100 zijn.")
else:
    #Input heeft de student minstens 75% deelgenomen aan de klas
    attended_classes = input("Heeft de student minstens 75% deelgenomen? (ja/nee): ")

    # Convert to bool
    if attended_classes.lower() == "ja":
        attended_classes = True
    elif attended_classes.lower() == "nee":
        attended_classes = False
    else:
        print("Foute ingave.")

    if exam_score >= 60 and attended_classes == True:
        print("Geslaagd!")
    elif exam_score >= 60 and attended_classes == False:
        print("Niet genoeg deelname. Niet geslaagd.")
    elif exam_score < 60 and attended_classes == True:
        print("Genoeg deelname, maar gebuisd op het examen. Niet geslaagd.")
    elif exam_score < 60 and attended_classes == False:
        print("Gebuisd op het examen EN niet genoeg deelname. Niet geslaagd.")
    else:
        print("Error.")

