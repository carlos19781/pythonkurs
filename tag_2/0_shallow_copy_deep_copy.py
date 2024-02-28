""" 
Flache und tiefe Kopie.
Flache Kopie kopiert nur unverändliche Datentypen (int, str,..)
Tiefe Kopie kopiert alle Ebenen. Muss aus dem copy-Modul geladen werden!
"""

# Flache Kopie von einer 1-Dimensionalen Liste
v1 = [1, 2, 3]  # Liste mit 3 unveränldicher Datentypen
print("id von v1:", id(v1))

v2 = v1.copy()  # Flache Kopie (shallow copy)
print("id von v2:", id(v2))

v1.append(4)
print(v2)

# Flache Kopie einer mehrdimensionalen Liste
m = [1, 2, [3, 5]]
print("id von m:", id(m))

m2 = m.copy()
print("id von m2:", id(m2))

# Liste m2 wurde an Index 2 geändert! 
m[2].append(9)
print("m2:", m2)


# Tiefe Kopie von einer mehrdimensionalen Liste (zb. Matrix)
import copy 
m3 = copy.deepcopy(m)  #erzeuge eine tiefe Kopie von m
