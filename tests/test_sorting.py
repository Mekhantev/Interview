from unittest import TestCase
from sorting import *


class TestSorting(TestCase):
    def test_merge(self):
        la = [1, 4, 6, 10, 15, 20]
        lb = [-3, -1, 0, 2, 3, 7, 9, 11, 12, 22, 25]
        expected = sorted(la + lb)
        merge(la, lb)
        self.assertEqual(la, expected)

    def test_sort_strings_by_anagram(self):
        strings = [
            'abc',
            'abcd',
            'bcd',
            'bac',
            'badc',
            'abcdef',
            'adbc'
        ]
        expected = [
            'abc',
            'bac',
            'abcd',
            'badc',
            'adbc',
            'abcdef',
            'bcd'
        ]
        result = sort_strings_by_anagram(strings)
        self.assertEqual(expected, result)