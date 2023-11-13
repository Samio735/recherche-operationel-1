import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


graph = {'0': {'1': {'weight': 0.4}, '2': {'weight': 0.5}, '3': {'weight': 0.1}}, '1': {'2': {'weight': 0.7}}, '2': {'3': {'weight': 0.9}},
         '3': {}}
G = nx.DiGraph(graph)
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, pos=pos)
labels = nx.get_edge_attributes(G, 'weight')
print(labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
