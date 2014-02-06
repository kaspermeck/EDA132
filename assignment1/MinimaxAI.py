import copy

# SimpleAI places
class MinimaxAI(object):

  def __init__(self, color):
    self.aicolor = color

  def getMove(self, board, color):
    return getScoreMove(board, color).highest

  def getScoreMove(self, board, color):
    moves = []
    

    for y in xrange(8):
      for x in xrange(8):
        moves.append(((y, x), score(y, x, color)))

    for i in moves:
      b = copy.deepcopy(board)
      b.place(*moves[i][0], color])
      score = getScoreMove(b, Board.oppositeColor(color))
      
      if color == aicolor: # next level is opponent
        moves[i][1] -= score 
      else:
        moves[i][1] += score

    return sorted(moves, key = lambda move: move[1])[0]

    

  def score(self, y, x, color):
    corners = ((0,0),(7,7),(0,7),(7,0))
    next_to_corners = (
      (0,1),(1,0),(1,1),
      (6,7),(7,6),(6,6),
      (0,6),(1,7),(1,6),
      (6,0),(7,1),(6,1)
    )

    score = board.score()
    
    if (y,x) in corners:
      score += 20
    if (y,x) in next_to_corners:
      score -= 10)

    return score
