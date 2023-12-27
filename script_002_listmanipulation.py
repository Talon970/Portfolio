#Aufgabe: Schreibe ein Programm, das eine Liste von Zahlen sortiert und Duplikate entfernt.
def sort_and_remove_duplicates(numbers):
    # Sortiert die Liste und entfernt Duplikate
    return sorted(set(numbers))

# Testen der Funktion
numbers = [3, 6, 2, 3, 2, 6, 8]
result = sort_and_remove_duplicates(numbers)
