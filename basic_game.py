board = ["X"," ","X"," "," "," "," "," "," "]
winning_board_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


def print_board():
	print(board[0:3])
	print(board[3:6])
	print(board[6:9])

def cats_game():
	return " " not in board

# This does not include, mark since player board positions
def player_has_winning_position(player_board_positions):
	for winning_combo in winning_board_combinations:
		if set(winning_combo).issubset(set(player_board_positions)):
			return True
	return False

def territory_held_by_player(player_mark):
	player_territory = []
	for index,board_mark in enumerate(board):
		if board_mark == player_mark:
			player_territory.append(index)
	return player_territory
	
def winning_move(index,mark):
	hypothetical_board = territory_held_by_player(mark) + [index]
	return player_has_winning_position(hypothetical_board)

def forking_move(index,mark):
	winningMoves = 0
	hypothetical_board = territory_held_by_player(mark) + [index]
	for index in range(0, 9):
		if player_has_winning_position(hypothetical_board + [index]) and board[index] == " ":
			winningMoves +=1
	return winningMoves >= 2
	

    
    
def get_user_move():
	print("Please enter your desired move location")
	return int(input())
	
def commit_move(index,mark):
	if board[index] == " ":
		board[index] = mark

print_board()
print(forking_move(4,"X"))