import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Exercice 3

# Graphe 1
G1=nx.Graph()
G1.add_nodes_from(["a","b","c","d"])
G1.add_edges_from([("b","a"),("c","b"),("a","d"),("b","d"),("d","c")])

#specifiy positions of nodes




# Graphe 2
DG1=nx.DiGraph()
DG1.add_nodes_from([1,2,3,4,5])
#specifiy positions of nodes
DG1.add_edges_from([(1,5),(1,3),(4,2),(5,2),(3,5)])


# Graphe 3
DG2=nx.DiGraph()
DG2.add_nodes_from([1,2,"a","b"])
#specifiy positions of nodes
DG2.add_edges_from([("a",2),(1,"b"),("b","a"),(1,2)])

fig,(ax1,ax2,ax3) = plt.subplots(1,3)
nx.draw(G1,with_labels=True,ax=ax1,node_color="lightblue",node_size=500)
nx.draw(DG1,with_labels=True,ax=ax2,node_color="lightblue",node_size=500)
nx.draw(DG2,with_labels=True,ax=ax3,node_color="lightblue",node_size=500)

ax1.set_title("Graphe non oriente G")
ax2.set_title("Graphe oriente DG1")
ax3.set_title("Graphe oriente DG2")
plt.tight_layout()
plt.show()