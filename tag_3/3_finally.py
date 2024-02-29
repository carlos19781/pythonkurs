""" 
Finally: zum Aufräumen
"""
try:
    32 / 0
except ValueError as e:
    print("Value Error ist aufgetreten")
finally:
    print("Finally wird ausgeführt")