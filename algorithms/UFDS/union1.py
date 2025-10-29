"""
1.2)
Para resolver el ejercicio 1.2, implementamos un algoritmo que gestiona los grupos de amigos utilizando la estructura de datos 
de conjuntos disjuntos (UFDS). El método manage_friend_groups procesa las relaciones de amistad dadas en la lista friendships, 
convirtiendo las letras a índices numéricos para trabajar con el arreglo interno. Cada relación se maneja con la operación union, 
que une los conjuntos de los amigos involucrados. Esto asegura que todos los amigos directos e indirectos queden en el mismo 
conjunto, representado por un único representante. Al final, usamos find para verificar si dos personas están en el mismo grupo, 
como en las consultas de ejemplo.

2.1)
El ejercicio 2.1 se enfoca en mejorar la eficiencia de UFDS mediante la compresión de caminos en la operación find. Esto se logra 
actualizando el padre de cada nodo al representante del conjunto durante la búsqueda recursiva, reduciendo la altura del árbol. 
En el código, modificamos find para que, al detectar que un nodo no es su propio padre, reasigne su padre al representante 
encontrado recursivamente. Esto aplana la estructura del árbol, disminuyendo el tiempo de futuras operaciones.
"""

class UnionFind:
    """
    Inicializa el arreglo parent donde cada elemento es su propio padre.
    """
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    """
    Encuentra el representante del conjunto que contiene a "i".
    Si "i" es su propio padre, es el representante.
    Para la compresión de caminos actualiza el padre de "i" al representante encontrado.
    """
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    """
    Encuentra los representantes de los conjuntos de "i" y "j".
    Si los representantes son diferentes, une los conjuntos.
    """
    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep != jrep:
            self.parent[irep] = jrep

    """
    Procesa las relaciones de amistad dadas, convierte las letras a índices y une los conjuntos de amigos.
    """
    def manage_friend_groups(self, friendships):
        for x, y in friendships:
            i = ord(x) - ord('a')
            j = ord(y) - ord('a')
            self.union(i, j)

"""
Relaciones de amistad del ejemplo: a-b, b-d, c-f, c-i, j-e, g-j
"""
if __name__ == "__main__":
    friendships = [('a', 'b'), ('b', 'd'), ('c', 'f'), ('c', 'i'), ('j', 'e'), ('g', 'j')]
    uf = UnionFind(10)
    uf.manage_friend_groups(friendships)
    print("¿a es amigo de d?", "Sí" if uf.find(0) == uf.find(3) else "No")
    print("¿a es amigo de e?", "Sí" if uf.find(0) == uf.find(4) else "No")

"""
Para el ejercicio 1.2, el código utiliza la estructura UFDS para agrupar amigos según las relaciones dadas. El método 
manage_friend_groups itera sobre las amistades, convierte letras a índices y aplica union para unir conjuntos. Las consultas 
se resuelven comparando los representantes devueltos por find, verificando si están en el mismo grupo.

Para el ejercicio 2.1, se implementa la compresión de caminos en find, reasignando el padre de cada nodo al representante 
durante la búsqueda recursiva. Esto reduce la altura del árbol, mejorando la eficiencia de futuras operaciones find.
"""