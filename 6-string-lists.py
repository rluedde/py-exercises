# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

# checks if a user-entered string is a palindrome

entry = input("enter a word to see if it is a palindrome: ")

# checks to see if entry is a palindrome
def is_palindrome(word):
	word_list = list(word)
	
	# creates a backward version of the input to check palindromeness
	reverse_word_list = list(word)
	reverse_word_list.reverse()
	
	if word_list == reverse_word_list:
		print("input is a palindrome!")
	else:
		print('input is NOT a palindrome!')

is_palindrome(entry)