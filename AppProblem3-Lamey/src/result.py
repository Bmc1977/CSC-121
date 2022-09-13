from enum import Enum


class Result(Enum):
    """
    These are the possible results from an attempted "play" on the connect-4 board.
    Look at the code below to see how they're used.
    """
    ILLEGAL = 1
    LEGAL = 2
    WIN = 3
    DRAW = 4
