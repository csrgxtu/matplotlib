#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 10/Apr/2016
# File: localmarkov.py
# Desc: draw graph of undirected with different node type for local markov
# property.
#
# Produced By CSRGXTU
import matplotlib.pyplot as plt
import networkx as nx
from numpy import array

G = nx.Graph()

# add 6 same nodes
nodes = [1, 2, 3, 4, 5]
G.add_nodes_from(nodes)

# nodes coordinates
pos = nx.spring_layout(G)
pos[1] = array([0, 0])
pos[2] = array([1, 0])
pos[3] = array([2, 0])
pos[4] = array([-1, 0])
pos[5] = array([-2, 0])

pos[6] = array([0, 1])
pos[7] = array([1, 1])
pos[8] = array([2,  1])
pos[9] = array([-1, 1])
pos[10] = array([-2, 1])

# add edges between nodes
edges = [(10, 9), (9, 8), (8, 7), (7, 6), (1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
G.add_edges_from(edges)

# draw the nodes
nx.draw_networkx_nodes(G, pos, nodelist=[1, 2, 3, 4, 5], node_color='b', node_size=200, alpha=1)
nx.draw_networkx_nodes(G, pos, nodelist=[6, 7, 8, 9, 10], node_color='r', node_size=200, alpha=1)

# draw the edges
# nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1.0, alpha=0.5)

# use plt plot the graph and remove axis
plt.axis('off')
plt.annotate(r'$Y_1$', (-2, 1.1))
plt.annotate(r'$Y_2$', (-1, 1.1))
plt.annotate(r'$Y_{i-1}$', (0, 1.1))
plt.annotate(r'$Y_i$', (1, 1.1))
plt.annotate(r'$Y_n$', (2, 1.1))

plt.annotate(r'$X_1$', (-2, -0.1))
plt.annotate(r'$X_2$', (-1, -0.1))
plt.annotate(r'$X_{i-1}$', (0, -0.1))
plt.annotate(r'$X_i$', (1, -0.1))
plt.annotate(r'$X_n$', (2, -0.1))

plt.savefig("linearchainsame.png")
plt.savefig("linearchainsame.eps", format="eps")
plt.show()
