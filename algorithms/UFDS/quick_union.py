def createList(size):
    return list(range(size))

"""
Esta función retorna el índice raíz (padre) de un nodo
lista (list) -> Esta es la lista del conjunto formado
p -> un índice (número de vértice) para comparar
"""
def find(lista, p):
    root = lista[p]
    while (root != p):
        p = root
        root = lista[p]
    return root

def union(lista, p, q):
    root_p = find(lista, p)
    root_q = find(lista, q)
    if p >= len(lista) or q >= len(lista):
        print("ERROR: no se puede unir índices mayores que el tamaño de la lista") 
    elif find(lista, p) == find(lista, q):
        print(f"El vértice {p} y {q} tienen el mismo padre (raíz)...")
    else:
        lista[root_p] = root_q

def printGroups(lista):
    dictionary = {}
    for id in range(len(lista)):
        root = find(lista, id)
        if root not in dictionary:
            dictionary[root] = []
        dictionary[root].append(str(id))
    for grupo in dictionary.values():
        print("{" + ",".join(grupo) + "}", end=" ")
    print() # Salto de línea

def main():
    n = int(input("Ingrese tamaño del conjunto: "))
    lista = createList(n)
    # La lista creada se forma de esta manera
    # los índices representan el número de vértice
    # los valores de la lista representan el grupo que pertenece ese vértice
    print("Lista inicial")
    print(lista)
    printGroups(lista)
    # Unir índice 3 con el 4
    print("Unir índice 3 con 4")
    union(lista, 3, 4)
    print(lista)
    printGroups(lista)
    # Unir índice 4 con el 9
    print("Unir índice 4 con 9")
    union(lista, 4, 9)
    print(lista)
    printGroups(lista)
    # Unir índice 2 con el 9
    print("Unir índice 2 con 9")
    union(lista, 2, 9)
    print(lista)
    printGroups(lista)
    # Unir índice 5 con el 6
    print("Unir índice 5 con 6")
    union(lista, 5, 6)
    print(lista)
    printGroups(lista)
main()