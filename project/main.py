from model.Graph import Graph
from model.Vehicle import Vehicle
import simpy

if __name__ == '__main__':
    env = simpy.Environment()
    graph = Graph()

    vehicle = Vehicle(env, 1, graph.start_node, graph.end_node, graph)
    vehicle2 = Vehicle(env, 2, graph.start_node, graph.end_node, graph)

    env.run(until=60)
