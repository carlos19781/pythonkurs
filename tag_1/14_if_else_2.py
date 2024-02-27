""""
if, elif, else


"""
user_eingabe = "2"


if user_eingabe:
    print("Der User hat was eingeben", user_eingabe)


if user_eingabe == "2":
    print("Die Eingabe war 2")
elif user_eingabe == "3":
    print("Die Eingabe war 3")
elif user_eingabe == "4":
    print("Die Eingabe war 4")
else:
    print("weder noch")

a = 3 
b = 7
c = 9 

# mit Klammern komplexe Ausdrücke gliedern
if (a * b) - 65 > 10 or (c / b <= 100):
    print("Aussage ist wahr")