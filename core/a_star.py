from api.node import Node
from .gui import Gui


class A_Star:
    def __init__(self, graph, origin, target):
        self.graph = graph
        self.gui = Gui(graph)

        self.origin = Node(origin, graph[origin]["x"], graph[origin]["y"])
        self.target = Node(target, graph[target]["x"], graph[target]["y"])

        self.stack = [self.origin]
        self.visited   = []

    def run(self):
        while self.stack:
            node = self.stack.pop(0)
            self.visited.append(node)

            # If the current node is the target node, stop looking
            if node == self.target:
                break

            # Draw the graph with the current path
            self.gui.draw_graph(path(node))

            for weight, name in self.graph[node.name]["edges"]:

                child = Node(name, self.graph[name]["x"], self.graph[name]["y"])
                new_weight = node.g + weight

                if child in self.visited:
                    continue

                if child not in self.stack:
                    self.update_node_in_stack(child, node, new_weight, is_new=True)
                else:
                    # Update the weight if it's better than the current one
                    child = find_node(self.stack, child.name)

                    if child.g > new_weight: # Being the same node, h is the same too
                        self.update_node_in_stack(child, node, new_weight)
          
        self.show(find_node(self.visited, self.target.name))
        

    def update_node_in_stack(self, node, parent, weight, is_new=False):
        node.g = weight
        node.estimate_path_length(self.target)

        node.parent = parent

        if is_new:
            self.stack.append(node)
                      
        self.stack.sort(key = lambda node: node.f)

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
