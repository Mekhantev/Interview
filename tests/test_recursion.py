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