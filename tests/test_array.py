from unittest import TestCase
from structures.array import *


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

    def test_merge(self):
        la = [1, 4, 6, 10, 15, 20]
        lb = [-3, -1, 0, 2, 3, 7, 9, 11, 12, 22, 25]
        expected = sorted(la + lb)
        merge(la, lb)
        self.assertEqual(la, expected)

    def test_search(self):
        ints = [11, 16, 20, 23, 27, 30, 1, 5, 7]
        left = 0
        right = len(ints) - 1
        first_number = 27
        second_number = 16
        self.assertEqual(4, search(ints, left, right, first_number))
        self.assertEqual(1, search(ints, left, right, second_number))
        for _ in range(3):
            ints.append(ints.pop(0))
        self.assertEqual(1, search(ints, left, right, first_number))
        self.assertEqual(7, search(ints, left, right, second_number))

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

    def test_search_string(self):
        strings = ['abc', '', 'bcd', '', '', 'ghj', 'nfm', '', 'pos', 'sdq']
        s = 'pos'
        self.assertEqual(strings.index(s), search_string(strings, 0, len(strings) - 1, s))
        s = 'abc'
        self.assertEqual(strings.index(s), search_string(strings, 0, len(strings) - 1, s))
        s = 'cba'
        self.assertRaises(IndexError, search_string, strings, 0, len(strings) - 1, s)

    def test_sort_by_height_width(self):
        people = [(200, 120), (170, 62), (180, 75), (190, 112), (175, 55), (186, 80), (170, 60), (190, 110)]
        expected = [(170, 60), (170, 62), (175, 55), (180, 75), (186, 80), (190, 110), (190, 112), (200, 120)]
        self.assertEqual(expected, sort_by_height_width(people))