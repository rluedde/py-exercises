# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

# this script asks the user for a string (with multiple words) and then returns the 
# words organized in reverse order (the individual words themselves are still normal though)

# my name is rei -> rei is name my

user_input = input("enter a string that you want backwards: ")

def reverse(string_to_reverse):
	list_to_reverse = string_to_reverse.split(" ")
	reverse_list = []
	for i in range(len(list_to_reverse)):
		reverse_list.append(list_to_reverse[-(i + 1)])
	return ' '.join(reverse_list)

print(reverse(user_input))

