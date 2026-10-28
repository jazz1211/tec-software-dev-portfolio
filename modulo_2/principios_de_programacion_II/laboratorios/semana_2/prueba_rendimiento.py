# ============================================================================================
# PRUEBA DE RENDIMIENTO: Esta prueba utiliza ColaCine de cine.py para medir el registro,
#                        ordenamiento, creación de índice y búsqueda de clientes generados
#                        automáticamente.
# ============================================================================================
#
# Datos de prueba:
#   - Se generan 10,000 clientes por defecto, con nombre, edad y un boleto por cliente.
#   - La cantidad puede ajustarse para probar 1,000, 10,000 y 100,000 clientes.
#   - La semilla 42 permite generar las mismas edades en cada ejecución.
#   - Los mismos datos se utilizan en todas las repeticiones.
#   - Cada operación se mide 5 veces por defecto y una vez adicional para medir memoria.
#
# Operaciones evaluadas:
#   - Registrar clientes   : crea una cola nueva y agrega cada cliente con agregar().
#   - Ordenar clientes     : fuerza obtener_ordenada() para ordenar los clientes.
#   - Crear índice         : fuerza actualizar_indice_nombres() para crear el índice.
#   - Buscar por nombre    : usa bisect_left y recorre los nombres con el prefijo
#                            "cliente 5000".
#
# Medición:
#   - medir()              : ejecuta cada operación y muestra sus resultados.
#   - perf_counter()       : mide el tiempo de ejecución de cada repetición.
#   - median()             : obtiene el valor central de los tiempos medidos.
#   - tracemalloc          : mide el pico de memoria rastreada en una ejecución separada.
#   - gc.collect()         : ejecuta el recolector de basura antes de cada medición.
#
# Resumen final:
#   - Muestra los clientes registrados, boletos a comprar, boletos gratis previstos
#     y clientes encontrados en la búsqueda.
#
# Consideraciones:
#   - La búsqueda reproduce la lógica por prefijo, pero no llama a buscar().
#   - El índice de nombres se crea antes de medir la búsqueda.
#   - Después del primer ordenamiento, la lista puede estar ordenada. Por ello,
#     la mediana puede reflejar el costo de ordenar una lista ya ordenada.
#   - La memoria medida corresponde a las asignaciones rastreadas durante la operación,
#     no a la memoria total del proceso.
#   - Los clientes existen solo en memoria y no se guardan en un archivo.
#
# Requisitos:
#   - Python 3.10 o superior.
#   - cine.py en la misma carpeta que este archivo.
#
# ============================================================================================

import gc
import random
import statistics
import time
import tracemalloc

from bisect import bisect_left
from cine import ColaCine

def medir(nombre, operacion, repeticiones=5, preparar=None):
    tiempos = []

    for _ in range(repeticiones):
        gc.collect()

        if preparar is not None:
            preparar()

        inicio = time.perf_counter()
        resultado = operacion()
        tiempos.append(time.perf_counter() - inicio)
        del resultado

    gc.collect()

    if preparar is not None:
        preparar()

    tracemalloc.start()
    try:
        resultado = operacion()
        _, pico = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()

    print(
        f"\n{nombre}:"
        f"\n- Tiempo mediano: {statistics.median(tiempos):.4f} segundos"
        f"\n- Memoria adicional pico: {pico / 1024:.2f} KiB"
    )

    return resultado

def comparar_rendimiento(cantidad=10_000, repeticiones=5):
    generador = random.Random(42)

    # Los mismos datos se utilizan en todas las repeticiones.
    datos = [
        (f"Cliente {numero}", generador.randint(0, 100), 1)
        for numero in range(1, cantidad + 1)
    ]

    def registrar_clientes():
        cola = ColaCine()
        for nombre, edad, boletos in datos:
            cola.agregar(nombre, edad, boletos)
        return cola

    # Cada repetición crea y registra una cola nueva.
    cola = medir("Registrar clientes", registrar_clientes, repeticiones)

    def ordenar_clientes():
        # Forzamos el ordenamiento en cada repetición.
        cola.ordenada = False
        return cola.obtener_ordenada()

    medir("Ordenar clientes", ordenar_clientes, repeticiones)

    def crear_indice():
        # Forzamos la creación del índice en cada repetición.
        cola.indice_actualizado = False
        cola.actualizar_indice_nombres()

    medir("Crear índice de nombres", crear_indice, repeticiones)

    def buscar_nombre():
        texto = "cliente 5000"
        posicion = bisect_left(cola.nombres_ordenados, texto)
        encontrados = []

        while (
            posicion < len(cola.indice_nombres)
            and cola.nombres_ordenados[posicion].startswith(texto)
        ):
            encontrados.append(cola.indice_nombres[posicion])
            posicion += 1

        return encontrados

    encontrados = medir("Buscar por nombre", buscar_nombre, repeticiones)

    print(
        "\nResumen final:"
        f"\n- Clientes registrados: {len(cola.clientes)}"
        f"\n- Boletos a comprar: {cola.total_boletos}"
        f"\n- Boletos gratis previstos: {cola.boletos_gratis}"
        f"\n- Clientes encontrados: {len(encontrados)}\n"
          )

if __name__ == "__main__":
    for cantidad in (1_000, 10_000, 100_000):
        print(f"\n# ===================== Prueba con {cantidad:,} clientes ===================== #")
        comparar_rendimiento(cantidad)

