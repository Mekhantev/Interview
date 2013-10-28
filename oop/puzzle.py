from abc import ABCMeta, abstractproperty
from collections.abc import Iterable


class Edge(metaclass=ABCMeta):
    @abstractproperty
    def suitable_edge(self):
        """ remove from coverage """

    def fits_with(self, edge) -> bool:
        if (isinstance(edge, self.suitable_edge) and
                self._image_fits(edge)):
            return True
        return False

    def _image_fits(self, edge):
        #compare images here
        return True


class InnerEdge(Edge):
    @property
    def suitable_edge(self):
        return OuterEdge


class OuterEdge(Edge):
    @property
    def suitable_edge(self):
        return InnerEdge


class FlatEdge(Edge):
    @property
    def suitable_edge(self):
        return FlatEdge


class Piece(metaclass=ABCMeta):
    def __init__(self, edges: Iterable):
        self.edges = []
        self.edges.extend(edges)


class CornerPiece(Piece):
    def __init__(self):
        super().__init__((
            FlatEdge(),
            InnerEdge(),
            OuterEdge(),
            FlatEdge()
        ))


class OuterEdgePiece(Piece):
    def __init__(self):
        super().__init__((
            FlatEdge(),
            OuterEdge(),
            InnerEdge(),
            OuterEdge()
        ))


class InnerEdgePiece(Piece):
    def __init__(self):
        super().__init__((
            FlatEdge(),
            InnerEdge(),
            OuterEdge(),
            InnerEdge(),
        ))


class RegularPiece(Piece):
    def __init__(self):
        super().__init__((
            InnerEdge(),
            OuterEdge(),
            InnerEdge(),
            OuterEdge()
        ))


class Puzzle():
    def __init__(self):
        self.pieces = []
        for _ in range(4):
            self.pieces.append(CornerPiece())
        for _ in range(6):
            self.pieces.append(OuterEdgePiece())
        for _ in range(6):
            self.pieces.append(InnerEdgePiece())
        for _ in range(8):
            self.pieces.append(RegularPiece())
        self.solution = []
        for _ in range(4):
            self.solution.append([None for _ in range(6)])

    def solve(self) -> bool:
        for index, line in enumerate(self.solution):
            self._solve_line(index, line)
        return False

    def _solve_line(self, line_i, line):
        #compare pieces here
        pass