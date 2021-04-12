'''

	engine

'''


class GameState():
	def __init__(self):
		self.board = [
			['-', '-', '-'],
			['-', '-', '-'],
			['-', '-', '-']
			]

		self.xToMove = True
		self.moveLog = []
	
	def checkWin(self, Board):
		x = 0
		for i in range(3):
			for j in range(3):
				if Board[i][j] != '-':
					x += 0
				else:
					x += 1
					break
		
		if (Board[0][0] == 'X' and Board[0][1] == 'X' and Board[0][2] == 'X'):
			return 'X1'
		elif (Board[1][0] == 'X' and Board[1][1] == 'X' and Board[1][2] == 'X'):
			return 'X2'
		elif (Board[2][0] == 'X' and Board[2][1] == 'X' and Board[2][2] == 'X'):
			return 'X3'
		elif (Board[0][0] == 'X' and Board[1][0] == 'X' and Board[2][0] == 'X'):
			return 'X4'
		elif (Board[0][1] == 'X' and Board[1][1] == 'X' and Board[2][1] == 'X'):
			return 'X5'
		elif (Board[0][2] == 'X' and Board[1][2] == 'X' and Board[2][2] == 'X'):
			return 'X6'
		elif (Board[0][0] == 'X' and Board[1][1] == 'X' and Board[2][2] == 'X'):
			return 'X7'
		elif (Board[0][2] == 'X' and Board[1][1] == 'X' and Board[2][0] == 'X'):
			return 'X8'
		
		#O
		
		elif (Board[0][0] == 'O' and Board[0][1] == 'O' and Board[0][2] == 'O'):
			return 'O1'
		elif (Board[1][0] == 'O' and Board[1][1] == 'O' and Board[1][2] == 'O'):
			return 'O2'
		elif (Board[2][0] == 'O' and Board[2][1] == 'O' and Board[2][2] == 'O'):
			return 'O3'
		elif (Board[0][0] == 'O' and Board[1][0] == 'O' and Board[2][0] == 'O'):
			return 'O4'
		elif (Board[0][1] == 'O' and Board[1][1] == 'O' and Board[2][1] == 'O'):
			return 'O5'
		elif (Board[0][2] == 'O' and Board[1][2] == 'O' and Board[2][2] == 'O'):
			return 'O6'
		elif (Board[0][0] == 'O' and Board[1][1] == 'O' and Board[2][2] == 'O'):
			return 'O7'
		elif (Board[0][2] == 'O' and Board[1][1] == 'O' and Board[2][0] == 'O'):
			return 'O8'
		elif x == 0:
			return 'D-'
		else:
			return '--'
	def Move(self, row, col):
		if self.board[row][col] == '-':
			if self.xToMove == True:
				self.board[row][col] = 'X'
				self.xToMove = not self.xToMove
				
			elif self.xToMove == False:
				self.board[row][col] = 'O'
				self.xToMove = not self.xToMove
		else:
			print("That square has already been taken by", self.board[row][col])








'''

self.board = [['X', 'X', 'X'],['-', '-', '-'],['-', '-', '-']]
self.board = [['-', '-', '-'],['X', 'X', 'X'],['-', '-', '-']]
self.board = [['-', '-', '-'],['-', '-', '-'],['X', 'X', 'X']]
self.board = [['X', '-', '-'],['X', '-', '-'],['X', '-', '-']]
self.board = [['-', 'X', '-'],['-', 'X', '-'],['-', 'X', '-']]
self.board = [['-', '-', 'X'],['-', '-', 'X'],['-', '-', 'X']]
self.board = [['X', '-', '-'],['-', 'X', '-'],['-', '-', 'X']]
self.board = [['-', '-', 'X'],['-', 'X', '-'],['X', '-', '-']]


if (self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X') or (self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X') or (self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X') or (self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X') or (self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X') or (self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X') or (self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X') or (self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X')


=================================================================================

if self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O'
if self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O'
if self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O'

if self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O'
if self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O'
if self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O'

if self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O'
if self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O'


==================================================================================
x = 0
for i in range(3):
	for j in range(3):
		if Board[i][j] == '-':
			x += 0
		else:
			x += 1




'''