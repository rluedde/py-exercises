# original exercise link - https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# make sure to run this program through command prompt and not through the text editor

# this program tells a user in how many days they will turn 100 (assuming all years are 365 days long) 

age = int(input("What is your age? "))
days_into_year = int(input("How many days into the year are we? "))

# calculates the amount of days until user turns 100
days_to_100 = ((100 - age) * 365) - days_into_year

print("you will turn 100 years old in", str(days_to_100), "days.")

