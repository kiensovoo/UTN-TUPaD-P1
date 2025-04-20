"""
7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
● Agregar clientes (encolar).
● Atender clientes (desencolar).
● Mostrar el siguiente cliente en la fila
"""

from collections import deque


class Cola:
    def __init__(self):
        self.cliente = deque()

    def esta_vacia(self):
        return len(self.cliente) == 0

    def encolar(self, cliente):
        self.cliente.append(cliente)

    def desencolar(self):
        return self.cliente.popleft() if not self.esta_vacia() else "Está vacía"

    def ver_siguiente(self):
        return self.cliente[0] if not self.esta_vacia() else "Está vacía"


cola_1 = Cola()
cola_1.encolar("valu")
cola_1.encolar("li")

print(f"Siguiente: {cola_1.ver_siguiente()}")
print(f"Se acaba de atender a: {cola_1.desencolar()}")
print(f"Siguiente: {cola_1.ver_siguiente()}")
