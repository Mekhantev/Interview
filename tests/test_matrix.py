from unittest import TestCase
from structures.matrix import *


class TestMatrix(TestCase):
    def test_rotate(self):
        m = [[10, 11, 12, 13],
             [14, 15, 16, 17],
             [18, 19, 20, 21],
             [22, 23, 24, 25]]

        expected_matrix = [[22, 18, 14, 10],
                           [23, 19, 15, 11],
                           [24, 20, 16, 12],
                           [25, 21, 17, 13]]
        self.assertEqual(rotate(m), expected_matrix)

    def test_set_zeros(self):
        m = [[10, 11, 12, 13],
             [14, 15, 16, 17],
             [18, 19, 0, 21],
             [22, 23, 24, 25]]
        expected_matrix = [[10, 11, 0, 13],
                           [14, 15, 0, 17],
                           [0, 0, 0, 0],
                           [22, 23, 0, 25]]
        self.assertEqual(set_zeros(m), expected_matrix)

    def test_find_element(self):
        m = [[10, 20, 40, 60],
             [22, 30, 50, 66],
             [32, 40, 55, 70],
             [49, 56, 68, 78]]

        self.assertTrue(find_element(m, 55))
        self.assertFalse(find_element(m, 31))