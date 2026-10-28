from bisect import insort

# Cada cliente: (nombre_normalizado, turno, nombre, edad, boletos)
clientes = []
turno = 0


def leer_entero(mensaje, minimo): 
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"Ingrese un número mayor o igual a {minimo}.")
        except ValueError:
            print("Ingrese un número entero válido.")

def registrar():
    global turno

    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    edad = leer_entero("Edad: ", 0)
    boletos = leer_entero("Boletos a comprar: ", 1)

    turno += 1
    insort(clientes, (boletos, turno, nombre.casefold().capitalize(), edad, boletos))
    print("Cliente registrado.")

def mostrar_cola():
    if not clientes:
        print("La cola está vacía.")
        return

    # Menor edad primero; en caso de empate, orden de registro.
    cola = sorted(clientes, key=lambda cliente: (cliente[3], cliente[1]))

    for posicion, (_, _, nombre, edad, boletos) in enumerate(cola, start=1):
        print(f"{posicion}. {nombre}: {edad} años, {boletos} boletos.")

def buscar():
    if not clientes:
        print("No hay clientes registrados todavia.")
        return
    texto = input("Nombre a buscar: ").strip().lower()

    for _, _, nombre, edad, boletos in clientes:
        if nombre.lower().startswith(texto):
            print(f"{nombre}: {edad} años, {boletos} boletos.")

    if not any(nombre.lower().startswith(texto) for _, _, nombre, _, _ in clientes):
        print("No se encontraron nombres relacionados.")

def ver_totales():
    print(f"Totales:\nClientes registrados: {len(clientes)}"
          f"\nBoletos a comprar: {sum(cliente[4] for cliente in clientes)}"
          f"\nBoletos gratis: {sum(cliente[3] < 12 for cliente in clientes)}")

def ejecutar_menu(menu, acciones, salida):
    print(menu)

    while True:
        opcion = input("\nElige una opción o presiona 0 para ver el menú: ").strip()

        if opcion == salida:
            return
        if opcion == "0":
            print(menu)
        elif opcion in acciones:
            acciones[opcion]()
        else:
            print("Opción inválida. Presiona 0 para ver el menú.")

def menu_cine():
    menu = ("\nMENÚ DE CINE:\n"
            "1. Registrarse\n"
            "2. Mostrar cola\n"
            "3. Buscar por nombre\n"
            "4. Ver totales\n"
            "5. Volver")
    
    acciones = {"1": registrar,"2": mostrar_cola,"3": buscar,"4": ver_totales}
    ejecutar_menu(menu, acciones, "5")

def main():
    menu = "\nMENÚ INICIAL\n1. Cine\n2. Salir"

    try:
        ejecutar_menu(menu, {"1": menu_cine}, "2")
    except (EOFError, KeyboardInterrupt):
        pass

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()