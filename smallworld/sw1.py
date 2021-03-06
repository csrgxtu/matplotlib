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

# list_x2_axis.pop()
# list_y2_axis.pop()
list_x2_axis = list_x2_axis[1:]
list_y2_axis = list_y2_axis[1:]
print len(list_x2_axis)

# set axis limits
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

G = nx.Graph()
nodes = range(1, 19)
G.add_nodes_from(nodes)
pos = nx.spring_layout(G)
for i in range(1, 19):
    pos[i] = array([list_x2_axis[i - 1], list_y2_axis[i - 1]])

print pos

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

for i in range(1, 19):
    edges.append((i, i + 1))
edges = edges[0:-1]
edges.append((18, 1))


nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color='k', node_size=50, alpha=1)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1.0, alpha=1)

# plot the coordinates
# plt.plot(list_x2_axis,list_y2_axis,c='r')
# plt.plot(list_x2_axis,list_y2_axis,'k*')

# show the plot
plt.axis('off')
plt.savefig("sw1.png")
plt.show()
