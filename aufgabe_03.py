""" **********************************************************
Aufgabe 3 Vokale und Konsonanten zaehlen mit match-Konstruktion
***********************************************************""" 

# Einlesen der Zeichenkette
text = input("Bitte geben Sie eine Zeichenkette ein: ")

anzahl_vokale = 0
anzahl_konsonanten = 0

# Definition der Vokale fuer Abgleiche 
VOKALE = ('a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü')

# Durchlaufen jedes einzelnen Zeichens in der eingegebenen Zeichenkette
for zeichen in text:
    # Das Zeichen in Kleinbuchstaben konvertieren, um GrossŸ- und Kleinbuchstaben gleichzeitig zu behandeln 
    klein_zeichen = zeichen.lower()

    # match-Anweisung fuer die Unterscheidung nutzen 
    match klein_zeichen:
        # Prueft ob das Zeichen mit einem der Vokale uebereinstimmt
        case 'a' | 'e' | 'i' | 'o' | 'u' | 'ä' | 'ö' | 'ü':
            anzahl_vokale += 1
        # Dies schliessŸt Konsonanten, Zahlen, Leerzeichen und Sonderzeichen ein.
        case _:
            anzahl_konsonanten += 1

# Ausgabe der Ergebnisse
print("\n--- Analyse der Zeichenkette ---")
print(f"Anzahl der Vokale: {anzahl_vokale}")
# Konsonanten sind hier definiert als alle Zeichen, die keine Vokale sind
print(f"Anzahl der Konsonanten (inkl. aller Nicht-Vokale): {anzahl_konsonanten}")


