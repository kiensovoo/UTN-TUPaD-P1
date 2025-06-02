"""
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique
"""

def fibonacci(n):
    serie = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
        
while True:
    try:
        print("-"*50)
        print("Menú de opciones:")
        print("0. Salir")
        print("1. Mostrar la serie de fibonacci hasta el numero n ")

        opcion = input("Ingresa tu opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            rango = int(input("Ingresa un valor numérico mayor o igual a 0: "))
            if rango >= 0:
                for i in range(rango+1):
                    print(f"Posición {i} = {fibonacci(i)}")
            else:
                print("El rango introducido no es válido! Debe ser un número positivo.")
        else:
            print("Opción no válida")
    except ValueError:
        print("Error! Durante la ejecución del programa introdujiste un número no válido.")