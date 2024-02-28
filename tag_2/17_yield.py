""" 
Yield Keyword: Generator Funktion
"""
def classic():
    """Klassische Funktion hat return-Wert."""
    return True

a = classic()
print(a)


def infinite_counter():
    x = 0
    while True:
        yield x # yield ist ernten
        x += 1

counter = infinite_counter() # erstellt ein Generator-Objekt
print(counter)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


def filter_values(values):
    filtered_list = []
    for value in values:
        if value > 10:
            filtered_list.append(value)

    return filtered_list


def filter_values_better(values):
    for value in values:
        if value > 10:
            yield value


values = [3, 9, 12, 39]
result = filter_values_better(values)
print(result)
print(list(result))