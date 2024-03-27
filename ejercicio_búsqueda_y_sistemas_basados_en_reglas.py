# -*- coding: utf-8 -*-

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Definición de la red de transporte
grafo = nx.Graph()

# Añadir estaciones/paradas como nodos
estaciones = {
    "Estación A": "A",
    "Estación B": "B",
    "Estación C": "C",
    "Estación D": "D",
    "Estación E": "E",
}

for nombre, id in estaciones.items():
    grafo.add_node(id)

# Añadir rutas (líneas) como aristas

rutas = {
    ("A", "B"): {"tiempo": 10, "costo": 2000},
    ("A", "C"): {"tiempo": 15, "costo": 3000},
    ("B", "C"): {"tiempo": 5, "costo": 10000},
    ("B", "D"): {"tiempo": 10, "costo": 2000},
    ("C", "D"): {"tiempo": 20, "costo": 4000},
    ("C", "E"): {"tiempo": 15, "costo": 3000},
    ("D", "E"): {"tiempo": 5, "costo": 10000},
}

for origen, destino in rutas.keys():
    tiempo, costo = rutas[(origen, destino)].values()
    grafo.add_edge(origen, destino, tiempo=tiempo, costo=costo)

# Función para calcular la ruta más rápida
def encontrar_ruta_rapida(origen, destino):
    ruta = nx.shortest_path(grafo, origen, destino, weight="tiempo")
    return ruta, calcular_costo_ruta(ruta)

# Función para calcular el costo total de una ruta
def calcular_costo_ruta(ruta):
    costo_total = 0
    for i in range(len(ruta) - 1):
        costo_total += grafo.edges[ruta[i], ruta[i + 1]]["costo"]
    return costo_total

# Ejemplo de uso
origen = "A"
destino = "E"

ruta, costo = encontrar_ruta_rapida(origen, destino)

print(f"Ruta más rápida: {ruta}")
print(f"Tiempo total: {sum(grafo.edges[u, v]['tiempo'] for u, v in zip(ruta, ruta[1:]))} minutos")
print(f"Costo total: {costo} pesos")

# Visualización de la red (opcional)
nx.draw(grafo, with_labels=True)
plt.show()
