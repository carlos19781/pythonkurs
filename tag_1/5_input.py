""" 
input: Usereingabe: wird immer als String ausgegeben
"""

x = input("Bitte gebe den Wert x ein: ")
print(x, type(x))

# Runden 
round(32.3434303, 2)

# Um Berechnungen auszuführen, muss der Rückgabewert von input
# in eine Zahl konvertiert werden.
x = int(x)
print(x, type(x))

y = int(input("Bitte gebe die y-Koordianate ein: "))