import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Exercice 2.1

G=nx.Graph()
G.add_nodes_from([1,2,3,4,5,6])

#specifiy positions of nodes
pos = {1:(0,0),2:(4,0),3:(2,3),4:(0,2),5:(4,2),6:(2,-1)}

G.add_edges_from([(1,2),(2,3),(3,1),(4,5),(5,6),(6,4)])

nx.draw(G,pos,with_labels=True)

plt.show()