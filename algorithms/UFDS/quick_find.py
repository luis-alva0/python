def createList(size):
    return list(range(size))

"""
Esta función retorna True si están en el mismo grupo y False
si no están en el mismo grupo (no están conectados)
La función find tiene de parámetros:
lista (list) -> Esta es la lista del conjunto formado
p -> un índice (número de vértice) para comparar
q -> un índice (número de vértice) para comparar
"""
def find(lista, p, q):
    return lista[p] == lista[q]

def union(lista, p, q):
    if p >= len(lista) or q >= len(lista):
        print("ERROR: no se puede unir índices mayores que el tamaño de la lista") 
    elif find(lista, p, q):
        print(f"El vértice {p} y {q} están en el mismo grupo...")
    else:
        # Si no están conectados los unimos
        grupoP = lista[p]
        grupoQ = lista[q]
        # El grupo P se convierte ahora en el grupo Q
        for id, grupo in enumerate(lista):
            if grupoP == grupo:
                lista[id] = grupoQ

def printGroups(lista):
    dictionary = {}
    for id, grupo in enumerate(lista):
        if grupo not in dictionary:
            dictionary[grupo] = []
        dictionary[grupo].append(str(id))
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
    # Unir índice 0 con el 8
    print("Unir índice 0 con 8")
    union(lista, 0, 8)
    print(lista)
    printGroups(lista)
    # Unir índice 1 con el 0
    print("Unir índice 1 con 0")
    union(lista, 1, 0)
    print(lista)
    printGroups(lista)
    # Unir índice 5 con el 6
    print("Unir índice 5 con 6")
    union(lista, 5, 6)
    print(lista)
    printGroups(lista)

main()