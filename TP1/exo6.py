import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


graph = {'1': ['1', '2', '3', '4', '5', '6'], '2': ['2',  '4', '6'],
         '3': ['3', '6'], '4': ['4'], '5': ['5'], '6': ['6']}
G = nx.DiGraph(graph)
nx.draw(G, with_labels=True)
plt.show()
