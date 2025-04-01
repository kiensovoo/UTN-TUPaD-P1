'''
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
'''

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(moda)
print(mediana)
print(media)

sesgo_positivo = media > mediana < moda
sesgo_negativo = media < mediana < moda
sin_sesgo = media == mediana == moda

if sesgo_positivo == True:
    print("Hay sesgo positivo.")
elif sesgo_negativo == True:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo.")
