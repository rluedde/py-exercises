# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
import sys

# function asks for a number and returns a list of all divisors of the number
def divisor_finder():
	
	# this t&e makes sure that a number is entered and if not, the script stops running
	try:
		number = int(input("Enter a number that you want to find the divisors of: "))
	except ValueError:
		print("Re-run the script and enter a valid number.")
		sys.exit()

	list_divisors = []

	# starts at 1 to avoid dividing by 0
	# finds all divisors of number and appends them to list_divisors
	for i in range(1,number):
		if number % i == 0:
			list_divisors.append(i)
			print(i)

	return(list_divisors)

list_divisors = divisor_finder()

# this following function takes list_divisors and finds what the number originally was
def number_constructor(list_divisors):
	orig_number = list_divisors[1] * list_divisors[-1]
	return("Your original number was " + str(orig_number))

print(number_constructor(list_divisors))


