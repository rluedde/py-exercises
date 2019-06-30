# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random as r

number = r.randint(1,9)

while True:
	guess = int(input("Enter a number between 0 and 10 (not including 0 and 10): "))

	# tells the user the relationship of their guess to the random number
	if guess == number:
		print("You guessed it!")
		break
	elif guess > number:
		print("You guessed too high, guess again!")
		continue
	elif guess < number:
		print("You guessed too low, guess again!")
		continue
	elif guess == "exit":
		break
