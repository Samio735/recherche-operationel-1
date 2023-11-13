import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


graph = {'1': ['1', '2', '3', '4', '5', '6'], '2': ['2',  '4', '6'],
         '3': ['3', '6'], '4': ['4'], '5': ['5'], '6': ['6']}
G = nx.Graph(graph)
posistion = nx.spring_layout(G)
nx.draw(G, with_labels=True, pos=posistion)
matrix = nx.to_numpy_array(G)
complete = True
print(G.nodes)
print(G.edges)
iterator = G.adjacency()
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
plt.show()

# 222f58
# F0c75c
