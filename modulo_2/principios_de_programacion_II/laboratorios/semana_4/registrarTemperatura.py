import math
from binarytree import Node

"""Registra temperaturas únicas en un árbol binario de búsqueda
autobalanceado (AVL) y muestra sus valores extremos.

▸ PARÁMETROS ───────────────────────────────────────────
  No recibe parámetros. Solicita temperaturas por consola
  y parte de los valores iniciales:
  30, 25, 32, 20, 27, 31 y 35.

▸ RETORNA ──────────────────────────────────────────────
  Imprime el árbol final y las temperaturas mínima y máxima.

▸ EXCEPCIONES ──────────────────────────────────────────
  ValueError: Se captura si la entrada no es un número válido.
  Los valores no finitos y duplicados se rechazan con un mensaje.

  ImportError: Si el paquete binarytree no está instalado.

▸ COMPLEJIDAD ──────────────────────────────────────────
  • Tiempo: O(log n) por inserción y por búsqueda de cada extremo.
  • Espacio: O(n) para almacenar el árbol.

  La visualización requiere tiempo y espacio adicionales.

▸ DEPENDENCIAS ─────────────────────────────────────────
  Instale binarytree antes de ejecutar el programa:
      /usr/bin/python3 -m pip install binarytree
"""

def altura(nodo):
    return nodo[3] if nodo else 0


def rotar(nodo, lado):
    # Lado 1: rotación derecha; lado 2: rotación izquierda.
    nueva_raiz = nodo[lado]
    opuesto = 3 - lado

    nodo[lado] = nueva_raiz[opuesto]
    nueva_raiz[opuesto] = nodo

    nodo[3] = 1 + max(altura(nodo[1]), altura(nodo[2]))
    nueva_raiz[3] = 1 + max(altura(nueva_raiz[1]), altura(nueva_raiz[2]))
    return nueva_raiz


def insertar(nodo, temperatura):
    if nodo is None:
        return [temperatura, None, None, 1], True

    if temperatura == nodo[0]:
        return nodo, False

    lado = 1 if temperatura < nodo[0] else 2
    nodo[lado], insertada = insertar(nodo[lado], temperatura)

    if not insertada:
        return nodo, False

    nodo[3] = 1 + max(altura(nodo[1]), altura(nodo[2]))
    balance = altura(nodo[1]) - altura(nodo[2])

    if abs(balance) > 1:
        lado = 1 if balance > 0 else 2
        hijo = nodo[lado]

        if (lado == 1 and temperatura > hijo[0]) or (
            lado == 2 and temperatura < hijo[0]
        ):
            nodo[lado] = rotar(hijo, 3 - lado)

        nodo = rotar(nodo, lado)

    return nodo, True


def extremo(nodo, lado):
    # Izquierda para el mínimo; derecha para el máximo.
    while nodo[lado] is not None:
        nodo = nodo[lado]
    return nodo[0]


def mostrar(nodo):
    def convertir(n):
        if n is None:
            return None

        resultado = Node(n[0])
        resultado.left = convertir(n[1])
        resultado.right = convertir(n[2])
        return resultado

    print(convertir(nodo) if nodo else "Árbol vacío")

arbol = None

for temperatura in [30, 25, 32, 20, 27, 31, 35]:
    arbol, _ = insertar(arbol, temperatura)

while True:
    entrada = input("Temperatura (Enter para terminar): ").strip()
    if not entrada:
        break

    try:
        temperatura = float(entrada)
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if not math.isfinite(temperatura):
        print("Ingrese una temperatura finita.")
        continue

    arbol, insertada = insertar(arbol, temperatura)
    if not insertada:
        print("La temperatura ya está registrada.")

print("\nÁrbol final:")
mostrar(arbol)
print(f"\n- Temperatura mínima: {extremo(arbol, 1)}",
      f"\n- Temperatura máxima: {extremo(arbol, 2)}")