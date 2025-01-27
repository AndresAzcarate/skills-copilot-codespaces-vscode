# Ejemplo: Funcion para convertir Farhenheit a Celsius

def fahrenheit_to_celsius(fahrenheit):
    """
    Convierte grados Fahrenheit a Celsius.

    :param fahrenheit: Grados Fahrenheit.
    :return: Grados Celsius.
    """
    return (fahrenheit - 32) * 5/9

# Ahora necesito una funcion para convertir Celsius a Kelvin

def celsius_to_kelvin(celsius):
    """
    Convierte grados Celsius a Kelvin.

    :param celsius: Grados Celsius.
    :return: Grados Kelvin.
    """
    return celsius + 273.15