# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

# this program simulates a game of rock-paper-scissors 

# could add functionality to make sure that whatever is entered is valid but that's easy
# and i'd rather learn other things

p1_wins = 0
p2_wins = 0

# sets up best of 3 RPS game
while p1_wins < 2 and p2_wins < 2: 
	while True:
		# takes each player's decision
		p1_input = input("P1: rock (R), paper (P) or scissors (S)? ")
		p2_input = input("P2: rock (R), paper (P) or scissors (S)? ")

		# checks to see if the players made the same decision
		if p1_input == p2_input:
			print("Each player made the same decision!")
			continue

		# handles all cases if P1 wins
		elif (p1_input == "R" and p2_input == "S") or (p1_input == "P" and p2_input == "R") or (p1_input == "S" and p2_input == "P"):
			print("P1 won once!")
			p1_wins += 1
			break

		# handles all cases if P2 wins
		else:
			print("P2 won once!")
			p2_wins += 1
			break

# prints message of who won the game
if p1_wins == 2:
	print("P1 wins!!")
else:
	print("P2 wins!!")


