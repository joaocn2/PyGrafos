# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:26:36 2023

@author: 372974
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.complete_graph(5)
plt.figure(1)
nx.draw(G, with_labels=(1))

MA = nx.to_numpy_array(G)
print(MA)

matriz = np.matrix([#1 2 3
                    [0,1,1], #1
                    [1,0,1], #2
                    [1,1,0], #3
    ])


print(matriz)
H = nx.from_numpy_matrix(matriz)
plt.figure(2)

nx.draw(H, with_labels=(1))