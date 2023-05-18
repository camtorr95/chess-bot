import os

from chess import Board

from solver import Solver, RandomSolver


class ChessGame:
    DEFAULT_GAMES_PATH = os.path.abspath('../games/')

    def __init__(self, board: Board = Board(), white_player: Solver = RandomSolver(),
                 black_player: Solver = RandomSolver()):
        self.board = board
        self.white_player = white_player
        self.black_player = black_player
        self.moves = 0

    def set_white_player(self, white_player: Solver):
        self.white_player = white_player

    def set_black_player(self, black_player: Solver):
        self.black_player = black_player

    def play(self, moves: int = 1):
        for _ in range(0, moves):
            move = self.white_player.move(self.board) \
                if self.moves % 2 == 0 else self.black_player.move(self.board)
            self.moves += 1
            self.board.push(move)

    def save(self, filename: str = 'my_game.fen'):
        fen = self.board.fen()

        if not filename.endswith('.fen'):
            filename = filename + '.fen'

        path = os.path.join(self.DEFAULT_GAMES_PATH, filename)
        print(f'saving in : {path}')

        with open(path, 'w') as f:
            f.write(fen)

    @staticmethod
    def load(filename: str = 'my_game.fen', path: str = DEFAULT_GAMES_PATH):
        path = os.path.join(path, filename)
        with open(path, 'r') as f:
            fen = f.read()
            return ChessGame(Board(fen=fen))
