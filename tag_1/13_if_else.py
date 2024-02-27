""" 
Logische Operatoren: AND, OR, NOT  && || ~
"""
a = 1 
b = 0 # Truthiness / Falsiness

if a and b: # 0 and 1
    print("auf beiden Leitungen fliesst Strom")

""" 
Wahrheitstabelle AND

a    b    AND
----------------
W    W    W  
W    f    f
f    f    f
f    w    f

"""
messwert_a = 10
messwert_b = 20 

if messwert_a > 100 and messwert_b < 200:
    print("Messwerte liegen im Bereich")
else:
    print("Messwerte liegen nicht im Bereich")


""" 
Wahrheitstabelle OR

a    b      OR
----------------
W    W      W 
W    f      W
f    f      F
f    w      W

"""
city = "Hamburg"
if city.startswith("S") or city.endswith("g"):
    print("Stadt ist S oder g")
