# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma = 0

print("Bienvenido! Calcularé la media de 100 números que me des.")
print("Recuerda que esos 100 son INTENTOS. si pones algo que no es un número, se restará de tus intentos.")

for intentos in range(0, 100):
    try:
        num = int(input("Ingresa un número entero"))
    except:
        input("Ocurrió un error! Recuerda que debes elegir un número.")
    suma += num

media_numeros = suma / 5
print(f"La media de tus numeros es de: {media_numeros}")
