from copy import deepcopy

__author__ = 'Dmitry Mekhantev'


class Node():
    next_node = None

    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data and self.next_node == other.next_node


def delete_dups(first_node: Node) -> Node:
    first_node = deepcopy(first_node)
    n = first_node
    previous_node = first_node
    data_dictionary = {}
    while n:
        if n.data in data_dictionary:
            previous_node.next_node = n.next_node
        else:
            data_dictionary[n.data] = True
        previous_node = n
        n = n.next_node
    return first_node