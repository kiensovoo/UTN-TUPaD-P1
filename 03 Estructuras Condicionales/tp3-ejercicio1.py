#  Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#  deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Se define la variable y se solicita la edad al usuario.
edadUsuario = int(input("Ingresa tu edad"));

# Se imprime Es mayor de edad en caso de que la edad sea mayor a 18.
if edadUsuario > 18:
    print("Es mayor de edad")