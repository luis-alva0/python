"""
En un videojuego multijugador, los jugadores pueden unirse en clanes. Cada jugador está identificado por un número 
del 0 al n-1. Al inicio, todos los jugadores están solos (un clan con un jugador). Durante el juego, ocurren dos 
tipos de eventos:

  - U a b: los jugadores a y b deciden unir sus clanes (si no estaban ya conectados). Se puede asumir que cada jugador 
    al iniciar pertenecen a su propio clan. 
  - C a b: el sistema debe responder si a y b pertenecen al mismo clan (es decir, si están directa o indirectamente 
  conectados). 

Se te pide implementar un programa que procese estos eventos y determine el resultado de cada consulta C. Se necesita 
implementar una estructura de datos que permita:

    1. Unir dos jugadores o clanes. 
    2. Verificar si dos jugadores pertenecen al mismo clan.

La función procesar_eventos(n, eventos) debe recibir:

    1. n: número total de jugadores. 
    2. eventos: lista de cadenas, donde cada una puede ser "U a b" o "C a b". 
    
La función debe devolver una lista con los resultados (True o False) de las consultas C.
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
        print("ERROR") 
    elif find(lista, p) == find(lista, q):
        print("MISMO PADRE")
    else:
        lista[root_p] = root_q

def createList(size):
    return list(range(size))

n = 6
eventos = [
    "U 0 1",
    "U 1 2",
    "C 0 2",
    "C 0 3",
    "U 3 4",
    "C 3 4",
    "C 2 4",
    "U 2 4",
    "C 0 4"
]

lista = createList(len(eventos))

def procesar_eventos(n: int, eventos: list):
    for line in eventos:
        words = line.split()
        if words[0] == "U":
            #print("union")
            union(lista, int(words[1]), int(words[2]))
        elif words[0] == "C":
            if find(lista, int(words[1])) == find(lista, int(words[2])):
                print("True")
            else:
                print("False")
        else:
            print("error")


procesar_eventos(n, eventos)