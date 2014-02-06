import copy
from random import choice

# SimpleAI places
class SimpleAI(object):
  def __init__(self):
    pass

  def getMove(self, board, color):
    self.board = copy.deepcopy(board)
    self.moves = []

    for y in xrange(8):
      for x in xrange(8):
        if board.isLegal(y, x, color):
          self.moves.append((y, x))

    return choice(self.moves)
