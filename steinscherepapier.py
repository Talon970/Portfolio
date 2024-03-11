# Computer soll zufällig zwischen
# Stein, Schere, Papier wählen

# Spieler soll eingabe machen können
# Ergebniss soll angezeigt werden

# Die Spielerpunktzahl soll in einer DB gespeichert werden
# und über das Script abgerufen werden können

import random as rd
def computer_wahl():
    strings = ["Schere", "Stein", "Papier"]
    return rd.choice(strings).lower()
    
def spieler_wahl():
    return input("Wähle Stein, Schere oder Papier?").lower()
    
def spiel_wertung(spieler, computer):
    if spieler == computer:
        return "Unentschieden!"
    elif (spieler == "schere" and computer == "papier") or \
        (spieler == "stein" and computer == "schere") or \
        (spieler == "papier" and computer == "stein"):
        return "Spieler gewinnt!"
    else:
        return "Computer gewinnt!"
    
computer = computer_wahl()
spieler = spieler_wahl()
ergebnis = spiel_wertung(spieler, computer)

print(f"Computer wählt: {computer}")
print(f"Spieler wählt: {spieler}")
print(ergebnis)
