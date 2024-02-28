""" 
Häufige Aufgabe: Filter von Ausgangslisten
"""

# Aufgabe: Wir wollen eine Liste mit städten, die mit h anfangen
cities = ["hamburg", "berlin", "stuttgart", "hanau"]
cities_filtered = []

for city in cities:
    if city.startswith("h"):
        cities_filtered.append(city)


# 3. Filtern einer Liste 2
numbers = [1, 4, 5, 2, 42, 200, 1, 99, 23, 323]
filtered_numbers = []
for number in numbers:
    # if number > 5 and number < 100:
    # # alternativ: if 5 < number < 100
    if 5 < number < 100:
        filtered_numbers.append(number)
print(sorted(filtered_numbers))


# 7. Bereiningen der Liste
a = ["x_x", "alpha_beta", "_"]
c = []
for el in a:
    el = el.replace('_', '')
    if el:
        c.append(el)
print(c)