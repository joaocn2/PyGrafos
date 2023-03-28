# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:13:35 2023

@author: 372974
"""

import networkx as nx


G = nx.Graph()

G.add_edges_from([
    ('A','B'), ('A','C'), ('A','D'),
    ('B','C'), ('B','D'),
    ('C','D'), ('D','E')
    ])
nx.draw_networkx(G)
print(nx.graph_number_of_cliques(G))
print(list(nx.enumerate_all_cliques(G)))