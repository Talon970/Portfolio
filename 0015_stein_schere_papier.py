import random

# Liste der möglichen Optionen
optionen = ["Stein", "Papier", "Schere"]

def spiel_runde():
    # Computer wählt zufällig
    computer_wahl = random.choice(optionen)

    # Benutzereingabe
    benutzer_wahl = input("Wähle Stein, Papier oder Schere: ")

    # Überprüfen, ob die Eingabe gültig ist
    if benutzer_wahl not in optionen:
        print("Ungültige Eingabe. Bitte versuche es erneut.")
        return

    print(f"Computer wählte: {computer_wahl}")
    print(f"Du wähltest: {benutzer_wahl}")

    # Entscheiden, wer gewinnt
    if benutzer_wahl == computer_wahl:
        print("Unentschieden!")
    elif (benutzer_wahl == "Stein" and computer_wahl == "Schere") or \
         (benutzer_wahl == "Papier" and computer_wahl == "Stein") or \
         (benutzer_wahl == "Schere" and computer_wahl == "Papier"):
        print("Du gewinnst!")
    else:
        print("Computer gewinnt!")

def spiel_starten():
    while True:
        spiel_runde()
        nochmal_spielen = input("Möchtest du nochmal spielen? (ja/nein): ")
        if nochmal_spielen.lower() != "ja":
            break

    print("Spiel beendet. Danke fürs Spielen!")

# Spiel starten
spiel_starten()
