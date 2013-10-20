from unittest.case import TestCase
from oop.puzzle import *

__author__ = 'Dmitry Mekhantev'


class TestPuzzle(TestCase):
    def test_solve(self):
        p = Puzzle()
        self.assertFalse(p.solve())


class TestEdge(TestCase):
    def test_fits_with(self):
        e1 = InnerEdge()
        e2 = OuterEdge()
        self.assertTrue(e1.fits_with(e2))
        e1 = OuterEdge()
        self.assertFalse(e1.fits_with(e2))
        e1 = FlatEdge()
        self.assertFalse(e1.fits_with(e2))