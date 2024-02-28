""" 
map-Funktionen: jedes Element eines Iterables (zb. list)
anwenden auf eine Funktion
"""
def f(el):
    return el ** 2

values = [3, 4, 5]

# MAP

# Via map-Funktion
result = map(f, values)
result = map(lambda x: x**2, values)
print(list(result))

# via List-Comprehension
result2 = [x**2 for x in values]
print(result2)

# FILTER
def fltr(n):
    return n > 4

values = [3, 4, 5, 7, 9, 23]
result = filter(fltr, values)
print(next(result))
print(next(result))
print(next(result))
print(next(result))

values = [
    [1, 2, 3],
    [4, 1, 4],
    [9, 3, 2]
]

result2 = [x for x in values if x[2] >= 3]
print(result2)