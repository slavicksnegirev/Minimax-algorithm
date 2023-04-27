from tree import *
from numpy import inf

text_output = []

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
        # print("maxEval = " + str(maxEval))
        return maxEval
    else:
        minEval = +inf
        for node in G.neighbors(position):
            eval = minimax(node, depth - 1, True)
            minEval = min(minEval, eval)
        G.nodes[position]['data'] = minEval
        # print("minEval = " + str(minEval))
        return minEval


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
        # print("maxEval = " + str(maxEval))
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
        # print("minEval = " + str(minEval))
        return minEval