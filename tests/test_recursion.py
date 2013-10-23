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
        f = Field()
        path = []
        point = (7, 8)
        expected_path = []
        for i in range(0, point[0] + 1):
            expected_path.append((point[0] - i, point[1]))
        for i in range(1, point[1] + 1):
            expected_path.append((0, point[1] - i))
        self.assertTrue(f.get_path(point, path))
        self.assertEqual(path, expected_path)