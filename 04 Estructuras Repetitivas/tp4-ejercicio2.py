# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.


while True:
    try:
        num = int(
            input("Ingresa un número entero y te diré la cantidad de digitos que tiene"))
        break
    except:
        input("Ocurrió un error! Recuerda que debes elegir un número.")

num_digitos = abs(num)

contador = 0

if num_digitos == 0:
    contador = 1
else:
    while num_digitos > 0:
        num_digitos //= 10
        contador += 1

print(f"La cantidad de digitos de {num} es de {contador}")
