import random
import os


column_size = 7
number_players = 2
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
game_board = []
players = []
players_turn = []
players_temp = []
player_symbol = ['X', 'O', 'V', 'H', 'M']
range_reverse = [6,5,4,3,2,1]
turn_temp = -1
c = 0
num = 0
a = 0
X = {}
O = {}
V = {}
H = {}
M = {}

# Game board display:
def board_display(column_size):
	print("C O N N E C T  4")
	print("'X O V H M'")
	print()
	for a in range(len(letters) - column_size):
		letters.pop()
	for a in range(len(letters)):
		print(' ',letters[a], end = ' ')
	print()
	for a in range(1,7):
		for b in range(len(letters)):
			print('+---', end = '')
		print('+')
		for i in range(column_size):
			print('|', game_board[a][i] ,'', end = '')
		print('|')
	for a in range(len(letters)):
		print('+---', end = '')
	print('+')

# Return the player's label (X, O, V, H, M) according to the players' move
def player_label(i):
	if i == 0:
		return 'X'
	elif i == 1:
		return 'O'
	elif i == 2:
		return 'V'
	elif i == 3:
		return 'H'
	elif i == 4:
		return 'M'

# Return the name of the player who is currently playing
def player_namee(i):
	name = players[i]
	return name

# Game process:
def player_board(f):
	# there are 8 possible ways to have 4 consecutive cells (2 horizontally, 2 vertically, 4 diagonally)
	c_0 = 0 # up vertically
	c_1 = 0 # up-right diagonally
	c_2 = 0 # right horizontally
	c_3 = 0 # down-right diagonally
	c_4 = 0 # down vertically
	c_5 = 0 # down-left diagonally
	c_6 = 0 # left horizontally
	c_7 = 0 # up-left diagonally

	coordinate = int(str(a_) + str(insert_index_)) # a_ and inser_index_ are global variables
	player_labell = player_label(f)

	if a_ - 2 >= 0: 
		c_0 = 1 # if the variable is equal to 1, 'up vertically' is possible
	else:
		c_0 = 0

	if a_ - 2 >= 0 and insert_index_ + 1 <= column_size - 1:
		c_1 = 1 # if the variable is equal to 1, 'up-right diagonally' is possible
	else:
		c_1 = 0

	if insert_index_ + 1 <= column_size - 1:
		c_2 = 1 # if the variable is equal to 1, 'right horizontally' is possible
	else:
		c_2 = 0

	if a_ + 1 <= 6 and insert_index_ + 1 <= column_size - 1:
		c_3 = 1 # if the variable is equal to 1, 'down-right diagonally' is possible
	else:
		c_3 = 0

	if a_ + 1 <= 6:
		c_4 = 1 # if the variable is equal to 1, 'down vertically' is possible
	else:
		c_4 = 0

	if a_ + 1 <= 6 and insert_index_ - 1 >= 0:
		c_5 = 1 # if the variable is equal to 1, 'down-left diagonally' is possible
	else:
		c_5 = 0

	if insert_index_ - 1 >= 0:
		c_6 = 1 # if the variable is equal to 1, 'left horizontally' is possible
	else:
		c_6 = 0

	if a_ - 2 >= 0 and insert_index_ - 1 >= 0:
		c_7 = 1 # if the variable is equal to 1, 'up-left diagonally' is possible
	else:
		c_7 = 0

	# 0 -> possible, '' -> not possible
	# there are 9 different cells on the board according to their possible ways of creating 4 consecutive cells
	if c_0 == 0 and c_1 == 0 and c_2 == 1 and c_3 == 1 and c_4 == 1 and c_5 == 1 and c_6 == 1 and c_7 == 0:
		if player_labell == 'X':
			X[coordinate] = ['', '', 0, 0, 0, 0, 0, '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'O':
			O[coordinate] = ['', '', 0, 0, 0, 0, 0, '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'V':
			V[coordinate] = ['', '', 0, 0, 0, 0, 0, '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'H':
			H[coordinate] = ['', '', 0, 0, 0, 0, 0, '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'M':
			M[coordinate] = ['', '', 0, 0, 0, 0, 0, '']# 8 items in the list are 8 possible ways to "connect 4"

	elif c_0 == 0 and c_1 == 0 and c_2 == 0 and c_3 == 0 and c_7 == 0:
		if player_labell == 'X':
			X[coordinate] = ['', '', '', '', 0, 0, 0, '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'O':
			O[coordinate] = ['', '', '', '', 0, 0, 0, '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'V':
			V[coordinate] = ['', '', '', '', 0, 0, 0, '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'H':
			H[coordinate] = ['', '', '', '', 0, 0, 0, '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'M':
			M[coordinate] = ['', '', '', '', 0, 0, 0, '']

	elif c_0 == 1 and c_1 == 0 and c_2 == 0 and c_3 == 0 and c_4 == 1 and c_5 == 1 and c_6 == 1 and c_7 == 1:
		if player_labell == 'X':
			X[coordinate] = [0, '', '', '', 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'O':
			O[coordinate] = [0, '', '', '', 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'V':
			V[coordinate] = [0, '', '', '', 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'H':
			H[coordinate] = [0, '', '', '', 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'M':
			M[coordinate] = [0, '', '', '', 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"

	elif c_1 == 0 and c_2 == 0 and c_3 == 0 and c_4 == 0 and c_5 == 0:
		if player_labell == 'X':
			X[coordinate] = [0, '', '', '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'O':
			O[coordinate] = [0, '', '', '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'V':
			V[coordinate] = [0, '', '', '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'H':
			H[coordinate] = [0, '', '', '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'M':
			M[coordinate] = [0, '', '', '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"

	elif c_0 == 1 and c_1 == 1 and c_2 == 1 and c_3 == 0 and c_4 == 0 and c_5 == 0 and c_6 == 1 and c_7 == 1:
		if player_labell == 'X':
			X[coordinate] = [0, 0, 0, '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'O':
			O[coordinate] = [0, 0, 0, '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'V':
			V[coordinate] = [0, 0, 0, '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'H':
			H[coordinate] = [0, 0, 0, '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'M':
			M[coordinate] = [0, 0, 0, '', '', '', 0, 0]# 8 items in the list are 8 possible ways to "connect 4"

	elif c_3 == 0 and c_4 == 0 and c_5 == 0 and c_6 == 0 and c_7 == 0:
		if player_labell == 'X':
			X[coordinate] = [0, 0, 0, '', '', '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'O':
			O[coordinate] = [0, 0, 0, '', '', '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'V':
			V[coordinate] = [0, 0, 0, '', '', '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'H':
			H[coordinate] = [0, 0, 0, '', '', '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'M':
			M[coordinate] = [0, 0, 0, '', '', '', '', '']# 8 items in the list are 8 possible ways to "connect 4"

	elif c_0 == 1 and c_1 == 1 and c_2 == 1 and c_3 == 1 and c_4 == 1 and c_5 == 0 and c_6 == 0 and c_7 == 0:
		if player_labell == 'X':
			X[coordinate] = [0, 0, 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'O':
			O[coordinate] = [0, 0, 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'V':
			V[coordinate] = [0, 0, 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'H':
			H[coordinate] = [0, 0, 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'M':
			M[coordinate] = [0, 0, 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"

	elif c_0 == 0 and c_1 == 0 and c_5 == 0 and c_6 == 0 and c_7 == 0:
		if player_labell == 'X':
			X[coordinate] = ['', '', 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'O':
			O[coordinate] = ['', '', 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'V':
			V[coordinate] = ['', '', 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'H':
			H[coordinate] = ['', '', 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'M':
			M[coordinate] = ['', '', 0, 0, 0, '', '', '']# 8 items in the list are 8 possible ways to "connect 4"

	else:
		if player_labell == 'X':
			X[coordinate] = [0, 0, 0, 0, 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'O':
			O[coordinate] = [0, 0, 0, 0, 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'V':
			V[coordinate] = [0, 0, 0, 0, 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'H':
			H[coordinate] = [0, 0, 0, 0, 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"
		if player_labell == 'M':
			M[coordinate] = [0, 0, 0, 0, 0, 0, 0, 0]# 8 items in the list are 8 possible ways to "connect 4"

	a_0 = ' ' # possible cell with the same label on the gameboard(up side)
	a_1 = ' ' # possible cell with the same label on the gameboard(up-right side)
	a_2 = ' ' # possible cell with the same label on the gameboard(right side)
	a_3 = ' ' # possible cell with the same label on the gameboard(down-left side)
	a_4 = ' ' # possible cell with the same label on the gameboard(down side)
	a_5 = ' ' # possible cell with the same label on the gameboard(down-left side)
	a_6 = ' ' # possible cell with the same label on the gameboard(left side)
	a_7 = ' ' # possible cell with the same label on the gameboard(up-left side)

	if player_labell == 'X':
		coordinate = str(coordinate) # rowcolumn
		a = int(coordinate[0]) # row 
		insert_index= int(coordinate[1]) # column
		coordinate = int(coordinate) # rowcolumn
		if a - 1 >= 0: 
			a_0 = int(str(a-1) + str(insert_index))
			a_1 = int(str(a-1) + str(insert_index+1))
		if insert_index - 1 >= 0:
			a_5 = int(str(a+1) + str(insert_index-1))
			a_6 = int(str(a) + str(insert_index-1))
		if a - 1 >= 0 and insert_index - 1 >= 0:
			a_7 = int(str(a-1) + str(insert_index-1))
		a_2 = int(str(a) + str(insert_index+1))
		a_3 = int(str(a+1) + str(insert_index+1))
		a_4 = int(str(a+1) + str(insert_index))

		if a_0 in X: # if True -> up side cell found
			temp_list = X[a_0]
			temp_list[4] = temp_list[4] + 1 # for the found cell, the "coordinate cell" is located at the down side
			X[a_0] = temp_list
			temp_list_1 = X[coordinate]
			temp_list_1[0] = temp_list_1[0] + 1
			X[coordinate] = temp_list_1
		if a_1 in X: # if True -> up-right side cell found
			temp_list = X[a_1]
			temp_list[5] = temp_list[5] + 1 # for the found cell, the "coordinate cell" is located at the down-left side
			X[a_1] = temp_list
			temp_list_1 = X[coordinate]
			temp_list_1[1] = temp_list_1[1] + 1 
			X[coordinate] = temp_list_1
		if a_2 in X: # if True -> right side cell found
			temp_list = X[a_2]
			temp_list[6] = temp_list[6] + 1 # for the found cell, the "coordinate cell" is located at the left side
			X[a_2] = temp_list
			temp_list_1 = X[coordinate]
			temp_list_1[2] = temp_list_1[2] + 1
			X[coordinate] = temp_list_1
		if a_3 in X: # if True -> down-right side cell found
			temp_list = X[a_3]
			temp_list[7] = temp_list[7] + 1 # for the found cell, the "coordinate cell" is located at the up-left side
			X[a_3] = temp_list
			temp_list_1 = X[coordinate]
			temp_list_1[3] = temp_list_1[3] + 1
			X[coordinate] = temp_list_1
		if a_4 in X: # if True -> down side cell found
			temp_list = X[a_4]
			temp_list[0] = temp_list[0] + 1 # for the found cell, the "coordinate cell" is located at the up side
			X[a_4] = temp_list
			temp_list_1 = X[coordinate]
			temp_list_1[4] = temp_list_1[4] + 1
			X[coordinate] = temp_list_1
		if a_5 in X: # if True -> down-left side cell found
			temp_list = X[a_5]
			temp_list[1] = temp_list[1] + 1 # for the found cell, the "coordinate cell" is located at the up-left side
			X[a_5] = temp_list
			temp_list_1 = X[coordinate]
			temp_list_1[5] = temp_list_1[5] + 1
			X[coordinate] = temp_list_1
		if a_6 in X: # if True -> left side cell found
			temp_list = X[a_6]
			temp_list[2] = temp_list[2] + 1 # for the found cell, the "coordinate cell" is located at the right side
			X[a_6] = temp_list
			temp_list_1 = X[coordinate]
			print(temp_list_1)
			temp_list_1[6] = temp_list_1[6] + 1
			X[coordinate] = temp_list_1
		if a_7 in X: # if True -> up-left side cell found
			temp_list = X[a_7]
			temp_list[3] = temp_list[3] + 1 # for the found cell, the "coordinate cell" is located at the down-right side
			X[a_7] = temp_list
			temp_list_1 = X[coordinate]
			temp_list_1[7] = temp_list_1[7] + 1
			X[coordinate] = temp_list_1

	if player_labell == 'O':
		coordinate = str(coordinate)
		a = int(coordinate[0])
		insert_index= int(coordinate[1])
		coordinate = int(coordinate)
		if a - 1 >= 0:
			a_0 = int(str(a-1) + str(insert_index))
			a_1 = int(str(a-1) + str(insert_index+1))
		if insert_index - 1 >= 0:
			a_5 = int(str(a+1) + str(insert_index-1))
			a_6 = int(str(a) + str(insert_index-1))
		if a - 1 >= 0 and insert_index - 1 >= 0:
			a_7 = int(str(a-1) + str(insert_index-1))
		a_2 = int(str(a) + str(insert_index+1))
		a_3 = int(str(a+1) + str(insert_index+1))
		a_4 = int(str(a+1) + str(insert_index))
		if a_0 in O:
			temp_list = O[a_0]
			temp_list[4] = temp_list[4] + 1
			O[a_0] = temp_list
			temp_list_1 = O[coordinate]
			temp_list_1[0] = temp_list_1[0] + 1
			O[coordinate] = temp_list_1
		if a_1 in O:
			temp_list = O[a_1]
			temp_list[5] = temp_list[5] + 1
			O[a_1] = temp_list
			temp_list_1 = O[coordinate]
			temp_list_1[1] = temp_list_1[1] + 1
			O[coordinate] = temp_list_1
		if a_2 in O:
			temp_list = O[a_2]
			temp_list[6] = temp_list[6] + 1
			O[a_2] = temp_list
			temp_list_1 = O[coordinate]
			temp_list_1[2] = temp_list_1[2] + 1
			O[coordinate] = temp_list_1
		if a_3 in O:
			temp_list = O[a_3]
			temp_list[7] = temp_list[7] + 1
			O[a_3] = temp_list
			temp_list_1 = O[coordinate]
			temp_list_1[3] = temp_list_1[3] + 1
			O[coordinate] = temp_list_1
		if a_4 in O:
			temp_list = O[a_4]
			temp_list[0] = temp_list[0] + 1
			O[a_4] = temp_list
			temp_list_1 = O[coordinate]
			temp_list_1[4] = temp_list_1[4] + 1
			O[coordinate] = temp_list_1
		if a_5 in O:
			temp_list = O[a_5]
			temp_list[1] = temp_list[1] + 1
			O[a_5] = temp_list
			temp_list_1 = O[coordinate]
			temp_list_1[5] = temp_list_1[5] + 1
			O[coordinate] = temp_list_1
		if a_6 in O:
			temp_list = O[a_6]
			temp_list[2] = temp_list[2] + 1
			O[a_6] = temp_list
			temp_list_1 = O[coordinate]
			temp_list_1[6] = temp_list_1[6] + 1
			O[coordinate] = temp_list_1
		if a_7 in O:
			temp_list = O[a_7]
			temp_list[3] = temp_list[3] + 1
			O[a_7] = temp_list
			temp_list_1 = O[coordinate]
			temp_list_1[7] = temp_list_1[7] + 1
			O[coordinate] = temp_list_1

	if player_labell == 'V':
		coordinate = str(coordinate)
		a = int(coordinate[0])
		insert_index= int(coordinate[1])
		coordinate = int(coordinate)
		if a - 1 >= 0:
			a_0 = int(str(a-1) + str(insert_index))
			a_1 = int(str(a-1) + str(insert_index+1))
		if insert_index - 1 >= 0:
			a_5 = int(str(a+1) + str(insert_index-1))
			a_6 = int(str(a) + str(insert_index-1))
		if a - 1 >= 0 and insert_index - 1 >= 0:
			a_7 = int(str(a-1) + str(insert_index-1))
		a_2 = int(str(a) + str(insert_index+1))
		a_3 = int(str(a+1) + str(insert_index+1))
		a_4 = int(str(a+1) + str(insert_index))
		if a_0 in V:
			temp_list = V[a_0]
			temp_list[4] = temp_list[4] + 1
			V[a_0] = temp_list
			temp_list_1 = V[coordinate]
			temp_list_1[0] = temp_list_1[0] + 1
			V[coordinate] = temp_list_1
		if a_1 in V:
			temp_list = V[a_1]
			temp_list[5] = temp_list[5] + 1
			V[a_1] = temp_list
			temp_list_1 = V[coordinate]
			temp_list_1[1] = temp_list_1[1] + 1
			V[coordinate] = temp_list_1
		if a_2 in V:
			temp_list = V[a_2]
			temp_list[6] = temp_list[6] + 1
			V[a_2] = temp_list
			temp_list_1 = V[coordinate]
			temp_list_1[2] = temp_list_1[2] + 1
			V[coordinate] = temp_list_1
		if a_3 in V:
			temp_list = V[a_3]
			temp_list[7] = temp_list[7] + 1
			V[a_3] = temp_list
			temp_list_1 = V[coordinate]
			temp_list_1[3] = temp_list_1[3] + 1
			V[coordinate] = temp_list_1
		if a_4 in V:
			temp_list = V[a_4]
			temp_list[0] = temp_list[0] + 1
			V[a_4] = temp_list
			temp_list_1 = V[coordinate]
			temp_list_1[4] = temp_list_1[4] + 1
			V[coordinate] = temp_list_1
		if a_5 in V:
			temp_list = V[a_5]
			temp_list[1] = temp_list[1] + 1
			V[a_5] = temp_list
			temp_list_1 = V[coordinate]
			temp_list_1[5] = temp_list_1[5] + 1
			V[coordinate] = temp_list_1
		if a_6 in V:
			temp_list = V[a_6]
			temp_list[2] = temp_list[2] + 1
			V[a_6] = temp_list
			temp_list_1 = V[coordinate]
			temp_list_1[6] = temp_list_1[6] + 1
			V[coordinate] = temp_list_1
		if a_7 in V:
			temp_list = V[a_7]
			temp_list[3] = temp_list[3] + 1
			V[a_7] = temp_list
			temp_list_1 = V[coordinate]
			temp_list_1[7] = temp_list_1[7] + 1
			V[coordinate] = temp_list_1

	if player_labell == 'H':
		coordinate = str(coordinate)
		a = int(coordinate[0])
		insert_index= int(coordinate[1])
		coordinate = int(coordinate)
		if a - 1 >= 0:
			a_0 = int(str(a-1) + str(insert_index))
			a_1 = int(str(a-1) + str(insert_index+1))
		if insert_index - 1 >= 0:
			a_5 = int(str(a+1) + str(insert_index-1))
			a_6 = int(str(a) + str(insert_index-1))
		if a - 1 >= 0 and insert_index - 1 >= 0:
			a_7 = int(str(a-1) + str(insert_index-1))
		a_2 = int(str(a) + str(insert_index+1))
		a_3 = int(str(a+1) + str(insert_index+1))
		a_4 = int(str(a+1) + str(insert_index))
		if a_0 in H:
			temp_list = H[a_0]
			temp_list[4] = temp_list[4] + 1
			H[a_0] = temp_list
			temp_list_1 = H[coordinate]
			temp_list_1[0] = temp_list_1[0] + 1
			H[coordinate] = temp_list_1
		if a_1 in H:
			temp_list = H[a_1]
			temp_list[5] = temp_list[5] + 1
			H[a_1] = temp_list
			temp_list_1 = H[coordinate]
			temp_list_1[1] = temp_list_1[1] + 1
			H[coordinate] = temp_list_1
		if a_2 in H:
			temp_list = H[a_2]
			temp_list[6] = temp_list[6] + 1
			H[a_2] = temp_list
			temp_list_1 = H[coordinate]
			temp_list_1[2] = temp_list_1[2] + 1
			H[coordinate] = temp_list_1
		if a_3 in H:
			temp_list = H[a_3]
			temp_list[7] = temp_list[7] + 1
			H[a_3] = temp_list
			temp_list_1 = H[coordinate]
			temp_list_1[3] = temp_list_1[3] + 1
			H[coordinate] = temp_list_1
		if a_4 in H:
			temp_list = H[a_4]
			temp_list[0] = temp_list[0] + 1
			H[a_4] = temp_list
			temp_list_1 = H[coordinate]
			temp_list_1[4] = temp_list_1[4] + 1
			H[coordinate] = temp_list_1
		if a_5 in H:
			temp_list = H[a_5]
			temp_list[1] = temp_list[1] + 1
			H[a_5] = temp_list
			temp_list_1 = H[coordinate]
			temp_list_1[5] = temp_list_1[5] + 1
			H[coordinate] = temp_list_1
		if a_6 in H:
			temp_list = H[a_6]
			temp_list[2] = temp_list[2] + 1
			H[a_6] = temp_list
			temp_list_1 = H[coordinate]
			temp_list_1[6] = temp_list_1[6] + 1
			H[coordinate] = temp_list_1
		if a_7 in H:
			temp_list = H[a_7]
			temp_list[3] = temp_list[3] + 1
			H[a_7] = temp_list
			temp_list_1 = H[coordinate]
			temp_list_1[7] = temp_list_1[7] + 1
			H[coordinate] = temp_list_1

	if player_labell == 'M':
		coordinate = str(coordinate)
		a = int(coordinate[0])
		insert_index= int(coordinate[1])
		coordinate = int(coordinate)
		if a - 1 >= 0:
			a_0 = int(str(a-1) + str(insert_index))
			a_1 = int(str(a-1) + str(insert_index+1))
		if insert_index - 1 >= 0:
			a_5 = int(str(a+1) + str(insert_index-1))
			a_6 = int(str(a) + str(insert_index-1))
		if a - 1 >= 0 and insert_index - 1 >= 0:
			a_7 = int(str(a-1) + str(insert_index-1))
		a_2 = int(str(a) + str(insert_index+1))
		a_3 = int(str(a+1) + str(insert_index+1))
		a_4 = int(str(a+1) + str(insert_index))
		if a_0 in M:
			temp_list = M[a_0]
			temp_list[4] = temp_list[4] + 1
			M[a_0] = temp_list
			temp_list_1 = M[coordinate]
			temp_list_1[0] = temp_list_1[0] + 1
			M[coordinate] = temp_list_1
		if a_1 in M:
			temp_list = M[a_1]
			temp_list[5] = temp_list[5] + 1
			M[a_1] = temp_list
			temp_list_1 = M[coordinate]
			temp_list_1[1] = temp_list_1[1] + 1
			M[coordinate] = temp_list_1
		if a_2 in M:
			temp_list = M[a_2]
			temp_list[6] = temp_list[6] + 1
			M[a_2] = temp_list
			temp_list_1 = M[coordinate]
			temp_list_1[2] = temp_list_1[2] + 1
			M[coordinate] = temp_list_1
		if a_3 in M:
			temp_list = M[a_3]
			temp_list[7] = temp_list[7] + 1
			M[a_3] = temp_list
			temp_list_1 = M[coordinate]
			temp_list_1[3] = temp_list_1[3] + 1
			M[coordinate] = temp_list_1
		if a_4 in M:
			temp_list = M[a_4]
			temp_list[0] = temp_list[0] + 1
			M[a_4] = temp_list
			temp_list_1 = M[coordinate]
			temp_list_1[4] = temp_list_1[4] + 1
			M[coordinate] = temp_list_1
		if a_5 in M:
			temp_list = M[a_5]
			temp_list[1] = temp_list[1] + 1
			M[a_5] = temp_list
			temp_list_1 = M[coordinate]
			temp_list_1[5] = temp_list_1[5] + 1
			M[coordinate] = temp_list_1
		if a_6 in M:
			temp_list = M[a_6]
			temp_list[2] = temp_list[2] + 1
			M[a_6] = temp_list
			temp_list_1 = M[coordinate]
			temp_list_1[6] = temp_list_1[6] + 1
			M[coordinate] = temp_list_1
		if a_7 in M:
			temp_list = M[a_7]
			temp_list[3] = temp_list[3] + 1
			M[a_7] = temp_list
			temp_list_1 = M[coordinate]
			temp_list_1[7] = temp_list_1[7] + 1
			M[coordinate] = temp_list_1

#checking for the winnings
def checking():
	for key in X: # every entered coordinate by the player with X label
		win_count = 0
		win_count_e = 0
		key_list = X[key]
		key = str(key)
		u_r = int(key[0])
		s_c = int(key[1])
		key = int(key)

		# checking for 4 consecutive cells(up)
		if key_list[0] == 1:
			if u_r - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in X:
						win_count = win_count + 1
					else:
						win_count = win_count
		# checking for 4 consecutive cells(up-right)
		if key_list[1] == 1:
			if u_r - 3 >= 0 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in X:
						win_count = win_count + 1
					else:
						win_count = win_count
		# checking for 4 consecutive cells(right)
		if key_list[2] == 1:
			if  s_c + 3 <= column_size - 1:
				for e in range(3):
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in X:
						win_count = win_count + 1
					else:
						win_count = win_count
		# checking for 4 consecutive cells(down-right)
		if key_list[3] == 1:
			if u_r + 3 <= 5 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in X:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		# checking for 4 consecutive cells(down)
		if key_list[4] == 1:
			if u_r + 3 <= 5:
				for e in range(3):
					u_r = u_r + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in X:
						win_count = win_count + 1
					else:
						win_count = win_count
		# checking for 4 consecutive cells(down-left)
		if key_list[5] == 1:
			if u_r + 3 <= 5 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in X:
						win_count = win_count + 1
					else:
						win_count = win_count
		# checking for 4 consecutive cells(left)
		if key_list[6] == 1:
			if s_c - 3 >= 0:
				for e in range(3):
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in X:
						win_count = win_count + 1
					else:
						win_count = win_count
		# checking for 4 consecutive cells(up-left)
		if key_list[7] == 1:
			if u_r - 3 >= 0 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in X:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		if win_count >= 4:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()
		if win_count_e >= 3:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()

	for key in O:
		win_count = 0
		win_count_e = 0
		key_list = O[key]
		key = str(key)
		u_r = int(key[0])
		s_c = int(key[1])
		key = int(key)
		if key_list[0] == 1:
			if u_r - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in O:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[1] == 1:
			if u_r - 3 >= 0 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in O:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[2] == 1:
			if  s_c + 3 <= column_size - 1:
				for e in range(3):
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in O:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[3] == 1:
			if u_r + 3 <= 5 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in O:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		if key_list[4] == 1:
			if u_r + 3 <= 5:
				for e in range(3):
					u_r = u_r + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in O:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[5] == 1:
			if u_r + 3 <= 5 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in O:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[6] == 1:
			if s_c - 3 >= 0:
				for e in range(3):
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in O:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[7] == 1:
			if u_r - 3 >= 0 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in O:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		if win_count >= 4:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()
		if win_count_e >= 3:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()

	for key in V:
		win_count = 0
		key_list = V[key]
		key = str(key)
		u_r = int(key[0])
		s_c = int(key[1])
		key = int(key)
		if key_list[0] == 1:
			if u_r - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in V:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[1] == 1:
			if u_r - 3 >= 0 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in V:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[2] == 1:
			if  s_c + 3 <= column_size - 1:
				for e in range(3):
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in V:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[3] == 1:
			if u_r + 3 <= 5 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in V:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		if key_list[4] == 1:
			if u_r + 3 <= 5:
				for e in range(3):
					u_r = u_r + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in V:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[5] == 1:
			if u_r + 3 <= 5 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in V:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[6] == 1:
			if s_c - 3 >= 0:
				for e in range(3):
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in V:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[7] == 1:
			if u_r - 3 >= 0 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in V:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		if win_count >= 4:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()
		if win_count_e >= 3:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()

	for key in H:
		win_count = 0
		key_list = H[key]
		key = str(key)
		u_r = int(key[0])
		s_c = int(key[1])
		key = int(key)
		if key_list[0] == 1:
			if u_r - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in H:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[1] == 1:
			if u_r - 3 >= 0 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in H:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[2] == 1:
			if s_c + 3 <= column_size - 1:
				for e in range(3):
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in H:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[3] == 1:
			if u_r + 3 <= 5 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in H:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		if key_list[4] == 1:
			if u_r + 3 <= 5:
				for e in range(3):
					u_r = u_r + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in H:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[5] == 1:
			if u_r + 3 <= 5 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in H:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[6] == 1:
			if s_c - 3 >= 0:
				for e in range(3):
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in H:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[7] == 1:
			if u_r - 3 >= 0 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in H:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		if win_count >= 4:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()
		if win_count_e >= 3:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()

	for key in M:
		win_count = 0
		key_list = M[key]
		key = str(key)
		u_r = int(key[0])
		s_c = int(key[1])
		key = int(key)
		if key_list[0] == 1:
			if u_r - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in M:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[1] == 1:
			if u_r - 3 >= 0 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in M:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[2] == 1:
			if  s_c + 3 <= column_size - 1:
				for e in range(3):
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in M:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[3] == 1:
			if u_r + 3 <= 5 and s_c + 3 <= column_size - 1:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in M:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		if key_list[4] == 1:
			if u_r + 3 <= 5:
				for e in range(3):
					u_r = u_r + 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in X:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[5] == 1:
			if u_r + 3 <= 5 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r + 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in M:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[6] == 1:
			if s_c - 3 >= 0:
				for e in range(3):
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in M:
						win_count = win_count + 1
					else:
						win_count = win_count
		if key_list[7] == 1:
			if u_r - 3 >= 0 and s_c - 3 >= 0:
				for e in range(3):
					u_r = u_r - 1
					s_c = s_c - 1
					key_check = int(str(u_r) + str(s_c))
					if key_check in M:
						win_count_e = win_count_e + 1
					else:
						win_count_e = win_count_e
		if win_count >= 4:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()
		if win_count_e >= 3:
			os.system("clear")
			print('THE MISSION IS COMPLETED!!! Player', player_nameee, 'won!!!')
			board_display(column_size)
			exit()


os.system("clear")
yn_c = 0
while yn_c != 1:
	yn = input("If you want to resize the column(default column size is 7), enter Y(if you don't want, enter whatever):")
	if yn == 'Y':
		column_size_checked = 0
		while column_size_checked != 1:
			try:
				column_size = int(input("Please choose the column size(from 7 to 26): "))
				while 7 > column_size > 26:
					column_size = int(input("Please enter a valid column size(7-26): "))
				if 7 <= column_size <= 26:
					column_size_checked = 1
			except ValueError:
				os.system("clear")
				print("Please enter a valid column size(7-26)")		
		yn_c = 1
	else:
		yn_c = 1	


'''
creating 2 dimensional list(gameboard)
'''
for a in range(7):
	row = []
	for i in range(column_size + 1):
		row.append(' ')
	game_board.append(row)
for a in range(column_size):
	game_board[0][a] = letters[a]

board_display(column_size)


'''
checking for the validity of the entered number of players
'''
yn_cc = 0
while yn_cc != 1:
	ync = input("If you want to change the number of players(by default 2 players), please enter Y(if you don't want, enter whatever): ")
	if ync == 'Y':
		number_players_checked = 0
		while number_players_checked != 1:
			try:
				number_players = int(input("Please enter the number of players(min - 2 players, max - 5 players): "))
				while 2 > number_players > 5:
					number_players = int(input("Please enter a valid number of players(2-5): "))
				if 2 <= number_players <= 5:
					number_players_checked = 1
			except ValueError:
				print("Please enter a valid number of players")	
		yn_cc = 1
	else:
		yn_cc = 1

os.system("clear")
board_display(column_size)

'''
a controlled loop for entering each player's name
'''
for a in range(number_players):
	print(a+1, "Player: ", end = '')
	player_name = input("Please enter your name: ")
	while player_name.strip() == '':
		print(a+1, "Player: ", end = '')
		player_name = input("the name must consist of elements(at least 1): ")
	players_temp.append(player_name)

'''
lines of code for alternating players sequence
'''
r = []
all_players = 0
while all_players != number_players:
	random_num = random.randint(0, number_players - 1)
	while random_num not in r:
		players.append(players_temp[random_num])
		all_players = all_players + 1
		r.append(random_num)
		break



cells = column_size * 6 # maximum number of cells on the board
draw = int(cells / number_players) # maximum number of moves

for i in range(draw+2):
	for f in range(0, number_players):
		d = 0 # this variable stores the number of filled columns
		for a in range(column_size+1):
			if game_board[1][a] != ' ':
				d = d + 1 # if all the columns are filled, the game ends in a draw
			if d == column_size:
				os.system("clear")
				print('DRAW...')
				board_display(column_size)
				exit()
		os.system('clear')
		board_display(column_size)
		player_nameee = player_namee(f)
		player_labell = player_label(f)
		print('Player',player_nameee + '(' + player_labell + ')', end = ' ')
		insert = input("choose the column(A, B, ...): ")

		'''
		lines of code to check the correctness of the entered column letter
		'''
		while insert not in letters:
			print('Player',player_nameee + '(' + player_labell + ')', end = ' ')
			insert = input("enter a valid column letter: ")
		insert_index_ = letters.index(insert)
		while game_board[1][insert_index_] != ' ':
			insert = input("The column is full, Please choose another column: ")
			while insert not in letters:
				print('Player',player_nameee + '(' + player_labell + ')', end = ' ')
				insert = input("enter a valid column letter: ")
			insert_index_ = letters.index(insert)
		for a_ in range_reverse: # a list with decreasing numbers because the board is filled from the bottom
			if game_board[a_][insert_index_] == ' ':
				player_labell = player_label(f)
				game_board[a_][insert_index_] = player_labell
				player_board(f)
				checking()
				break