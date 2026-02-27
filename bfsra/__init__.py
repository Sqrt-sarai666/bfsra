import itertools
import networkx as nx

def is_hamiltonian_cycle(graph, cycle):
    """Checks if cycle is a hamiltonian cycle in graph.
    Graph is a Networkx graph and cycle is a list of vertices"""
    n= len(set(cycle))
    if n != graph.order():
        return False
    for i in range(n-1):
        if not graph.has_edge(cycle[i],cycle[i+1]):
            return False
    if not graph.has_edge(cycle[n-1],cycle[0]):
        return False
    return True

def is_hamiltonian(graph):
    """Checks if cycle is a hamiltonian cycle in graph.
    Graph is a Networkx graph """
    vertices = list(graph.nodes())
    if len (vertices) < 3 or not nx.is_connected(graph):
        return False
    perms =  itertools.permutations(vertices)
    for perm in perms:
        if is_hamiltonian_cycle(graph, perm):
            return perm
    return False


def is_proper_coloring(graph, coloring):
    for edge in graph.edges():
        if coloring[edge[0]] == coloring[edge[1]]:
            return False
    return True

def is_3_colorable(graph):
    n = graph.order()
    colorings = itertools.product([0,1,2], repeat = n)
    for coloring in colorings:
        if is_proper_coloring(graph, coloring):
            return coloring
    return False

def sum_of_values(values, keys):
    # Hace la suma de los valores del arreglo
    n = len(values)
    sum = 0
    for i in range(n):
        sum += values[i]*keys[i]
    return sum

def knapsack_problem(profits, weights, capacity, goal):
    #Solucion por fuerza bruta para knapsack problem
    if len(weights) != len(profits):
        return False
    n = len(profits)
    sequences = itertools.product([0,1],repeat = n)
    for secuence in sequences:
        if sum_of_values(weights , secuence) <= capacity:
            if sum_of_values(profits, secuence) >= goal:
                return secuence
    return False

