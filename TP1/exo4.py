import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


graph = {'0': ['1', '2'], '1': ['2', '4'],
         '3': ['6'], '4': ['1'], '5': [], '6': ['3']}
G = nx.Graph(graph)
nx.draw(G, with_labels=True)
plt.show()
