import random
from abc import ABC

from chess import Board, Move


class Solver(ABC):
    def move(self, board: Board) -> Move:
        raise NotImplementedError


class RandomSolver(Solver):
    def move(self, board: Board) -> Move:
        moves = list(board.legal_moves)
        return random.choice(moves)
