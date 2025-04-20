"""
4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
años."
"""


class Persona:

    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(
            f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años")


persona_1 = Persona("Valentina", "Argentina", 18)
persona_1.saludar()
