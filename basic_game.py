# Basic Prototype of how Tic Tac Toe works

board = [" "," "," "," "," "," "," "," "," "]
def print_board():
	print(board[0:3])
	print(board[3:6])
	print(board[6:9])
	
def has_player_won(player_board_positions):
	winning_board_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	for winning_combo in winning_board_combinations:
		if set(winning_combo).issubset(set(player_board_positions)):
			return True
	return False
		
def player_board_indexes(mark):
	player_territory = []
	for index,board_mark in enumerate(board):
		if board_mark == mark:
			player_territory.append(index)
	return player_territory
	
def get_user_move():
	print("Please enter your desired move location")
	return int(input())
	
def commit_move(index,mark):
	if board[index] == " ":
		board[index] = mark

while True:
	if has_player_won(player_board_indexes("X")):
		print("X has won!")
		break
	if has_player_won(player_board_indexes("O")):
		print("O has won!")
		break
	if " " not in board:
		print("Cat's Game!")
		break
	print_board()
	commit_move(get_user_move(),"X")
	commit_move(get_user_move(),"O")
	