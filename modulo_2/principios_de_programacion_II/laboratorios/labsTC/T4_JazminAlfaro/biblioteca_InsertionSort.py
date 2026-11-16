def ordenar_libros_por_titulo(libros):
    """Ordena libros por título mediante Insertion Sort.

    ▸ PARÁMETROS ───────────────────────────────────────────
    libros (list): Diccionarios con las claves obligatorias "titulo",
        "autor" y "anio_publicacion". Las claves "isbn" y "stock"
        son opcionales. Si falta "stock", se muestra 1.

    ▸ RETORNA ──────────────────────────────────────────────
    None: Imprime los libros en orden ascendente por título.

    ▸ EXCEPCIONES ──────────────────────────────────────────
    KeyError: Si falta alguna clave obligatoria.
    TypeError: Si algún título no es una cadena de texto.
    Ambas validaciones ocurren antes de modificar la lista.

    ▸ COMPLEJIDAD ──────────────────────────────────────────
    • Tiempo: O(n²) en el peor caso; O(n) en el mejor, considerando
      constante el costo de comparar títulos.
    • Espacio: O(L) auxiliar por las cadenas temporales de casefold(),
      donde L es la longitud máxima de un título.

    ▸ EJEMPLO ──────────────────────────────────────────────
    >>> libros = [
    ...     {"titulo": "Temporada de huracanes", "autor": "Fernanda Melchor", "anio_publicacion": 2017},
    ...     {"titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "anio_publicacion": 1995}]
    >>> ordenar_libros_por_titulo(libros)
    Ensayo sobre la ceguera - José Saramago (1995) - ISBN: n/a - stock: 1
    Temporada de huracanes - Fernanda Melchor (2017) - ISBN: n/a - stock: 1
    """
    
    # Comprueba las claves antes de modificar la lista.
    for libro in libros:
        titulo = libro["titulo"]
        libro["autor"]
        libro["anio_publicacion"]

        if not isinstance(titulo, str):
            raise TypeError("El título debe ser una cadena de texto.")

    # Ordena por título usando Insertion Sort.
    for i in range(1, len(libros)):
        actual = libros[i]
        titulo_actual = actual["titulo"].casefold()
        j = i - 1

        try:
            while j >= 0 and libros[j]["titulo"].casefold() > titulo_actual:
                libros[j + 1] = libros[j]
                j -= 1
        finally:
            libros[j + 1] = actual

    for libro in libros:
        print(f'{libro["titulo"]} - {libro["autor"]} ({libro["anio_publicacion"]}) - ISBN: {libro.get("isbn", "n/a")} - stock: {libro.get("stock", 1)}')


def registrar_libro(libros, nuevo):
    """Agrega un libro o aumenta el stock si su ISBN ya existe."""
    titulo = nuevo["titulo"]
    nuevo["autor"]
    nuevo["anio_publicacion"]

    if not isinstance(titulo, str):
        raise TypeError("El título debe ser una cadena de texto.")

    stock_nuevo = nuevo.get("stock", 1)
    if type(stock_nuevo) is not int or stock_nuevo <= 0:
        raise ValueError("El stock debe ser un número entero positivo.")

    isbn_nuevo = nuevo.get("isbn")

    if isbn_nuevo:
        for libro in libros:
            if libro.get("isbn") == isbn_nuevo:
                stock_actual = libro.get("stock", 1)
                if type(stock_actual) is not int or stock_actual < 0:
                    raise ValueError("El stock existente debe ser un entero no negativo.")
                libro["stock"] = stock_actual + stock_nuevo
                return

    # Sin ISBN o sin coincidencia, se agrega como libro nuevo.
    libros.append(nuevo.copy())

if __name__ == "__main__":
    libros = [
        {"titulo": "Temporada de huracanes", "autor": "Fernanda Melchor", "anio_publicacion": 2017, "isbn": "978-9968-31-011-6", "stock": 1},
        {"titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "anio_publicacion": 1995, "isbn": "978-9930-619-33-0", "stock": 1},
        {"titulo": "Las flores del mal", "autor": "Charles Baudelaire", "anio_publicacion": 1857, "isbn": "978-9977-65-422-5", "stock": 1},
    ]

    print("\nLibros ordenados:")
    ordenar_libros_por_titulo(libros)

    # ISBN existente: aumenta el stock.
    registrar_libro(libros, {"titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "anio_publicacion": 1995, "isbn": "978-9930-619-33-0", "stock": 1})

    # Sin ISBN: agrega el libro al inventario.
    registrar_libro(libros, {"titulo": "Pedro Páramo", "autor": "Juan Rulfo", "anio_publicacion": 1955, "stock": 1})

    print("\nLibros después de actualizar el inventario:")
    ordenar_libros_por_titulo(libros)

    print("\nPrueba con lista vacía:")
    ordenar_libros_por_titulo([])

    print("\nPrueba con clave faltante:")
    try:
        ordenar_libros_por_titulo([{"titulo": "Libro incompleto"}])
    except KeyError as error:
        print(f"Falta la clave: {error}")