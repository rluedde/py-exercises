# second solution for 5 - except with a list comprehension
# all of this code is probably doable with a single list comprehension

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# loops through a and b lists and if there is overlap, it is appended to common_list
common_list = [number_a for number_a in a for number_b in b if (number_b == number_a)]

# removes dupes - probably doable with another list comprehension
for number in common_list:
	if common_list.count(number) > 1:
		common_list.remove(number)

print(common_list)