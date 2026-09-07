# Laboratorio 1 – Primeros Paso en Python

# Nombre: Jazmin Alfaro Castañeda
# Curso: Principios de Programación 1
# Profesor: Bryan Hernandez Sibaja 
# Fecha: 21/07/2026

# ===== EJERCICIO 1: Conversión de Temperatura =====
#Nota: para ver la version extensa, quitar el # al inicio de la version corta 
# y agregar el # al inicio de la version extensa.

"""version extensa:
def celsiusAFahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit
temperatura = float(input("Ingrese la temperatura en Celsius: "))
resultado = celsiusAFahrenheit(temperatura)
print("La temperatura en Fahrenheit es:", resultado)
#"""

#""" version corta:
def celsiusAFahrenheit(celsius):
    return celsius * 9 / 5 + 32
print(celsiusAFahrenheit(32))
#"""

# ===== EJERCICIO 2: Calcular Área de un Triángulo =====
"""version extensa:
def areaTriangulo(base, altura):
    return (base * altura) / 2

base = float(input("Ingresa la base de tu triangulo: "))
altura = float(input("Ingresa la altura de tu triangulo: "))

area = areaTriangulo(base, altura)
print("El área del triángulo es:", area)
#"""

#""" version corta:
def area_triangulo(base, altura):
    return (base * altura) / 2
print("El área del triángulo es:", area_triangulo(10, 15))
#"""s

# ===== EJERCICIO 3: Saludo Personalizado =====
"""version extensa:
def saludo():
    nombre = input("Hey! ¿Cuál es tu nombre? ")
    apellido1 = input("¿Y tu primer apellido? ")
    apellido2 = input("Ahora tu segundo apellido: ")
    edad = input("¿Qué edad tienes? Te ves joven! ")
    ubicacion = input("Sin querer invadir tu privacidad... ¿De dónde eres? 👀 ")
    cumpleanos = input("¿Cuándo es tu cumpleaños? ¡Para felicitarte! ")
    input(f"Ahora tu numero de tarjeta de crédito, \n"
          f"junto con la fecha de vencimiento y el CVV, por favor. \n"
          f"(Es broma, no lo hagas jajaja)")

    print(f"\nAhora sí, hola {nombre} {apellido1} {apellido2}!\n"
          f"Tienes {edad} años. (La juventud está en el interior, no te preocupes!)\n"
          f"Eres de {ubicacion}.\n"
          f"Y cumples el {cumpleanos}.\n"
          f"Mucho gusto en conocerte!")
saludo()
#"""

#"""#version corta:
def saludo(nombre, apellido1, apellido2, edad, ubicacion, cumpleanos):
    return (
        f"Hola {nombre} {apellido1} {apellido2}\n"
        f"Tienes {edad} años.\n"
        f"Eres de {ubicacion}.\n"
        f"Y cumples el {cumpleanos}.\n"
        f"Mucho gusto en conocerte!\n"
    )
print(saludo("Daniel", "Rodríguez", "López", 18, "Cartago", "25 de abril"))
#"""

# ===== EJERCICIO 4: Cálculos Matemáticos =====
"""#version extensa:

a = int(input("Ingrese el numero A: "))
b = int(input("Ingrese el numero B: "))
def calculos_matematicos(a, b):
    print("La suma es =", a + b)
    print("La resta es =", a - b)
    print("La multiplicacion es =", a * b)
    print("La division es =", a / b)
    print("La division entera es =", a // b)
    print("La potencia es =", a ** b)
    print("El modulo (Residuo) es =", a % b)

calculos_matematicos(a, b)
#"""

#"""version corta:
def calculosMatematicos(a, b):
    print("La suma es =", a + b)
    print("La resta es =", a - b)
    print("La multiplicacion es =", a * b)
    print("La division es =", a / b)
    print("La division entera es =", a // b)
    print("La potencia es =", a ** b)
    print("El modulo (Residuo) es =", a % b)

calculosMatematicos(5, 2)
#"""

# ===== EJERCICIO 5: Menú Calculadora =====
"""version extensa:
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un numero entero positivo: "))
tabla_multiplicar(numero)

#"""

#"""version corta:
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(2)
#"""