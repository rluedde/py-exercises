# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

less_than_5 = [number for number in my_list if number < 5]

print(less_than_5)