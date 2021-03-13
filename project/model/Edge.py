from enum import Enum


class EdgeType(Enum):
    basic = 1
    traffic_light = 2


class Edge:
    def __init__(self, edge_type, source_node, dest_node, distance):
        self.type = edge_type
        self.sourceNode = source_node
        self.destNode = dest_node
        self.distance = distance

    def __str__(self):
        return '%s --> %s' % (self.sourceNode, self.destNode)
