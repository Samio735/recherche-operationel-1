import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G = nx.DiGraph({'a': ['b', 'c'], 'b': ['c', 'a'], 'c': ['b']})
print(nx.to_pandas_adjacency(G))


def calc_matrix_adj(G):
    nodes = G.nodes
    matrix = list(nodes)
    i = 0
    for node in nodes:
        row = list(nodes)
        j = 0
        for other_node in nodes:
            if G.has_successor(node, other_node):
                row[j] = 1
            else:
                row[j] = 0
            j = j + 1
        matrix[i] = row
        i = i + 1
    df = pd.DataFrame(matrix)
    print(df)
    return matrix


def sqr_matrix(M):
    new_matrix = M
    i = 0
    for row in M:
        j = 0

        for el in row:
            new_matrix[i][j] = el
            j = j + 1

    i = i + 1
    return new_matrix


print("the adj matrix M : \n")
M = calc_matrix_adj(G)
df = pd.DataFrame(M)
print("\n M^2 : \n")
df2 = df * df
print(df2)
print(sqr_matrix(M))
# df4 = df2.dot(df2)
# print("\n M^4 : \n")
# print(df4)
# df3 = df2 + df
# print("\n M + M^2 : \n")
# print(df3)
# df7 = df + df2 + df3 + df4
# print("\n M + M^2 + M^3 + M^4 : \n")
# print(df7)
nx.draw(G, with_labels=True)
plt.show()
