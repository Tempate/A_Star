from api.node import Node
from .gui import Gui


TRANSSHIPMENT_PENALTY = 6


class A_Star:
    def __init__(self, graph, origin, target):
        self.graph = graph
        self.gui = Gui(graph)

        self.origin = Node(origin, graph[origin]["x"], graph[origin]["y"])
        self.target = Node(target, graph[target]["x"], graph[target]["y"])

        self.queue = [self.origin]
        self.visited = []


    def run(self):
        while self.queue:
            node = self.queue.pop(0)

            self.visited.append(node)

            # If the current node is the target node, stop looking
            if node == self.target:
                break

            self.gui.draw_graph(path(node))

            for weight, name in self.graph[node.name]["edges"]:

                child = Node(name, self.graph[name]["x"], self.graph[name]["y"])
                new_weight = self.calc_new_weight(node, child, weight)

                if child in self.visited:
                    child = find_node(self.visited, child.name)

                    if child.g > new_weight:
                        self.visited.remove(child)
                        self.update_node_in_queue(child, node, new_weight, is_new=True)
                elif child in self.queue:
                    # Update the weight if it's better than the current one
                    child = find_node(self.queue, child.name)

                    if child.g > new_weight: # Being the same node, h is the same too
                        self.update_node_in_queue(child, node, new_weight)
                else:
                    self.update_node_in_queue(child, node, new_weight, is_new=True)

          
        self.show(find_node(self.visited, self.target.name))
        

    def update_node_in_queue(self, node, parent, weight, is_new=False):
        node.g = weight
        node.estimate_path_length(self.target)

        node.parent = parent

        if is_new:
            self.queue.append(node)
                      
        self.queue.sort(key = lambda node: node.f)


    def parent_in_queue(self, parent):
        for node in self.queue:
            if node.parent == parent:
                return True

        return False


    def calc_new_weight(self, node, child, weight):
        new_weight = node.g + weight

        if self.graph[node.name]["color"] != self.graph[child.name]["color"]:
            new_weight += TRANSSHIPMENT_PENALTY

        return new_weight


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
    for node in nodes:
        if node.name == name:
            return node

    raise ValueError("The node isn't in the list!")
