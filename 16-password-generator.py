# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

# this function generates passwords of varying, user-defined strengths

import random, string

# uncomment me out for final copy
# length = input("how many characters long should the password be?")
# strength = input("Aa123, Aa, a")

def passwordGenerator(length = input("how many characters long should the password be? "), strength = input("Aa123, Aa, a? ")):
	password = ''
	length = int(length)
	if strength == "Aa123":
		characters = string.ascii_letters + string.digits
		for i in range(length):
			password = password + random.choice(characters)
	elif strength == "Aa":
		characters = string.ascii_letters
		for i in range(length):
			password = password + random.choice(characters)
	else:
		characters = string.ascii_lowercase
		for i in range(length):
			password = password + random.choice(characters)
	
	return password

# this function brute forces the password to "crack it"
# it has to have the password the begin with though lmao 

def bruteForce(password):
	characters = string.ascii_letters + string.digits
	password_answer = ""
	for password_character in password:
		for character in characters:
			if password_character == character:
				password_answer = password_answer + password_character

	print("the password was", password)
	print("the cracked password was", password_answer)

# the arguments for passwordGenerator() are user input so they are not neccessary here

bruteForce(passwordGenerator())