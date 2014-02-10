import copy, pygame, time
from Board import *
from pygame.locals import *

# SimpleAI places
class MinimaxAI(object):

  def __init__(self, gui, board, color, timelimit):
    self.aicolor = color
    self.board = board
    self.gui = gui
    self.maxtime = timelimit

  def makeMove(self):
    print self.aicolor, "MinimaxAI player is thinking..."
    y, x = self.getMove(self.board, self.aicolor)
    self.board.place(y, x, self.aicolor)
    
    #a = True
    #while a:
    #  for event in self.gui.pygame.event.get():
    #    if event.type == MOUSEBUTTONUP:
    #      a = False

    print "Chose location", y, x, "\n"
    return y, x

  def getMove(self, board, color):
    # Always do the first depth, regardless off timelimit
    bestmost = self.getScoreMove(board, color, 0, 0)

    # Iterative deepening. Never deeper than 10 however.
    self.starttime = time.time()
    for maxDepth in range(1,10):
      move = self.getScoreMove(board, color, 0, maxDepth)

      if move == "cutoff":
        print "Broke off during depth", maxDepth
        break
      else:
        bestmove = move[0]

    # Return the best move
    return bestmove

  def getScoreMove(self, board, color, depth, maxDepth):
    moves = []
    
    for y in xrange(8):
      for x in xrange(8):
        # cutoff check
        if board.isLegal(y, x, color):
          score = self.score(board, y, x, color)
          score *= (-1) if color != self.aicolor else 1
          moves.append([(y, x), score])

    if depth < maxDepth:
      for move in moves:
        if time.time() - self.starttime > self.maxtime:
          return "cutoff"

        b = copy.deepcopy(board)
        b.place(move[0][0], move[0][1], color)
        m = self.getScoreMove(b, Board.oppositeColor(color), depth + 1, maxDepth)

        if not m: # If the move list is empty, no move can be made, this is very good/bad.
          move[1] += 1000 if color == self.aicolor else -1000
        elif m == "cutoff":
          return m
        else:
          move[1] += m[-1]

    # Print
    #print depth, " -> possible moves:"
    #for move in moves:
    #  print move

    # Return max/min
    if not moves:
      return []
    else:
      if color == self.aicolor:
        return sorted(moves, key = lambda move: move[1])[-1] #max
      else:
        return sorted(moves, key = lambda move: move[1])[0] #min

    

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
