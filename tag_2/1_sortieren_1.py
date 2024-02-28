""" 
Sortieren von Listen (und anderen Datentypen)

sort()
sorted()
"""

persons = ["bob", "Bob", "Trudy", "Alice"]
persons.sort()  # Inplace-Sortierung (aufsteigend)
print(persons)

persons.sort(reverse=True)  # Inplace-Sortierung (absteigend)
print(persons)

# numerischer Wert eines Zeichen (Codepoint)
print("WErt von b:", ord("b"))
print("WErt von B:", ord("B"))

# Funktion sorted(): erzeugt eine neue Liste
persons = ["bob", "Bob", "Trudy", "Alice"]
persons_sorted = sorted(persons)
print(persons_sorted)