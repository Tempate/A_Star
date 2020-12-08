import math


PIXELS_TO_SECONDS = 16.6


class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

        self.parent = None
        
        self.g = 0
        self.f = 0

    def __str__(self):
        if self.parent:
            return "Name: {0}, Parent: {1}".format(self.name, self.parent.name)
        else:
            return "Name: " + self.name

    def __eq__(self, node):
        return self.name == node.name

    def estimate_path_length(self, target):
        h = math.sqrt((self.x - target.x)**2 + (self.y - target.y)**2) / PIXELS_TO_SECONDS
        self.f = self.g + h
