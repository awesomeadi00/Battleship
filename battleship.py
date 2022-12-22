import random
import os

SHIP_SIZE = 4
DIMENSION = 10
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
board = [[' ' for i in range(DIMENSION)] for j in range (DIMENSION)] 	#2D List: For each letter, there are 8 digits (0-7)

#================================================================================================================================================
#Print Board: This function will print the board: 
def print_board(lis): 
	#Generates the letters on top for each column
	for let in LETTERS:    
		print('   ' + str(let), end = "")

	#Generates the first grid border below the numbers (repeats it 'DIMENSION' times)
	print("\n +" + "---+" * DIMENSION)

	#Generates bars between each dot for each row and column. Also generates the grid border for each row. 
	for row in range(DIMENSION):    
		print(str(row) + '|', end = " ")
		for col in range(DIMENSION):        
			print(lis[row][col] + ' | ', end = "") 
		print("\n +" + "---+" * DIMENSION)
#================================================================================================================================================
#Board: Function to set up the board
def update_board(cord): 
	#If the program just starts, it will initialize the board
	if(cord == "new"): 
		print_board(board)
	
	#If the input is something else, then it will update the board instead
	else: 
		update_row = int(cord[1])
		update_col = ord(cord[0])-65

		if(cord in cd):
			board[update_row][update_col] = 'X'
			cd.remove(cord)
			print_board(board)

		else: 
			board[update_row][update_col] = '#'
			print_board(board)
#================================================================================================================================================
#Position: Function to randomly place the ships in different positions and orientations of the board:
def position(): 
	#Row and Column will determine the start coordinate of where we will place our ship
	#Orient will determine the orientation. If it is '0' it will be horizontal, if it is '1' it will be vertical
	row = random.randint(0,9)
	column = random.randint(0,9)
	orient = random.randint(0,1)

	#Ships coordinates
	ship_cd = []

	#If the ship is vertical
	if(orient == 1):
		up = 1
		down = 0
		for num in range(SHIP_SIZE):
			if(row+down < DIMENSION and row+down > -1):
				ship_cd.append(chr(column+65)+str(row+down))
				down += 1

			else:
				ship_cd.append(chr(column+65)+str(row-up))
				up += 1


	#If the ship is horizontal
	else: 
		left = 1
		right = 0
		for num in range(SHIP_SIZE):
			if(column+right < DIMENSION and row+right > -1):
				ship_cd.append(chr((column+right)+65)+str(row))
				right += 1

			else:
				ship_cd.append(chr((column-left)+65)+str(row))
				left += 1

	return ship_cd
#================================================================================================================================================
#User Guess: Function to ask the user for a valid guess
def user_guess(): 
	g = input("Enter a coordinate to target (e.g. A1): ")
	if(g == "exit"):
		return("exit")


	while((ord(g[0]) < 65 or ord(g[0]) > 74) or (int(g[1]) < 0 or int(g[1]) > 9) or (not g[1].isdigit())):
		g = input("Invalid Input! Enter a valid coordinate to target (e.g. A1): ")

	return(g)
#================================================================================================================================================

#MAIN CODE: ====================================================================================================================================
print("\n")
print("========================WELCOME TO BATTLESHIP========================")
print("Objective: Find and Destroy the Ship as fast as possible!")

update_board("new")
cd = position()
#print(cd)
guesses = 0

for num in range(DIMENSION*DIMENSION): 
	if(len(cd) == 0):
		break;
	guess = user_guess()
	if(guess == "exit"):
		exit()

	os.system("clear")
	update_board(guess)
	guesses+=1

print("Congrats! You Successfully destoryed the Ship!")
print("Total Points:", (100*SHIP_SIZE)-guesses,"points")
