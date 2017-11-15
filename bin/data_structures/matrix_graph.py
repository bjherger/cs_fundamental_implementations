import numpy


class MatrixGraph(object):

    def __init__(self, max_nodes):
        self.adjacency_matrix = numpy.zeros(shape=(max_nodes, max_nodes))
        self.node_to_index_lookup = dict()
        self.index_to_node_lookup = dict()
        self.num_nodes = 0

    def add_node(self, data):
        self.node_to_index_lookup[data] = self.num_nodes
        self.index_to_node_lookup[self.num_nodes] = data
        self.num_nodes += 1

    def to_node_list(self):
        return self.node_to_index_lookup.keys()

    def to_adjacency_list(self):

        agg = list()
        for parent_index in range(0,self.num_nodes, 1):
            for child_index in range(0, self.num_nodes, 1):
                if self.adjacency_matrix[parent_index][child_index] !=0:
                    # Parent data, child data, weight
                    agg.append(
                        (self.index_to_node_lookup[parent_index], self.index_to_node_lookup[child_index],
                         self.adjacency_matrix[parent_index][child_index])
                    )
        return agg

    def add_edge(self, parent, child, weight=1):
        parent_index = self.node_to_index_lookup[parent]
        child_index = self.node_to_index_lookup[child]
        self.adjacency_matrix[parent_index][child_index] = weight
