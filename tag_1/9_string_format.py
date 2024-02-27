""" 
String formatieren

https://www.w3schools.com/python/ref_string_format.asp
"""
value = 100_000 # 100_000_000
kilo = 299
# Das Auto kostet 100000 Euro

print("Das Auto kostet", value, "Euro")

output_str = "Das Auto kostet {:,} Euro und wiegt {} Kilo"
final_str = output_str.format(value, kilo)
print(final_str)

output_str = "Der Sensor {} hat den Messwert: {:.3f}"
messwert = 0.2322434374
name = "Sensor 1"
print(output_str.format(name, messwert))

# Bankers Rounding (Default Rundung von IEEE 754)
print(round(4.5, 1))
print(round(5.5, 1))
