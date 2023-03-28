# -*- coding: utf-8 -*-
import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])

print('NODES: ')
print(G.nodes())


G.add_edge(1,2)
e = (2,3)
G.add_edge(*e)
G.add_edges_from([(2,3),(3,2), (1,3)])
print('ARESTAS: ', G.edges())

nx.draw(G, with_labels=(1), node_color='b')