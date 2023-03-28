# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:13:35 2023

@author: 372974
"""

import networkx as nx


G = nx.barbell_graph(10,2)
nx.draw_networkx(G)
print('Tem pontes? ', 'SIM' if nx.has_bridges(G) else 'Nao')
print('Pontes:', list(nx.bridges(G)))
print('Pontes numero:', len(list(nx.bridges(G))))