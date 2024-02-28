""" 
Generator Expression
"""
import itertools

# List-Comprehension berechnet die ganze Liste vor
result = [x**2 for x in range(1000_000)]  # Iterable

# Als Generator-Expression (Iterator)
result_gen = (x**2 for x in range(1000_000))
print(result_gen)
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))
# print(result_gen[5000])

print(list(itertools.islice(result_gen, 5000, 5002)))

# for el in itertools.cycle([1, 2]):
#     print(el)