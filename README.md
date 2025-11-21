# Vokal- und Konsonanten-Zähler

Ein Python-Programm zur Analyse von Zeichenketten, das die moderne `match`-Konstruktion (Pattern Matching) demonstriert.

## Aufgabenstellung
Entwicklung eines Programms mit folgenden Anforderungen:
1.  Einlesen einer beliebigen Zeichenkette.
2.  Zählung aller **Vokale** (inklusive Umlaute).
3.  Zählung aller **Konsonanten** (definiert als alle Zeichen, die *keine* Vokale sind, also auch Zahlen und Sonderzeichen).
4.  Groß- und Kleinschreibung soll ignoriert werden.
5.  **Technische Vorgabe:** Zwingende Verwendung der `match`-Anweisung zur Fallunterscheidung.

## Technische Umsetzung
Der Code nutzt Python 3.10+ Features für sauberen und lesbaren Code:
*   **Pattern Matching:** Nutzung von `match` und `case` anstelle von langen `if-elif`-Ketten.
*   **Case-Insensitivity:** Umwandlung der Eingabe mittels `.lower()` für eine robuste Erkennung.
*   **Wildcard-Pattern:** Nutzung des `case _:` (Wildcard), um effizient alle Nicht-Vokale abzufangen, wie in der Aufgabenstellung gefordert.
*   **Umlaut-Support:** Erkennt auch deutsche Umlaute (ä, ö, ü) korrekt als Vokale.

## Nutzung
Führen Sie das Skript in der Konsole aus (benötigt Python 3.10 oder höher):

```bash
python main.py
