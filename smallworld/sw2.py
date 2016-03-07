#!/usr/bin/env python
# I wish I had payed more attention in my calculus class
# when I was at school. Could have saved me ages.

from math import sin,cos,pi
import matplotlib.pyplot as plt
import networkx as nx
from numpy import array


# use radians instead of degrees - OBVIOUSLY!!
list_radians = [0]

# from degrees to radians, the 0 is already included so
# we don't make the universe collapse by dividing by zero.
for i in range(0, 360, 20):
    float_div = 180.0/(i+1)
    list_radians.append(pi/float_div)

# list of coordinates for each point
list_x2_axis = []
list_y2_axis = []

# calculate coordinates
# and append to above list
for a in list_radians:
    list_x2_axis.append(cos(a))
    list_y2_axis.append(sin(a))

list_x2_axis = list_x2_axis[1:]
list_y2_axis = list_y2_axis[1:]

# set axis limits
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

# G = nx.Graph()
G=nx.grid_graph(dim=[6,6])

nodes = range(1, 19)
G.add_nodes_from(nodes)
pos = nx.spring_layout(G)
# pos=nx.spring_layout(G,iterations=100)

for i in range(1, 19):
    pos[i] = array([list_x2_axis[i - 1], list_y2_axis[i - 1]])

edges = []
for i in range(1, 19):
    edges.append((i, i + 2))

edges = edges[0:-2]
edges.append((17, 1))
edges.append((18, 2))

edges.append((4, 9))
edges.append((6, 12))
edges.append((10, 16))
edges.append((14, 18))
edges.append((11, 17))
edges.append((3, 10))
edges.append((8, 12))
edges.append((16, 4))
edges.append((18, 7))
edges.append((1, 8))

plt.subplot(221)
# plt.subplot(111)

plt.axis('off')
npos = {}
for key, val in pos.items():
    # print type(key)
    if type(key) == int:
        # print key, val
        npos[key] = array(val)
nx.draw_networkx_nodes(G, npos, nodelist=nodes, node_color='k', node_size=50, alpha=1)
# nx.draw_networkx_edges(G, npos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, npos, edgelist=edges, width=1.0, alpha=1)

plt.subplot(222)
plt.axis('off')
nx.draw_networkx_nodes(G, npos, nodelist=nodes, node_color='k', node_size=50, alpha=1)
nx.draw_networkx_edges(G, npos, edgelist=edges, width=1.0, alpha=1)

plt.subplot(223)
plt.axis('off')
nx.draw_networkx_nodes(G, npos, nodelist=nodes, node_color='k', node_size=50, alpha=1)
nx.draw_networkx_edges(G, npos, edgelist=edges, width=1.0, alpha=1)

# show the plot
plt.show()
