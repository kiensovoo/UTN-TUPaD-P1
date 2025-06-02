# 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
# balanceados usando una pila.

class Pila:
    def __init__(self):
        self.elementos = []

    def encolar(self, elementos):
        self.elementos.append(elementos)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_frente(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None


def esta_balanceado(cadena):
    pila = Pila()
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in cadena:
        if caracter in '([{':
            pila.encolar(caracter)
        elif caracter in ')]}':
            tope = pila.desencolar()
            if tope != pares[caracter]:
                return False

    return pila.esta_vacia()


print(esta_balanceado("({[]})"))
