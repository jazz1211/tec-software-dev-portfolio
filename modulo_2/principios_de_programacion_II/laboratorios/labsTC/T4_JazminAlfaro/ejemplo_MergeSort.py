def merge_sort(lista):
    """Ordena una lista en orden ascendente mediante Merge Sort.
    Divide la lista recursivamente y fusiona las subsecuencias
    ordenadas. Es estable y no modifica la lista original.

    ▸ PARÁMETROS ───────────────────────────────────────────
      lista (list): Elementos comparables mediante <=.

    ▸ RETORNA ──────────────────────────────────────────────
      list: Nueva lista con los elementos ordenados.

    ▸ EXCEPCIONES ──────────────────────────────────────────
      TypeError: Si los elementos no admiten la comparación <=.

    ▸ COMPLEJIDAD ──────────────────────────────────────────
      • Tiempo:  O(n log n).
      • Espacio: O(n) auxiliar y O(log n) de pila de recursión.

    ▸ EJEMPLO ──────────────────────────────────────────────
      >>> merge_sort([3, 1, 2, 1])
      [1, 1, 2, 3]
    """
    
    # Caso base: una secuencia de tamaño 0 o 1 está ordenada.
    if len(lista) <= 1:
        return lista.copy()

    # Fase 1: División de la secuencia.
    mitad = len(lista) // 2

    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    # Fase 2: Fusión ordenada de las subsecuencias.
    resultado = []
    indice_izq = 0
    indice_der = 0

    while (indice_izq < len(izquierda) and
           indice_der < len(derecha)):

        if izquierda[indice_izq] <= derecha[indice_der]:
            resultado.append(izquierda[indice_izq])
            indice_izq += 1
        else:
            resultado.append(derecha[indice_der])
            indice_der += 1

    # Fase 3: Incorporación de los elementos pendientes.
    resultado.extend(izquierda[indice_izq:])
    resultado.extend(derecha[indice_der:])

    return resultado

if __name__ == "__main__":
    precios = [2500, 1200, 3800, 900, 1700] # Datos de entrada.
    precios_ordenados = merge_sort(precios) # Ejecución del algoritmo.

    # Presentación de resultados.
    print("\nLista original:", precios, "\nLista ordenada:", precios_ordenados)
