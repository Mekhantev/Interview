from unittest import TestCase
from oop.reversi import *

__author__ = 'Dmitry Mekhantev'


class TestPiece(TestCase):
    def test_flip(self):
        piece = Piece(Color.white)
        piece.flip()
        self.assertEqual(Color.black, piece.color)


class TestBoard(TestCase):
    def test_place_piece(self):
        board = Board(10, 10)
        board.place_piece(5, 6, Color.black)


class TestPlayer(TestCase):
    def test_place_piece(self):
        player = Player(Color.white)
        player.place_piece(2, 2)


class TestGame(TestCase):
    def test_is_over(self):
        game = Game()
        self.assertFalse(game.is_over)