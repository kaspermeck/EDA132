import copy, pygame, time
from Board import *
from pygame.locals import *

# SimpleAI places
class MinimaxAlphaBetaAI(object):

  def __init__(self, gui, board, color, timelimit):
    self.aicolor = color
    self.board = board
    self.gui = gui
    self.maxtime = timelimit

  def makeMove(self):
    print self.aicolor, "MinimaxAI player is thinking..."
    y, x = self.minimax(self.board, self.aicolor)
    self.board.place(y, x, self.aicolor)
     
    a = False
    while a:
      for event in self.gui.pygame.event.get():
        if event.type == MOUSEBUTTONUP:
          a = False
    
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
    
    best_move = self.maxValue(board, color, 5, float('-inf'), float('inf'))
    # Iterative deepening. Never deeper than 10 however.
    """
    for depth in range(10):
      print "\n----------------------------------------"
      print "Searching with depth", depth
      print "----------------------------------------"
      move = self.maxValue(board, color, depth, float('-inf'), float('inf'))

      if move == "cutoff":
        print "Broke off during depth", depth, "hence the computed depth is", (depth-1)
        break
      else:
        best_move = move
        print "SAVED BEST MOVE", best_move
    """
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

  def maxValue(self, board, color, depth, alpha, beta):
    moves = self.allMoves(board, color)

    if not moves:
      if color == self.aicolor:
        return [0, -0]
      else:
        return [0, 0]
    elif depth == 0:
      best_move = []
      scr = 0
      #print "\nMax", color, "at", depth, "("+ str(alpha) + "," + str(beta)+ "):",
      for m in moves:
        b = copy.deepcopy(board)
        y, x = m[0]
        b.place(y, x, color)
        scr = self.scr(b, color)
       # print scr,
        if scr >= alpha:
          best_move = [(y, x), scr]
          alpha = scr
        if alpha >= beta:
          return best_move
      
      if not best_move:
        return [0, scr+1]
      else:
        return best_move
    else:
      best_move = []
      scr = [0, 0]
      #print "\nMax", color, "at", depth, "("+ str(alpha) + "," + str(beta)+ "):",
      for m in moves:
        if time.time() - self.starttime > self.maxtime:
          return "cutoff"

        b = copy.deepcopy(board)
        y, x, = m[0]
        b.place(y, x, color)
        scr = self.minValue(b, Board.oppositeColor(color), depth-1, alpha, beta)
       # print scr,
        #print "\n--Min at", (depth-1), "returned", [(y, x), scr[1]], alpha, beta,

        if scr == "cutoff":
          return scr
        else:
          if scr[1] >= alpha:
            best_move = [(y, x), scr[1]]
            alpha = scr[1]
         # print "\n", alpha, beta,
          if alpha >= beta:
            #print "\nbm", best_move,
            return best_move

      #print "\nbm", best_move,
      if not best_move:
        return [0, (scr[1]+1)]
      else:
        return best_move

  def minValue(self, board, color, depth, alpha, beta):
    moves = self.allMoves(board, color)

    if not moves:
      if color == self.aicolor:
        return [0, 0]
      else:
        return [0, -0]
    elif depth == 0:
      best_move = []
      #print "\nMin", color, "at", depth, "("+ str(alpha) + "," + str(beta)+ "):",
      for m in moves:
        b = copy.deepcopy(board)
        y, x, = m[0]
        b.place(y, x, color)
        scr = self.scr(b, color)
        #print [(y, x), scr],
       # print scr,
        if scr <= beta:
          best_move = [(y, x), scr]
          beta = scr
        if alpha >= beta:
          return best_move
           
      if not best_move:
        return [0, scr-1]
      else:
        return best_move 
    else:
      best_move = []
      scr = [0,0]
      #print "\nMin", color, "at", depth, "("+ str(alpha) + "," + str(beta)+ "):",
      for m in moves:
        if time.time() - self.starttime > self.maxtime:
          return "cutoff"

        b = copy.deepcopy(board)
        y, x = m[0]
        b.place(y, x, color)
        scr = self.maxValue(b, Board.oppositeColor(color), depth-1, alpha, beta)

        #print "\n--Max at", (depth-1), "returned", [(y, x), scr[1]],
        if scr == "cutoff":
          return scr
        else:
          if scr[1] <= beta:
            best_move = [(y, x), scr[1]]
            beta = scr[1]
          if alpha >= beta:
           # print "\nbm", best_move,
            return best_move
  
     # print "\nbm", best_move,
      if not best_move:
        return [0, scr[1]-1]
      else:
        return best_move


