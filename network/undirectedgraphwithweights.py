#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 06/Mar/2016
# File: undirectedgraphwithweightsnode.py
# Desc: draw graph of undirected with weights
#
# Produced By CSRGXTU
import matplotlib.pyplot as plt
import networkx as nx
from numpy import array

G = nx.Graph()

# add 6 same nodes
nodes = [1, 2, 3, 4, 5, 6]
G.add_nodes_from(nodes)

# nodes coordinates
pos = nx.spring_layout(G)
pos[1] = array([-1,  0])
pos[2] = array([-0.6, -1])
pos[3] = array([0.7, -1])
pos[4] = array([1,  0.2])
pos[5] = array([-0.5,  1])
pos[6] = array([0, 0])

# add edges between nodes
edges = [(1, 2), (1, 6), (2, 4), (3, 4), (3, 6), (4, 6), (5, 6)]
G.add_edges_from(edges)

# draw the nodes
# nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color='r', node_size=500, alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[1, 3], node_size=500, alpha=1)
nx.draw_networkx_nodes(G, pos, nodelist=[2, 5], node_size=100, alpha=1)
nx.draw_networkx_nodes(G, pos, nodelist=[4, 6], node_size=300, alpha=1)

# draw the edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1.0, alpha=0.5)

# use plt plot the graph and remove axis
plt.axis('off')
plt.savefig("undirectedgraphwithweightnodse.png")
plt.show()
