from tree import *
from numpy import inf

text_output = []

def minimax(position, depth, is_reverse_order, maximizing_player):
    if depth == 0:
        # or game over in position
        return G.nodes[position]['data']

    if maximizing_player:
        max_eval = -inf
        if not is_reverse_order:
            for node in G.neighbors(position):
                text_output.append("Рассматриваемая вершина: " + str(node) + "\n")
                eval = minimax(node, depth - 1, is_reverse_order, False)
                max_eval = max(max_eval, eval)
        else:
            for node in reversed(list(G.neighbors(position))):
                text_output.append("Рассматриваемая вершина: " + str(node) + "\n")
                eval = minimax(node, depth - 1, is_reverse_order, False)
                max_eval = max(max_eval, eval)
        G.nodes[position]['data'] = max_eval
        text_output.append("Вершине " + str(position) + " присвоено значение: " + str(max_eval) + " (max)\n")
        return max_eval
    else:
        min_eval = +inf
        if not is_reverse_order:
            for node in G.neighbors(position):
                text_output.append("Рассматриваемая вершина: " + str(node) + "\n")
                eval = minimax(node, depth - 1, is_reverse_order, True)
                min_eval = min(min_eval, eval)
        else:
            for node in reversed(list(G.neighbors(position))):
                text_output.append("Рассматриваемая вершина: " + str(node) + "\n")
                eval = minimax(node, depth - 1, is_reverse_order, True)
                min_eval = min(min_eval, eval)
        G.nodes[position]['data'] = min_eval
        text_output.append("Вершине " + str(position) + " присвоено значение: " + str(min_eval) + " (min)\n")
        return min_eval


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