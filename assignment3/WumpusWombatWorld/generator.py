from random import choice
import sys, exceptions
n = 0
size = 0

def generate(grid_size, n_wumpus, n_pits, n_gold):
  global size
  global n
  size = grid_size
  n = size*size
  
  raw_data_inits = []
  raw_data_objects = []
  raw_data_goals = []
  
  # (sqr = int, relations = [], ins = [])
  grid = [(x, [], []) for x in xrange(n)]

  # Set up grid
  for i, (sqr, relations, ins) in enumerate(grid):
    if has_north(i):
      relations.append(('north', i + size, i))    
    if has_west(i):
      relations.append(('west',  i - 1, i))
    if has_south(i):
      relations.append(('south', i - size, i))
    if has_east(i):
      relations.append(('east',  i + 1, i))
  
  # Set up agent
  grid[0][2].append('agent') #add agent in ins-list
  raw_data_objects.append('agent - worldobj ;self')
  
  raw_data_inits.append(';inits due to agent spawning')
  raw_data_inits.append(p('facing east'))
  raw_data_inits.append(p('visited ' + fs(0)))
  raw_data_inits.append(p('safe ' + fs(0)))
  raw_data_inits.append(p('safe ' + fs(1)))
  raw_data_inits.append(p('safe ' + fs(size)))
  raw_data_inits.append(p('not-in pit ' + fs(0)))
  raw_data_inits.append(p('not-in wumpus ' + fs(0)))
  raw_data_inits.append(p('not-in pit ' + fs(1)))
  raw_data_inits.append(p('not-in wumpus ' + fs(1)))
  raw_data_inits.append(p('not-in pit ' + fs(size)))
  raw_data_inits.append(p('not-in wumpus ' + fs(size)))

  # Set up world objects
  raw_data_objects.append('north west south east - direction')
  raw_data_objects.append('pit     - worldobj')
  raw_data_objects.append('wumpus  - worldobj')
  raw_data_objects.append('breeze  - worldobj')
  raw_data_objects.append('stench  - worldobj')
  raw_data_objects.append('glimmer - worldobj')
  raw_data_objects.append('gold    - worldobj ;that good ol\' gold')
   
  # Set up random wampus, gold and pits
  positions = range(n)
  del positions[size]
  del positions[1]
  del positions[0]

  for k in xrange(n_wumpus):
    i = choice(positions)
    spawn_wumpus(i, grid)

  for k in xrange(n_pits):
    i = choice(positions)
    spawn_pit(i, grid)

  for k in xrange(n_gold):
    i = choice(positions)
    grid[i][2].append('gold')

  # Set up goals
  raw_data_goals.append(p('has-gold'))
  raw_data_goals.append(p('in agent ' + fs(0)))

  # Return the whole dataset
  return format_data(raw_data_objects, raw_data_inits, raw_data_goals, grid)

def format_data(raw_objects, raw_inits, raw_goals, grid):
  def indent(dep):
    return ' '*dep*2

  # Create problem
  problem = p('problem wumpus-world-' + `n`)

  # Create domain
  domain = indent(1) + p(':domain wumpusworld')

  # Create objects
  objects = ''
  for o in raw_objects:
    objects += indent(2) + o + '\n' 
  objects += indent(2) + format_sqr_objects(grid) + '\n'
  objects = indent(1) + p(':objects\n' + objects + indent(1))

  # Create inits
  inits = '\n'
  for i in format_grid_relations(grid):
    inits += indent(2) + i + '\n'
  for i in raw_inits:
    inits += indent(2) + i + '\n'
  inits += '\n'
  for i in format_grid_ins(grid):
    inits += indent(2) + i + '\n'
  inits = indent(1) + p(':init\n' + inits + indent(1))

  # Create goals
  goals = ''
  for g in raw_goals:
    goals += indent(2) + g + '\n'
  goals = p('and\n' + goals + indent(1)) 
  goals = indent(1) + p(':goal ' + goals)

    

  # Combine
  data = p('define ' + problem + 
    '\n\n' + domain +
    '\n\n' + objects +
    '\n\n' + inits +
    '\n\n' + goals +
    '\n')

  return data

def spawn_wumpus(i, grid):
  grid[i][2].append('wumpus')

  if has_north(i):
    grid[i+size][2].append('stench')
  if has_west(i):
    grid[i-1][2].append('stench')
  if has_south(i):
    grid[i-size][2].append('stench')
  if has_east(i):
    grid[i+1][2].append('stench')

def spawn_pit(i, grid):
  grid[i][2].append('pit')

  if has_north(i):
    grid[i+size][2].append('breeze')
  if has_west(i):
    grid[i-1][2].append('breeze')
  if has_south(i):
    grid[i-size][2].append('breeze')
  if has_east(i):
    grid[i+1][2].append('breeze')

def has_north(i):
  return i < (n - size)

def has_west(i):
  return i % size != 0

def has_south(i):
  return i >= size

def has_east(i):
  return (i+1) % size != 0

def format_grid_ins(grid):
  data = []
  data.append(';world objects inside squares')
  for (sqr, relations, ins) in grid:
    for inn in ins:
      data.append( p('in ' + inn + ' ' + fs(sqr)) )
  return data

def format_grid_relations(grid):
  data = []
  for (sqr, relations, ins) in grid:
    data.append(';square ' + fs(sqr))
    for (direction, sqr1, sqr2) in relations:
      data.append( p('sqr-' + direction + '-of ' + fs(sqr1) + ' ' + fs(sqr2)) )
    data.append('')
  return data

def format_sqr_objects(grid):
  data = ''
  for (sqr, relations, ins) in grid:
    data += fs(sqr) + ' '
  data += '- square'
  return data

def format_sqr(sqr):
  return 's' + `sqr`

def fs(sqr):
  return format_sqr(sqr)

def p(expr):
  return '(' + expr + ')'

def format_input_error():
  return ("Run the generator with the command\n" +
    "python generator.py n w p g\n" +
    "where\n" +
    "    n = sqrt(size) (minimum 2),  thus n = 4 gives a game of 4x4\n" +
    "    w = number of wumpuses\n" +
    "    p = number of pits\n" +
    "    g = number of gold piles (minimum 1)\n")
    

def main(argv=sys.argv):
  try:
    n = int(argv[1]) if int(argv[1]) >= 2 else 2
    w = int(argv[2]) if int(argv[2]) >= 0 else 0
    p = int(argv[3]) if int(argv[3]) >= 0 else 0
    g = int(argv[4]) if int(argv[4]) >= 1 else 1
  except exceptions.ValueError:
    print format_input_error() 
    return 
  except exceptions.IndexError:
    print format_input_error()
    return

  print generate(n, w, p, g)

if __name__ == "__main__":
	main()
