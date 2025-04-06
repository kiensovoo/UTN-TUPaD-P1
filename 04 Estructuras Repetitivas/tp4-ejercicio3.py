# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

def validar_numero():
    while True:
        try:
            num = int(
                input("Ingresa un número entero"))
            return num
        except:
            input("Ocurrió un error! Recuerda que debes elegir un número.")


valor1 = validar_numero()
valor2 = validar_numero()

suma = 0

for numeros in range(valor1 + 1, valor2):
    suma += numeros

print(
    f"La suma de todos los números enteros entre {valor1} y {valor2} es de {suma}")
