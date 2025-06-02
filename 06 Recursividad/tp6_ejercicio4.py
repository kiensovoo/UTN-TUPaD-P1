"""
Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
"""

def convertir_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        #Dividimos el número por 2 y concatenamos el resto
        return convertir_a_binario(n//2) + str(n%2)

while True:
    num = int(input("Ingresa un numero entero positivo: "))

    if num < 0:
        print("El numero no es positivo.")
    else:
        print(f"{num} en binario es {convertir_a_binario(num)}")
        break