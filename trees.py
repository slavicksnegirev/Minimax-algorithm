from tree_variants.tree_var1 import *
from tree_variants.tree_var2 import *
from networkx.drawing.nx_agraph import graphviz_layout

current_tree_var = '1'
trees_dict = {'1': tree_var1, '2': tree_var2}

def color_map_update(G):
    for u, v in G.edges:
        G.edges[u, v]['color'] = 'grey'


def draw_tree(G):
    pos = graphviz_layout(G, prog='dot')
    node_keys = {n: n for n, d in G.nodes(data=True)}
    node_values = {n: (d["data"]) for n, d in G.nodes(data=True)}
    edge_color_map = {(u, v): (d["color"]) for u, v, d in G.edges(data=True)}

    nx.draw(G, pos, arrows=True, node_size=90, node_color="green", edge_color=edge_color_map.values())
    nx.draw_networkx_labels(G, pos, labels=node_values,font_size=10, font_color="white")

    for i in pos:
        my_list = list(pos[i])
        my_list[1] -= 10
        pos[i] = tuple(my_list)

    nx.draw_networkx_labels(G, pos, labels=node_keys, font_size=6, font_color="blue")

    # plt.show()