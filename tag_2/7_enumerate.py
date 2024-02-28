""" 
Liste: Index und Wert ausgeben
"""
names = ["Bob", "Alice", "Trudy"]

# klassische Variante
for i in range(len(names)):
    print(f"Index:{i}: {names[i]}")


# Pythonische Variante mit enumerate
for i, name in enumerate(names):
    print(f"Index:{i}: {name}")