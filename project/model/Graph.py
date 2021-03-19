from model.Node import Node, NodeType


class Graph:
    def __init__(self):
        self.start_node, self.end_node = self.init_nodes()

    def init_nodes(self):
        start_node = Node(1, NodeType.basic)

        fork_node = Node(2, NodeType.fork)
        start_node.add_edge(fork_node, 0.208)

        left_node = Node(3, NodeType.basic)
        fork_node.add_edge(left_node, 0.1)
        right_node = Node(4, NodeType.basic)
        fork_node.add_edge(right_node, 0.15)

        return start_node, left_node
