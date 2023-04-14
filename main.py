import sys
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

path = []
text_output = []
G = nx.Graph()

G.add_nodes_from([
    ("1", {"heuristics": 14}),
    ("2", {"heuristics": 13}),
    ("3", {"heuristics": 12}),
    ("4", {"heuristics": 11}),
    ("5", {"heuristics": 10}),
    ("6", {"heuristics": 9}),
    ("7", {"heuristics": 8}),
    ("8", {"heuristics": 7}),
    ("9", {"heuristics": 6}),
    ("10", {"heuristics": 5}),
    ("11", {"heuristics": 4}),
    ("12", {"heuristics": 3}),
    ("13", {"heuristics": 2}),
    ("14", {"heuristics": 1}),
    ("15", {"heuristics": 0}),
    ("16", {"heuristics": 14}),
    ("17", {"heuristics": 13}),
    ("18", {"heuristics": 12}),
    ("19", {"heuristics": 11}),
    ("20", {"heuristics": 10}),
    ("21", {"heuristics": 9}),
    ("22", {"heuristics": 8}),
    ("23", {"heuristics": 7}),
    ("24", {"heuristics": 6}),
    ("25", {"heuristics": 5}),
    ("26", {"heuristics": 4}),
    ("27", {"heuristics": 3}),
    ("28", {"heuristics": 2}),
    ("29", {"heuristics": 1}),
    ("30", {"heuristics": 0}),
])

G.add_edges_from([
    ("1", "2", {"weight": 0}),
    ("1", "3", {"weight": 0}),

])
# G.add_edges_from([
#     ("1", "2", {"weight": 10}),
#     ("1", "3", {"weight": 12}),
#     ("1", "5", {"weight": 23}),
#     ("2", "4", {"weight": 14}),
#     ("2", "5", {"weight": 6}),
#     ("2", "6", {"weight": 18}),
#     ("3", "4", {"weight": 4}),
#     ("3", "5", {"weight": 20}),
#     ("3", "7", {"weight": 34}),
#     ("4", "6", {"weight": 26}),
#     ("4", "7", {"weight": 7}),
#     ("4", "9", {"weight": 40}),
#     ("5", "6", {"weight": 7}),
#     ("5", "7", {"weight": 10}),
#     ("5", "8", {"weight": 23}),
#     ("6", "8", {"weight": 3}),
#     ("6", "12", {"weight": 14}),
#     ("7", "10", {"weight": 6}),
#     ("8", "10", {"weight": 1}),
#     ("8", "12", {"weight": 8}),
#     ("9", "10", {"weight": 5}),
#     ("9", "13", {"weight": 8}),
#     ("10", "11", {"weight": 1}),
#     ("10", "13", {"weight": 4}),
#     ("11", "12", {"weight": 4}),
#     ("11", "15", {"weight": 9}),
#     ("12", "14", {"weight": 6}),
#     ("12", "15", {"weight": 4}),
#     ("13", "14", {"weight": 3}),
#     ("14", "15", {"weight": 6}),
# ])



def draw_path():
    tmp_paar_path = []
    for i in range(len(path) - 1):
        tmp_paar_path.append(path[i])
        tmp_paar_path.append(path[i + 1])
    tmp_paar_path = np.array(tmp_paar_path).reshape(-1, 2)
    # print(tmp_paar_path)

    tmp_edge_array = []
    for u, v, d in G.edges:
        tmp_edge_array.append(u)
        tmp_edge_array.append(v)
    tmp_edge_array = np.array(tmp_edge_array).reshape(-1, 2)
    # print(tmp_edge_array)

    if len(path) > 0:
        edge_colors = []
        for u1, v1 in tmp_edge_array:
            flag = 0
            for u2, v2 in tmp_paar_path:
                if u1 == u2 and v1 == v2:
                    flag = 1
                else:
                    pass
            edge_colors.append(flag)
        return np.array(edge_colors)
    else:
        return np.full(len(G.edges), 0)


def draw_graph():
    pos = nx.planar_layout(G)

    node_labels = {n: (d["heuristics"]) for n, d in G.nodes(data=True)}
    edge_labels = {(u, v): (d["weight"]) for u, v, d in G.edges(data=True)}

    # edge_colors = draw_path()

    nx.draw(G, pos, with_labels=True, node_size=200, node_color="pink", font_size=10, width=1)
    nx.draw_networkx_edge_labels(G, pos, font_color="maroon", font_size=6)

    plt.show()

draw_graph()
