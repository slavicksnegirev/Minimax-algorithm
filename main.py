import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


def hierarchy_pos(G, root, levels=None, width=1., height=1.):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node
       levels: a dictionary
               key: level number (starting from 0)
               value: number of nodes in this level
       width: horizontal space allocated for drawing
       height: vertical space allocated for drawing'''
    TOTAL = "total"
    CURRENT = "current"

    def make_levels(levels, node=root, currentLevel=0, parent=None):
        """Compute the number of nodes for each level
        """
        if not currentLevel in levels:
            levels[currentLevel] = {TOTAL: 0, CURRENT: 0}
        levels[currentLevel][TOTAL] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            if not neighbor == parent:
                levels = make_levels(levels, neighbor, currentLevel + 1, node)
        return levels

    def make_pos(pos, node=root, currentLevel=0, parent=None, vert_loc=0):
        dx = 1 / levels[currentLevel][TOTAL]
        left = dx / 2
        pos[node] = ((left + dx * levels[currentLevel][CURRENT]) * width, vert_loc)
        levels[currentLevel][CURRENT] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            if not neighbor == parent:
                pos = make_pos(pos, neighbor, currentLevel + 1, node, vert_loc - vert_gap)
        return pos

    if levels is None:
        levels = make_levels({})
    else:
        levels = {l: {TOTAL: levels[l], CURRENT: 0} for l in levels}
    vert_gap = height / (max([l for l in levels]) + 1)
    return make_pos({})


G = nx.Graph()
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
    ("27", {"data": 0}),
    ("28", {"data": 0}),
    ("29", {"data": 0}),
    ("30", {"data": 0}),
    ("31", {"data": 0}),
    ("32", {"data": 0}),
    ("33", {"data": 0}),
    ("34", {"data": 0}),
    ("35", {"data": 0}),
    ("36", {"data": 0}),
    ("37", {"data": 0}),
    ("38", {"data": 0}),
    ("39", {"data": 0}),
    ("40", {"data": 0}),
    ("41", {"data": 0}),
    ("42", {"data": 0}),
    ("43", {"data": 0}),
    ("44", {"data": 0}),
    ("45", {"data": 0}),
    ("46", {"data": 0}),
    ("47", {"data": 0}),
    ("48", {"data": 0}),
    ("49", {"data": 0}),
    ("50", {"data": 0}),
    ("51", {"data": 0}),
    ("52", {"data": 0}),
    ("53", {"data": 0}),
    ("54", {"data": 0}),
    ("55", {"data": 0}),
    ("56", {"data": 0}),
    ("57", {"data": 0}),
    ("58", {"data": 0}),
    ("59", {"data": 0}),
    ("60", {"data": 0}),
    ("61", {"data": 0}),
    ("62", {"data": 0}),
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

# G.add_edges_from([(1,2), (1,3), (1,4), (2,5), (2,6), (2,7), (3,8), (3,9), (4,10),
#                   (5,11), (5,12), (6,13)])
pos = graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True, arrows=True, node_size=100, font_size=8, font_color="white")
plt.show()
