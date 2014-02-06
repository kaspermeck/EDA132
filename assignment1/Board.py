class Board(object):
  # Colors
  empty = "empty"
  black = "black"
  white = "white"
  colors = (black, white)
  
  # Direction modifiers
  directions = (
    (-1,  0), # north
    (-1,  1), # northeast
    ( 0,  1), # east
    ( 1,  1), # southeast
    ( 1,  0), # south
    ( 1, -1), # southwest 
    ( 0, -1), # west
    (-1, -1)  # northwest
  )

  def __init__(self):
    self.clear()
        
  def place(self, y, x, color):
    if self.isLegal(y, x, color):
      self.grid[y][x] = color

      # Flip disks
      orgY = y
      orgX = x

      for i in xrange(8):
        y = orgY
        x = orgX

        if self.isLegalInDirection(y, x, color, self.directions[i]):
          y += self.directions[i][0]
          x += self.directions[i][1]

          while self.grid[y][x] == self.oppositeColor(color):
            self.grid[y][x] = color
            y += self.directions[i][0]
            x += self.directions[i][1]

  def clear(self): 
    self.grid = [[self.empty for x in xrange(8)] for x in xrange(8)]
    self.grid[3][3] = self.white
    self.grid[3][4] = self.black
    self.grid[4][3] = self.black
    self.grid[4][4] = self.white

  def isLegal(self, y, x, color):
    if self.isLegalCoordinate(y, x) and color in self.colors and grid[y][x] == Board.empty:
      # Serach for a match in all directions
      for i in xrange(8):
        if self.isLegalInDirection(y, x, color, self.directions[i]):
          return True

      # Didn't find a match in any direction
      return False
    else:
      return False

  # Assumed (y, x) is a legal coordinate
  def isLegalInDirection(self, y, x, color, direction):
    oColor = self.oppositeColor(color)
    y += direction[0]
    x += direction[1]
    offset = 1
       
    while self.isLegalCoordinate(y, x):
      if self.grid[y][x] == self.empty:
        return False
      if self.grid[y][x] == color: 
        return (True if offset > 1 else False)
      if self.grid[y][x] == oColor:
        y += direction[0]
        x += direction[1]
        offset += 1

  def isLegalCoordinate(self, y, x):
    return x in range(8) and y in range(8)

  def oppositeColor(self, color):
    if color == self.black:
      return self.white
    if color == self.white:
      return self.black
    raise Exception("Trying to get opposite color for an invalid color.")

  def printBoard(self):
    res = "";
    for y in range(8):
      for x in range(8):
        if self.grid[y][x] == self.empty:
          res += "- "
        elif self.grid[y][x] == self.black:
          res += "x "
        elif self.grid[y][x] == self.white:
          res += "o "
      res += "\n"
    print res
