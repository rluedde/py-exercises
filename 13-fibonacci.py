# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

# this script creates a list of fibonacci number of length specified by user
# input is from the argument passed into the function, not the input() function

def fib_list(amount_fib_nums):
	current_num = 1
	list_nums = [1,1]

	if amount_fib_nums > 1:
		for i in range(amount_fib_nums):
			# need code here to calculate the fibonacci values using indexing
			current_num = list_nums[-1] + list_nums[-2]
			list_nums.append(current_num)
		return list_nums
			
	elif amount_fib_nums == 0:
		list_nums = []
		return list_nums

	else:
		list_nums = [1]
		return list_nums

print(fib_list(8))

