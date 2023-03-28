# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:11:54 2023

@author: 372974
"""
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    (1,2),(1,5),
    (2,3),(2,6),
    (3,7),
    (5,7)
    ])

#plt.figure(1)
# nx.draw_networkx(G)

#print('é conexo?', 'SIM' if nx.is_connected(G) else 'Nao')
#print('# de componenetes conexas', nx.number_connected_components(G))


##





H = nx.Graph()

H.add_edges_from([
    (1,3),(1,5),
    (2,6),
    (3,7),
    (5,7)
    ])

plt.figure(2)
nx.draw_networkx(H)

print('é conexo?', 'SIM' if nx.is_connected(H) else 'Nao')
print('# de componenetes conexas', nx.number_connected_components(H))