import itertools
import random

from model.TrafficLight import TrafficLightStatus


class TrafficLightManager:
    def __init__(self, env, groups, time):
        self.env = env
        self.time = time
        self.groups = groups
        self.lights = {light : TrafficLightStatus.red for group in groups for light in group}
        self.process = env.process(self.simulate())

    def simulate(self):
        for group in itertools.cycle(self.groups):
            self.set_lights_status(group, TrafficLightStatus.green)
            yield self.env.timeout(random.randint(0.85*self.time, 1.15*self.time))
            self.set_lights_status(group, TrafficLightStatus.yellow)
            yield self.env.timeout(1)
            self.set_lights_status(group, TrafficLightStatus.red)

    def set_lights_status(self, lights, status):
        for light in lights:
            # print('Set light: %s to %s' % (light, status))
            self.lights[light] = status

    def get_light_status(self, node_id):
        return self.lights[node_id]
