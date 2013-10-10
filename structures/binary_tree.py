__author__ = 'Dmitry Mekhantev'


class TreeNode():
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def __eq__(self, other):
        return (self.value == other.value
                and self.right == other.right
                and self.left == other.left)


def get_height(root) -> int:
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1


def check_height(root) -> int:
    if root is None:
        return 0
    left_height = check_height(root.left)
    if left_height == -1:
        return -1
    right_height = check_height(root.right)
    if right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


def create_binary_search_tree(ints) -> TreeNode:
    def f(ints, start, end) -> TreeNode:
        if end < start:
            return None
        middle_index = (start + end) // 2
        node = TreeNode()
        node.value = ints[middle_index]
        node.left = f(ints, start, middle_index - 1)
        node.right = f(ints, middle_index + 1, end)
        return node

    return f(ints, 0, len(ints) - 1)

