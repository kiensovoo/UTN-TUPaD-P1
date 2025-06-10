"""
Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.

"""

def consultar_stock():
    producto = input("¿De cuál producto deseas saber el stock?: ")
    if producto in stock.keys():
        print(f"Stock de {producto}: {stock[producto]}")
    else:
        print("No existe ese producto.")

def agregar_producto():
    producto = input("Ingresa el nombre del producto: ")
    if producto not in stock.keys():
        while True:
            try:
                unidades = int(input("Ingresa la cantidad de unidades en número: "))
                stock[producto] = unidades
                return
            except ValueError:
                print("Intenta de nuevo, pero esta vez solo un numero natural!")
    else:
        print("Ya hay un producto con ese nombre.")

def agregar_unidades():
    producto = input("Ingresa el nombre del producto: ")
    if producto in stock.keys():
        while True:
            try:
                unidades = int(input("Cantidad de unidades a agregar: "))
                stock[producto] += unidades
                return
            except ValueError:
                print("Error! Intenta con un numer natural.")
    else:
        print("No existe un producto con ese nombre.")

stock = {}
while True:
    print("-"*50)
    print("Menú de opciones:")
    print("0. Salir")
    print("1. Consultar stock")
    print("2. Agregar nuevo producto")
    print("3. Agregar unidades")

    opcion = input("Ingresa tu opción: ")

    if opcion == "0":
        break
    elif opcion == "1":
        consultar_stock()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        agregar_unidades()
    else:
        print("La opción elegida no es correcta. Escribe solo el número que ves en pantalla.")