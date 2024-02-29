""" 
Raise: Fehler ergeben (Exception selbst auslösen)
"""
import math 

def ellipse_area(a: float, b: float):
    """Berechnung einer Ellipsenfläche.
    
    Args:
        a (float): grosse Halbachse
        b (float): kleine Halbachse
    
    Raises:
        ValueError: wenn b > a
    
    Returns:
        Ellipsenfläche
    """
    if b > a:
        raise ValueError("a muss größer sein als b")
    
    return math.pi * a * b


ellipse_area(4, 4)