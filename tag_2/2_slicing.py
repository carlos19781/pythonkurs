"""
Slicing Operator: Substrings aus Strings schneiden

Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String
"""

messwert = "12.3 mm"
print(messwert[2:4]) # .3
print(messwert[2:])  # .3mm
print(messwert[:3])  # 12.

print(messwert[:messwert.index(" ")])

# Slicing auf Listen
persons = ["bob", "Bob", "Trudy", "Alice"]
persons_neu = persons[1:3]
print(persons_neu)

## 
messungs = ["3.22222 mm", "4.22222 mm"]

## 3. Paramter der Slicing-Funtion: Schrittweite 
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("alle geraden Zahlen: ", numbers[1::2])

# mit negativher Schrittweite lassen sich Strings und LIsten umdrehen
print("Numbers umgedreht:", numbers[::-1])