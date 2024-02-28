""" 
IN-Operator (erzeugt boolschen Wert (True oder False))
Befindet sich ein Element in einer Sequenz, als String/Liste
"""
messpunkt = "12.3 mm"

if "mm" in messpunkt:
    print("in diesem String befindet sich das Wort mm")


values = [3, 21, 9]
if 9 in values:
    print("Die 9 befindet sich in values")

# Alternative zum In-Operator
for v in values:
    if v == 9:
        print("Die 9 ist enthalten")
