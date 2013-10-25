from unittest import TestCase
from structures.array import *

__author__ = 'Dmitry Mekhantev'


class TestArray(TestCase):
    def test_binary_search(self):
        ints = [0, 3, 6, 7, 12, 22, 31, 49]
        result = binary_search(ints, 7, 0, len(ints))
        self.assertEqual(result, 3)

    def test_get_subsets(self):
        ints = [1, 2, 3]
        subsets = get_subsets(ints)
        expected_result = [
            [],
            [1], [2], [1, 2],
            [3], [1, 3], [2, 3],
            [1, 2, 3]
        ]
        self.assertEqual(expected_result, subsets)