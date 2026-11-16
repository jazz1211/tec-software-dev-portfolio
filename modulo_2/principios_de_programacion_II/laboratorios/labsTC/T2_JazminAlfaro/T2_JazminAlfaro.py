productos = [
    ("Café", 1500),
    ("Queque", 3000),
    ("Empanada", 2000),
    ("Jugo", 500)
]

def buscar(inicio, total, presupuesto, combo):
    if total == presupuesto:
        return True

    for i in range(inicio, len(productos)):
        nombre, precio = productos[i]
        nuevo_total = total + precio

        if nuevo_total > presupuesto:
            print(f"Añadiendo {nombre} ({precio})... "
                  "¡Se pasó! Retrocediendo...")
            continue

        print(f"Añadiendo {nombre} ({precio})... Total: {nuevo_total}")
        combo.append(nombre)

        if buscar(i + 1, nuevo_total, presupuesto, combo):
            return True

        combo.pop()
        print(f"Quitando {nombre}... Retrocediendo")

    return False


while True:
    opcion = input("\n1. Armar combo\n2. Salir\nOpción: ")

    if opcion == "2":
        break
    if opcion != "1":
        print("Opción inválida")
        continue

    try:
        presupuesto = int(input("Presupuesto exacto: "))
        if presupuesto <= 0:
            print("Ingrese un presupuesto positivo")
            continue
    except ValueError:
        print("Ingrese un número entero")
        continue

    combo = []
    if buscar(0, 0, presupuesto, combo):
        print(f"¡Combo encontrado! [{', '.join(combo)}]. "
              f"Total exacto: {presupuesto}.")
    else:
        print("No existe un combo con ese presupuesto exacto.")