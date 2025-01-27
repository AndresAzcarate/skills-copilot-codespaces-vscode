def filter_even_numbers(list):
  """
  Filtra y devuelve los números pares de una lista dada.

  :param lista: Lista de números enteros.
  :return: Lista de números pares.
  """
  return [num for num in list if num % 2 == 0]

# Ejemplo de uso
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print(even_numbers)  # Salida: [2, 4, 6, 8, 10]