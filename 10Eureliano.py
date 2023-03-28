# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:24:56 2023

@author: 372974
"""

import networkx as nx

G = nx.Graph()

G.add_edges_from([
    
        (1,2), (1,3),
        (2,3),(2,4),(2,6),
        (3,4),(3,5),
        (4,5),(4,6),
        (5,6),(5,7),
        (6,7)
    ])

pos = {
     1: (.5,1), 2:  (0, .75),
     3: (0,.75), 4:(.5, .5),
     5: (.5,1), 6:(0, .25), 7:(.5,0)
     }

# nx.draw_networkx(G, pos=pos)

print("Grafo G é eureleiano?", "SIM" if nx.is_eulerian(G) else 'NAO')


H = nx.Graph()

H.add_edges_from([
    
        (1,2), (1,3),
        (2,3),(2,4),(2,6),
        (3,4),(3,5),
        (4,5),(4,6),
        (5,6)
    ])

pos = {
     1: (.5,1), 2:  (0, .75),
     3: (0,.75), 4:(.5, .5),
     5: (.5,1), 6:(0, .25)
     }


# nx.draw_networkx(H, pos=pos)

print("Grafo H é eureleiano?", "SIM" if nx.is_eulerian(H) else 'NAO')
print("Grafo H é SEMI - eureleiano?", "SIM" if nx.is_semieulerian(H) else 'NAO')

###############################################



I = nx.Graph()

I.add_edges_from([
    
        (1,2), (1,3), (1,5)
        (2,3),(2,4),
        (3,4),(3,5),
        (4,5)
    ])

pos = {
     1: (0, .75),
     2: (0,.75), 3:(.5, .5),
     4: (.5,1), 5:(0, .25), 7:(.5,0)
     }

# nx.draw_networkx(I, pos=pos)

print("Grafo I é eureleiano?", "SIM" if nx.is_eulerian(I) else 'NAO')
print("Grafo I é SEMI - eureleiano?", "SIM" if nx.is_semieulerian(I) else 'NAO')