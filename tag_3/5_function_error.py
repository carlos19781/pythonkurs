def berechnung(a, b):
    """gebe a und b ein. a und b müssen größer als 0 sein."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Die Zahlen müssen Int sein")
    return a / b


try:
    berechnung(3.3, 5)
except ZeroDivisionError as e:
    print(e)


