"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""

def suma_digitos(n):
    if n < 10: # Si n es de un solo dígito, devolver n
        return n 
    else:
        return (n%10) + suma_digitos(n//10)

while True:
    num = int(input("Ingresa un número para calcular la suma de sus digitos: "))
    if num < 0:
        print("El numero debe ser mayor o igual a 0")
    else:
        print(f"La suma de los digitos de {num} es igual a {suma_digitos(num)}")
        break

