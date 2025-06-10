"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""

cantidad_de_alumnos = 3

print("-"*50)
print(f"Programa para promediar notas de {cantidad_de_alumnos} alumnos.")

notas_alumnos = {}

for i in range(cantidad_de_alumnos):
    alumno = input(f"Ingresa el nombre del alumno n°{i+1}: ")
    nota = input("Ingresa las notas del alumno de esta manera: 10,7,8. Sin espacios y usa las comas.\n")

    nota_numerica = tuple(float(nota) for nota in nota.split(",")) #Separa las notas por "," y se añaden como tupla
    notas_alumnos[alumno] = nota_numerica # Añadimos la nota y el alumno al diccionario
    

for alumno, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas) # Suma las notas y se divide por la longitud
    print(f"Promedio del alumno/a {alumno}: {promedio:.2f}") # Se imprime el promedio con 2 decimales.