# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

# script finds commonalities between two lists

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = []

for number_a in a:
	for number_b in b:
		if number_b == number_a and number_a not in common_list:
			common_list.append(number_a)

print(common_list)