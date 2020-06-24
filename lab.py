#1 Create 2 variables. Swap them and print their values
a = 2
b = 5
a,b = b,a
print(a); print(b)

# 2. Write an if statement that compares two numbers and prints the larger.
c = 510
d = 9
if c > d:
    print("greater is c")
else:
    print("greater is d")

# 3. Write an if statement that compares two strings and prints the larger.

c = 'abb'
d = 'b'
if len(c) > len(d):
    print("greater is c")
else:
    print("greater is d")

#4  Write for loop that prints even numbers from 1-100
for i in range(101):
    if i % 2 ==0:
        print("the number is even --->", i)

# 5 Rewrite #4 using while loop.

i = 0
while i <= 100:
    if i %2 ==0:
        print("the number is even", i)
    i += 1

# 6 Write a nested loop that print the following pattern:
# ***
# ***
# ***

for i in range(3):
    print("*", end='')
    for j in range(2):
        print('*', end='')
    print("\n")


#7 Write a nested loop which prints the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(5):
    for j in range(i+1):
        print("*", end='')
    print("\n")

# 8 Create a list that has 10 random numbers. Iterate through the list and sum them. Use the builtin random module.

from random import randint

list = []
for i in range(10):
    list.append(randint(1,10))

sum = 0
for items in list:
    sum = sum+items

print(sum)

# 9 Create a dictionary called grocery that contains a grocery list of 10 items. Create another
# dictionary called amazon which represents any five items. Write code to combine both
# dictionaries into a new dictionary.

grocery = {'Pen' :'$3', 'Mouse': '$5', 'keyboard': '$6', 'headphones': '$200', 'Monitor': '$100', 'Table': '$150'}
amazon = {'Pen':'$20', 'Mouse': '$6', 'Keyboard': '$10', 'headphones': '$200', 'Monitor': '$150'}

new = {}

for x, y in grocery.items():
    new.update({x:y})
for x, y in amazon.items():
    new.update({x:y})

print(new)

# 10 Create a string which holds the content of text.txt in a string. Generate a new string
# which uppercases every character in the following set: {a, e, I, o, u, y}

set = ['a', 'e', 'i', 'o', 'u']

with open("/Users/maheshkumar/Documents/PycharmProjects/text.txt", "r") as file:
    text = file.read()


with open("/Users/maheshkumar/Documents/PycharmProjects/text.txt", "w") as new_file:
    for word in set:
        text = text.replace(word, word.upper())


    new_file.write(text)

print(new_file)

# 11. Create a function named summation that accepts an arbitrary number of arguments and
# prints the summation of all the values. I.e:
# >>> summation(1, 5, 10)
# …
# 16
# >>> summation(1, 3, 4, 5, 10)
# …
# 23
# summation(1 , 2)
# …
# 3

def summation(*kwargs):
    sum = 0
    for i in kwargs:
        sum = sum + int(i)

    return sum

print(summation(1, 5, 10))
print(summation(1, 3, 4, 5, 10))
print(summation(1 , 2))
