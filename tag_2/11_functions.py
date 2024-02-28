""" 
Funktionen

alles, was ausserhalb der Funktionen liegt, wird als global bezeichnet.
global scope

Datentyp Check mit mpypy
https://realpython.com/python-type-checking/

"""
# def hello_world():
#     print("hello")


# hello_world()  # Funktionsaufruf

def rauminhalt(a, b, c):
    # alles innerhalb einer funktion wird als lokal bezeichnet
    volume = a * b * c 
    return volume

volume2 = rauminhalt(10, 20, 30)
print(volume2)


# Aufgabe: 
    
# Aufgabe: area, diese Funktion hat zwei Parameter (Länge, Breite),
# Rückgabewert der Funktion ist die errechnete Fläche (return)
# falls a oder b kleinergleich 0, soll die Funktion 0 zurückgeben

def area(a, b):
    if a <= 0 or b <= 0:
        return 0
    else:
        result = a * b
        return result
    
area(3, 4)

lengths_widths = [(22, 24.3), (-1, 34), (0.2, 0.2), (0, 23)]

areas = []
for a, b in lengths_widths:
    areas.append(area(a, b))


# multiply kann mit int und str aufgerufen werden.
# deshalb Datentypen nutzen (a: int) sagt aus, dass
# a ein Integer sein sollte.
def multiply(a: int, b: int):
    return a * b 


print(multiply(3, 5))
print(multiply("3", 2))  # Aufpassen

# Entpacken von Sequenzen
values = [1, 2, 3]
a = values[0]
b = values[1]
c = values[2]

# pythonische Weg
a, b, c = values

# Entpacken mit Sternchen-Operator
a, *b ,c = [1, 2, 3, 4, 5, 8]
print(a, b, c)