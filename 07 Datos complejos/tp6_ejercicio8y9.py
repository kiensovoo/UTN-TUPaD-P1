# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
# los valores almacenados.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza

        while actual is not None:
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
        print("None")

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior


lista = ListaEnlazada()
lista.insertar_al_inicio("valu")
lista.insertar_al_inicio("li")

print(f"Elementos de la lista:")
lista.mostrar()

lista.invertir()
print("\nLista invertida:")
lista.mostrar()
