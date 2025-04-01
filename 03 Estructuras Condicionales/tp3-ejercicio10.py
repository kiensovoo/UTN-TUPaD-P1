'''
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
'''

hemisferio = input("¿En cuál hemisferio te ubicas? (N/S)")
mes = int(input("Ingresa el numero del mes"))
dia = int(input("Ingresa el numero del día"))

if hemisferio == 'N':
    if (mes == 12 and 21 <= dia <= 31) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Invierno"
    elif (mes == 3 and 21 <= dia <= 31) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 12 and (mes != 12 or dia <= 20)):
        estacion = "Otoño"

elif hemisferio == 'S':
    if (mes == 12 and 21 <= dia <= 31) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Verano"
    elif (mes == 3 and 21 <= dia <= 31) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 12 and (mes != 12 or dia <= 20)):
        estacion = "Primavera"

print(f"Según tu hemisferio y fecha actual, estás en la estación {estacion}")
