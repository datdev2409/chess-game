from enum import Enum
from collections import defaultdict
from copy import deepcopy
from Piece import Bishop, King, Knight, Pawn, Piece, Queen, Rock
from Square import Square
from constants import Color as C, PieceType as T, File as F, Rank as R


class Board:
    def __init__(self, num_files: int = 8, num_ranks: int = 8):
        self.n_files = num_files
        self.n_ranks = num_ranks
        self.n_squares = self.n_files * self.n_ranks

        self.squares = [Square(i) for i in range(self.n_squares)]

    def get_square(self, coordinate: (F, R)) -> Square:
        file = coordinate[0]
        rank = coordinate[1]
        return self.squares[int(file) * self.n_ranks + int(rank)]

    def draw(self):
        for rank in range(self.n_ranks - 1, -1, -1):
            row = f"{rank + 1} |"
            for file in range(self.n_files - 1, -1, -1):
                square = self.get_square((file, rank))
                row += f" {square.get_symbol()} "

            print(row)

        file_row = "   "
        for file in range(self.n_files):
            file_row += f" {F(file).name} "

        print("-" * len(row))
        print(file_row)
