import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Exercice 1

G=nx.Graph()
G.add_nodes_from(["a","b","c","d","e"])
G.add_edges_from([("a","b"),("a","d"),("a","e"),("b","c"),("b","d"),("c","d"),("c","e"),("d","e")])

nx.draw(G,with_labels=True)
plt.show()