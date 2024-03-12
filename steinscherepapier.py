import random as rd
import sqlite3

# Funktion zum Herstellen einer Verbindung zur Datenbank
def connect_db():
    return sqlite3.connect('spiel.db')

# Funktion zum Erstellen der Tabelle, wenn sie nicht existiert
def create_table(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            player_name TEXT PRIMARY KEY,
            points INTEGER
        )
    ''')

# Funktion zum Speichern der Punktzahl in der Datenbank
def save_score(conn, player_name, points):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO scores (player_name, points)
        VALUES (?, ?)
    ''', (player_name, points))
    conn.commit()

# Funktion zum Abrufen des Highscores aus der Datenbank
def get_highscore(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT player_name, points FROM scores
        ORDER BY points DESC
        LIMIT 1
    ''')
    return cursor.fetchone()

# Funktion zum Abrufen aller Highscores aus der Datenbank
def get_all_highscores(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT player_name, points FROM scores
        ORDER BY points DESC
    ''')
    return cursor.fetchall()

# Funktion zum Herstellen einer Verbindung zur Datenbank
def connect_db():
    return sqlite3.connect('spiel.db')

# Hauptfunktion des Spiels
def main():
    conn = connect_db()
    create_table(conn)

    punkte = 0
    player_name = input("Bitte gib deinen Namen ein: ")

    while True:
        while True:
            computer = computer_wahl()
            spieler = spieler_wahl()

            if spieler == computer:
                print("Unentschieden!")
            elif (spieler == "schere" and computer == "papier") or \
                (spieler == "stein" and computer == "schere") or \
                (spieler == "papier" and computer == "stein"):
                punkte += 1
                print("Spieler gewinnt!")
            else:
                print("Computer gewinnt!")

            print(f"Computer wählt: {computer}")
            print(f"Spieler wählt: {spieler}")
            print(f"Aktuelle Punktzahl: {punkte}")

            nochmal = input("Willst du nochmal spielen? (y/n)").lower()
            if nochmal == "n":
                save_score(conn, player_name, punkte)
                print("Bis zum nächsten Mal!")
                break
            elif nochmal != "y":
                print("Ungültige Eingabe. Bitte gib 'y' für Ja oder 'n' für Nein ein.")

        highscore = get_highscore(conn)
        if highscore:
            print(f"Highscore: {highscore[0]} - {highscore[1]} Punkte")
        else:
            print("Kein Highscore vorhanden.")

        all_highscores = get_all_highscores(conn)
        if all_highscores:
            print("Alle Highscores:")
            for hs in all_highscores:
                print(f"{hs[0]} - {hs[1]} Punkte")
        else:
            print("Keine Highscores vorhanden.")

        nochmal_spielen = input("Willst du noch eine Runde spielen? (y/n)").lower()
        if nochmal_spielen != "y":
            print("Bis zum nächsten Mal!")
            break

    conn.close()

# Die restlichen Funktionen des Spiels bleiben unverändert

def computer_wahl():
    strings = ["Schere", "Stein", "Papier"]
    return rd.choice(strings).lower()

def spieler_wahl():
    return input("Wähle Stein, Schere oder Papier?").lower()

def spiel_wertung(spieler, computer, punkte):
    if spieler == computer:
        print("Unentschieden!")
    elif (spieler == "schere" and computer == "papier") or \
        (spieler == "stein" and computer == "schere") or \
        (spieler == "papier" and computer == "stein"):
        punkte += 1
        print("Spieler gewinnt!")
    else:
        print("Computer gewinnt!")
    return punkte

main()
