from copy import deepcopy
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

    def test_find_magic_index(self):
        ints = (-10, -5, -1, 2, 4, 6, 8, 10)
        i = find_magic_index(ints, 0, len(ints) - 1)
        self.assertEqual(i, 4)

    def test_generate_brackets(self):
        expected = [
            '()',
            '(())',
            '()()',
            '((()))',
            '(()())',
            '(())()',
            '()(())',
            '()()()']
        l = [s for s in generate_brackets(3)]
        self.assertEqual(expected, l)

    def test_flood_fill(self):
        l = 4
        old_color = Color.red
        new_color = Color.blue
        screen = [[Color.red for _ in range(l)] for _ in range(l)]
        screen[0][1] = Color.black
        screen[1][0] = Color.black
        screen[2][3] = Color.black
        screen[3][1] = Color.black
        screen[3][0] = Color.blue
        screen[3][2] = Color.blue
        expected = deepcopy(screen)
        for line in range(0, len(expected)):
            for column in range(0, len(expected[line])):
                if expected[column][line] == old_color:
                    expected[column][line] = new_color
        expected[0][0] = old_color
        expected[3][3] = old_color
        flood_fill(screen, 2, 1, old_color, new_color)
        self.assertEqual(screen, expected)


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