from trees import *
from numpy import inf

text_output = []


def minimax(G, position, depth, is_reverse_order, maximizing_player):
    if depth == 0:
        return G.nodes[position]['data']

    if maximizing_player:
        max_eval = -inf
        if not is_reverse_order:
            for node in G.neighbors(position):
                text_output.append(f"Рассматриваемая вершина: {node}\n")
                eval = minimax(G, node, depth - 1, is_reverse_order, False)
                max_eval = max(max_eval, eval)
        else:
            for node in reversed(list(G.neighbors(position))):
                text_output.append(f"Рассматриваемая вершина: {node}\n")
                eval = minimax(G, node, depth - 1, is_reverse_order, False)
                max_eval = max(max_eval, eval)
        G.nodes[position]['data'] = max_eval
        text_output.append(f"Вершине {position} присвоено значение: {max_eval} (max)\n")
        return max_eval
    else:
        min_eval = +inf
        if not is_reverse_order:
            for node in G.neighbors(position):
                text_output.append(f"Рассматриваемая вершина: {node}\n")
                eval = minimax(G, node, depth - 1, is_reverse_order, True)
                min_eval = min(min_eval, eval)
        else:
            for node in reversed(list(G.neighbors(position))):
                text_output.append(f"Рассматриваемая вершина: {node}\n")
                eval = minimax(G, node, depth - 1, is_reverse_order, True)
                min_eval = min(min_eval, eval)
        G.nodes[position]['data'] = min_eval
        text_output.append(f"Вершине {position} присвоено значение: {min_eval} (min)\n")
        return min_eval


def alpha_beta_pruning(G, position, depth, alpha, beta, is_reverse_order, maximizing_player):
    if depth == 0:
        return G.nodes[position]['data']

    if maximizing_player:
        max_eval = -inf
        if not is_reverse_order:
            for node in G.neighbors(position):
                text_output.append(f"Рассматриваемая вершина: {node}\n")
                eval = alpha_beta_pruning(G, node, depth - 1, alpha, beta, is_reverse_order, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    for item in G.neighbors(position):
                        if int(item) > int(node):
                            text_output.append(f"Вершина {item} отсечена,  т.к.  альфа ({alpha}) >= бета ({beta})\n")
                            G.edges[position, item]['color'] = 'red'
                    break
        else:
            for node in reversed(list(G.neighbors(position))):
                text_output.append(f"Рассматриваемая вершина: {node}\n")
                eval = alpha_beta_pruning(G, node, depth - 1, alpha, beta, is_reverse_order, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    for item in reversed(list(G.neighbors(position))):
                        if int(item) < int(node):
                            text_output.append(f"Вершина {item} отсечена,  т.к.  альфа ({alpha}) >= бета ({beta})\n")
                            G.edges[position, item]['color'] = 'red'
                    break
        G.nodes[position]['data'] = max_eval
        text_output.append(f"Вершине {position} присвоено значение: {max_eval} (max)\n")
        return max_eval
    else:
        min_eval = +inf
        if not is_reverse_order:
            for node in G.neighbors(position):
                text_output.append(f"Рассматриваемая вершина: {node}\n")
                eval = alpha_beta_pruning(G, node, depth - 1, alpha, beta, is_reverse_order, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    for item in G.neighbors(position):
                        if int(item) > int(node):
                            text_output.append(f"Вершина {item} отсечена,  т.к.  альфа ({alpha}) >= бета ({beta})\n")
                            G.edges[position, item]['color'] = 'red'
                    break
        else:
            for node in reversed(list(G.neighbors(position))):
                text_output.append(f"Рассматриваемая вершина: {node}\n")
                eval = alpha_beta_pruning(G, node, depth - 1, alpha, beta, is_reverse_order, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    for item in reversed(list(G.neighbors(position))):
                        if int(item) < int(node):
                            text_output.append(f"Вершина {item} отсечена,  т.к.  альфа ({alpha}) >= бета ({beta})\n")
                            G.edges[position, item]['color'] = 'red'
                    break
        G.nodes[position]['data'] = min_eval
        text_output.append(f"Вершине {position} присвоено значение: {min_eval} (min)\n")
        return min_eval