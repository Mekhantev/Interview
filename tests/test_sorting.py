from unittest import TestCase
from sorting import merge


class TestSorting(TestCase):
    def test_merge(self):
        la = [1, 4, 6, 10, 15, 20]
        lb = [-3, -1, 0, 2, 3, 7, 9, 11, 12, 22, 25]
        expected = sorted(la + lb)
        merge(la, lb)
        self.assertEqual(la, expected)