__author__ = 'Dmitry Mekhantev'


class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None


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




