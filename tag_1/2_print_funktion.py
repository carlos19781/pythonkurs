# print Funktion

# Seperator
print("hallo", "welt", 3.1, sep=",")  # sep gibt das Trennungszeichen an

# end: Zeilenende
print("x", end="")  #  default Zeilenende end="\n"
print("y", end="")
print("z")

# Beispiel: Programm addiert zwei zahlen
x = 10 
y = 19
result = x + y

print("Das Ergebnis der Operation ist:", end="")  # 3
print("Ergebnis:", result)   # 3\n
