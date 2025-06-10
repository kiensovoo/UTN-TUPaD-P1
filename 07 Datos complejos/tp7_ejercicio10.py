"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

invertido = {capital: pais for pais, capital in original.items()}

print(f"Original: {original}")
print(f"Invertido: {invertido}")