# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_aleatorio = random.randint(0, 9)
num = -1
contador = 0

while num != numero_aleatorio:
    try:
        num = int(input("Ingresa un número entre 0 y 9 (incluidos)"))
        if 0 > num or num > 9:
            print("El numero debe estar entre 0 y 9 (incluidos)")
            contador += 1
            continue
        else:
            contador += 1
    except:
        input("Ocurrió un error! Recuerda que debes elegir un número.")
        continue

print(
    f"Te tomó {contador} intentos encontrar al número correcto ({numero_aleatorio})")
