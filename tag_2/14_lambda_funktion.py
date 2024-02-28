""" 
Lambda Funktionen (anonymen Funktionen)
Einsatz zum Sortieren
"""
def fn(a, b):
    return a + b

fn(2, 3)
print(fn)

g = lambda a, b: a + b
g(4, 9)
print(g)

################ Sortieraufgabe Wojtek. Nach dem dritten Wert sortieren

def fn(el: list):
    return el[2]


values = [
    [1, 2, 3],
    [4, 1, 4],
    [9, 3, 2]
]

print(sorted(values, key=fn))
print(sorted(values, key=lambda el: el[2]))
print(sorted(values, key=lambda el: sum(el)))

# Sortieren von Listen mit Dicts
values = [
    {"a": 12, "b": 923},
    {"a": 112, "b": 223},
    {"a": 212, "b": 423},
]

# Zugriff auf Key b von el (el ist ein Dict)
print(sorted(values, key=lambda el: el["b"]))