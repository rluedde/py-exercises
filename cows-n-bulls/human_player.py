# here's the project link: https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

# this script allows a HUMAN player to play cows n bulls - which is a numerical version of Mastermind
import num_creator as nc

# creates the special 4-digit number that the user will be trying to guess
special_number = nc.num_creator()

# loop to provoke guesses from user
while True:
	guess = input("Enter a 4-digit number as your guess: ")
	
	try:
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

		# finds if there's duplicated digits in the special_number
		# game can be REAL frustrating if there is dupes and you don't know
		# something to ossibly come back and try to fix down the line?
		dupe = None
		if len(list(special_number)) != len(set(list(special_number))):
			dupe = True
		else:
			dupe = False
		
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
		print(str(cows),cow_word, ",", str(bulls),bull_word,"\n" + "dupes:",dupe)

	# if an unknown error happens during play (i think i've handled all of the errors though), 
	# this error message pops up
	except:
		print("Something went wrong but here is the number you were after:", special_number)