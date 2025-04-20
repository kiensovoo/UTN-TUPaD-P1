# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    print(f"Tu imc calculado es de: {imc}")


calcular_imc(int(input("Ingresa tu peso en kilogramos: ")),
             float(input("Ingresa tu altura en metros (Ej: 1.80): ")))
