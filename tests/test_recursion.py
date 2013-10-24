from unittest import TestCase
from recursion import *

__author__ = 'Dmitry Mekhantev'


class TestRecursion(TestCase):
    def test_count_ways(self):
        ways = count_ways(10)
        self.assertEqual(274, ways)

    def test_count_ways_dynamic(self):
        i = 10
        ways = count_ways_dynamic(i, [None for _ in range(i + 1)])
        self.assertEqual(274, ways)


class TestField(TestCase):
    def test_get_path(self):
        f = Field(nonfree_points=((2, 4),))
        path = []
        point = (4, 4)
        expected_path = [
            (4, 4),
            (3, 4),
            (3, 3),
            (2, 3),
            (1, 3),
            (0, 3),
            (0, 2),
            (0, 1),
            (0, 0)
        ]
        self.assertTrue(f.get_path(point, path, {}))
        self.assertEqual(path, expected_path)