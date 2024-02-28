""" 
Funktionsobjekt
Grundprinzip der funktionalen Programmierung:
Funktionen sind "First class citziens"

https://de.wikipedia.org/wiki/Funktionale_Programmierung
"""
def fn(a):
    print(a)


def g(parameter, value):
    parameter(value)

x = 3  # Objekt der Klasse Integer
fn  # Funktionsobjekt

f = fn
f(3)
fn(4)
g(fn, 100)