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
    y, x = self.minimax(self.board, self.aicolor)
    self.board.place(y, x, self.aicolor)
    """   
    a = True
    while a:
      for event in self.gui.pygame.event.get():
        if event.type == MOUSEBUTTONUP:
          a = False
    """
    print "Chose location", y, x, "\n"
    return y, x

  def scr(self, board, color):
    corners = ((0,0),(7,7),(0,7),(7,0))
    next_to_corners = (
      (0,1),(1,0),(1,1),
      (6,7),(7,6),(6,6),
      (0,6),(1,7),(1,6),
      (6,0),(7,1),(6,1)
    )

    square_weights = [
      [99, -24,  8,  6,  6,  8, -24, 99],
      [-24, -24, -4, -3, -3, -4, -24,-24],
      [ 8, - 4,  7,  4,  4,  7, - 4,  8],
      [ 6, - 3,  4,  0,  0,  4, - 3,  6],
      [ 6, - 3,  4,  0,  0,  4, - 3,  6],
      [ 8, - 4,  7,  4,  4,  7, - 4,  8],
      [-24, -24, -4, -3, -3, -4, -24,-24],
      [99, -24,  8,  6,  6,  8, -24, 99]
    ]

    bscr, wscr = board.score()
    scr = bscr-wscr if color == Board.black else wscr-bscr

    for y in xrange(8):
      for x in xrange(8):
        if board.grid[y][x] == color:
          scr += square_weights[y][x]
        elif board.grid[y][x] == Board.oppositeColor(color):
          scr -= square_weights[y][x]

    if color != self.aicolor:
      scr *= -1

    return scr

  def minimax(self, board, color):
    # Always do the first depth, regardless off time limit
    best_move = []
    self.starttime = time.time()
    
    # Iterative deepening. Never deeper than 10 however.
    for depth in range(10):
      move = self.maxValue(board, color, depth)

      if move == "cutoff":
        print "Broke off during depth", depth, "hence the computed depth is", (depth-1)
        break
      else:
        best_move = move
    
    # Return the best move
    print "Time passed:", time.time() - self.starttime
    return best_move[0]

  def allMoves(self, board, color):
    moves = []
    
    for y in xrange(8):
      for x in xrange(8):
        if board.isLegal(y, x, color):
          moves.append([(y, x)])

    return moves

  def maxValue(self, board, color, depth):
    moves = self.allMoves(board, color)

    if not moves:
      if color == self.aicolor:
        return [0, -1000]
      else:
        return [0, 1000]
    elif depth == 0:
      for m in moves:
        b = copy.deepcopy(board)
        y, x, = m[0]
        b.place(y, x, color)
        m.append(self.scr(b, color))
      
      return max(moves, key = lambda move: move[1])
    else:
      for m in moves:
        if time.time() - self.starttime > self.maxtime:
          return "cutoff"

        b = copy.deepcopy(board)
        y, x, = m[0]
        b.place(y, x, color)
        scr = self.minValue(b, Board.oppositeColor(color), depth-1)

        if scr == "cutoff":
          return scr
        else:
          m.append(scr[1])

      return max(moves, key = lambda move: move[1])

  def minValue(self, board, color, depth):
    moves = self.allMoves(board, color)

    if not moves:
      if color == self.aicolor:
        return [0, 1000]
      else:
        return [0, -1000]
    elif depth == 0:
      for m in moves:
        b = copy.deepcopy(board)
        y, x, = m[0]
        b.place(y, x, color)
        m.append(self.scr(b, color))
  
      return min(moves, key = lambda move: move[1])
    else:
      for m in moves:
        if time.time() - self.starttime > self.maxtime:
          return "cutoff"

        b = copy.deepcopy(board)
        y, x = m[0]
        b.place(y, x, color)
        scr = self.maxValue(b, Board.oppositeColor(color), depth-1)

        if scr == "cutoff":
          return scr
        else:
          m.append(scr[1])
  
      return min(moves, key = lambda move: move[1])


