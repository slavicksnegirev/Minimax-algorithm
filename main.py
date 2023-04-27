import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt
# G = nx.DiGraph()
#
# G.add_node("ROOT")
#
# for i in range(5):
#     G.add_node("Child_%i" % i)
#     G.add_node("Grandchild_%i" % i)
#     G.add_node("Greatgrandchild_%i" % i)
#
#     G.add_edge("ROOT", "Child_%i" % i)
#     G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
#     G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)
#
# # write dot file to use with graphviz
# # run "dot -Tpng test.dot >test.png"
# write_dot(G,'test.dot')
#
# # same layout using matplotlib with no labels
# # plt.title('draw_networkx')
# pos =graphviz_layout(G, prog='dot')
# nx.draw(G, pos, with_labels=False, arrows=True)
# plt.show()




# import networkx as nx
# import matplotlib.pyplot as plt
# from networkx.drawing.nx_agraph import graphviz_layout
#
#
# def main():
#     # Create a directed graph
#     G = nx.DiGraph()
#
#     # An example
#     l = [('a', 'b'),
#          ('b', 'c'),
#          ('c', 'd'),
#          ('d', 'e'),
#          ('e', 'f'),
#          ('w', 'x'),
#          ('w', 't'),
#          ('t', 'q'),
#          ('q', 'r'),
#          ('q', 'u')]
#
#     # Build up a graph
#     for t in l:
#         G.add_edge(t[0], t[1])
#
#     # Plot trees
#     pos = graphviz_layout(G, prog='dot')
#     nx.draw(G, pos, with_labels=True, arrows=False)
#
#     plt.savefig('draw_trees_with_pygraphviz.png', bbox_inches='tight')
#     plt.show()
#
#
# if __name__ == '__main__':
#     main()


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
            levels[currentLevel] = {TOTAL : 0, CURRENT : 0}
        levels[currentLevel][TOTAL] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            if not neighbor == parent:
                levels =  make_levels(levels, neighbor, currentLevel + 1, node)
        return levels

    def make_pos(pos, node=root, currentLevel=0, parent=None, vert_loc=0):
        dx = 1/levels[currentLevel][TOTAL]
        left = dx/2
        pos[node] = ((left + dx*levels[currentLevel][CURRENT])*width, vert_loc)
        levels[currentLevel][CURRENT] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            if not neighbor == parent:
                pos = make_pos(pos, neighbor, currentLevel + 1, node, vert_loc-vert_gap)
        return pos
    if levels is None:
        levels = make_levels({})
    else:
        levels = {l:{TOTAL: levels[l], CURRENT:0} for l in levels}
    vert_gap = height / (max([l for l in levels])+1)
    return make_pos({})

G=nx.Graph()
G.add_edges_from([(1,2), (1,3), (1,4), (2,5), (2,6), (2,7), (3,8), (3,9), (4,10),
                  (5,11), (5,12), (6,13)])
pos = hierarchy_pos(G,1)
nx.draw(G, pos=pos, with_labels=True)
plt.show()
