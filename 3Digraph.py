# -*- coding: utf-8 -*-
import networkx as nx


G = nx.DiGraph()

G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(2,3),(3,1),(4,5),(5,4),(4,6),(6,5)])

nx.draw(G, with_labels=(1), node_color='g')