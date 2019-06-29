# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

# script asks a user for a number and finds all valid divisors of the number

print("script is working")
try:
	number = int(input("Enter a number that you want to find the divisors of: "))
except ValueError:
	print("Re-run the script and enter a valid number")


list_divisors = []

# look if number can be divided by 2 so the script can work more efficiently
# 	may have to add 1 to number because of the 0 indexing
for i in range(1,number):
	if number % i == 0:
		list_divisors.append(i)
		print(i)

print(list_divisors)
