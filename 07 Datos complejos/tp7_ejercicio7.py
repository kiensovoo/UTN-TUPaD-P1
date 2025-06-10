"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""


print("-"*50)
print("Análisis de estudiantes que aprobaron parciales")
print("Se aprueba con 6 o más. Máxima nota: 10")
print("-"*50)

# Representan IDs o podría ser el legajo.
parcial_1 = {101, 102, 103, 104, 105, 106, 107}
parcial_2 = {103, 104, 105, 108, 109, 110}

print(f"Estudiantes que aprobaron Parcial 1: {parcial_1}")
print(f"Estudiantes que aprobaron Parcial 2: {parcial_2}")
print()

ambos_parciales = parcial_1 & parcial_2  # Intersección de las dos varaibles
solo_uno = (parcial_1 ^ parcial_2)       # Diferencia simétrica
al_menos_uno = parcial_1 | parcial_2     # Unión

print("Resultados:")
print(f"• Aprobaron AMBOS parciales: {ambos_parciales}")
print(f"• Aprobaron SOLO UNO de los dos: {solo_uno}")
print(f"• Aprobaron AL MENOS UN parcial: {al_menos_uno}")

