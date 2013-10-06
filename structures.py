from copy import deepcopy

__author__ = 'Dmitry Mekhantev'


class Node():
    def __init__(self, data):
        self.next = None
        self.data = data

    def __eq__(self, other):
        return self.data == other.data and self.next == other.next


def make_linked_list(l) -> Node:
    first_node = Node(l[0])
    previous_node = first_node
    for i in l[1:len(l)]:
        previous_node.next = Node(i)
        previous_node = previous_node.next
    return first_node


def delete_dups(first_node: Node) -> Node:
    first_node = deepcopy(first_node)
    n = first_node
    previous_node = first_node
    data_dictionary = {}
    while n:
        if n.data in data_dictionary:
            previous_node.next = n.next
        else:
            data_dictionary[n.data] = True
        previous_node = n
        n = n.next
    return first_node


def get_from_end(first_node: Node, k: 'Index from the end of list') -> Node:
    n = first_node
    length = 0
    while n:
        length += 1
        n = n.next
    n = first_node
    for i in range(0, length - k - 1):
        n = n.next
    return n


def delete_node(node: Node) -> Node:
    node.data = node.next.data
    node.next = node.next.next
    return node


def partition(first_node: Node, i: 'Node data value') -> Node:
    first_node = deepcopy(first_node)
    n = first_node
    center_node = None
    first_left_node = None
    last_left_node = None
    first_right_node = None
    last_right_node = None
    while n:
        if n.data < i:
            if first_left_node is None:
                first_left_node = n
            if last_left_node:
                last_left_node.next = n
            last_left_node = n
        elif center_node is None and n.data == i:
            center_node = n
        else:
            if first_right_node is None:
                first_right_node = n
            if last_right_node:
                last_right_node.next = n
            last_right_node = n
        n = n.next
    last_left_node.next = center_node
    center_node.next = first_right_node
    return first_left_node


def custom_sum(first_node1: Node, first_node2: Node) -> Node:
    first_result_node = None
    last_result_node = None
    n1 = first_node1.next
    n2 = first_node2.next
    carry = 0
    while n1 or n2:
        r = (n1.data if n1 else 0) + (n2.data if n2 else 0) + carry
        node = Node(r % 10)
        if first_result_node is None:
            first_result_node = node
        if last_result_node:
            last_result_node.next = node
        last_result_node = node
        carry = r // 10
        n1 = n1.next if n1 else None
        n2 = n2.next if n2 else None
    r = first_node1.data + first_node2.data + carry
    node = Node(r if r < 10 else r // 10)
    node.next = first_result_node
    first_result_node = node
    if r > 9:
        node = Node(r % 10)
        last_result_node.next = node
    return first_result_node


def get_loop_beginning(first_node: Node) -> Node:
    slow = first_node
    fast = first_node
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow.data == fast.data:
            break
    slow = first_node
    while slow.data != fast.data:
        slow = slow.next
        fast = fast.next
    return fast


def is_palindrome(first: Node) -> bool:
    slow = first
    fast = first
    stack = []
    while fast:
        if fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                return False
        else:
            break
        stack.append(slow)
        slow = slow.next
    slow = slow.next
    while slow:
        if slow.data != stack.pop().data:
            return False
        slow = slow.next
    return True









