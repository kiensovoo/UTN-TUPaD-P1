"""
Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""

print("-"*50)
print("Bienvenido a tu agenda de contactos. Te pediré que agregues 5 contactos para continuar.")

agenda = {}

for i in range(5):
    nombre = input(f"Ingresa el nombre de tu contacto n°{i+1}\n")
    numero = input("Ingresa el numero a asociar\n")
    agenda[nombre] = numero

print("\nAhora busca un nombre dentro de tus contactos\n")
busqueda = input("Nombre a buscar: ")

if busqueda in agenda.keys():
    print(f"Lo encontré! el número de {busqueda} es {agenda[busqueda]}")
else:
    print(f"{busqueda} no está en tus contactos.")
