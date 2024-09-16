
"""
Sistemas Expertos 
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
Busqueda bidireccional
"""


from collections import deque
# Definimos el grafo como un diccionario de adyacencias (intersecciones conectadas 
por calles)
mapa_ciudad = {
 'Casa': ['Intersecci�n A', 'Intersecci�n B'],
 'Intersecci�n A': ['Casa', 'Intersecci�n C'],
 'Intersecci�n B': ['Casa', 'Tienda'],
 'Intersecci�n C': ['Intersecci�n A', 'Tienda'],
 'Tienda': ['Intersecci�n B', 'Intersecci�n C']
}
# Funci�n para la b�squeda bidireccional
def bidirectional_search(grafo, inicio, objetivo):
 # Dos colas, una para la b�squeda desde el inicio y otra desde el objetivo
 cola_inicio = deque([inicio])
 cola_objetivo = deque([objetivo])
 
 # Conjuntos de visitados
 visitados_inicio = {inicio}
 visitados_objetivo = {objetivo}
 
 # Mapas para rastrear el camino recorrido desde ambos extremos
6
 padres_inicio = {inicio: None}
 padres_objetivo = {objetivo: None}
 
 # Funci�n para reconstruir el camino encontrado
 def reconstruir_camino(nodo, padres_inicio, padres_objetivo):
 # Reconstituir el camino desde el nodo encontrado hacia ambos lados
 camino = []
 while nodo:
 camino.append(nodo)
 nodo = padres_inicio[nodo]
 camino.reverse() # Camino desde el nodo de inicio
 nodo = padres_objetivo[camino[-1]]
 while nodo:
 camino.append(nodo)
 nodo = padres_objetivo[nodo]
 return camino
 
 # Mientras ambas colas tengan elementos
 while cola_inicio and cola_objetivo:
 # Expansi�n desde el inicio
 nodo_actual = cola_inicio.popleft()
 for vecino in grafo[nodo_actual]:
 if vecino not in visitados_inicio:
 visitados_inicio.add(vecino)
7
 padres_inicio[vecino] = nodo_actual
 cola_inicio.append(vecino)
 # Si el nodo se encuentra en el lado opuesto, reconstruir camino
 if vecino in visitados_objetivo:
 return reconstruir_camino(vecino, padres_inicio, padres_objetivo)
 
 # Expansi�n desde el objetivo
 nodo_actual = cola_objetivo.popleft()
 for vecino in grafo[nodo_actual]:
 if vecino not in visitados_objetivo:
 visitados_objetivo.add(vecino)
 padres_objetivo[vecino] = nodo_actual
 cola_objetivo.append(vecino)
 # Si el nodo se encuentra en el lado opuesto, reconstruir camino
 if vecino in visitados_inicio:
 return reconstruir_camino(vecino, padres_inicio, padres_objetivo)
 
 # Si no se encuentra un camino
 return None
# Ejecuci�n de la b�squeda bidireccional entre 'Casa' y 'Tienda'
camino = bidirectional_search(mapa_ciudad, 'Casa', 'Tienda')
print(f"Camino m�s corto: {camino}")
