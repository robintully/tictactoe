from time import sleep
import os
from random import shuffle

banner = """

\033[1;31m        __  __ _                           _____			\033[0m
\033[1;31m    ___ \ \/ /| |_  _ _  ___  _ __   ___  |_   _|__ _  __  \033[0m
\033[1;33m   / -_) >  < |  _|| '_|/ -_)| '  \ / -_)   | | / _` |/ _| \033[0m
\033[1;32m   \___|/_/\_\ \__||_|  \___||_|_|_|\___|   |_| \__,_|\__| \033[0m
\033[1;34m                   _____           _  _  _     			\033[0m
\033[1;34m                  |_   _|___  ___ | || || |    			\033[0m
\033[1;36m                    | | / _ \/ -_)|_||_||_|     			\033[0m
\033[1;35m                    |_| \___/\___|(_)(_)(_)				\033[0m

"""

available_spaces = [0,1,2,3,4,5,6,7,8]
x_spaces,o_spaces = [],[]
winning_board_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def start_game():
	print(banner)
	sleep(2)
	user_input = select_players()
	if user_input == 1:
		player_one,player_two = "human","human"
	if user_input == 2:
		player_one,player_two = "human","computer"
	if user_input ==3:
		player_one,player_two = "computer","human"
	while True:
		clearscreen()
		print_board()
		if player_one == "human":
			commit_move(x_spaces,get_user_move())
		else:
			commit_move(x_spaces,get_computer_move(x_spaces,o_spaces))
		if is_game_over(x_spaces):
			declare_winner()
			break
		clearscreen()
		print_board()
		if player_two == "human":
			commit_move(o_spaces,get_user_move())
		else:
			commit_move(o_spaces,get_computer_move(o_spaces,x_spaces))
		if is_game_over(o_spaces):
			declare_winner()
			break

def select_players():
	clearscreen()
	print("""
	\033[1;31m  Select From the Following \033[0m
	\033[1;33m  1. Play Another Human \033[0m
	\033[1;32m  2. Go first Against the Computer \033[0m 
	\033[1;34m  3. Go Second against the Computer \033[0m
	""")
	try:
		user_input = int(input())
		if user_input in [1,2,3]:
			return user_input
		return select_players()
	except ValueError:
		return select_players()

def clearscreen():
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    else:
        print ('\n')* 5

def print_board():
	board_display =["| 1 |","| 2 |","| 3 |","| 4 |","| 5 |","| 6 |","| 7 |","| 8 |","| 9 |"]
	for space in x_spaces:
		board_display[space] = "| \033[1;34;40mX\033[0m |"
	for space in o_spaces:
		board_display[space] = "| \033[1;31;40mO\033[0m |"
	print(''.join(board_display[0:3]),''.join(board_display[3:6]),''.join(board_display[6:9]),	sep='\n ============== \n')

def commit_move(players_spaces,index):
		available_spaces.remove(index)
		players_spaces.append(index)
	
def get_user_move():
	try:
		print("Select your move")
		selected_space = int(input()) - 1  
		if selected_space in available_spaces:
			return selected_space
		return get_user_move()
	except ValueError:
		print("That's not an integer")
		return get_user_move()

def get_computer_move(computer_spaces,players_spaces):
	for space in available_spaces:
		if is_winning_position(computer_spaces + [space]):
			return space
	for space in available_spaces:
		if is_winning_position(players_spaces + [space]):
			return space
	for space in available_spaces:
		if is_forking_move(computer_spaces + [space]):
			return space
	player_forks = 0
	for space in available_spaces:
		if is_forking_move(players_spaces + [space]):
			player_forks += 1
			tempMove = space
	if player_forks == 1:
		return tempMove
	elif player_forks == 2:
		for space in [1,3,5,7]:
			if space in available_spaces:
				return space
	for space in random_order_moves():
		if space in available_spaces:
			return space

def random_order_moves():
	corners = [0,2,6,8]
	sides = [1,3,5,7]
	shuffle(sides)
	shuffle(corners)
	return [4] + corners + sides


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

def is_game_over(players_spaces):
	if is_winning_position(players_spaces) or not available_spaces:
		return True

def declare_winner():
	clearscreen()
	print_board()
	if is_winning_position(x_spaces):
		print ("\033[1;34;40mX has won!\033[0m")
	elif is_winning_position(o_spaces):
		print ("\033[1;31;40mO has won!\033[0m")
	elif not available_spaces:
		print ("Tie Game!")
		
start_game()