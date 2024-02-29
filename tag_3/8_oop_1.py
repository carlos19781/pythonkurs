"""
Einführung in OOP
In Python ist alles ein Objekt
"""
x = int(3)
y = int(2)
print(type(x))  # ist ein Objekt der Klasse int
print(dir(x), x.to_bytes(1))

class House:
    def get_size(self):
        print("")

house_1 = House()
house_2 = House()
print(dir(house_1))