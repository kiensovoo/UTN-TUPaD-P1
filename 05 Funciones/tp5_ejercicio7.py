# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    tupla_suma = (a+b,)
    tupla_resta = (a-b,)
    tupla_multiplicar = (a*b,)
    tupla_dividir = (a/b,)

    print(f"Si sumamos esos dos numeros nos da: {tupla_suma}")
    print(f"Si restamos esos dos numeros nos da: {tupla_resta}")
    print(f"Si multiplicamos esos dos numeros nos da: {tupla_multiplicar}")
    print(f"Si dividimos esos dos numeros nos da: {tupla_dividir}")


operaciones_basicas(int(input("Ingresa un primer valor: ")),
                    int(input("Ingresa un segundo valor: ")))
