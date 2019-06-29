# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

# this program tells the user whether an entered number is odd or even

number = int(input("Enter a number: "))

if number % 4 == 0:
	print("Your number is divisible by 4 and even!!")
elif number % 2 == 0:
	print("Your number is even but not divisible by 4!! ")
else:
	print("Your number is odd!!!")