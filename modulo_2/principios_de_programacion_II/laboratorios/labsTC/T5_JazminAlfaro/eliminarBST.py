'''
arbolBinario = [
    1,      # raíz
    [2,[4,None,None],[5,None,None]],
    [3,[6,None,None],[7,None,None]]
]
'''
def insertarBst(bst, valor):
    if bst is None:
        return [valor,None,None]

    if valor < bst[0]:
        bst[1] = insertarBst(bst[1], valor)

    elif valor > bst[0]:
        bst[2] = insertarBst(bst[2], valor)

    return bst

bst = [
    15,
    [10,[5,[2,None,None],[7,None,None]],[12,None,None]],
    [20,[17,None,None],[25,None,None]]
]
#bst = None
arbol = insertarBst(bst, 19)
print(arbol)


''' Eliminar un nodo de un árbol binario de búsqueda (BST) ''' 
def eliminarBst(bst, valor):
    if bst is None:
        return None

    if valor < bst[0]:
        bst[1] = eliminarBst(bst[1], valor)

    elif valor > bst[0]:
        bst[2] = eliminarBst(bst[2], valor)

    else:
        if bst[1] is None:
            return bst[2]

        if bst[2] is None:
            return bst[1]

        sucesor = bst[2]
        while sucesor[1] is not None:
            sucesor = sucesor[1]

        bst[0] = sucesor[0]
        bst[2] = eliminarBst(bst[2], sucesor[0])

    return bst

bst = [15,[10, [5, [2, None, None], [7, None, None]], [12, None, None]],
    [20, [17, None, None], [25, None, None]]]

bst = eliminarBst(bst, 15)
print("\nEliminar BST: ", bst)
