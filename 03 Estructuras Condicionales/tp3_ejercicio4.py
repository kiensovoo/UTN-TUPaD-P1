'''
Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
'''

edadUsuario = int(input("Ingresa tu edad"))

if edadUsuario < 12:
    print("Perteneces a la categoría Niño/a")
elif edadUsuario >= 12 and edadUsuario < 18:
    print("Perteneces a la categoría Adolescente")
elif edadUsuario >= 18 and edadUsuario < 30:
    print("Perteneces a la categoría Adulto/a joven")
else:
    print("Perteneces a la categoría Adulto/a")