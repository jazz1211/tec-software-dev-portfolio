# EJERCICIO 1: TARIFA DE TAXI
def tarifa_taxi():
    km = float(input("\n1. Tarifa de Taxi:\n* Ingrese la cantidad de kilómetros recorridos: "))
    tarifaBase = 700

    if km <= 5:
        total = tarifaBase + (km * 650)
    elif km <= 15:
        total = tarifaBase + (5 * 650) + ((km - 5) * 550)
    else:
        total = tarifaBase + (5 * 650) + (10 * 550) + ((km - 15) * 500)

    print(f"* Monto total a pagar: ₡{total:.2f}")

# EJERCICIO 2: APROBAR CRÉDITO
def aprobar_credito():
    nombre = input("\n2. Aprobar Crédito:\n* Ingrese el nombre del solicitante: ")
    salario = float(input("* Ingrese el salario mensual: "))
    antiguedad = int(input("* Ingrese la antigüedad laboral (años): "))
    deudas = bool(int(input("* Posee otras deudas? (1= sí, 0= no): ")))
    cumpleCondiciones = (salario >= 600000) + (antiguedad >= 2) + (not deudas)

    if cumpleCondiciones == 3:
        print(f"\n* {nombre}, su crédito fue APROBADO!")
    elif cumpleCondiciones == 2:
        print(f"\n* {nombre}, su crédito fue APROBADO CON REVISIÓN.")
    else:
        print(f"\n* {nombre}, su crédito fue RECHAZADO.")

# EJERCICIO 3: PAGO SEMANAL
def pago_semanal():
    horas = float(input("\n3. Pago Semanal:\n* Ingrese las horas trabajadas: "))
    pagoHora = float(input("* Ingrese el pago por hora: "))

    if horas <= 40:
        salario = horas * pagoHora
    else:
        horasExtra = horas - 40
        salario = (40 * pagoHora) + (horasExtra * pagoHora * 2)

    print(f"\n* Salario semanal es de: ₡{salario:.2f}")

# EJERCICIO 4: CONVERSIÓN DE DISTANCIAS
def conversion_distancia():
    kilometros = float(input("\n4. Conversión de Kilómetros:\n* Ingrese la cantidad de kilómetros: "))
    metros = kilometros * 1000
    centimetros = kilometros * 100000
    milimetros = kilometros * 1000000

    print("* Conversión:",
        f"\n- Metros: {metros}",
        f"\n- Centímetros: {centimetros}",
        f"\n- Milímetros: {milimetros}\n")

# EJERCICIO 5: POTENCIA DE UN NÚMERO
def potencia_numero():
    base = int(input("\n5. Potencia de un número:\n* Ingrese la base: "))
    exponente = int(input("* Ingrese el exponente: "))
    resFor = 1
    resWhile = 1
    proceso = f"{base}"

    for i in range(exponente):
        resFor *= base
    
    while exponente > 1:
        resWhile *= base
        proceso += f" * {base}"
        exponente -= 1

    resWhile *= base

    print(f"\n* Proceso utilizando FOR: {proceso} = {resFor}",
          f"\n* Proceso utilizando WHILE: {proceso} = {resWhile}")
        
# EJERCICIO 6: SERIE DE NÚMEROS
def serie_numeros():
    numeroInicial = int(input("\n6. Serie de Números:\n* Ingrese el número inicial: "))
    limite = int(input("* Ingrese el límite: "))
    
    print(f"\n* Serie de números desde {numeroInicial} hasta {limite}:")
    i = 0
    
    for numero in range(numeroInicial, limite + 1, numeroInicial): 
        i += 1 
        if numero == limite: 
            print(numero) 
        elif i % 10 == 0: 
            print(numero, end=" →\n") 
        else: print(numero, end=" → ") 
    print()


# EJERCICIO 7: NÚMERO PRIMO
def es_primo():
    numero = int(input("\n7. Número Primo:\n* Ingrese un número entero: "))
    if numero <= 1:
        print(f"* {numero} no es un número primo.")
        return

    for i in range(2, numero):
        if numero % i == 0:
            print(f"* {numero} no es un número primo.")
            return
        
    print(f"* {numero} es un número primo.")

# EJERCICIO 8: MENÚ PRINCIPAL
def main():
    while True:
        opcion = int(input(
            "\nMENU DE OPCIONES:\n"
            "\n1. Tarifa de Taxi"
            "\n2. Aprobar Crédito"
            "\n3. Pago Semanal"
            "\n4. Conversión de Kilómetros"
            "\n5. Potencia de un Número"
            "\n6. Serie de Números"
            "\n7. Número Primo"
            "\n8. Salir\n"
            "\nSeleccione una opción: "
        ))

        if opcion == 1:
            tarifa_taxi()
        elif opcion == 2:
            aprobar_credito()
        elif opcion == 3:
            pago_semanal()
        elif opcion == 4:
            conversion_distancia()
        elif opcion == 5:
            potencia_numero()
        elif opcion == 6:
            serie_numeros()
        elif opcion == 7:
            es_primo()
        elif opcion == 8:
            print("\nGracias por utilizar el programa!\n")
            break
        else:
            print("\n(!) Opción no válida. Intente nuevamente.")

main()
