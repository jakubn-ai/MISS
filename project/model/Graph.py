from model.Node import Node, NodeType
from model.Edge import EdgeType


class Graph:
    def __init__(self):
        self.start_node, self.end_node = self.init_nodes()

    def init_nodes(self):
        start_node = Node(1, NodeType.basic)

        fork_node = Node(2, NodeType.fork)
        start_node.add_edge(EdgeType.basic, fork_node, 0.208)

        left_node = Node(3, NodeType.basic)
        fork_node.add_edge(EdgeType.basic, left_node, 0.1)
        right_node = Node(4, NodeType.basic)
        fork_node.add_edge(EdgeType.basic, right_node, 0.15)

        return start_node, left_node
