# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

while True:
    try:
        numero = int(input("Ingresá un número entero: "))
        break
    except:
        print("Error! No pusiste un número valido.")


es_negativo = numero < 0
numero = abs(numero)

numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10

# Si el numero original era negativo, lo multiplicamos por -1 para también hacerlo negativo.
# ya que habiamos usado un abs(numero)
if es_negativo:
    numero_invertido *= -1

print(f"Tu numero invertido resulta en: {numero_invertido}")
