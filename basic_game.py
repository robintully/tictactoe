
from time import sleep
banner = """

\033[1;31;40m        __  __ _                           _____			\033[0m
\033[1;31;40m    ___ \ \/ /| |_  _ _  ___  _ __   ___  |_   _|__ _  __  \033[0m
\033[1;33;40m   / -_) >  < |  _|| '_|/ -_)| '  \ / -_)   | | / _` |/ _| \033[0m
\033[1;32;40m   \___|/_/\_\ \__||_|  \___||_|_|_|\___|   |_| \__,_|\__| \033[0m
\033[1;34;40m                   _____           _  _  _     			\033[0m
\033[1;34;40m                  |_   _|___  ___ | || || |    			\033[0m
\033[1;36;40m                    | | / _ \/ -_)|_||_||_|     			\033[0m
\033[1;35;40m                    |_| \___/\___|(_)(_)(_)				\033[0m

"""

available_spaces = [0,1,2,3,4,5,6,7,8]
human_spaces,computer_spaces = [],[]
winning_board_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Fix invalid literal

def print_board():
	board_display =["| 1 |","| 2 |","| 3 |","| 4 |","| 5 |","| 6 |","| 7 |","| 8 |","| 9 |"]
	for space in human_spaces:
		board_display[space] = "| \033[1;34;40mX\033[0m |"
	for space in computer_spaces:
		board_display[space] = "| \033[1;31;40mO\033[0m |"
	print(''.join(board_display[0:3]),''.join(board_display[3:6]),''.join(board_display[6:9]),	sep='\n ============== \n')
	
def is_winning_position(players_spaces):
	for winning_combo in winning_board_combinations:
		if set(winning_combo).issubset(set(players_spaces)):
			return True
			
def is_forking_move(players_spaces):
	winningMoves = 0
	for space in available_spaces:
		if is_winning_position(players_spaces + [space]):
			winningMoves +=1
	return winningMoves >= 2

def get_computer_move():
	for space in available_spaces:
		if is_winning_position(computer_spaces + [space]):
			return space
	for space in available_spaces:
		if is_winning_position(human_spaces + [space]):
			return space
	for space in available_spaces:
		if is_forking_move(computer_spaces + [space]):
			return space
	player_forks = 0
	for space in available_spaces:
		if is_forking_move(human_spaces + [space]):
			player_forks += 1
			tempMove = space
	if player_forks == 1:
		return tempMove
	elif player_forks == 2:
		for space in [1,3,5,7]:
			if space in available_spaces:
				return space
	for space in [4,0,2,6,8,1,3,5,7]:
		if space in available_spaces:
			return space

def get_user_move():
	print("Select your move")
	user_input = int(input())
	if user_input - 1 in available_spaces:
		return int(user_input) - 1
	else:
		return get_user_move()

def commit_move(players_spaces,index):
		available_spaces.remove(index)
		players_spaces.append(index)
		
def is_game_over(players_spaces):
	if is_winning_position(players_spaces) or not available_spaces:
		return True
		
def clearscreen(numlines=5):
    import os
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    else:
        print ('\n')* numlines


print(banner)
sleep(2)
while True:
	clearscreen()
	print_board()
	commit_move(human_spaces,get_user_move())
	if is_game_over(human_spaces):
		print("Game Over")
		break
	commit_move(computer_spaces,get_computer_move())	
	if is_game_over(computer_spaces):
		print("Game Over")
		break
