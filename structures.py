from copy import deepcopy

__author__ = 'Dmitry Mekhantev'


class Node():
    next_node = None

    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data and self.next_node == other.next_node


def make_linked_list(l) -> Node:
    first_node = Node(l[0])
    previous_node = first_node
    for i in l[1:len(l)]:
        previous_node.next_node = Node(i)
        previous_node = previous_node.next_node
    return first_node


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


def get_from_end(first_node: Node, k: 'Index from the end of list') -> Node:
    n = first_node
    length = 0
    while n:
        length += 1
        n = n.next_node
    n = first_node
    for i in range(0, length - k - 1):
        n = n.next_node
    return n


def delete_node(node: Node) -> Node:
    node.data = node.next_node.data
    node.next_node = node.next_node.next_node
    return node


