import pygame, sys, time
from pygame.locals import *
from Board import Board
from SimpleAI import SimpleAI

# Load pygame
pygame.init()
fpsClock = pygame.time.Clock()

# Load game mechanics
board = Board()
ai = SimpleAI() # replace with ai-object ai = AI(board)
human = "human"
currentPlayer = human

# Setup screen
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 128, 0)
sqs = 70
bs = 8*sqs

screen = pygame.display.set_mode((bs, bs))
pygame.display.set_caption('Othello ala Linus och Kasper!')
pygame.mouse.set_visible(True)

# Main application loop
while True:

	# Draw current screen
	screen.fill(green)
	for y in xrange(8):
		for x in xrange(8):
			# Draw black background squares
			pygame.draw.rect(screen, black, (y*sqs, x*sqs, sqs, sqs), 2)
			
			# Draw disks
			if board.grid[y][x] == Board.black:
				pygame.draw.circle(screen, black, (x*sqs+sqs/2, y*sqs+sqs/2), sqs/2, 0)
			elif board.grid[y][x] == Board.white:
				pygame.draw.circle(screen, white, (x*sqs+sqs/2, y*sqs+sqs/2), sqs/2, 0)

	# Handle actions
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONUP:
			boolHuman = board.canMakeMove(Board.black)
			boolAI = board.canMakeMove(Board.white)
			if not boolHuman and not boolAI:
				print 'gg'
			if currentPlayer==human and boolHuman:
				x, y = event.pos
				x /= sqs
				y /= sqs
				print "Clicked at", y, x
				
				if board.isLegal(y, x, Board.black):
					board.place(y, x, Board.black)
					currentPlayer = ai
			elif currentPlayer==human and not boolHuman:
				currentPlayer = ai
			elif currentPlayer==ai and boolAI:
				y, x = ai.getMove(board, Board.white)
				board.place(y, x, Board.white)
				print "AI clicked at", y, x
				currentPlayer = human
			elif currentPlayer==ai and not boolAI:
				currentPlayer = human

	pygame.display.update()
	fpsClock.tick(30)
