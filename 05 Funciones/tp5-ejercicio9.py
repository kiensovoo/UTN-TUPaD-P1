# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius}°C equivalen a {fahrenheit}°F")


celsius_a_fahrenheit(
    int(input("Ingresa tu temperatura en Celsius y la convertiré a Fahrenheit: ")))
