import itertools
import networkx as nx

from bfsra import is_hamiltonian

def test_hamiltonian():
    G = nx.graph_atlas_g()
    G1 = [ i for i in G[1:] if nx.is_connected(i)]
    assert is_hamiltonian(G[1]) == False
    assert is_hamiltonian(G1[888]) == (0, 1, 4, 5, 6, 2, 3)
    assert is_hamiltonian(G1[77]) == False
    
