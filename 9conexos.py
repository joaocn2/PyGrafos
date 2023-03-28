# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:45:10 2023

@author: 372974
"""

import networkx as nx


G = nx.DiGraph()
G.add_edges_from([
    (1,4),
    (2,1),(2,5),(2,6),
    (3,2),(3,4),
    (4,5),
    (5,4),
    (6,3), (6,5)
    ])

pos = {
           1:   (1.5, .5),
           2:   (1,1),
           3:   (2,2),
           4:   (2,0),
           5:   (0,0),
           6:   (0,2)
       }

# nx.draw_networkx(G, pos = pos)

print('Componenetes fracamente conexas: ')
print(list(nx.weakly_connected_components(G)))

print('GRAFO G EH FRACAMANETE (SIMPLESMENTE CONEXO)?', 'SIM' if nx.is_weakly_connected(G) else 'NAO')

print('GRAFO G EH SEMI CONEXO', 'SIM' if nx.is_semiconnected(G) else 'NAO')

print('GRAFO G EH FORTEMENTE CONEXO', 'SIM' if nx.is_strongly_connected(G) else 'NAO')

print('NUMERO DE COMPONENTES CONEXOS', nx.number_strongly_connected_components(G))

MCOMPCONXO = max(nx.strongly_connected_components(G), key=len)
print('MAIOR COMPONENETE CONEXA', MCOMPCONXO)

grafo_reduzido = nx.condensation(G)

print('grafo reduzido', grafo_reduzido.nodes())

mapa = grafo_reduzido.graph['mapping']
print(mapa)
# nx.draw_networkx(grafo_reduzido)

rotulos = {}
for chave, valor in mapa.items():
    rotulos.setdefault(valor, [].append(chave))
    
    print(rotulos)
    
nx.draw_networkx(grafo_reduzido, with_labels=True, labels = rotulos )