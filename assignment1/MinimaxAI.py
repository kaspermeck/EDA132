import copy
from Board import *

# SimpleAI places
class MinimaxAI(object):

  def __init__(self, board, color):
    self.aicolor = color
    self.board = board

  def makeMove(self):
    y, x = self.getMove(self.board, self.aicolor)
    self.board.place(y, x, self.aicolor)
    return y, x

  def getMove(self, board, color):
    return self.getScoreMove(board, color, 0, 3)[0]

  def getScoreMove(self, board, color, depth, maxDepth):
    moves = []
    
    for y in xrange(8):
      for x in xrange(8):
        if board.isLegal(y, x, color):
          moves.append([(y, x), self.score(board, y, x, color)])

    if depth < maxDepth:
      for move in moves:
        b = copy.deepcopy(board)
        b.place(move[0][0], move[0][1], color)
        score = self.getScoreMove(b, Board.oppositeColor(color), depth + 1, maxDepth)

        if not score: # opponent can make no move, good? (note negation)
          score = -1000  
        else:
          score = score[1]
      
        if color == self.aicolor: # next level is opponent, therefor minus
          move[1] -= score 
        else:
          move[1] += score

    # Sort by score, return last element (highest score)
    if not moves:
      return []
    else:
      return sorted(moves, key = lambda move: move[1])[-1]

    

  def score(self, board, y, x, color):
    corners = ((0,0),(7,7),(0,7),(7,0))
    next_to_corners = (
      (0,1),(1,0),(1,1),
      (6,7),(7,6),(6,6),
      (0,6),(1,7),(1,6),
      (6,0),(7,1),(6,1)
    )

    scoreboard = [
      [99, - 8,  8,  6,  6,  8, - 8, 99],
      [-8, -24, -4, -3, -3, -4, -24, -8],
      [ 8, - 4,  7,  4,  4,  7, - 4,  8],
      [ 6, - 3,  4,  0,  0,  4, - 3,  6],
      [ 6, - 3,  4,  0,  0,  4, - 3,  6],
      [ 8, - 4,  7,  4,  4,  7, - 4,  8],
      [-8, -24, -4, -3, -3, -4, -24, -8],
      [99, - 8,  8,  6,  6,  8, - 8, 99]
    ]

    score = board.scorediff(y, x, color)
    score += scoreboard[y][x]

    return score
