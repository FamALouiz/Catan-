from pycatan import Game
from pycatan.board import BeginnerBoard, BoardRenderer

game = Game(BeginnerBoard())
renderer = BoardRenderer(game.board)
