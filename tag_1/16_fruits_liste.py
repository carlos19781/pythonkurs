fruits = ["banana", "apple", "strawberry"]
fruits_kopie = fruits
print(id(fruits))

# Element an index 0 ändern
fruits[0] = "lemon"
print(fruits)
print(id(fruits))

# String Beispiel
x = "abc"
x_kopie = x
print("x:", id(x))
x = x.upper()
print("x:", id(x))
print("x_kopie:", x_kopie)

# Methoden der Liste
fruits.append("pineapple")
print(fruits)

# pop löscht letztes Element und gibt es zurück
last_element = fruits.pop()
print("last lement", last_element)
print(fruits)

# extend: Liste zur Liste hinzufügen
fruits_new = ["pearse", "cherry"]
fruits.extend(fruits_new)
print("fruits:", fruits)
print("fruits_kopie:", fruits_kopie)
# pop-Beispiel
a = [1, 2]
b = [3, 4]
a.append(b.pop())
print(a)