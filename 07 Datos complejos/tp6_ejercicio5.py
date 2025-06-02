# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.

import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        print(f"Area del circulo: {area}")

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        print(f"Perimetro del circulo: {perimetro}")


circulo_1 = Circulo(2)
circulo_1.calcular_area()
circulo_1.calcular_perimetro()
