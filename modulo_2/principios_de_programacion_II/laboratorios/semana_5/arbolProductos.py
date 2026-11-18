"""
Organiza productos por precio mediante un árbol binario de búsqueda.
Inserta precios menores a la izquierda y mayores o iguales a la derecha.
Muestra los recorridos y calcula el total, promedio y precios extremos.

▸ PARÁMETROS ───────────────────────────────────────────
    productos (list): Tuplas con el nombre y precio de cada producto.

▸ RETORNA ──────────────────────────────────────────────
    No retorna un valor general. Imprime los resultados.

▸ EXCEPCIONES ──────────────────────────────────────────
    TypeError: Si los precios no se pueden comparar o sumar.
    RecursionError: Si se supera el límite de recursión.

▸ COMPLEJIDAD ──────────────────────────────────────────
    • Inserción: O(h) por producto.
    • Recorridos: O(n) en tiempo y O(h) en espacio auxiliar.
    n es la cantidad de productos y h la altura del árbol.

▸ EJEMPLO ──────────────────────────────────────────────
    >> Precio total: ₡23700
    -  Producto más barato: Arroz (₡1200)
    -  Producto más caro: Café molido (₡4800)
    -  Precio promedio: ₡2370.00
"""

class Nodo:
    """Representa un producto como nodo del árbol."""
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.izquierda = None
        self.derecha = None


class ArbolProductos:
    """Administra un árbol binario de búsqueda por precio."""
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, precio): # Inserta un producto según su precio.
        
        nuevo = Nodo(nombre, precio)

        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz

        while True:
            if precio < actual.precio:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    return
                actual = actual.derecha

    def inorden(self, nodo): # Muestra los productos ordenados y calcula sus estadísticas.

        if nodo is None:
            return 0, 0, None, None

        total_izq, cantidad_izq, minimo_izq, _ = self.inorden(
            nodo.izquierda
        )

        print(f"{nodo.nombre}: ₡{nodo.precio}")

        total_der, cantidad_der, _, maximo_der = self.inorden(
            nodo.derecha
        )

        total = total_izq + nodo.precio + total_der
        cantidad = cantidad_izq + 1 + cantidad_der
        minimo = minimo_izq if minimo_izq is not None else nodo
        maximo = maximo_der if maximo_der is not None else nodo

        return total, cantidad, minimo, maximo

    def preorden(self, nodo): # Muestra los productos en orden nodo, izquierda y derecha.
        if nodo is not None:
            print(f"{nodo.nombre}: ₡{nodo.precio}")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def postorden(self, nodo): # Muestra los productos en orden izquierda, derecha y nodo.
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(f"{nodo.nombre}: ₡{nodo.precio}")


def main():
    """Crea el árbol de ejemplo y muestra los resultados."""
    productos = [
        ("Pan integral", 1800),
        ("Leche", 2500),
        ("Arroz", 1200),
        ("Frijoles negros", 1400),
        ("Café molido", 4800),
        ("Azúcar blanca", 1600),
        ("Atún en agua", 2200),
        ("Cereal de avena", 3500),
        ("Jugo natural", 2000),
        ("Aceite vegetal", 2700),
    ]

    arbol = ArbolProductos()

    for nombre, precio in productos:
        arbol.insertar(nombre, precio)

    print("\n=== Recorrido inorden ===")
    total, cantidad, minimo, maximo = arbol.inorden(arbol.raiz)

    print("\n=== Recorrido preorden ===")
    arbol.preorden(arbol.raiz)

    print("\n=== Recorrido postorden ===")
    arbol.postorden(arbol.raiz)

    print(f"\n>> Precio total: ₡{total}")

    if cantidad > 0:
        print(f"\n-  Producto más barato: {minimo.nombre} (₡{minimo.precio})"
              f"\n-  Producto más caro: {maximo.nombre} (₡{maximo.precio})"
              f"\n-  Precio promedio: ₡{total / cantidad:.2f}")
    else:
        print("No hay productos en el árbol.")

if __name__ == "__main__":
    main()