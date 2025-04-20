"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
contador_par = 0
contador_impar = 0
contador_positivo = 0
contador_negativo = 0

for total_numeros in range(0, 100):
    try:
        num = int(input("Ingresa un número entero"))

        if num % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1

        if num > 0:
            contador_positivo += 1
        else:
            contador_negativo += 1
    except:
        input("Ocurrió un error! Recuerda que debes elegir un número.")
        input("Se restó de los 100 numeros a indicar.")


print(f"Tienes en total:\n {contador_par} numeros pares\n{contador_impar} numeros impares\n{contador_positivo} numeros positivos\n{contador_negativo} numeros negativos")
