"""
Titulo: Tarea 1: Dijkstra
Nombre completo: Dante Tlacaelel Mendoza Alcantar
Fecha de creación: 15 de Octubre del 2026

"""




class Nodo:
    """Vértice del grafo: guarda su nombre y las conexiones hacia sus vecinos."""

    def __init__(self, nombre):
        # Identificador del nodo (ej. "A"); sirve para localizarlo en el grafo
        self.nombre = nombre

        # Lista de adyacencia {vecino: peso}; sirve para saber a quién se
        # conecta este nodo y cuánto cuesta cada conexión
        self.vecinos = {}


class Grafo:
    """Grafo ponderado no dirigido modelado con nodos y listas de adyacencia."""

    def __init__(self):
        # Diccionario {nombre: Nodo}; sirve para acceder rápido a cualquier nodo
        self.nodos = {}

    def agregar_nodo(self, nombre):
        """Crea un nodo nuevo y lo registra en el grafo."""
        self.nodos[nombre] = Nodo(nombre)

    def agregar_conexion(self, origen, destino, peso):
        """Conecta dos nodos en ambos sentidos con el peso indicado."""
        self.nodos[origen].vecinos[destino] = peso
        self.nodos[destino].vecinos[origen] = peso

    def dijkstra(self, inicio, destino):
        """Devuelve (costo_total, ruta) del camino mínimo entre inicio y destino."""

        # Menor costo conocido desde el origen hasta cada nodo;
        # sirve para comparar y elegir siempre el nodo más cercano
        distancias = {}

        # Nodo previo de cada nodo en el mejor camino encontrado;
        # sirve para reconstruir la ruta al final
        anteriores = {}

        # Nodos cuyo costo ya es definitivo; sirve para no procesarlos dos veces
        visitados = set()

        # Inicializar: todos en infinito y sin nodo previo
        for nombre in self.nodos:
            distancias[nombre] = float("inf")
            anteriores[nombre] = None

        # El origen cuesta 0 llegar a sí mismo; es el punto de partida
        distancias[inicio] = 0

        while len(visitados) < len(self.nodos):
            # Nodo no visitado con menor distancia; es el que se procesa en
            # esta iteración
            nodo_actual = None

            # Menor distancia encontrada en la búsqueda; sirve para comparar
            # contra los demás nodos no visitados
            menor_distancia = float("inf")

            # Seleccionar: buscar el nodo no visitado más cercano
            for nombre in self.nodos:
                if nombre not in visitados:
                    if distancias[nombre] < menor_distancia:
                        menor_distancia = distancias[nombre]
                        nodo_actual = nombre

            # Si no hay nodo alcanzable, se termina
            if nodo_actual is None:
                break

            # Si se llegó al destino, su costo ya es el mínimo
            if nodo_actual == destino:
                break

            # Marcar: el costo de este nodo ya es definitivo
            visitados.add(nodo_actual)

            # Objeto Nodo actual; sirve para leer sus vecinos y pesos
            nodo = self.nodos[nodo_actual]

            # Relajar: revisar si pasar por el nodo actual mejora el costo
            # de sus vecinos
            for vecino, peso in nodo.vecinos.items():
                # Costo de llegar al vecino pasando por el nodo actual
                nueva_distancia = distancias[nodo_actual] + peso

                # Solo se actualiza si el nuevo camino es estrictamente más corto
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual

        # Lista con el recorrido completo; se arma de atrás hacia adelante
        ruta = []

        # Nodo que se está recorriendo al reconstruir la ruta; inicia en el destino
        actual = destino

        while actual is not None:
            ruta.append(actual)
            actual = anteriores[actual]

        # Se invierte para que quede de origen a destino
        ruta.reverse()

        return distancias[destino], ruta


# Grafo de ejemplo (red de ciudades); sirve para probar el algoritmo
grafo = Grafo()

for ciudad in ["A", "B", "C", "D", "E", "F"]:
    grafo.agregar_nodo(ciudad)

grafo.agregar_conexion("A", "B", 7)
grafo.agregar_conexion("A", "C", 9)
grafo.agregar_conexion("A", "F", 14)
grafo.agregar_conexion("B", "C", 10)
grafo.agregar_conexion("B", "D", 15)
grafo.agregar_conexion("C", "D", 11)
grafo.agregar_conexion("C", "F", 2)
grafo.agregar_conexion("D", "E", 6)
grafo.agregar_conexion("E", "F", 9)

# Costo total y ruta exacta entre el nodo origen "A" y el destino "E"
distancia, ruta = grafo.dijkstra("A", "E")

print("Costo total:", distancia)
print("Ruta:", " -> ".join(ruta))
