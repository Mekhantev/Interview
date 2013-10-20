from enum import Enum
from utils import Singleton

__author__ = 'Dmitry Mekhantev'


class Color(Enum):
    white = 1,
    black = 2


class Piece():
    def __init__(self, color):
        self.color = color

    def flip(self):
        self.color = Color.white if self.color == Color.black else Color.black


class Board():
    def __init__(self, rows, columns):
        self.white_number = 0
        self.black_number = 0
        self.rows = rows
        self.columns = columns
        self.pieces = [[None for _ in range(columns)] for _ in range(rows)]

    def place_piece(self, row, column, color):
        """Place piece on board"""

    def _flip_section(self, row, column, end_row, end_column):
        """Flip section using Piece flip """


class Player():
    def __init__(self, color):
        self.color = color
        self.score = 0

    def place_piece(self, row, column):
        Game().board.place_piece(row, column, self.color)


class Game(metaclass=Singleton):
    @property
    def is_over(self):
        pieces_number = self.board.white_number + self.board.black_number
        spots_number = len(self.board.pieces) * len(self.board.pieces[0])
        return pieces_number == spots_number

    def __init__(self):
        self.players = (Player(Color.white),
                        Player(Color.black))
        self.board = Board(10, 10)