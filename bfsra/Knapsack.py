import itertools
import networkx as nx

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
