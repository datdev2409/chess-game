from constants import Color, PieceType


class Piece:
    def __init__(self, type: PieceType, color: Color):
        self.type = type
        self.color = color

    def get_symbol(self):
        return self.type.name

    def move(self):
        pass


class Rock(Piece):
    def __init__(self, color):
        super().__init__(PieceType.R, color)


class King(Piece):
    def __init__(self, color):
        super().__init__(PieceType.K, color)


class Queen(Piece):
    def __init__(self, color):
        super().__init__(PieceType.Q, color)


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(PieceType.P, color)


class Knight(Piece):
    def __init__(self, color):
        super().__init__(PieceType.K, color)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(PieceType.B, color)
