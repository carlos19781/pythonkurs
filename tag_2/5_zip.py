"""
mit zip lassen sich mehrere Listen iterieren
"""
names = ["Bob", "Alice"]
grades = [3, 4]
schools = ["ABC", "XYZ"]

for i in range(len(names)):
    print(names[i])
    print(grades[i])
    print(schools[i])

for name, grade, school in zip(names, grades, schools):
    print(name, grade, school)