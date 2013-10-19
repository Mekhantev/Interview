from unittest.case import TestCase
from oop.puzzle import *

__author__ = 'Dmitry Mekhantev'


class TestPuzzle(TestCase):
    def test_solve(self):
        p = Puzzle()
        self.assertEqual(False, p.solve())


class TestEdge(TestCase):
    def test_fits_with(self):
        e1 = InnerEdge()
        e2 = OuterEdge()
        self.assertEqual(True, e1.fits_with(e2))
        e1 = OuterEdge()
        self.assertEqual(False, e1.fits_with(e2))
        e1 = FlatEdge()
        self.assertEqual(False, e1.fits_with(e2))