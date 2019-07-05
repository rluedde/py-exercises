# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

# this script defines two functions: list_creator returns a random list of either strings or integers and
# dupe_remover removes any duplicates from the list that list_creator returns

import random, string

# returns a list of random elements
def list_creator(strings_or_integers):
	random_list = []
	list_length = random.randint(1,100) 
	
	# creates list of list_length integers
	if strings_or_integers == "I":
		random_list = [random.randint(1,500) for x in range(list_length)]
	
	# creates list of list_length strings of length 2
	elif strings_or_integers == "S":
		lowercase_letters = string.ascii_lowercase

		# creates list_length words and appends them to random_list
		for i in range(list_length):
			random_string = []
			
			# creates a random string of string_length length
			string_length = 2
			for i in range(string_length):
				letter = random.choice(lowercase_letters)
				random_string.append(letter) 
			random_list.append("".join(random_string))
	print(len(random_list))
	return random_list

# takes a list potentially with duplicate elements and returns a list
# without any duplicates

def dupe_remover(list_with_dupes):
	list_without_dupes = []
	for thing in list_with_dupes:
		if thing not in list_without_dupes:
			list_without_dupes.append(thing)
	print(len(list_without_dupes))
	return list_without_dupes


list_with_dupes = list_creator("S")
list_without_dupes = dupe_remover(list_with_dupes)

# question I am going to look into: how does the distribution of integer lists change when dupes are 
# removes versus kept
# how to go about this: create a histogram of the random list before dupe removal and after dupe removal
# (not much else to really do to answer this question)