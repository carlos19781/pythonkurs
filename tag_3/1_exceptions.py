# Look before you leap

d = {
    "a": 1,
    "b": 3
}

if "c" in d:
    print(d["c"])
else:
    print("der Key c ist nicht vorhanden")

# Try Ansatz
try:
    print(d["c"])
except:
    print("der Key c ist nicht vorhanden")

print("hallo")


    