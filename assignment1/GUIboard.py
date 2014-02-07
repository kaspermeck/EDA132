import pygame, sys, time
from pygame.locals import *
from Board import Board
from SimpleAI import SimpleAI
from MinimaxAI import MinimaxAI
from Human import Human

class GUIboard(object):
	# Load pygame
	def __init__(self):
		self.pygame = pygame
		self.pygame.init()
		self.fpsClock = pygame.time.Clock()
		self.board = Board()
		self.whitePlayer = SimpleAI(self.board, Board.white)
		#self.whitePlayer = MinimaxAI(self.board, Board.white)
		self.blackPlayer = MinimaxAI(self, self.board, Board.black)
		self.currentPlayer = self.blackPlayer
		self.screen = self.drawscreen()

	def drawscreen(self):
		# Setup screen
		sqs = 70
		bs = 8*sqs
		screen = self.pygame.display.set_mode((bs, bs))
		tit = 'Othello ala Linus och Kasper!'
		pygame.display.set_caption(tit)
		pygame.mouse.set_visible(True)
		self.myfont = self.pygame.font.SysFont("monospace", 20)
		return screen

	def updatescreen(self):
		black = pygame.Color(0, 0, 0)
		white = pygame.Color(255, 255, 255)
		green = pygame.Color(0, 128, 0)
		sqs = 70
		bs = 8*sqs
		self.screen.fill(green)
		for y in xrange(8):
			for x in xrange(8):
				# Draw black background squares
				self.pygame.draw.rect(self.screen, black, (y*sqs, x*sqs, sqs, sqs), 2)
				
				# Draw coordinate
				label = self.myfont.render("("+str(y)+","+str(x)+")", 1, (0,0,0))
				self.screen.blit(label, (x*sqs+5, y*sqs+5))

				# Draw disks
				if self.board.grid[y][x] == Board.black:
					self.pygame.draw.circle(self.screen, black, (x*sqs+sqs/2, y*sqs+sqs/2), sqs/2, 0)
				elif self.board.grid[y][x] == Board.white:
					self.pygame.draw.circle(self.screen, white, (x*sqs+sqs/2, y*sqs+sqs/2), sqs/2, 0)


	def rungame(self):
		# Main application loop
		while True:
			self.updatescreen()
			self.pygame.display.update()
			self.fpsClock.tick(30)
			# Handle actions
			canWhite = self.board.canMakeMove(Board.white)
			canBlack = self.board.canMakeMove(Board.black)

			if not canWhite and not canBlack:
				print "Score (black, white):", self.board.score()
				while True:
					for event in self.pygame.event.get():
						if event.type == QUIT:
							self.pygame.quit()
							sys.exit()
			elif self.currentPlayer == self.whitePlayer and canWhite:
				y,x = self.whitePlayer.makeMove()
				self.currentPlayer = self.blackPlayer
			elif self.currentPlayer == self.whitePlayer and not canWhite:
				self.currentPlayer = self.blackPlayer
			elif self.currentPlayer == self.blackPlayer and canBlack:
				y,x = self.blackPlayer.makeMove()
				self.currentPlayer = self.whitePlayer
			elif self.currentPlayer == self.blackPlayer and not canBlack:
				self.currentPlayer = self.whitePlayer

if __name__ == "__main__":
	GB = GUIboard()
	GB.rungame()
