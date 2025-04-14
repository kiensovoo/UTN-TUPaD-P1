# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y
# devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como
# parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

import math


def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El area del circulo es: {area}")


def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo es: {perimetro}")


radio = int(
    input("Ingresa el radio del circulo y calcularé el área y el perímetro"))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
