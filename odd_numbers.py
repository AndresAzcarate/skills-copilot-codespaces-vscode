# Write a simple flask app tht return a list of odd numbers from a list of numbers
# Create a function that takes a list of numbers and return only the odd numbers.
# Create a sample list od numbers.
# Create a list of odd numbers from the sample list.
# Return the list of odd numbers.

from flask import Flask, jsonify

app = Flask(__name__)

def filter_odd_numbers(list):      
  """
  Filtra y devuelve los números impares de una lista dada.

  :param lista: Lista de números enteros.
  :return: Lista de números impares.
  """
  return [num for num in list if num % 2 != 0]

@app.route('/')
def get_odd_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = filter_odd_numbers(numbers)
    return jsonify(odd_numbers)

if __name__ == '__main__':
    app.run(debug=True)
