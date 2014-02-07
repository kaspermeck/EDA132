import pygame, sys
from pygame.locals import *
from Board import Board

class Human(object):
	def __init__(self, GUIboard, board, color):
		self.GUIboard = GUIboard
		self.board = board
		self.color = color


	def makeMove(self):
		while(True)
			for event in self.GUIboard.pygame.event.get():
				if event.type == QUIT:
					self.GUIboard.pygame.quit()
					sys.exit()
				elif event.type == MOUSEBUTTONUP:
					x, y = event.pos
					x /= sqs
					y /= sqs
					if self.board.isLegal(y, x, self.color):
						self.board.place(y, x, self.color)
						return x, y