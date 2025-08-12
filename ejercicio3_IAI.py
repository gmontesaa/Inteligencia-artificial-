from collections import deque
import time
import tracemalloc

# Definición de la clase Node
class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

# Definición de la clase Problem
class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return self.graph.get(state, [])

    def is_goal(self, state):
        return state == self.goal

    def result(self, state, action):
        return action

# Reconstrucción del camino
def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))

# BFS
def bfs(problem):
    start_node = Node(problem.initial)
    if problem.is_goal(start_node.state):
        return reconstruct_path(start_node)

    frontier = deque([start_node])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node.state)

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            if child_state not in explored and all(n.state != child_state for n in frontier):
                child_node = Node(child_state, parent=node)
                if problem.is_goal(child_state):
                    return reconstruct_path(child_node)
                frontier.append(child_node)
    return None

# DFS con límite de profundidad
def dfs_limited(problem, limit):
    def recursive_dls(node, problem, limit):
        if problem.is_goal(node.state):
            return reconstruct_path(node)
        elif limit == 0:
            return None
        else:
            for action in problem.actions(node.state):
                child_state = problem.result(node.state, action)
                child_node = Node(child_state, parent=node, depth=node.depth + 1)
                result = recursive_dls(child_node, problem, limit - 1)
                if result is not None:
                    return result
            return None
    return recursive_dls(Node(problem.initial), problem, limit)

# IDS
def ids(problem):
    depth = 0
    while True:
        result = dfs_limited(problem, depth)
        if result is not None:
            return result
        depth += 1

# Grafo de la red de metro
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H', 'I'],
    'F': ['C', 'J'],
    'G': ['D'],
    'H': ['E'],
    'I': ['E', 'J'],
    'J': ['F', 'I']
}

problem = Problem(initial='A', goal='J', graph=graph)

# Comparación BFS
tracemalloc.start()
start_time = time.perf_counter()
path_bfs = bfs(problem)
bfs_time = time.perf_counter() - start_time
bfs_mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

# Comparación IDS
tracemalloc.start()
start_time = time.perf_counter()
path_ids = ids(problem)
ids_time = time.perf_counter() - start_time
ids_mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

# Resultados
print("BFS path:", path_bfs)
print(f"BFS tiempo: {bfs_time:.6f} s, Memoria: {bfs_mem} bytes")

print("IDS path:", path_ids)
print(f"IDS tiempo: {ids_time:.6f} s, Memoria: {ids_mem} bytes")

# Explicación de diferencias
print("\nDiferencias:")
print("- BFS explora por niveles, siempre encuentra la ruta más corta en pasos.")
print("- IDS combina DFS y BFS: aumenta el límite de profundidad progresivamente, garantizando solución óptima en pasos, pero puede repetir exploraciones y ser más lento.")
