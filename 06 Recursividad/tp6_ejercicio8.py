"""
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
"""

def contar_digito(num, digito):
    if num == 0:
        return 0
    else:
        return (num % 10 == digito) + contar_digito(num // 10, digito)



n = int(input("Ingresa un número entero positivo: "))
d = int(input("Ingresa un digito entre 0 y 9: "))

if 0 > d > 9:
    print("El dígito debe estar entre 0 y 9.")
elif n < 0:
    print("El número debe ser positivo.")
else:
    print(f"El dígito {d} aparece {contar_digito(n, d)} veces en el número {n}")

