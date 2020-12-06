from api.node import Node


class A_Star:
    def __init__(self, graph, origin, target):
        self.graph = graph

        self.origin = Node(origin, self.graph[origin]["x"], self.graph[origin]["y"])
        self.target = Node(target, self.graph[target]["x"], self.graph[target]["y"])

        self.stack = [self.origin]
        self.visited = []

    def run(self):
        while self.stack:
            node = self.stack.pop(0)

            for edge in self.graph[node.name]["edges"]:
                name = edge[1]
                entry = self.graph[name]

                child = Node(name, entry["x"], entry["y"], node)

                new_g = node.g + edge[0]

                if child not in self.visited:
                    if child not in self.stack:
                        child.g = new_g
                        child.set_f(self.target)

                        self.stack.append(child)
                        self.stack.sort(key = lambda node: node.f)
                    else:
                        child = find_node_by_name(self.stack, child.name)

                        if child.g > new_g:
                            child.g = new_g
                            child.set_f(self.target)

                            child.parent = node                    
                            self.stack.sort(key = lambda node: node.f)

            self.visited.append(node)

        self.target = find_node_by_name(self.visited, self.target.name)
        
        print("Minimum weight: " + str(self.target.g))
        print("Minimum path: " + ", ".join(n.name for n in self.path(self.target)))

    def path(self, node):
        nodes = [node]

        while node.parent:
            node = node.parent
            nodes.append(node)

        nodes.reverse()

        return nodes


def find_node_by_name(nodes, name):
    for node in nodes:
        if node.name == name:
            return node

    raise ValueError("The node wasn't in the list!")
