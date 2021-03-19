import random

from model.Node import NodeType

SPEED = 13  # m/s
DX = 1  # smallest distance a vehicle try to travel in meters


class Vehicle:
    def __init__(self, env, vehicle_id, position, destination, graph, speed=SPEED, start_delay=0):
        self.env = env
        self.id = vehicle_id
        self.speed = SPEED
        self.position = position
        self.destination = destination
        self.graph = graph
        self.startDelay = start_delay
        self.speed = speed  # vehicle speed in m/s
        self.length = 5  # vehicle length in meters

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

            yield from self.drive_road(edge)
            self.position = edge.destNode

    def drive_road(self, road):
        print('VehicleId: %d Trying to join road %s' % (self.id, road))
        while not road.join_user(self):
            yield self.env.timeout(0.1)
        print('VehicleId: %d Started driving through edge %s' % (self.id, road))

        distanceToTravel = road.distance
        distanceTraveled = 0

        while distanceTraveled < distanceToTravel:
            dx = min(DX, distanceToTravel - distanceTraveled)
            if road.can_user_move(self, dx):
                yield self.env.timeout(self.next_event_time(dx))
                distanceTraveled += dx
                road.move_user(self, dx)
                self.totalDistance += dx
            else:
                yield self.env.timeout(0.1)

        road.leave_user(self)

    def next_event_time(self, distance):
        return float(distance) / self.speed
