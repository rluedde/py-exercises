# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

# the following list comprehension adds put all even elements from a into a new list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_elements = [number for number in a if number % 2 == 0]

print(even_elements)