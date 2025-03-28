# Ejercicio 1
# Se utiliza el comando print para imprilir Hola Mundo!
print("Hola Mundo!")

# Ejercicio 2
# Se define variable nombre, almacenando su valor, el cual es asignado por el usuario, como un string.
nombre = str(input("Ingresa tu nombre, por favor."))
# Se imprime el nombre utilizando un f string.
print(f"Hola, {nombre}!")

# Ejercicio 3
# Se definen variables y se almacenan según su tipo de dato.
nombre = str(input("Ingresa tu nombre"))
apellido = str(input("Ingresa tu apellido"))
edad = int(input("Ingresa tu edad"))
residencia = str(input("Ingresa tu lugar de residencia"))

# Se imprime lo solicitado utilizando un f string.
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# Ejercicio 4
# Se definen variables. El valor de radio lo da el usuario a través de un input.
radio = int(input("Ingresa el radio del circulo"))
# Se utilizan las formulas para obtener área y perímetro.
area = (3.1416 * radio ** 2)
perimetro = (2 * 3.1416 * radio)

# Se imrpimen los resultados con un f string.
print(f"El area del circulo es {area} y su perimetro es {perimetro}")

# Ejercicio 5
# Se define la varaible segundos. Su valor lo da el usuario y se almacena como entero.
segundos = int(input("Ingresa una cantidad de segundos y la pasaré a horas"))

# Se utiliza la conversión de segundos a horas. Se almacena el resultado en la variable horas
horas = segundos / 3600

# Se imprime el resultado con un f string.
print(f"{segundos} segundos equivalen a {horas} horas")

# Ejercicio 6
# Se define la variable número. Su valor es almacenado como un entero a través del usuario.
numero = int(input("Ingrese un número: "))

# Puesto así ya que no aprendimos los bucles en python.
# Se imrpime la tabla de multiplicar hasta el 10. Linea por linea.
print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} * 1 = {numero * 1}")
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5 = {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10 = {numero * 10}")

# Ejercicio 7

# Se definen las variables num1 y num2.
num1 = int(input("Ingresa el primer numero. Debe ser distinto de 0"))
num2 = int(input("Ingresa el segundo numero. Debe ser distinto de 0"))

# Se utilizan operaciones matemáticas para almacenar resultados de cada operación en una variable.
sumar = num1 + num2
restar = num1 - num2
multiplicar = num1 * num2
dividir = num1 / num2

# Se imprime cada resultado con un f string.
print(f"Los numeros sumados da: {sumar}")
print(f"Los numeros restados da {restar}")
print(f"Los numeros multiplicados da {multiplicar}")
print(f"Los numeros divididos da {dividir}")

# Ejercicio 8
# Se definen varaibles. Se almacena como float porque pueden llevar coma.
altura = float(input("Ingresa tu altura en metros"))
peso = float(input("Ingresa tu peso actual en kilogramos"))

# Se utiliza la formula para calcular el IMC y se almacena en la variable imc.
imc = peso / (altura ** 2)

# Se imprime el resultado con un f string.
print(f"Tu IMC calculado es de {imc}")

# Ejercicio 9
# Se define la variable y, a su vez, se pide el ingreso del dato de temperatura en grados C.
temperaturaCelsius = int(input("Ingresa la temperatura en grados celsius."))
# Se convierte Celsius a Fahrenheit.
temperaturaFahrenheit = ((9/5) * temperaturaCelsius + 32)

# Se imprime el resultado con un f string.
print(f"El equivalente de {temperaturaCelsius}°C en Fahrenheit es de {temperaturaFahrenheit}")

# Ejercicio 10
# Se definen variables y se almacenan como float al poder llevar coma.
nota1 = float(input("Ingresa el primer numero"))
nota2 = float(input("Ingresa el segundo numero"))
nota3 = float(input("Ingresa el tercer numero"))

# Se promedia sumando las notas y dividiendo por la cantidad total que hay (3)
promedio = (nota1+nota2+nota3) / 3

# Se imprime el resultado del promedio utilizando un f string.
print(f"El promedio de esas tres notas es de {promedio}")
