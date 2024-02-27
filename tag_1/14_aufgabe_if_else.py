import random 

# random.seed(0)

random_number = random.randint(1, 6)
print(random_number)

# Aufgabe: in welchen Wertebereich fällt die Zahl
# 1 - 4: A
# 5 - 6: B
# Aussage: die Zahl 4 ist im Wertebereich A

if random_number <= 4:
    print(f"A: {random_number}")
else:
    print(f"B: {random_number}")