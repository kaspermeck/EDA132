#import Board as board

class Main_program(object):
	def __init__(self):
		" black is player, white is computer "
		color = 'black'
		board = self.make_board()

	def make_board(self):
		return board

	def place(self):
		if color == 'black':
			# wait for action from game board
			# action generates x,y-coordinates

			# check if the coordinates are legal
			if self.board.isLegal(y, x, self.color):
				self.board.place()
				self.color = 'white'
				return True
			else:
				# print out with illegal argument
				self.place()
			
		else:
			for x in range(7):
				for y in range(7):
					if board.isLegal(y, x, self.color):
						board.place(y, x, self.color)
						self.color = 'black'
						return True
		return False

	def update():
		# rewrite the entire board
		pass

if __name__ == '__main__':
	main = main_program()
	while 1:
		main.update()
		if not main.place():
			break
