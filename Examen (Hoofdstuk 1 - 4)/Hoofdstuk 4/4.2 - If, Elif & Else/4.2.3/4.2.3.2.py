# Tekst vragen aan de gebruiker
user_text = input("Geef tekst in: ")

# Check voor een bepaald woord
word_to_find = input("Op welk woord wil je zoeken? ")

# Zoek met de juiste string functie of het woord is gevonden of niet
# Bij niet gevonden is het resultaat 0
if user_text.count(word_to_find) == 0:
    print("Dat woord zit niet in de tekst.")
# Bij gevonden is het resultaat groter dan 0
else:
    # Ask for substring to replace with
    replace_word = input("Wat is het vervangende woord? ")

    # replace the substring with the new substring, then print
    user_text = user_text.replace(word_to_find, replace_word)
    print(user_text)