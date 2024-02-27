# Ganzzahlen

x  = 12  # Variablenzuweisung
y = 3

print(x)
z = x + y

print("x + y", x + y)
print("12 / 3", x / y)  # Division von Ganzzahlen erzeugt Kommanzahl (True div)
print("12 // 5", x // 5)  # 12.8 => 12 (Floor-Div)

# Exponentiation
x = 4 
print("x²:", x**2)


# Modulo und floor-division

# Aufgabe: Wieviele Baumstämme passen der Länge nach in eine Halle 34m?
HALL_LENGTH = 40
tree_length = 3

number_trees = HALL_LENGTH // tree_length
rest = HALL_LENGTH % tree_length  # 40 % 3 
print("Es passen", number_trees, "Baumstämme in die Halle")
print("Es bleiben", rest, "Meter übrig")
