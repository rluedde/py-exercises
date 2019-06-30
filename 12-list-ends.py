# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

# this script randomly generates a list of random length between 2 and 10 and 
# the ncreates a list of the first and last elements from the randomly generated 
# list

import random as r

# how long the list of random numbers will be
list_length = r.randint(2,10)

# creates list of random elements and list of first and last elements from that list
def random_list():
	# creates list of random elements
	elements = [r.randint(1,100) for i in range(list_length)]
	# creates list with first and last elements of list elements
	final_list = [elements[0],elements[-1]]
	print(elements, final_list)

random_list()

