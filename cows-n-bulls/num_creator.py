# this script creates and formats the special number for cows n bulls

import random

# object that represents a guess. when the bot_player.game_flow() is called, the guess object will
# have the cows and bulls attribute updated and the whole object will be store somewhere
class Guess:

	def __init__(self,first,second,third,fourth):	
		self.first = first
		self.second = second
		self.third = third
		self.fourth = fourth
		self.cows = 0
		self.bulls = 0

	def __repr__(self):
		return("".join([self.first,self.second,self.third,self.fourth]) + "\n" + "cows: " + str(self.cows) + "\n"
			"bulls: " + str(self.bulls))

	def to_string(self):
		return("".join([self.first,self.second,self.third,self.fourth]))

def num_creator():
	# number that user is trying to guess 
	# this range allows for all possible numbers that can be convted into 4 digits (or already are)
	while True:	
		special_number = str(random.randint(1,9999))

		# these if statements make non 4-digit numbers into 4 digit numbers
		# ex. if the number generated is 2 then it will be converted into 0002 so 
		# it's still playable
		if len(special_number) == 3:
			special_number = "0" + str(special_number)
		elif len(special_number)== 2:
			special_number = "00" + str(special_number)
		elif len(special_number)== 1:
			special_number = "000" + str(special_number)
		
		# makes sure that there are no repeated digits (this code works for sure)
		if len(list(special_number)) != len(set(list(special_number))):
			continue
		else:
			break
	return(Guess(special_number[0],special_number[1],special_number[2],special_number[3]))

g1 = num_creator()

print(g1.to_string())