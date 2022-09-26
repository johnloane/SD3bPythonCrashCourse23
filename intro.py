import copy
from math import ceil

# region Arithmetic Operators
print("Hello, World")
print(1 + 1)
print(1 - 1)
print(5 * 10)
print(13 / 2)
print(13//2)
print(((6+9)*3)+3)
print(7 % 2)
print(6 ^ 2)
# ** means raise to the power of
print(6 ** 2)
# endregion

# region Mutable
a = 1
b = a
a = "Hello, World"

print(b)
print(a)

a = 1
b = a
a = a - 1
print(a)
print(b)

# Lists are mutable data structures
list_1 = [1, 2, 3]
list_2 = list_1
list_2 = [4, 5, 6]

list_1 = [1, 2, 3]
list_2 = list_1
list_1[0] = 100
print(list_2)
# endregion

# region Shallow and Deep Copies
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = [a, b]
d = copy.copy(c)
a[0] = -1
c[0][1] = -3
print(d)

# Deep Copy
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = [a, b]
d = copy.deepcopy(c)
a[0] = -1
c[0][1] = -3
print(d)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a == c)
print(a is b)
print(a is c)

# Numeric data types
x = 7
y = 3
z = x/y
print(z)
print(type(z))
print(ceil(3.7))
print(round(7.778, 2))

# endregion

# region Strings
name = 'Sergej'
dialog = 'Sergej said "Hello World" and the world said "You\'re the best Sergej"'
print(dialog)

string_1 = "Hello"
string_2 = " How are you?"
full_sentence = string_1 + string_2
print(full_sentence*10)
print(len(full_sentence))
# endregion

# region Boolean
dkit_is_the_best = True
dkit_is_not_the_best = False
comparison = 1 > 2
print(comparison)

print(1 < 2 or 2 < 3)
print(1 < 2 or 2 > 3)
print(1 < 2 and 2 > 3)
print(not(1 < 2))

movie_title = "Avengers"
print(movie_title.upper())
print(movie_title.count('A'))

# endregion

names = ["Kasper", "Sergej", "James"]
print(names[0])

random_variables = [True, False, "Hello", 1, 1.2]
print(len(random_variables))

print(random_variables[-1])

ordered_numbers = list(range(0, 101))
print(ordered_numbers)
print(ordered_numbers[-51:])
print(ordered_numbers[:len(ordered_numbers)//2])

print(list(range(501)))
print(list(range(0, 501, 5)))

show_title = "Breaking Bad"
print(show_title[9:12])
words = show_title.split()
print(words[1])

months = ['Jan', 'Feb', 'Mar']
print("Jan" in months)
print("Jun" in months)

course = "Internet of Things"
print('of'.lower() in course.lower())

# region Mutability
grocery_list = ['Bananas', 'Apples', 'Cauliflower']
grocery_list[2] = 'Broccoli'
print(grocery_list)

misspelled_vegetable = "Cucomber"
correctly_spelled_vegetable = "Cucumber"

name = "Liam"
other_name = name
name = "Isaac"
print(name)
print(other_name)

books = ["48 Laws of Power", "How to become a better man", "Rangers apprentice"]
more_books = books
books[0] = "Verity"
print(more_books)

numbers = [1, 3, 5, 7]
print(len(numbers))
print(max(numbers))

names = ["John", "David", "Liam"]
print(max(names))
print(min(names))

print(sorted(names))

random_numbers = [2, 7, 12, 21, 3, 4]
print(sorted(random_numbers))

print('-'.join(['Jan', 'Feb', 'Mar']))
print(' '.join(['Jan', 'Feb', 'Mar']))

print("This person is {}, {} and {}".format('tall', 'thin', 'old'))

months = ['Jan', 'Feb', 'Mar']
months.append('Apr')
print(months)

# endregion

# region Tuples
traits = ('Tall', 'Thin', 24, True)
height = traits[0]
build = traits[1]
age = traits[2]
smoker = traits[3]
print(height, build, age, smoker)

height, build, age, smoker = traits
print(height, build, age, smoker)


# endregion

# region Sets
# Mutable, unordered, contain unique elements
duplicate_numbers = [1, 1, 2, 2, 3, 3]
unique_numbers = set(duplicate_numbers)
print(unique_numbers)
unique_numbers.add(4)
unique_numbers.add(3)
print(2 in unique_numbers)

# endregion

# region Dictionaries
inventory = {'bananas': 1.49, 'braeburnapples': 2.99, 'grapes': 3.99}
print(inventory['bananas'])
inventory['bananas'] = 1.29
print(inventory['bananas'])

bananas_price = inventory.get('bananas')
strawberries_price = inventory.get('strawberries')
print(strawberries_price)

print('strawberries' in inventory)

grocery_items = {'bananas': {'price': 1.29, 'country_of_origin': 'Brazil'}}
print(grocery_items['bananas']['price'])
# endregion

item = 'cabbage'
price = 0.79
if item in grocery_items:
    print("Found the ", item)
elif price > 3.99:
    print("Too expensive for us")
else:
    print("Not found")
    grocery_items.update({item : {'price': 0.79, 'country_of_origin': 'Ireland'}})

print(grocery_items)

# For loop
months = ['Jan', 'Feb', 'Mar']
for month in months:
    print(month)

for number in range(0, 100):
    print(number)

names = ['terence', 'jeremy', 'yue xing']
for index in range(len(names)):
    names[index] = names[index].istitle()
print(names)

movies = {"Avengers": 2012, "John Wick": 2014, "The Matrix": 1999}
for key in movies:
    print(key)

for key, value in movies.items():
    print(f"The movie {key}, was released in {value}")

random_number = 20
while random_number < 31:
    print(random_number)
    random_number += 1

numbers = list(range(0, 10))
for number in numbers:
    if number % 2 == 0:
        break
    print(number)

# region Functions


def square(n):
    return n*n


print(square(10))
the_best_student = 'Clinton'

def random_function():
    print(the_best_student)

random_function()
print(the_best_student)
# endregion

# region Doc Strings

"""
    INPUT: width, length
    OUTPUT: area 
"""


def rectangle_area(width, length):
    return width*length


# endregion

# region Higher Order Functions and Lambdas
numbers = [1, 2, 3, 4, 5]
numbers_r = list(range(1, 6))
print(numbers)
print(numbers_r)


def even_or_odd(number):
    return number % 2 == 0


print(list(filter(even_or_odd, numbers)))

# Lambda, anonymous function, used once

print(list(filter(lambda number: number % 2 == 0, numbers)))


# endregion
