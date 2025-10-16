# test_app.py
from app import suma

def test_suma_basica():
    """Prueba básica de la función suma."""
    assert suma(2, 3) == 5
