# this program is a bot that plays cows and bulls in the most efficient manner possible

from num_creator import Guess, num_creator

# creates an instance of the Guess class (from num_creator.py)
special_number = num_creator()

# while loop that does all game actions:
# takes a Guess and returns the Guess but with cows and bulls
def game_flow():
	# default guess for initial pre-algorithm purposes
	guess = Guess(0,1,2,3)
	# creates the special 4-digit number that the user will be trying to guess
	special_number = num_creator()
	while True:
		# checks win condition
		if special_number == guess:
			print("You guessed the special number!")
			break

		# finds how many cows (right number right position) and bulls (right number wrong position)
		# there are in the guess
		# makes the guess and special_number objects into strings so indexing can be used
		string_special_number = special_number.to_string()
		string_guess = guess.to_string()

		for i in range(len(string_special_number)):
			if string_special_number[i] == string_guess[i]:
				guess.cows += 1
			elif (string_guess[i] in string_special_number) and (string_guess[i] != string_special_number[i]):
				guess.bulls += 1
		break
	return guess


# test code
something = game_flow()

print(something)



