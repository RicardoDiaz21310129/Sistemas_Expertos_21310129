"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
Busqueda de profundidad
"""

# Definimos el grafo como un diccionario de adyacencias
grafo = {
 'Museo': ['Parque', 'Monumento'],
 'Parque': ['Restaurante', 'Hotel'],
 'Monumento': [],
 'Restaurante': ['Hotel'],
 'Hotel': ['Monumento']
}
# Función para realizar la búsqueda en profundidad (DFS)
def dfs(grafo, nodo_inicial, visitados=None):
 if visitados is None:
 visitados = set()
 
 # Marca el nodo actual como visitado
 visitados.add(nodo_inicial)
 print(nodo_inicial)
 
 # Recorre los nodos adyacentes (vecinos)
 for vecino in grafo[nodo_inicial]:
 if vecino not in visitados:
 dfs(grafo, vecino, visitados)
 
 return visitados
# Ejecución de DFS a partir del nodo inicial 'Museo'
dfs(grafo, 'Museo')