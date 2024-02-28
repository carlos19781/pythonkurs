""" 
Datentyp set (unterstützt die Mengenoperationen)
Schnittmenge, Differenzmenge, Vereiningsungsmenge

Verändlicher Datentyp, ungeorndet. 
Die Elemente müssen unverändlerlich sein
"""
a = set()  # leere Menge 
b = {"a", "a", "b", "c", 34}

print("b:", b)

# Aufgabe: entferne alle die mehrfach vorkommen
values = [2, 3, 4, 5, 6, 6, 8, 9, 2] 
values_unique = []
for value in values:
    if value not in values_unique:
        values_unique.append(value)

# mit Set 
values_unique = list(set(values))
print(values_unique)


# Schnittmenge (Menge der Elemente, die in beiden Mengen vorkommt)
a = [2, 3, 4, 5]
b = [2, 3, 6, 7]

c = list(set(a) & set(b))
print(c)

# Frozenset: kann als Key für ein Dict genommen werden
d = {}
d[frozenset(a)] = 3

