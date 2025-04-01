'''
Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”
'''

# Se define nota y se solicita su valor al usuario.
nota = float(input("Ingresa tu nota."))

# Si la nota es mayor o igual a 6 se imprime  Aprobado. En caso contrario se imprimirá Desaprobado.
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")