from __future__ import annotations

import math
import originpro
import csv



class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self._intern = 10  # _ hat internen Charakter

    def __add__(self, other: Vector):
        """Überlade + Operator. other ist der andere Vector."""
        v = Vector(self.x + other.x, self.y + other.y)
        return v

    def __str__(self):
        """Strings-Repräsentation eines Objekts. 
        Immer, wenn Objekt ausgedruck wird, soll das der Name 
        des Objekts sein
        """
        return f"Vector {self.x=}, {self.y=}"

    # @property 
    # def x(self):
    #     return self._x
    
    # @x.setter
    # def x(self, value):
    #     if value > 0:
    #         self._x = value
    #     else:
    #         self._x = 0
 
    def distance(self):
        return math.hypot(self.x, self.y)
    
v1 = Vector(0, 0)
v2 = Vector(4, 0)
# v1.set_x(10) in Java/C++ ist das die Schnittstelle
v1.x = 7
print(v1.x)
v1._intern = 10

# Operatoren-Overloading
"a" + "b"
v3 = v1 + v2
print(v3)


x = 32
print(f"{x=}")