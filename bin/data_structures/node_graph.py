class NodeGraph(object):
    def __init__(self):
        self.nodes = list()

    def to_adjacency_list(self):
        agg = list()

        for node in self.nodes:
            for child in node.children:
                agg.append((node.data, child.data))
        return agg

    def to_node_list(self):
        return map(lambda x: x.data, self.nodes)


    def add_node(self, data):
        new_node = GraphNode(data)
        if new_node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(new_node)

    def add_edge(self, parent_data, child_data):
        parent = self.get_node(parent_data)
        parent.children.append(self.get_node(child_data))

    def get_node(self, data):
        # Can return first element, because we are guaranteed that there are no duplicates
        results = filter(lambda x: x.data == data, self.nodes)

        if len(results) < 1:
            raise ValueError('Node not found')
        else:
            return results[0]


class GraphNode(object):
    def __init__(self, data):
        self.data = data
        self.children = list()

    def __eq__(self, other):
        return self.data == other.data

