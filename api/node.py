import math


class Node:
    def __init__(self, name, x, y, parent=None):
        self.name = name
        self.x = x
        self.y = y

        self.parent = parent
        
        self.g = 0
        self.f = 0

    def __str__(self):
        if self.parent:
            return "Name: {0}, Parent: {1}, f: {2}".format(self.name, self.parent.name, self.f)
        else:
            return "Name: " + str(self.name)

    def __eq__(self, node):
        return self.name == node.name

    def set_f(self, target):
        h = math.sqrt((self.x - target.x)**2 + (self.y - target.y)**2)
        self.f = self.g + h
