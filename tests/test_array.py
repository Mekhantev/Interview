from unittest import TestCase
from structures.array import *

__author__ = 'Dmitry Mekhantev'


class TestArray(TestCase):
    def test_binary_search(self):
        ints = [0, 3, 6, 7, 12, 22, 31, 49]
        result = binary_search(ints, 7, 0, len(ints))
        self.assertEqual(result, 3)