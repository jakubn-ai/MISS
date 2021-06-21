from enum import Enum

from model.Edge import Road


class NodeType(Enum):
    basic = 1
    fork = 2
    traffic_light = 3


class Node:
    def __init__(self, node_id, node_type):
        self.id = node_id
        self.type = node_type
        self.outEdges = []

    def add_edge(self, dest_node, distance):
        self.outEdges.append(Road(self, dest_node, distance))

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.__str__()

