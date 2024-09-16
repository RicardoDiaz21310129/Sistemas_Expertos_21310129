
"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
Busqueda de anchura
"""

from collections import deque
# Definimos el grafo como un diccionario de adyacencias (amistades)
red_social = {
 'Ana': ['Bob', 'Carlos'],
 'Bob': ['Ana', 'Diana', 'Eva'],
 'Carlos': ['Ana', 'Fabián'],
 'Diana': ['Bob'],
 'Eva': ['Bob'],
 'Fabián': ['Carlos']
}
# Función para realizar la búsqueda en anchura (BFS)
def bfs(red_social, nodo_inicial):
 visitados = set()
 cola = deque([nodo_inicial]) # Inicializamos la cola con el nodo inicial
 
 while cola:
 persona_actual = cola.popleft() # Desencolamos la primera persona
 
 if persona_actual not in visitados:
 print(persona_actual) # Imprimimos la persona visitada
 visitados.add(persona_actual)
4
 
 # Agregamos los amigos (vecinos) a la cola si no han sido visitados
 for amigo in red_social[persona_actual]:
 if amigo not in visitados:
 cola.append(amigo)
# Ejecución de BFS a partir del nodo inicial 'Ana'
bfs(red_social, 'Ana')