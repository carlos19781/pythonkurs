""" 
Dictionary: Key-Value-Paar
"""
player = {
    "life_points": 430, 
    "power": 1, 
    "speed": 2,
    "weapons": ["knife", "gun", "bazooka"]
    }

print("Lebenspunkte des Players:", player["life_points"])
# Die Waffen des Players
weapons = player["weapons"]
print(weapons)

##################
d = {}
print(type(d))

d = {
    "a": 3.2,
    "b": 44
}
print(d)

en_de = {
    "cat": "katze",
    "dog": "Hund"
}

# Länder und Hauptstädte mit Dictionary
capitals = {
    "de": "Berlin",
    "uk": "London"
}
print(capitals["uk"])
capitals_neu = capitals # Vorsicht! Nur die Referenz wurde kopiert!

# Prüfen, ob ein Key im Dict
if "de" in capitals:
    print(capitals["de"])

# Länder und Hauptstädte mit Listen (alternative)
cities = ["Berlin", "London"]
countries = ["de", "uk"]
index_uk = countries.index("uk")

# Iteration über ein Dict mit Key-Value-Paaren
for country, captial in capitals.items():
    print(country, captial)

# mehrere Elemente hinzufügen
capitals.update({"fr": "Paris", "pl": "Warschau"})
print(capitals)

# Neues Element zum Dict hinzufügen
capitals["it"] = "Rom"

# Element aus Dict rauspoppen
print(capitals.pop("it"))