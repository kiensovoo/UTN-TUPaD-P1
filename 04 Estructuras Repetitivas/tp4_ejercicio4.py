# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
num = 1

while num != 0:
    try:
        num = int(input("Ingresa un número entero"))
    except:
        input("Ocurrió un error! Recuerda que debes elegir un número.")
        continue
    suma += num

print(f"La suma de todos tus numeros es de {suma}")
