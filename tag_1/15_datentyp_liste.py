""" 
Datentyp Liste
"""

user_eingabe = "12 14 18.4"
values = user_eingabe.split() # default trennt an Leerzeichen
print(values, type(values))

names = ["Bob", "Alice", "Mallory"]
grades = [3, 4, 1]

# Ausgabe: Alice hat die Note 4
print(f"{names[1]} hat die Note {grades[1]}")
print(f"{names[-2]} hat die Note {grades[-2]}")

# Vektor
v = [1, 9]

# Matrix (besser mit numpy machen!)
m = [
    [0, 0],
    [0, 1]
]
print(f"{m[1][1]}")