import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Exercice 2.1

G=nx.Graph()
G.add_nodes_from(["a","b","c","d","e","f","g","h","i"])
G.add_edges_from([("a","b"),("b","c"),("a","d"),("b","e"),("c","f"),("d","g"),("e","h"),("f","i"),("d","e"),("e","f"),("g","h"),("h","i")])

#specifiy positions of nodes
pos = {"a":(0,0),"b":(1,0),"c":(2,0),"d":(0,1),"e":(1,1),"f":(2,1),"g":(0,2),"h":(1,2),"i":(2,2)}

nx.draw(G,pos,with_labels=True)

plt.show()