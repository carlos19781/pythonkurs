""" 
Datentyp String: unverändlicher, sequentieller Datentyp
"""

name = "Hamburg"
print("erste Zeichen:", name[0])
print("Zugriff auf b:", name[3])
print("letzes Zeichen:", name[-1])  # negative Zählung von hinten

# Zahl in String konvertieren
x = 34
x = str(x)
print(x)

# Einfache Möglichkeit, Strings zu verbinden
# Überladung des Additionsoperators
vorname = "Bob"
nachname = "Sponge"

name = vorname + " " + nachname
print(name)

# Strings multiplizieren
# Überladung des Multiplikationsoperators asdfasfdsdfa
print("+++++++++++++++++++++++++++++++++")
print("+!" * 33)  # erzeugt neuen String mit 33 "+""

print("Der Name hat eine Länge von:", len(name))
print("Letzes zeichen mit len:", name[len(name) - 1])

# name = name.upper()
print(name)

# Ersetzen von a mit b
value = "3,3 mm"
comma = ","
punkt = "."
value = value.replace(comma, punkt)  # 3.3 mm
value = value.replace("mm", "")  # 3.3
print(float(value))

# find (Substring Spon in Bob Sponge suchen)
print(name.find("Spon"))  # -1 nicht gefunden, oder Index

# startswith, endwith, Prüfen ob ein Substring in einem 
# anderen vorkommt
artikel_nummer = "P1_33423"
print(artikel_nummer.startswith("P1"))  # True
print(artikel_nummer.endswith("P1"))    # False

"""
3. String Ersetzung
Ersetze alle Vorkommen von b in a durch c
a = "Bellavista"
b = "Bella"
c = "Buena"
"""
a = "Bellavista"
b = "Bella"
c = "Buena"

neu_a = a.replace(b, c)
print("a:", a)
print("b:", neu_a)

print("Es kommt der Buchstabe e:", a.count("e"))

# String von Leer- und Steuerzeichen am Anfang und Ende bereinigen
# praktisch beim Einlesen von Daten
daten_value = " 76.3\n\r \t"
print(daten_value.strip())

# Split => erzeugt eine Liste anhand eines Separators
csv_row = "3, 4, 89.1, 100"
print(csv_row.split(","))