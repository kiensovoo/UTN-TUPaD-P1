"""
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.

Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
"""

def es_palindromo(palabra):
    #Si tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si la primera y última letra son diferentes, no es palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra sin espacios ni tildes: ").lower()

print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")
