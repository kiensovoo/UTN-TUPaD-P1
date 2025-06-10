"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""

print("-"*50)
frase = input("A continuación ingresa tu frase:\n")
# Separamos la frase por espacios en blanco.
# utilizamos set para obtener las palabras únicas

palabras = frase.split() # Separamos las palabras por espacios vacíos
nueva_frase = set(frase.strip().split()) 

frecuencias = {} 

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1 # Si ya estaba en el diccionario, se suma 1
    else:
        frecuencias[palabra] = 1 # Si no está en el diccionario, se encontró 1 vez por lo menos.

print(f"Palabras únicas: {nueva_frase}")
print(f"Diccionario de frecuencias de cada palabra: {frecuencias}")
