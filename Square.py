from enum import Enum
from typing import Tuple
from Piece import Piece
from constants import State


class Square:
    def __init__(
        self, coordinates: int, state: State = State.EMPTY, piece: Piece = None
    ):
        self.coordinates = coordinates
        self.state = state
        self.piece = piece

    def released(self):
        self.piece = None
        self.state = State.EMPTY

    def occupied(self, piece: Piece):
        self.piece = piece
        self.state = piece.color

    def get_coordinate(self):
        return self.coordinates

    def get_symbol(self):
        return "-" if self.piece is None else self.piece.get_symbol()
