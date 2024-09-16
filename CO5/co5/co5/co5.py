"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
A star
"""

import heapq
# Definimos el grafo como un diccionario de adyacencias con costos (distancias entre 
intersecciones)
mapa_ciudad = {
 'Centro de Distribución': {'Intersección A': 2, 'Intersección B': 4},
 'Intersección A': {'Centro de Distribución': 2, 'Intersección C': 3},
 'Intersección B': {'Centro de Distribución': 4, 'Intersección D': 1},
 'Intersección C': {'Intersección A': 3, 'Tienda': 5},
 'Intersección D': {'Intersección B': 1, 'Tienda': 2},
 'Tienda': {'Intersección C': 5, 'Intersección D': 2}
}
# Heurística (distancia en línea recta al destino)
heuristica = {
 'Centro de Distribución': 7,
 'Intersección A': 6,
 'Intersección B': 4,
 'Intersección C': 4,
 'Intersección D': 2,
 'Tienda': 0
}
12
# Función para realizar la búsqueda A*
def a_star_search(grafo, heuristica, inicio, objetivo):
 # Cola de prioridad para seleccionar el siguiente nodo basado en costo f = g + h
 cola_prioridad = []
 heapq.heappush(cola_prioridad, (0 + heuristica[inicio], 0, inicio))
 
 # Conjunto de nodos visitados
 visitados = set()
 
 # Mapa para rastrear el costo acumulado y el camino
 costo_acumulado = {inicio: 0}
 padres = {inicio: None}
 
 while cola_prioridad:
 # Tomamos el nodo con el menor costo f
 _, costo_g, nodo_actual = heapq.heappop(cola_prioridad)
 
 # Si encontramos el objetivo, reconstruimos el camino
 if nodo_actual == objetivo:
 camino = []
 while nodo_actual:
 camino.append(nodo_actual)
 nodo_actual = padres[nodo_actual]
 camino.reverse() # Invertimos el camino para que vaya de inicio a destino
13
 return camino, costo_acumulado[objetivo]
 
 # Si el nodo no ha sido visitado, lo procesamos
 if nodo_actual not in visitados:
 visitados.add(nodo_actual)
 
 # Exploramos los vecinos del nodo actual
 for vecino, costo in grafo[nodo_actual].items():
 costo_nuevo = costo_g + costo
 if vecino not in costo_acumulado or costo_nuevo < 
costo_acumulado[vecino]:
 costo_acumulado[vecino] = costo_nuevo
 padres[vecino] = nodo_actual
 costo_f = costo_nuevo + heuristica[vecino]
 heapq.heappush(cola_prioridad, (costo_f, costo_nuevo, vecino))
 
 # Si no se encuentra un camino
 return None, float('inf')
# Ejecución de la búsqueda A* desde 'Centro de Distribución' hasta 'Tienda'
camino, costo = a_star_search(mapa_ciudad, heuristica, 'Centro de Distribución', 
'Tienda')
print(f"Camino más corto: {camino}")
print(f"Costo total: {costo} km")