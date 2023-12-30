from Board import Board
from Game import Game
from History import History

board = Board()
history = History()

game = Game(board, history)
game.start()
