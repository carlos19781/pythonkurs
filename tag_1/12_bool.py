""" 
Boolescher Wert (wahr oder falsch)

0 => unwahr
"" => unwahr
[] => unwahr
None => unwahr
"""
print(bool(0))
print(bool(0.00000001))

a = True 
print(a, type(a))

artikel_nummer = "P1_33423"
print(artikel_nummer.startswith("P1"))  # True

##### Arithmetische Vergleichsoperatoren
# >, >=, <, <=, !=, ==

THRESHOLD = 42
value = 9

if value < THRESHOLD:
    print(f"{value} ist kleiner als Schwellenwert {THRESHOLD}")
    print("das gehört auch dazu!")

print("value < THRESHOLD: ", value < THRESHOLD)  # erzeugt einen boolschen Wert

messwert_a = 0.3
messwert_b = 0.1 + 0.1 + 0.1

# Floats vergleichen mit mit.isclose
# https://www.w3schools.com/python/ref_math_isclose.asp

if messwert_a == messwert_b:
    print("diese Werte sind gleich")
else:
    print("Die Werte sind ungleich")


