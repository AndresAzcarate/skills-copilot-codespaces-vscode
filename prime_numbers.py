# Create a sample list of numbers.
# Create a list of prime numbers from the samople list.
# Return the list of prime numbers.
# Example: [1,2,3,4,5,6,7,8,9,10,11] => [2,3,5,7,11]

from flask import Flask, jsonify

app = Flask(__name__)

def filter_prime_numbers(list):
  """
  Filtra y devuelve los números primos de una lista dada.

  :param lista: Lista de números enteros.
  :return: Lista de números primos.
  """
  return [num for num in list if num > 1 and all(num % i != 0 for i in range(2, num))]

@app.route('/')
def get_prime_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    prime_numbers = filter_prime_numbers(numbers)
    return jsonify(prime_numbers)

if __name__ == '__main__':
    app.run(debug=True)