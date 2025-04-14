# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas} horas")


segundos_a_horas(
    int(input("Ingresa una cantidad de segundos y los convertiré a horas")))