"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
Busqueda voraz
"""

import heapq
# Definimos el grafo como un diccionario de adyacencias (conexiones entre ciudades)
mapa_logistica = {
 'Centro de Distribuci�n': ['Ciudad A', 'Ciudad B'],
 'Ciudad A': ['Centro de Distribuci�n', 'Ciudad C'],
 'Ciudad B': ['Centro de Distribuci�n', 'Ciudad D'],
 'Ciudad C': ['Ciudad A', 'Destino'],
 'Ciudad D': ['Ciudad B', 'Destino'],
 'Destino': ['Ciudad C', 'Ciudad D']
}
# Heur�stica (distancia en l�nea recta al destino)
heuristica = {
 'Centro de Distribuci�n': 10,
 'Ciudad A': 8,
 'Ciudad B': 5,
 'Ciudad C': 3,
 'Ciudad D': 2,
 'Destino': 0
}
# Funci�n para realizar la b�squeda voraz
9
def busqueda_voraz(grafo, heuristica, inicio, objetivo):
 # Cola de prioridad para seleccionar el siguiente nodo basado en la heur�stica
 cola_prioridad = []
 heapq.heappush(cola_prioridad, (heuristica[inicio], inicio))
 
 # Conjunto de nodos visitados
 visitados = set()
 
 # Mapa para rastrear el camino
 padres = {inicio: None}
 
 while cola_prioridad:
 # Tomamos el nodo con la menor heur�stica
 _, nodo_actual = heapq.heappop(cola_prioridad)
 
 # Si encontramos el objetivo, reconstruimos el camino
 if nodo_actual == objetivo:
 camino = []
 while nodo_actual:
 camino.append(nodo_actual)
 nodo_actual = padres[nodo_actual]
 camino.reverse() # Invertimos el camino para que vaya de inicio a destino
 return camino
 
10
 # Si el nodo no ha sido visitado, lo procesamos
 if nodo_actual not in visitados:
 visitados.add(nodo_actual)
 
 # Exploramos los vecinos del nodo actual
 for vecino in grafo[nodo_actual]:
 if vecino not in visitados:
 padres[vecino] = nodo_actual
 heapq.heappush(cola_prioridad, (heuristica[vecino], vecino))
 
 # Si no se encuentra un camino
 return None
# Ejecuci�n de la b�squeda voraz desde 'Centro de Distribuci�n' hasta 'Destino'
camino = busqueda_voraz(mapa_logistica, heuristica, 'Centro de Distribuci�n', 
'Destino')
print(f"Camino encontrado: {camino}")