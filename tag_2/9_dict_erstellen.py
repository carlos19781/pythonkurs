""" 
Ein Dict aus LIsten erstellen
"""
alphabet_liste = [
    ["A", "aleph"],  # muss aus zwei Elementen 
    ["B", "beth"]
]
alphabet_dict = dict(alphabet_liste)
print(alphabet_dict)

# Dict aus zwei Listen erstellen
countries = ["Deutschland", "Türkei", "USA", "Schweden"]
food = ["Currywurst", "Pilav", "Mais", "Hering"]

country_food = dict(zip(countries, food))
print(country_food)