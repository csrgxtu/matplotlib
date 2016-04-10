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
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
G.add_nodes_from(nodes)

# nodes coordinates
pos = nx.spring_layout(G)
pos[1] = array([-1,  0]) # O[1]
pos[2] = array([-0.6, -1]) #W[0]
pos[3] = array([0.7, -1]) #W[1]
pos[4] = array([1,  0.2]) #W[2]
pos[5] = array([-0.5,  1]) #W[3]
pos[6] = array([0, 0]) # o
pos[7] = array([0.7, 1]) #O[2]
pos[8] = array([0.2, 0.8]) #O[3]
pos[9] = array([-1, 1]) # O[0]
pos[10] = array([1, -1]) #O[4]

# add edges between nodes
# edges = [(1, 2), (1, 6), (2, 4), (3, 4), (3, 6), (4, 6), (5, 6)]
edges = [(6, 2), (6, 3), (6, 4), (6,5), (2, 1), (4, 7), (7, 8), (5, 8)]
G.add_edges_from(edges)

# draw the nodes
nx.draw_networkx_nodes(G, pos, nodelist=[6, 8], node_color='b', node_size=300, alpha=1, label='C')
nx.draw_networkx_nodes(G, pos, nodelist=[3, 4, 7], node_color='r', node_size=200, alpha=1, label='A')
nx.draw_networkx_nodes(G, pos, nodelist=[5, 2, 1], node_color='g', node_size=250, alpha=1, label='B')
# nx.draw_networkx_nodes(G, pos, nodelist=[1], node_color='r', node_size=300, alpha=1)
# nx.draw_networkx_nodes(G, pos, nodelist=[3, 6], node_color='b', node_size=300, alpha=1)
# nx.draw_networkx_nodes(G, pos, nodelist=[4, 5], node_color='g', node_size=300, alpha=1)
# draw the edges
# nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1.0, alpha=0.5)
# nx.drawl(G)

# use plt plot the graph and remove axis
plt.axis('off')
plt.legend(scatterpoints=1, loc='upper left', frameon=False)
plt.savefig("globalmarkov.png")
plt.savefig("globalmarkov.eps", format="eps")
plt.show()
