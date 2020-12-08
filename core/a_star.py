from api.node import Node
from .gui import Gui


TRANSSHIPMENT_PENALTY = 6


class A_Star:
    def __init__(self, graph, origin, target):
        self.graph = graph
        self.gui = Gui(graph)

        # We find one of the names of the station to get the coordinates
        target_name = self.get_names_for_station(target)[0]
        self.target = Node(target, graph[target_name]["x"], graph[target_name]["y"])

        self.queue = []
        self.visited = []

        # Start the queue with the origin station
        # As it may have different names, if it's an intersection,
        # it can get added multiple times, with initial cost 0
        for name in self.get_names_for_station(origin):
            self.queue.append(Node(name, graph[name]["x"], graph[name]["y"]))


    def get_names_for_station(self, station):
        return [name for name in self.graph.keys() if station == name.split('(')[0]]


    def run(self):
        node = None

        while self.queue:
            node = min(self.queue, key = lambda node: node.f)
            
            self.queue.remove(node)
            self.visited.append(node)

            # If the current node is the target node, stop looking
            if node.name.split('(')[0] == self.target.name:
                break

            self.gui.draw_graph(path(node))

            for weight, name in self.graph[node.name]["edges"]:

                child = Node(name, self.graph[name]["x"], self.graph[name]["y"])
                cost = self.calculate_cost(node, child, weight)

                if child in self.visited:
                    # Update the weight of a visited node
                    # The children will get updated when the new node pops out of the queue
                    child = find_node(self.visited, child.name)

                    if child.g > cost:
                        self.update_node_in_queue(child, node, cost, is_new=True)
                        self.visited.remove(child)
                elif child in self.queue:
                    # Update the weight of a queued node
                    child = find_node(self.queue, child.name)

                    if child.g > cost: # Being the same node, h is preserved
                        self.update_node_in_queue(child, node, cost)
                else:
                    # Add the new node to the queue
                    self.update_node_in_queue(child, node, cost, is_new=True)

          
        if node.x != self.target.x or node.y != self.target.y:
            raise ValueError("The target is inaccessible")

        self.show(node)
        

    def calculate_cost(self, node, child, weight):
        cost = node.g + weight

        if self.graph[node.name]["color"] != self.graph[child.name]["color"]:
            cost += TRANSSHIPMENT_PENALTY

        return cost


    def update_node_in_queue(self, node, parent, cost, is_new=False):
        node.g = cost
        node.estimate_path_length(self.target)

        node.parent = parent

        if is_new:
            self.queue.append(node)


    def show(self, node):
        node_path = path(node)
        
        print("Minimum weight: " + str(node.g))
        print("Minimum path: " + ", ".join(n.name for n in node_path))

        self.gui.draw_graph(node_path, permanent=True)


def path(node):
    """ Go up the tree to get the best path of a node """
    nodes = [node]

    while node.parent:
        node = node.parent
        nodes.append(node)

    nodes.reverse()

    return nodes


def find_node(nodes, name):
    """ Find a node in a list of nodes """
    for node in nodes:
        if node.name == name:
            return node

    raise ValueError("The node isn't in the list!")
