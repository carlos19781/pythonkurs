"""
SET Comprehension
"""
cartesian_product = {(a, b) for a in range(3) for b in range(3)}

cart = set()
for a in range(3):
    for b in range(3):
        cart.add((a, b))

# Datentyp set kennt kein Ordnung
print(cart)
print(cartesian_product)

"""
DICT Comprehension
"""
names = ["Bob", "Alice"]
grades = [3, 5]

d = {name:grade for name, grade in zip(names, grades)}
print(d)
