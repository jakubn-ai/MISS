from model.Node import Node, NodeType


class Graph:
    def __init__(self, traffic_manager):
        self.trafficManager = traffic_manager
        ends = self.init_nodes()
        self.start_nodes = ends[1::2]
        self.end_nodes = ends[::2]
        # print('Start nodes: %s' % self.start_nodes)
        # print('End nodes: %s' % self.end_nodes)

    def init_nodes(self):
        ends = []
        forks_before_lights = []
        forward_right_lights = []
        left_backward_lights = []
        forks_after_lights = []

        for i in range(4):
            dest = Node(i * 2, NodeType.basic)
            ends.append(dest)
            src = Node(i * 2 + 1, NodeType.basic)
            ends.append(src)

        for i in range(4):
            src_fork_before_lights = Node(i + 8, NodeType.fork)
            ends[i*2+1].add_edge(src_fork_before_lights, 1000)
            forks_before_lights.append(src_fork_before_lights)

            forward_right_light = Node(i + 12, NodeType.traffic_light)
            src_fork_before_lights.add_edge(forward_right_light, 50)

            left_backward_light = Node(i + 16, NodeType.traffic_light)
            src_fork_before_lights.add_edge(left_backward_light, 50)

            left_backward_lights.append(left_backward_light)
            forward_right_lights.append(forward_right_light)

            forward_right_fork = Node(i + 20, NodeType.fork)
            forward_right_light.add_edge(forward_right_fork, 50)
            forward_right_fork.add_edge(ends[(i*2 + 4) % len(ends)], 1000)
            forward_right_fork.add_edge(ends[(i*2 + 2) % len(ends)], 1000)

            left_backward_fork = Node(i + 24, NodeType.fork)
            left_backward_light.add_edge(left_backward_fork, 50)
            left_backward_fork.add_edge(ends[(i*2+6) % len(ends)], 1000)
            left_backward_fork.add_edge(ends[(i*2) % len(ends)], 1000)

            forks_after_lights.append(left_backward_fork)
            forks_after_lights.append(forward_right_fork)






        # start_node = Node(1, NodeType.basic)
        #
        # fork_node = Node(2, NodeType.fork)
        # start_node.add_edge(fork_node, 50)
        #
        # left_node = Node(3, NodeType.basic)
        # fork_node.add_edge(left_node, 50)
        # right_node = Node(4, NodeType.basic)
        # fork_node.add_edge(right_node, 50)

        return ends
