import string,random

lowercase_letters = string.ascii_lowercase

random_word = []
for i in range(5):
	
	random_letter = random.choice(lowercase_letters)
	random_word.append(random_letter)

random_word = "".join(random_word)
print(random_word)