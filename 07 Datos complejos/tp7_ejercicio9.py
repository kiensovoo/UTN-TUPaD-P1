"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
Permití consultar qué actividad hay en cierto día y hora.

"""

agenda = {
    ("lunes", "09:00"): "Clase de matemáticas",
    ("martes", "10:00"): "Clase de AySO",
    ("miercoles", "09:00"): "Clase de Org. Empresarial",
    ("jueves", "09:00"): "Clase de programación",
}

while True:
    print("-"*50)
    print("Para detener el programa presiona Ctrl+C.")
    try:
        dia = input("Ingresa el día: ").lower()
        hora = input("Ingresa la hora (XX:YY): ")

        clave = (dia, hora)
        if clave in agenda:
            print(f"En el día {dia} a las {hora} tienes el evento: {agenda[clave]}")
        else:
            print("El día elegido no tiene ningún evento o no existe.")
    except KeyboardInterrupt:
        break