# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

print("Bienvenido! Calcularé la suma de todos los números comprendidos entre 0 y un número entero positivo")
print("que tú mismo me darás! (tu número estará incluido en la suma")
while True:
    try:
        num = int(
            input("Ingresa un número entero"))
        if num >= 0:
            break
        else:
            print("Error! El número debe ser positivo o igual a 0.")
    except:
        input("Ocurrió un error! Recuerda que debes elegir un número.")

suma = 0
for numeros in range(0, num+1):
    suma += numeros

print(f"La suma de tus numeros es de {suma}")
