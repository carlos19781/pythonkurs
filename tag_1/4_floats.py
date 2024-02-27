""" 
Datentyp Float (Fließkommazahl)

Trennung mit Punkt

weiteres Modul im Arbeiten mit floats:
decimal
"""
a = 1.2
# b = 1,2 # Tupel

# Multiplikation von int und float
print(3 - 1.0)

# Umwandlen von int nach float 
x = 122
x = float(x)
print("float(x):", x)

# Umwandeln von Float in int
y = 1.22338478
y = int(y)
print("int(y):", y)

# Konvertieren einer Zeichenkette in ein Float
eingabe = float("2.2")
result = eingabe + 2
print(result)

# Konvertieren einer Zeichenkette in ein int
eingabe = "2.2"
eingabe = float(eingabe)  # 2.2
eingabe = int(eingabe)    # 2
result = eingabe + 2
print(result)

# Runden (round(zahl, Präzision))
z = 1 / 3
print(round(z, 6))

# Unschärfe durch Addition (Fehler summiert sich)
r = 0.1 + 0.1 + 0.1
print(r)