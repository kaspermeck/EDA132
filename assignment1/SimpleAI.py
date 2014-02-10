import copy, time
from random import choice

# SimpleAI places
class SimpleAI(object):
  def __init__(self, board, color, pause):
    self.aicolor = color
    self.board = board
    self.pause = pause

  def makeMove(self):
    y, x = self.getMove()
    self.board.place(y, x, self.aicolor)
    time.sleep(self.pause)
    return y, x

  def getMove(self):
    moves = []
    for y in xrange(8):
      for x in xrange(8):
        if self.board.isLegal(y, x, self.aicolor):
          moves.append((y, x))

    return choice(moves)
