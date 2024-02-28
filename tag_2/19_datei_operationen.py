""" 
Datei öffnen

pathlib.Path ist eine Klasse zum Arbeiten mit Verzeichnissen
"""
from pathlib import Path 
current_dir = Path(__file__).parent

print("Aktuelles Verzichnis:", current_dir)

# Datei lesen (mode=r)
# Datei öffnen
f = open(current_dir / "data.txt", mode="r", encoding="utf-8")
content = f.read() # liest komplette Datei ein
print(content)
f.close()

# Datei lesen (mode=r)
# Besser so zu schreiben (close ist nicht nötig, da with selber macht)
with open(current_dir / "data.txt", mode="r", encoding="utf-8") as f:
    content = f.read() # liest komplette Datei ein
    print(content)


# Datei schreiben (mode=w)
# falls Datei nicht existiert, wird die Datei angelegt
with open(current_dir / "data_neu.txt", mode="w", encoding="utf-8") as f:
    f.write("hallo, das ist mein neues File")
