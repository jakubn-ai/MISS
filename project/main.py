import simpy
import time

from model.Graph import Graph
from model.Vehicle import Vehicle

if __name__ == '__main__':
    env = simpy.rt.RealtimeEnvironment()
    graph = Graph()

    vehicle = Vehicle(env, 1, graph.start_node, graph.end_node, graph, 10)
    vehicle2 = Vehicle(env, 2, graph.start_node, graph.end_node, graph, 20)

    env.run(until=10)