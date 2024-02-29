""" 
Fehler im Programm (Ausnahmen)

Arten von Fehler:
1. Syntax-Error (kann man nix machen)
2. Logik-Fehler (Endlos-Loop, kann man nix machen) Muss testen
3. Runtime-Error (Laufzeit-Fehler)
"""
import dis 

def fn():
    x = 23
    y = x + 34

# print(dis.dis(fn))
user_input = int("0")
values = [1, 2, 3, 4]

try:
    z = 3 / user_input
    x = values[user_input]
except:
    print("Fehler wurde abgefangen")