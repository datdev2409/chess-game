from copy import deepcopy
from collections import defaultdict
from Board import Board
from History import History
from Piece import Piece
from Square import Square
from Piece import Bishop, King, Knight, Pawn, Piece, Queen, Rock
from constants import Color as C, PieceType as T, File as F, Rank as R


class Game:
    def __init__(self, board: Board, history: History):
        self.turn = C.WHITE  # white goes first
        self.board = board
        self.history = history

        self.white_pieces = defaultdict(list)
        self.black_pieces = defaultdict(list)

        self.initialize()

    def initialize(self):
        # Initialize the pawns
        self.place_pieces(Pawn(C.WHITE), R.r2)
        self.place_pieces(Pawn(C.BLACK), R.r7)

        # Initialize the others
        initial_positions = [
            (Knight(C.WHITE), (F.b, R.r1)),
            (Knight(C.WHITE), (F.g, R.r1)),
            (Knight(C.BLACK), (F.b, R.r8)),
            (Knight(C.BLACK), (F.g, R.r8)),
            (Bishop(C.WHITE), (F.c, R.r1)),
            (Bishop(C.WHITE), (F.f, R.r1)),
            (Bishop(C.BLACK), (F.c, R.r8)),
            (Bishop(C.BLACK), (F.f, R.r8)),
            (Rock(C.WHITE), (F.a, R.r1)),
            (Rock(C.WHITE), (F.h, R.r1)),
            (Rock(C.BLACK), (F.a, R.r8)),
            (Rock(C.BLACK), (F.h, R.r8)),
            (King(C.WHITE), (F.e, R.r1)),
            (King(C.BLACK), (F.e, R.r8)),
            (Queen(C.WHITE), (F.d, R.r1)),
            (Queen(C.BLACK), (F.d, R.r8)),
        ]

        for piece, coordinate in initial_positions:
            self.place_piece(piece, coordinate)

    def place_piece(self, piece: Piece, coordinate: (F, R)):
        square = self.board.get_square(coordinate)
        square.occupied(piece)

        if piece.color == C.WHITE:
            self.white_pieces[piece.type].append(piece)
        else:
            self.black_pieces[piece.type].append(piece)

    def place_pieces(self, piece: Piece, rank: R):
        for file in range(self.board.n_files):
            self.place_piece(deepcopy(piece), (file, rank))

    def start(self):
        while True:
            self.board.draw()
            move = input(f"{'White' if self.turn == C.WHITE else 'Black'} move: ")

            piece_type = T[move[0]]
            file = F[move[-2]]
            rank = R[f"r{move[-1]}"]
            print(f"You moved {piece_type} to {file}{rank}")
