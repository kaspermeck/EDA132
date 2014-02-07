import pygame, sys, time
from pygame.locals import *
from Board import Board
from SimpleAI import SimpleAI
from MinimaxAI import MinimaxAI

# Load pygame
pygame.init()
fpsClock = pygame.time.Clock()

# Load game mechanics
board = Board()
whitePlayer = Human(self, board, Board.white)
blackPlayer = MinimaxAI(board, Board.black)
currentPlayer = blackPlayer

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
	canWhite = board.canMakeMove(Board.white)
	canBlack = board.canMakeMove(Board.black)

	if not canWhite and not canBlack:
		print board.score()
	if currentPlayer == whitePlayer and canWhite:
		whitePlayer.makeMove()
		currentPlayer = blackPlayer
	elif currentPlayer == whitePlayer and not canWhite:
		currentPlayer = blackPlayer
	elif currentPlayer == blackPlayer and canBlack:
		blackPlayer.makeMove()
		currentPlayer = blackPlayer
	elif currentPlayer == blackPlayer and not canBlack:
		currentPlayer = blackPlayer
	
	pygame.display.update()
	fpsClock.tick(30)
