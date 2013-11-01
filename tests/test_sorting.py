from unittest import TestCase
from sorting import merge


class TestSorting(TestCase):
    def test_merge(self):
        la = [1, 4, 6, 10, 15, 20]
        lb = [-3, -1, 0, 2, 3, 7, 9, 11, 12, 22, 25]
        merge(la, lb)
        expected = [-3, -1, 0, 1, 2, 3, 4, 6, 7, 9, 10, 11, 12, 15, 20, 22, 25]
        self.assertEqual(la, expected)