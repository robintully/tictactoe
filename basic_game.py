# X is Human
# O is Computer
available_spaces = [0,1,2,3,4,5,6,7,8]
x_spaces,o_spaces = [],[]
winning_board_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def print_board():
	board_display = [" "," "," "," "," "," "," "," "," "]
	for space in x_spaces:
		board_display[space] = "X"
	for space in o_spaces:
		board_display[space] = "0"
	print(board_display[0:3])
	print(board_display[3:6])
	print(board_display[6:9])
	print(" ")
	
def commit_move(players_spaces,index):
	if index in available_spaces:
		available_spaces.remove(index)
		players_spaces.append(index)
		
def is_winning_position(players_spaces):
	for winning_combo in winning_board_combinations:
		if set(winning_combo).issubset(set(players_spaces)):
			return True
			
def is_forking_move(fork_space,players_spaces):
	winningMoves = 0
	for space in available_spaces:
		if is_winning_position(players_spaces + [fork_space] + [space]):
			winningMoves +=1
	return winningMoves >= 2
	
def determine_computer_move():
	for space in available_spaces:
		if is_winning_position(o_spaces + [space]):
			return space
	for space in available_spaces:
		if is_winning_position(x_spaces + [space]):
			return space
	for space in available_spaces:
		if is_forking_move(space,o_spaces):
			return space
	player_forks = 0
	for space in available_spaces:
		if is_forking_move(space,x_spaces):
			player_forks += 1
			tempMove = space
	if player_forks == 1:
		return tempMove
	elif player_forks == 2:
		for space in [1,3,5,7]:
			if space in available_spaces:
				return space
	if 4 in available_spaces:
		return 4
	for space in [0,2,6,8]:
		if space in available_spaces:
			return space
	for space in [1,3,5,7]:
		if space in available_spaces:
			return space
			
def get_user_move():
	print("Please enter your desired move location")
	return int(input())
	
while True:
	print_board()
	commit_move(x_spaces,get_user_move())
	if is_winning_position(x_spaces):
		print_board()
		print ("You win!")
		break
	commit_move(o_spaces,determine_computer_move())
	if is_winning_position(o_spaces):
		print_board()
		print ("You lose!")
		break
	


