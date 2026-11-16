def vaciar(pila):
    if not pila:
        return 0, 0

    titulo, paginas = pila.pop()
    print(f"{titulo}: {paginas} páginas")
    total, cantidad = vaciar(pila)
    return total + paginas, cantidad + 1


while True:
    opcion = input("\n1. Biblioteca\n2. Salir\nOpción: ")

    if opcion == "2":
        break
    if opcion != "1":
        print("Opción inválida")
        continue

    pila = []
    while True:
        opcion = input("\n1. Apilar libro\n2. Vaciar pila\nOpción: ")

        if opcion == "1":
            titulo = input("Título: ")
            try:
                paginas = int(input("Páginas: "))
            except ValueError:
                print("Ingrese un número entero")
                continue
            pila.append((titulo, paginas))

        elif opcion == "2":
            total, cantidad = vaciar(pila)
            print(f"Total de páginas: {total}\nLibros en la pila: {cantidad}")
            break
        else:
            print("Opción inválida")
