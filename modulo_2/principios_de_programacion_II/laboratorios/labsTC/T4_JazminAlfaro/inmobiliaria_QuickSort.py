import random

def quicksort(casas):
    """Ordena casas por precio y área mediante QuickSort.

    ▸ PARÁMETROS ───────────────────────────────────────────
    casas (list): Diccionarios con las claves obligatorias
                  "precio" y "area", cuyos valores deben ser
                  números enteros o decimales, excepto NaN.

    ▸ RETORNA ──────────────────────────────────────────────
    list: Nueva lista ordenada por precio y, en caso de empate,
          por área. Contiene los diccionarios originales.

    ▸ EXCEPCIONES ──────────────────────────────────────────
    KeyError: Si falta "precio" o "area".
    TypeError: Si algún valor no es int o float, o es bool.
    ValueError: Si algún valor es NaN.
    RecursionError: Si se supera el límite de recursión.
    Las tres primeras validaciones ocurren antes de ordenar.

    ▸ COMPLEJIDAD ──────────────────────────────────────────
    • Tiempo: O(n log n) esperado; O(n²) en el peor caso.
    • Espacio: O(n log n) esperado; O(n²) en el peor caso,
      incluyendo las listas de partición y la recursión.

    ▸ EJEMPLO ──────────────────────────────────────────────
    >>> casas = [
    ...     {"precio": 250000, "area": 120},
    ...     {"precio": 180000, "area": 90},
    ...     {"precio": 250000, "area": 100}
    ... ]
    >>> quicksort(casas)
    [{'precio': 180000, 'area': 90}, {'precio': 250000, 'area': 100}, {'precio': 250000, 'area': 120}]
    """
    
    # Validar cada casa antes de ordenar, incluso si hay una sola.
    for casa in casas:
        for campo in ("precio", "area"):
            valor = casa[campo]

            # Aceptar enteros y decimales, pero no valores booleanos.
            if not isinstance(valor, (int, float)) or isinstance(valor, bool):
                raise TypeError(f"'{campo}' debe ser un número")

            # NaN no es igual a sí mismo y no se puede ordenar de forma fiable.
            if valor != valor:
                raise ValueError(f"'{campo}' no puede ser NaN")

    def ordenar(lista):
        if len(lista) <= 1:
            return lista.copy()

        # Elegir un pivote aleatorio para comparar por precio y luego por área.
        pivote = random.choice(lista)
        clave_pivote = (pivote["precio"], pivote["area"])

        # Separar las casas en tres grupos según su relación con el pivote.
        menores, iguales, mayores = [], [], []

        for casa in lista:
            clave = (casa["precio"], casa["area"])

            if clave < clave_pivote:
                menores.append(casa)
            elif clave > clave_pivote:
                mayores.append(casa)
            else:
                iguales.append(casa)

        # Ordenar los grupos extremos recursivamente y unir los tres.
        return ordenar(menores) + iguales + ordenar(mayores)

    return ordenar(casas)


# Ejecutar el ejemplo solo cuando se ejecuta el archivo directamente.
if __name__ == "__main__":
    casas = [
        {"nombre": "Casa A", "precio": 250000, "area": 120},
        {"nombre": "Casa B", "precio": 180000, "area": 90},
        {"nombre": "Casa C", "precio": 250000, "area": 100},
        {"nombre": "Casa D", "precio": 320000, "area": 150},
        {"nombre": "Casa E", "precio": 180000, "area": 110},
    ]
    for casa in quicksort(casas):
        print(f'{casa["nombre"]}: ${casa["precio"]:,}, {casa["area"]} m²')
