import random

from model.Node import NodeType

SPEED = 50


class Vehicle:
    def __init__(self, env, vehicle_id, position, destination, graph, start_delay=0):
        self.env = env
        self.id = vehicle_id
        self.speed = SPEED
        self.position = position
        self.destination = destination
        self.graph = graph
        self.startDelay = start_delay

        self.totalDistance = 0
        self.process = env.process(self.simulate())

    def simulate(self):
        yield self.env.timeout(self.startDelay)
        print('VehicleId: %d Started driving' % self.id)

        while True:
            print('VehicleId: %d Current node: %s - %s' % (self.id, self.position, self.position.type.name))
            if self.position == self.destination:
                print('VehicleId: %d Reached my destination. Total distance: %.2f km' % (self.id, self.totalDistance))
                break

            if len(self.position.outEdges) == 0:
                print('VehicleId: %d End of the road. Total distance: %.2f km' % (self.id, self.totalDistance))
                break

            outEdges = self.position.outEdges
            if self.position.type == NodeType.basic:
                edge = outEdges[0]
            elif self.position.type == NodeType.fork:
                edge = outEdges[random.randint(0, len(outEdges) - 1)]

            print('VehicleId: %d Started driving through edge %s' % (self.id, edge))
            yield self.env.timeout(self.next_event_time(edge))
            self.totalDistance += edge.distance
            self.position = edge.destNode

    def next_event_time(self, edge):
        return float(edge.distance) / self.speed * 3600
