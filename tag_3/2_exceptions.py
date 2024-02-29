""" 
Spezifizieren der Ausnahme
"""
user_input = 5
values = [1, 2, 3, 4]

try:
    z = 3 / user_input  # ZeroDivisionError
    x = values[user_input]  # IndexError
except ZeroDivisionError as e:
    print("ZeroDivisionError abgefangen", e)
    z = 1
except (IndexError, ValueError) as e:
    print("ein INdex oder Value Error aufgetreten", e)
    x = values[0]
except Exception as e:
    print("Alle Fehler auffagen")

print("Aktuelle Werte:", x, z)