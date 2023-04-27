import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from numpy import inf
from networkx.drawing.nx_agraph import graphviz_layout


G = nx.DiGraph()

G.add_nodes_from([
    ("1", {"data": 0}),
    ("2", {"data": 0}),
    ("3", {"data": 0}),
    ("4", {"data": 0}),
    ("5", {"data": 0}),
    ("6", {"data": 0}),
    ("7", {"data": 0}),
    ("8", {"data": 0}),
    ("9", {"data": 0}),
    ("10", {"data": 0}),
    ("11", {"data": 0}),
    ("12", {"data": 0}),
    ("13", {"data": 0}),
    ("14", {"data": 0}),
    ("15", {"data": 0}),
    ("16", {"data": 0}),
    ("17", {"data": 0}),
    ("18", {"data": 0}),
    ("19", {"data": 0}),
    ("20", {"data": 0}),
    ("21", {"data": 0}),
    ("22", {"data": 0}),
    ("23", {"data": 0}),
    ("24", {"data": 0}),
    ("25", {"data": 0}),
    ("26", {"data": 0}),
    ("27", {"data": 3}),
    ("28", {"data": 2}),
    ("29", {"data": 1}),
    ("30", {"data": 0}),
    ("31", {"data": 3}),
    ("32", {"data": 4}),
    ("33", {"data": 3}),
    ("34", {"data": 3}),
    ("35", {"data": 2}),
    ("36", {"data": 5}),
    ("37", {"data": 4}),
    ("38", {"data": 5}),
    ("39", {"data": 6}),
    ("40", {"data": 5}),
    ("41", {"data": 6}),
    ("42", {"data": 5}),
    ("43", {"data": 4}),
    ("44", {"data": 2}),
    ("45", {"data": 1}),
    ("46", {"data": 5}),
    ("47", {"data": 6}),
    ("48", {"data": 1}),
    ("49", {"data": 0}),
    ("50", {"data": 2}),
    ("51", {"data": 7}),
    ("52", {"data": 6}),
    ("53", {"data": 4}),
    ("54", {"data": 3}),
    ("55", {"data": 1}),
    ("56", {"data": 3}),
    ("57", {"data": 2}),
    ("58", {"data": 1}),
    ("59", {"data": 0}),
    ("60", {"data": 2}),
    ("61", {"data": 2}),
    ("62", {"data": 1}),
])

G.add_edges_from([
    ("1", "2"),
    ("1", "3"),
    ("1", "4"),
    ("2", "5"),
    ("2", "6"),
    ("3", "7"),
    ("3", "8"),
    ("3", "9"),
    ("4", "10"),
    ("4", "11"),
    ("5", "12"),
    ("5", "13"),
    ("5", "14"),
    ("6", "15"),
    ("6", "16"),
    ("6", "17"),
    ("7", "18"),
    ("7", "19"),
    ("8", "20"),
    ("8", "21"),
    ("9", "22"),
    ("9", "23"),
    ("10", "24"),
    ("10", "25"),
    ("11", "26"),

    ("12", "27"),
    ("12", "28"),
    ("13", "29"),
    ("13", "30"),
    ("14", "31"),
    ("14", "32"),
    ("14", "33"),
    ("15", "34"),
    ("15", "35"),
    ("16", "36"),
    ("16", "37"),
    ("16", "38"),
    ("17", "39"),
    ("17", "40"),
    ("17", "41"),
    ("18", "42"),
    ("18", "43"),
    ("19", "44"),
    ("19", "45"),
    ("20", "46"),
    ("20", "47"),
    ("21", "48"),
    ("21", "49"),
    ("21", "50"),
    ("22", "51"),
    ("22", "52"),
    ("23", "53"),
    ("23", "54"),
    ("23", "55"),
    ("24", "56"),
    ("24", "57"),
    ("25", "58"),
    ("25", "59"),
    ("26", "60"),
    ("26", "61"),
    ("26", "62"),
])




def minimax(position, depth, maximizingPlayer):
    if depth == 0:
        # or game over in position
        return G.nodes[position]['data']

    if maximizingPlayer:
        maxEval = -inf
        for node in G.neighbors(position):
            eval = minimax(node, depth - 1, False)
            maxEval = max(maxEval, eval)
        G.nodes[position]['data'] = maxEval
        print("maxEval = " + str(maxEval))
        return maxEval
    else:
        minEval = +inf
        for node in G.neighbors(position):
            eval = minimax(node, depth - 1, True)
            minEval = min(minEval, eval)
        G.nodes[position]['data'] = minEval
        print("minEval = " + str(minEval))
        return minEval


# minimax("1", 4, True)

def alpha_beta_pruning(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0:
        # or game over in position
        return G.nodes[position]['data']

    if maximizingPlayer:
        maxEval = -inf
        for node in G.neighbors(position):
            eval = alpha_beta_pruning(node, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        G.nodes[position]['data'] = maxEval
        print("maxEval = " + str(maxEval))
        return maxEval
    else:
        minEval = +inf
        for node in G.neighbors(position):
            eval = alpha_beta_pruning(node, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        G.nodes[position]['data'] = minEval
        print("minEval = " + str(minEval))
        return minEval



def draw_tree():
    pos = graphviz_layout(G, prog='dot')
    node_labels = {n: (d["data"]) for n, d in G.nodes(data=True)}

    nx.draw(G, pos, arrows=True, node_size=100, node_color="brown")
    nx.draw_networkx_labels(G, pos, labels=node_labels,font_size=10, font_color="white")

    plt.show()


alpha_beta_pruning("1", 4, -inf, +inf, True)
draw_tree()
