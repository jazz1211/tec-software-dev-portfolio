# =============================================================================
# BÚSQUEDAS LINEAL Y BINARIA
# =============================================================================
#
# Búsqueda lineal:
#   Recorre la lista hasta encontrar el valor. No requiere orden previo.
#
# Búsqueda binaria:
#   Divide la búsqueda en mitades. Requiere una lista ordenada.
#
# =============================================================================

# Búsqueda Lineal
def busqueda_lineal(lista: list[int], valor: int) -> int:
    for indice, elemento in enumerate(lista):
        if elemento == valor:
            return indice
    return -1


# Búsqueda Binaria
def busqueda_binaria(lista: list[int], valor: int) -> int:
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


# Ejemplos
if __name__ == "__main__":
    datos = [15, 30, 8, 45, 12, 7, 20]
    valor = 20
    datos_ordenados = sorted(datos)

    print(
        f"Búsqueda lineal"
        f"\n- Lista: {datos}"
        f"\n- Valor: {valor}"
        f"\n- Índice: {busqueda_lineal(datos, valor)}"
    )

    print(
        f"\nBúsqueda binaria"
        f"\n- Lista: {datos_ordenados}"
        f"\n- Valor: {valor}"
        f"\n- Índice: {busqueda_binaria(datos_ordenados, valor)}"
    )

