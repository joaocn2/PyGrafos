# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:26:15 2023

@author: 372974
"""

import networkx as nx
import collections

G = nx.Graph()
G.add_edges_from([
    ('C','A'), ('C','B'), ('C','D'), ('C', 'F'),
    ('F','E'), ('F','G'), ('F','H'), ('F', 'I'), ('F','J'),
    ('I','H'), ('I','J'), ('I','L'),
    ('B','E'), ('D','G'), ('E','H'), ('G', 'J'),
    ('L','K'), ('L','M')
    ])
# nx.draw_networkx(G)

print('Diametro:', nx.diameter(G))
print('Raio:', nx.radius(G))
print('Centro:', nx.center(G))

ex_vertices = sorted(nx.eccentricity(G).items())
print('Exentricidade: ',dict(ex_vertices))

dex = dict(ex_vertices)
print(dex['H'])

for v,e in ex_vertices:
    print(v,e)