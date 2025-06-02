"""
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""

def fact(num):
    return 1 if num == 0 else num * fact(num-1)

while True:
    try:
        print("-"*50)
        print("Menú de opciones:")
        print("0. Salir")
        print("1. Calcular el factorial de los numeros de 1 hasta n: ")

        opcion = input("Ingresa tu opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            num = int(input("Ingresa un valor numérico mayor o igual a 0: "))
            if num >= 0:
                for i in range(1, num+1):
                    print(f"{i}! = {fact(i)}")
            else:
                print("El rango introducido no es válido! Debe ser un número positivo.")
        else:
            print("Opción no válida")
    except ValueError:
        print("Error! Durante la ejecución del programa introdujiste un número no válido.")
