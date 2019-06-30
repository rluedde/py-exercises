# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

# function returns whether or not a number is prime
def is_prime():
	number = int(input("Enter a number that you want to check the primality of: "))

	for i in range(2,number):
		divisor = number % i
		if divisor == 0:
			return("Number is NOT prime")

	return("Number IS prime")

print(is_prime())
