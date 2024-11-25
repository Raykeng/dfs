import time
import networkx as nx
import matplotlib.pyplot as plt

def order_dfs(graph, start_node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph.neighbors(start_node):
            if node not in visited:
                order_dfs(graph, node, visited, order)
    return order

def shortest_path_dijkstra(graph, start_node, target_node):
    # Utiliza el algoritmo de Dijkstra para encontrar la ruta más corta
    try:
        path = nx.dijkstra_path(graph, start_node, target_node)
        return path
    except nx.NetworkXNoPath:
        return None

def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        colors = ['r' if n == node else 'g' for n in G.nodes]
        nx.draw(G, pos, with_labels=True, node_color=colors)
        if i > 1:
            nx.draw_networkx_edges(G, pos, edgelist=list(zip(order[:i-1], order[1:i])), edge_color='b', width=2.0)
        plt.draw()
        plt.pause(1.5)
    plt.show()
    time.sleep(0.5)

# Creación de un grafo con pesos en las aristas
G = nx.Graph()
edges = [
    ('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 1), ('B', 'E', 2), ('C', 'F', 1), ('C', 'G', 3)
]
G.add_weighted_edges_from(edges)
pos = nx.spring_layout(G)

# DFS (no ponderado)
dfs_order = order_dfs(G, start_node='A')
visualize_search(dfs_order, 'Visualización DFS', G, pos)

# Dijkstra (ruta más corta en un grafo ponderado)
start_node = 'A'
target_node = 'D'
path = shortest_path_dijkstra(G, start_node, target_node)
if path:
    visualize_search(path, 'Visualización de la Ruta Más Óptima (Dijkstra)', G, pos)
else:
    print(f"No hay ruta entre {start_node} y {target_node}.")
