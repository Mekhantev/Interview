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
    if not root:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1


def check_height(root) -> int:
    if not root:
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


def create_lists_from_binary_tree(root: TreeNode) -> list:
    lists = []
    current = [root]
    while len(current) > 0:
        lists.append(current)
        parents = current
        current = []
        for parent in parents:
            if parent.left:
                current.append(parent.left)
            if parent.right:
                current.append(parent.right)
    return lists


def check_binary_search_tree(root: TreeNode) -> bool:
    _check_binary_search_tree.last_value = None
    return _check_binary_search_tree(root)


def _check_binary_search_tree(root: TreeNode) -> bool:
    if not root:
        return True
    if not _check_binary_search_tree(root.left):
        return False

    if (isinstance(_check_binary_search_tree.last_value, int) and
                root.value < _check_binary_search_tree.last_value):
        return False
    _check_binary_search_tree.last_value = root.value
    if not _check_binary_search_tree(root.right):
        return False
    return True


_check_binary_search_tree.last_value = None


def find_successor(node: TreeNode, root: TreeNode) -> TreeNode:
    if node.right:
        return find_left_most_child(node.right)
    else:
        return find_successor_from_root(node, root)


def find_left_most_child(node: TreeNode) -> TreeNode:
    while node.left:
        node = node.left
    return node


def find_successor_from_root(node: TreeNode, root: TreeNode) -> TreeNode:
    successor = None
    while root:
        if node.value < root.value:
            successor = root
            root = root.left
        elif node.value > root.value:
            root = root.right
        else:
            break
    return successor


def find_common_ancestor(root: TreeNode, node1: TreeNode, node2: TreeNode):
    if not root:
        return None
    if root == node1 or root == node2:
        return root
    else:
        left = find_common_ancestor(root.left, node1, node2)
        right = find_common_ancestor(root.right, node1, node2)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right


def contains_subtree(tree: TreeNode, subtree: TreeNode):
    if not tree:
        return False
    if contains_subtree(tree.left, subtree):
        return True
    if tree == subtree:
        return True
    if contains_subtree(tree.right, subtree):
        return True
    return False


def find_sum(tree: TreeNode, sum: int):
    _find_sum.result = []
    _find_sum(tree, tree.left, sum)
    _find_sum(tree, tree.right, sum)
    return _find_sum.result if _find_sum.result else None


def _find_sum(root: TreeNode, node: TreeNode, sum: int):
    if not node:
        return
    _find_sum(root, node.left, sum)
    if root.value + node.value == sum:
        _find_sum.result.append(node)
    _find_sum(root, node.right, sum)
    return


_find_sum.result = None


def find_path_by_sum(tree: TreeNode, sum: int):
    _find_path_by_sum.result = []
    _find_path_by_sum.values = []
    _find_path_by_sum(tree, sum)
    return _find_path_by_sum.result


def _find_path_by_sum(node: TreeNode, sum_value: int):
    if not node:
        return
    _find_path_by_sum.values.append(node.value)
    if sum(_find_path_by_sum.values) == sum_value:
        _find_path_by_sum.result.append(node)
    _find_path_by_sum(node.left, sum_value)
    _find_path_by_sum(node.right, sum_value)
    _find_path_by_sum.values.pop()
    return


_find_path_by_sum.result = None
_find_path_by_sum.values = None


class RankNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.left_size = 0

    def insert(self, number):
        if number < self.value:
            self.left_size += 1
            if not self.left:
                self.left = RankNode(number)
            else:
                self.left.insert(number)
        else:
            if not self.right:
                self.right = RankNode(number)
            else:
                self.right.insert(number)

    def get_rank(self, number):
        if number == self.value:
            return self.left_size
        elif number < self.value:
            return self.left.get_rank(number)
        else:
            right_rank = -1 if not self.right else self.right.get_rank(number)
            if right_rank == -1:
                return -1
            else:
                return self.left_size + 1 + right_rank


class RankTreeManager():
    def __init__(self, root: RankNode=None):
        self.root = root

    def track(self, number: int):
        if not self.root:
            self.root = RankNode(number)
        else:
            self.root.insert(number)

    def get_rank(self, number: int) -> int:
        return self.root.get_rank(number)