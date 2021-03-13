from enum import Enum

from model.Edge import Edge


class NodeType(Enum):
    basic = 1
    fork = 2


class Node:
    def __init__(self, node_id, node_type):
        self.id = node_id
        self.type = node_type
        self.outEdges = []

    def add_edge(self, edge_type, dest_node, distance):
        self.outEdges.append(Edge(edge_type, self, dest_node, distance))

    def __str__(self):
        return str(self.id)
