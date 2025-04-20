# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de tus tres numeros es: {promedio}")


calcular_promedio(int(input("Ingresa tu primer valor: ")),
                  int(input("Ingresa tu segundo valor: ")),
                  int(input("Ingresa tu tercer valor: ")))
