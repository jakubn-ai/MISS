import random

from model.Node import NodeType
from model.TrafficLight import TrafficLightStatus

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
        self.data = {
            'travelTime': 0.0,
            'waitOnRedLightTime': 0.0,
            'distanceTraveled': 0.0,
            'waitTime': 0.0,
            'driveTime': 0.0
        }
        self.startTime = 0

    def simulate(self):
        yield self.env.timeout(self.startDelay)
        self.startTime = self.env.now
        # print('VehicleId: %d Started driving' % self.id)

        while True:
            # print('VehicleId: %d Current node: %s - %s' % (self.id, self.position, self.position.type.name))
            if self.position == self.destination:
                self.data['travelTime'] = self.env.now - self.startTime
                # print('VehicleId: %d Reached my destination. Total distance: %.2f m' % (self.id, self.data['distanceTraveled']))
                break

            if len(self.position.outEdges) == 0:
                self.data['travelTime'] = self.env.now - self.startTime
                # print('VehicleId: %d End of the road. Total distance: %.2f m' % (self.id, self.data['distanceTraveled']))
                break

            outEdges = self.position.outEdges
            if self.position.type == NodeType.basic:
                edge = outEdges[0]
            elif self.position.type == NodeType.fork:
                edge = outEdges[random.randint(0, len(outEdges) - 1)]
            elif self.position.type == NodeType.traffic_light:
                while self.graph.trafficManager.get_light_status(self.position.id) == TrafficLightStatus.red:
                    self.data['waitOnRedLightTime'] += 0.1
                    self.data['waitTime'] += 0.1
                    yield self.env.timeout(0.1)
                edge = outEdges[random.randint(0, len(outEdges) - 1)]

            yield from self.drive_road(edge)
            self.position = edge.destNode

    def drive_road(self, road):
        # print('VehicleId: %d Trying to join road %s' % (self.id, road))
        while not road.join_user(self):
            self.data['waitTime'] += 0.1
            yield self.env.timeout(0.1)
        # print('VehicleId: %d Started driving through edge %s' % (self.id, road))
        # print('Curr time: %f' % self.env.now)

        distanceToTravel = road.distance
        distanceTraveled = 0

        while distanceTraveled < distanceToTravel:
            dx = min(DX, distanceToTravel - distanceTraveled)
            if road.can_user_move(self, dx):
                self.data['driveTime'] += 1.5
                yield self.env.timeout(1.5)
                self.data['driveTime'] += self.next_event_time(dx)
                yield self.env.timeout(self.next_event_time(dx))
                distanceTraveled += dx
                road.move_user(self, dx)
                self.data['distanceTraveled'] += dx
            else:
                self.data['waitTime'] += 0.1
                yield self.env.timeout(0.1)

        road.leave_user(self)

    def next_event_time(self, distance):
        return float(distance) / self.speed
