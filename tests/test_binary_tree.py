from random import random
from unittest import TestCase
from structures.binary_tree import *


class TestBinaryTree(TestCase):
    def test_get_height(self):
        root = TreeNode()
        root.left = TreeNode()
        root.left.right = TreeNode()
        root.left.right.left = TreeNode()
        root.right = TreeNode()
        self.assertEqual(4, get_height(root))

    def test_check_height(self):
        root = TreeNode()
        root.left = TreeNode()
        root.left.left = TreeNode()
        root.left.left.left = TreeNode()
        root.right = TreeNode()
        self.assertEqual(-1, check_height(root))
        root = TreeNode()
        root.right = TreeNode()
        root.right.right = TreeNode()
        root.right.right.right = TreeNode()
        root.left = TreeNode()
        self.assertEqual(-1, check_height(root))

    def test_create_binary_search_tree(self):
        ints = [i for i in range(5)]
        tree = create_binary_search_tree(ints)
        expected_tree = TreeNode(2)
        expected_tree.left = TreeNode(0)
        expected_tree.left.right = TreeNode(1)
        expected_tree.right = TreeNode(3)
        expected_tree.right.right = TreeNode(4)
        self.assertEqual(tree, expected_tree)

    def test_create_lists_from_binary_tree(self):
        ints = [i for i in range(5)]
        tree = create_binary_search_tree(ints)
        expected_tree = TreeNode(2)
        expected_tree.left = TreeNode(0)
        expected_tree.left.right = TreeNode(1)
        expected_tree.right = TreeNode(3)
        expected_tree.right.right = TreeNode(4)
        l = [
            [expected_tree],
            [expected_tree.left, expected_tree.right],
            [expected_tree.left.right, expected_tree.right.right]
        ]
        result = create_lists_from_binary_tree(tree)
        self.assertEqual(l, result)

    def test_check_binary_search_tree(self):
        ints = [i for i in range(5)]
        tree = create_binary_search_tree(ints)
        self.assertTrue(check_binary_search_tree(tree))
        tree.left.right.value = -1
        self.assertFalse(check_binary_search_tree(tree))

    def test_find_successor(self):
        ints = [i for i in range(20)]
        root = create_binary_search_tree(ints)
        successor = find_successor(root.right, root)
        self.assertEqual(successor, root.right.right.left)
        successor = find_successor(root.left.right.left, root)
        self.assertEqual(successor, root.left.right)

    def test_find_common_ancestor(self):
        ints = [i for i in range(20)]
        root = create_binary_search_tree(ints)
        result = find_common_ancestor(root, root.right.left.left,
                                      root.right.right.left.right)
        self.assertEqual(result, root.right)

    def test_contains_subtree(self):
        ints = [i for i in range(20)]
        tree = create_binary_search_tree(ints)
        b = contains_subtree(tree, tree.left.right.left)
        self.assertTrue(b)

    def test_find_sum(self):
        ints = [i for i in range(20)]
        tree = create_binary_search_tree(ints)
        tree.right.left.right.right.value = 1
        tree.left.right.right.right.value = 1
        result = find_sum(tree, 10)
        expected_result = [
            tree.left.left,
            tree.right.left.right.right,
            tree.left.right.right.right
        ]
        self.assertEqual(expected_result, result)

    def test_find_path_by_sum(self):
        ints = [i for i in range(20)]
        root = create_binary_search_tree(ints)
        result = find_path_by_sum(root, 34)
        expected_result = [
            root.left.right.right.right,
            root.right.left
        ]
        self.assertEqual(expected_result, result)


class TestRankTreeManager(TestCase):
    def test_track(self):
        manager = RankTreeManager()
        ints = [10, 12, 5, 15, 7, 2, 1, 4, 3]
        for i in ints:
            manager.track(i)
        self.assertEqual(1, manager.get_rank(4))

    def test_get_rank(self):
        manager = RankTreeManager()
        ints = [10, 12, 5, 15, 7, 2, 1, 4, 3]
        for i in ints:
            manager.track(i)
        self.assertEqual(1, manager.get_rank(4))