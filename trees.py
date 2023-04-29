from copy import deepcopy
from tree_variants.tree_var1 import *
from tree_variants.tree_var2 import *
from tree_variants.tree_var3 import *
from tree_variants.tree_var4 import *
from tree_variants.tree_var5 import *
from tree_variants.tree_var6 import *
from tree_variants.tree_var7 import *
from tree_variants.tree_var8 import *
from tree_variants.tree_var9 import *
from tree_variants.tree_var10 import *
from tree_variants.tree_var11 import *
from tree_variants.tree_var12 import *
from networkx.drawing.nx_agraph import graphviz_layout


class Current_tree_variation:
    def __init__(self):
        self.current_tree_var = '1'

    def __str__(self):
        return current_tree_var

    def get(self):
        return self.current_tree_var

    def change(self, new_value):
        assert isinstance(new_value, str)
        self.current_tree_var = new_value


class Data_list:
    def __init__(self):
        self.data_list = []
        for item in trees_dict.values():
            self.data_list.append(list(item.nodes(data=True)))

    def __str__(self):
        return data_list

    def get(self):
        return self.data_list


trees_dict = {
    '1': tree_var1,
    '2': tree_var2,
    '3': tree_var3,
    '4': tree_var4,
    '5': tree_var5,
    '6': tree_var6,
    '7': tree_var7,
    '8': tree_var8,
    '9': tree_var9,
    '10': tree_var10,
    '11': tree_var11,
    '12': tree_var12,
}
data_list = list()
for item in trees_dict.values():
    data_list.append(list(item.nodes(data=True)))
data_list = deepcopy(data_list)
current_tree_var = Current_tree_variation()


def data_update(G, index):
    G.add_nodes_from(data_list[index])


def color_map_update(G):
    for u, v in G.edges:
        G.edges[u, v]['color'] = 'grey'


def draw_tree(G):
    pos = graphviz_layout(G, prog='dot')
    node_keys = {n: n for n, d in G.nodes(data=True)}
    node_values = {n: (d["data"]) for n, d in G.nodes(data=True)}
    edge_color_map = {(u, v): (d["color"]) for u, v, d in G.edges(data=True)}

    nx.draw(G, pos, arrows=True, node_size=90, node_color="green", edge_color=edge_color_map.values())
    nx.draw_networkx_labels(G, pos, labels=node_values,font_size=8, font_color="white")

    for i in pos:
        my_list = list(pos[i])
        my_list[1] -= 10
        pos[i] = tuple(my_list)

    nx.draw_networkx_labels(G, pos, labels=node_keys, font_size=6, font_color="blue")
    # plt.show()