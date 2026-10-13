# Ejercicio 1: Inventario de Productos
def total_unidades(productos):
    total = 0

    for cant in productos:
        total += cant

    return total

# Ejercicio 2: Películas Populares
def pelis_populares(listaPelis):
    
    resultado = []
    for peli in listaPelis:
        if len(peli) >= 8:
            resultado.append(peli)

    return resultado

# Ejercicio 3: Registro de Ciudades
def registro_ciudades():

    ciudades = []
    cant = int(input("* Ejercicio 3 - Registro de ciudades:\n- Ingrese la cantidad de ciudades que desea registrar: "))

    while True:
        ciudad = input("- Ingrese el nombre de una ciudad: ")
        ciudades.append(ciudad)

        if len(ciudades) == cant:
            break
        
    print("- Ciudades registradas:", str(ciudades).strip('[]').replace("'", ''))

# Ejercicio 4: Contador de vocales
def contar_vocales():
    frase = input("\n* Ejercicio 4 - Contador de vocales:\n- Ingrese una frase: ")
    contador = 0
    vocales = "aeiouAEIOU"
    inverso = ""

    # Construcción del texto en orden inverso
    for caracter in frase:
        inverso = caracter + inverso

    # Conteo de vocales
    for caracter in frase:
        if caracter in vocales:
            contador += 1

    print("- Texto en inverso:", inverso)
    return contador

# Testeo:
listaProd = [12, 8, 15, 20, 5, 10]
print("\n* Ejercicio 1 - Total unidades: ", total_unidades(listaProd))

listaPelis = ["Avatar", "Titanic", "Gladiador", "Cars", "Interstellar", "Up", "Frozen"]
print("\n* Ejercicio 2 - Pelis populares:", str(pelis_populares(listaPelis)).strip("[]").replace("'", ""), "\n")

registro_ciudades()
print("- Cantidad de vocales:", contar_vocales())