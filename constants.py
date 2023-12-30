from enum import IntEnum


class Color(IntEnum):
    WHITE = 1
    BLACK = -1


class State(IntEnum):
    EMPTY = 0
    WHITE = Color.WHITE
    BLACK = Color.BLACK


class PieceType(IntEnum):
    K = 0
    Q = 1
    R = 2
    B = 3
    N = 4
    P = 5


class File(IntEnum):
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    h = 7


class Rank(IntEnum):
    r1 = 0
    r2 = 1
    r3 = 2
    r4 = 3
    r5 = 4
    r6 = 5
    r7 = 6
    r8 = 7
