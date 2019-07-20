# this script creates and formats the special number for cows n bulls

import random

def num_creator():
	# number that user is trying to guess 
	# this range allows for all possible numbers that can be convted into 4 digits (or already are)
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
	
	return(special_number)
