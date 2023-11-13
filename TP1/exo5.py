import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


graph = {'0': ['1', '2', '3', '4'], '1': ['0', '2', '3', '4'], '2': ['0', '1', '3', '4'],
         '3': ['0', '1', '2', '4'], '4': ['0', '1', '2', '3']}
G = nx.DiGraph(graph)
nx.draw(G, with_labels=True)
plt.show()
