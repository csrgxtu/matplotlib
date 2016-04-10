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
pos[1] = array([0,  0]) # O[1]
pos[2] = array([-4, 1]) #W[0]
pos[3] = array([-2, 1]) #W[1]
pos[4] = array([2,  1]) #W[2]
pos[5] = array([4, 1]) #W[3]

# add edges between nodes
edges = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (3, 4, {'linestyle': 'dotted'}), (4, 5)]
G.add_edges_from(edges)

# draw the nodes
nx.draw_networkx_nodes(G, pos, nodelist=[1], node_color='b', node_size=300, alpha=1)
nx.draw_networkx_nodes(G, pos, nodelist=[2, 3, 4, 5], node_color='r', node_size=200, alpha=1)

# draw the edges
# nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1.0, alpha=0.5)

# use plt plot the graph and remove axis
plt.axis('off')
plt.annotate(r'$Y_1$', (-4.1, 1.1))
plt.annotate(r'$Y_2$', (-2.1, 1.1))
plt.annotate(r'$Y_i$', (2.1, 1.1))
plt.annotate(r'$Y_n$', (4.1, 1.1))
plt.annotate(r'$X=(X_1, X_2, \cdots, X_n)$', (-0.2, -0.1))
plt.savefig("linearchain.png")
plt.savefig("linearchain.eps", format="eps")
plt.show()
