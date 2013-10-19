from enum import Enum

__author__ = 'Dmitry Mekhantev'


class Status(Enum):
    white = 1
    grey = 2
    black = 3


class GraphNode:
    def __init__(self):
        self.links = []
        self.status = Status.white


def search(start: GraphNode, end: GraphNode) -> bool:
    queue = []
    node = start
    node.status = Status.grey
    queue.append(node)
    while len(queue) > 0:
        node = queue.pop(0)
        node.status = Status.black
        if node == end:
            return True
        white_nodes = (n for n in node.links if n.status == Status.white)
        for n in white_nodes:
            queue.append(n)
    return False
