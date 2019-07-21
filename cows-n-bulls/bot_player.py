# this program is a bot that plays cows and bulls in the most efficient manner possible

import num_creator as nc

# creates the special 4-digit number that the user will be trying to guess
special_number = nc.num_creator()

# this function algorithmically formulates a new guess on each iteration of the 
# program
def guesser():

# loop to provoke guesses from user
while True:

	guess = guesser()
	# checks win condition
	if str(special_number) == guess:
		print("You guessed the special number!")
		break
	
	# makes sure that the guess is 4 digits and if it's not it asks for another guess
	if len(guess) != 4:
		print("Enter a *4* digit number! ")
		continue

	cows = 0
	bulls = 0
	
	# finds how many cows there are
	#	(right number right position)
	for i in range(len(guess)):
		if special_number[i] == guess[i]:
			cows += 1

	# finds how many bulls there are
	# 	(right number wrong position)
	for digit in guess:
		if digit in special_number:
				bulls += 1
	
	# decides the plurality of the words that are printed after a guess
	if cows == 1:
		cow_word = "cow"
	else:
		cow_word = "cows"
	if bulls == 1:
		bull_word = "bull"
	else:
		bull_word = "bulls"

	# prints neccessary game information after each turn
	print(str(cows),cow_word, ",", str(bulls),bull_word)
