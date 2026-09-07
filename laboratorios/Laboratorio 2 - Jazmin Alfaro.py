# Ejercicio 1: Numero Divisible
def numDivisible(num1, num2):
    if num2 == 0:
        return False
    return num1 % num2 == 0
    
print("\nEjercicio 1: ", numDivisible(27, 5))  # False

# Ejercicio 2: Edad
def clasificar(edad):
    if 0 <= edad <= 3:
        return "Bebé"
    elif 4 <= edad <= 12:
        return "Niño(a)"
    elif 13 <= edad <= 17:
        return "Adolescente"
    elif 18 <= edad <= 30:
        return "Adulto joven"
    elif 31 <= edad <= 65:
        return "Adulto"
    elif edad > 65:
        return "Adulto mayor"
    else:
        return "Edad no válida"

edad = int(input("\nEjercicio 2: Clasificación por edad\nIngrese la edad: "))
print(clasificar(edad))


# Ejercicio 3: Año bisiesto
print("\nEjercicio 3: Año bisiesto")

def esBisiesto(anno):
    if not isinstance(anno, int) or anno <= 0:
        return False
    return (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0)
print(" - EJEMPLO 1: ", esBisiesto(2008), # True
      "\n - EJEMPLO 2: ", esBisiesto(2025))  # False


# Ejercicio 4: Menú calculadora
def leerOpcion():
    while True:
        print("\nMenú Calculadora:",
              "\n1. Suma",
              "\n2. Resta",
              "\n3. Multiplicación",
              "\n4. Potencia",
              "\n5. División",
              "\n6. División entera",
              "\n0. Salir\n")

        try:
            opcion = int(input("Ingrese una opción: "))
            if 0 <= opcion <= 6:
                return opcion
        except ValueError:
            pass

        print("\n(!) Entrada Inválida. Ingrese un número entero entre 0 y 6\n")

def leerNumero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("\n(!) Entrada Inválida, ingrese un número válido.\n")
            
def calculadora():
    opcion = -1

    while opcion != 0:
        opcion = leerOpcion()

        if opcion == 0:
            print("\nAdiós!\n")
            break
        else:
            a = leerNumero("Ingrese el primer número: ")
            b = leerNumero("Ingrese el segundo número: ")

            if opcion == 1: # SUMA
                print("\nResultado de la suma:", a + b)
            elif opcion == 2: # RESTA
                print("\nResultado de la resta:", a - b)
            elif opcion == 3: # MULTIPLICACION
                print("\nResultado de la multiplicación:", a * b)
            elif opcion == 4: # POTENCIA
                print("\nResultado de la potencia:", a ** b)
            elif opcion == 5 or opcion == 6: # VALIDACION B!= 0
                while b == 0:
                    print("\n(!) Entrada inválida. No se puede dividir entre cero.\n")
                    b = leerNumero("Ingrese el segundo número: ")
                if opcion == 5: # DIVISION
                    print("\nResultado de la división:", a / b)
                else:  # DIVISION ENTERA
                    print("\nResultado de la división entera:", a // b)
calculadora()