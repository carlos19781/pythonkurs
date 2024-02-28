"""
der for loop: sammlungskontrolliert
"""
messdaten = ["3.22222 mm", "4.22222 mm"]
messdaten_clean = []

for messpunkt in messdaten:
    messpunkt = float(messpunkt[0:-3])
     
    messpunkt += 1 # kurzschreibweise messpunkt = messpunkt + 1
    messdaten_clean.append(messpunkt)

print(messdaten)
print(messdaten_clean)

# A) AusgangsListe sollte während der Iteration nicht verändert werden
values = [1, 2, 3]
counter = 0
for value in values:
    value = value ** 2
    values[counter] = value
    counter = counter + 1
print(values)

# B) Bessere Variante: mit neuer Liste
values = [1, 2, 3]
values_squared = []

for value in values:
    value = value ** 2
    values_squared.append(value)
print(values_squared)