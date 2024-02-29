import math

class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def distance(self):
        return math.hypot(self.x, self.y)

   
p1 = Vector(3, 5)
print("Das Objekt p1 hat folgende Attribute:", p1.__dict__)
p1.distance()  # Methode distance

print(p1.x)  # Attribut x ausgeben
p1.x = 100
print(p1.distance())

x = str("hasdfjaslkdf")
x.capitalize()