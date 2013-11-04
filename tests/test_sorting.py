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

    def test_search(self):
        ints = [11, 16, 20, 23, 27, 30, 1, 5, 7]
        left = 0
        right = len(ints) - 1
        first_number = 27
        second_number = 11
        self.assertEqual(4, search(ints, left, right, first_number))
        self.assertEqual(0, search(ints, left, right, second_number))
        for _ in range(3):
            ints.append(ints.pop(0))
        self.assertEqual(1, search(ints, left, right, first_number))
        self.assertEqual(6, search(ints, left, right, second_number))

    def test_search_string(self):
        strings = ['abc', '', 'bcd', '', '', 'ghj', 'nfm', '', 'pos', 'sdq']
        s = 'pos'
        self.assertEqual(strings.index(s), search_string(strings, 0, len(strings) - 1, s))
        s = 'abc'
        self.assertEqual(strings.index(s), search_string(strings, 0, len(strings) - 1, s))
        s = 'cba'
        self.assertRaises(IndexError, search_string, strings, 0, len(strings) - 1, s)