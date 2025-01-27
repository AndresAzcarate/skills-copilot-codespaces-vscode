# Necesito una funcion para convertir Celsius a Fahrenheit

from flask import Flask, jsonify

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    """
    Convierte grados Celsius a Fahrenheit.

    :param celsius: Grados Celsius.
    :return: Grados Fahrenheit.
    """
    return (celsius * 9/5) + 32

@app.route('/')
def convert_temperature():
    celsius = 20
    fahrenheit = celsius_to_fahrenheit(celsius)
    return jsonify(fahrenheit)

if __name__ == '__main__':
    app.run(debug=True)