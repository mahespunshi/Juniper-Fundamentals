##############################
# Secret number game
#-------------------
# the program generates a random num between 1-100 and we want him to guess a number bndddd
#
# import random
# secret_num = random.randint(1,100)
# print(secret_num)
#
# def run_game():
#     while True:
#         guess_num = int(input("Guess a number:"))
#
#         if guess_num == secret_num:
#             print("You guessed it right, You won!")
#             break
#         elif guess_num > secret_num:
#             print("Please try again, the number is >")
#         elif guess_num < secret_num:
#             print("Please try again, the number <")
#
#
# run_game()


# '''Extermely important .. data structures: they are abstract but important, in every modern programming language'''
# Help process and organize the data in program, ex: SQL database, Oracle, mango DB, they all have data structures.
# You want to create a web-app and hold user information in a variable.
# four core data structure. 1_  list: Mutable type 2: Tuple: immutable type 3: set: unique elements, 4: Dictionary: Key/value mappings.
# x = [] , y = [1, 3, 2, 10, 100] inside them are called elements separated by commas
# y[0] <<-- to access index number (first in this case) element.
# # in Java list is similar to array
#
# y = [1, 3, 2, 10, 100]
# y.append(20)
#
# # slice is used to extrace certain parts of elements of list as y[begin:end:step=1] by default step = 1
# y[:]
# y[2:3]
# print(y[::2]) # steps 2 shows 2 index, by default it has 1 step y[::]
# print(y)
# ip = ['192.169.1.1', '182.1.1.1']
# ip[0]
# ip[0].count('192')
#
# ip_1 = '192.160.10.1'
# print(ip_1[:4])

# # 1) create a list that's stored in variable x. the list should contain 5 elements
# x = [1,2,3,4,5]
# # 2) Access the firsst, 3rd, and 5th element of the list
# print(x[0]); print(x[2]); print(x[4])
# # 3) slice the list and return every two items in the list.
# print(x[::2])
#
# x = [1, 2, 3, 4, 5]
# print(f"First:- {x[0]} Third :-{x[2]} Fifth:-{x[4]}")
# print("First, third and fifth", x[::2])
#
# init_list = [0,10,30,40,50,60]
# list_count = len(init_list)
# count = 0
# print(list_count)
# for i in init_list:
#     if count % 2 != 0 :
#         pass
#         print("This is the : ", count, "in this list with value in list is :", i)
#     count +=1

# odds = [1,3,5,6,7]
# evens = [2,4,6,8,10]
# odds.extend(evens)
# print(odds)
# odds.pop()
# print(odds)
# del odds[5]
# print(odds)
# odds.remove(5)
# print(odds)
# odds.insert(0,9)
# print(odds)
# odds.count(9)
# odds.reverse()
# odds[::-1]
# odds.sort()

# create a list and use any 3 function on it i.e sort, assend, etc.
# list = [10,20,30,40,50]
# print(list)
# list.copy()
# print(list)
# list.clear()
# for i in range(2):
#     list.extend(i)
# print(list)

# x = [1, 3, 5, 2, 10]
# x.extend(x)   ## check this out.
# print(x)
#
# # # for loop example
# # for item in x:
# #     print(item, end=' ')
#
# item = 0
# while item <= len(x)-1:
#     print(x[item])
#     item += 1

# for index, item in enumerate(x):
#     print(index, item)
#
# nested = ['a', 'b', 100, ['a', 'e', 'i'], 100]
# nested[0]
# nested[1]
# print(nested[3])
# print(nested[3][1])   # items in index 3.
# print(nested)

# how to create a Matrix, Matrix is also a list
# matrix = [
#     [1, 3, 5],
#     [10, 20, 5],
#     [3, 8, 2]
# ]
# # print(matrix)
# # print(matrix[0][0], matrix[1][1], matrix[2][2])
# # print(matrix[0][0]* matrix[1][1]*matrix[2][2])
#
# # check out
# for row in matrix:
#     for col in row:
#         print(col)

# built in function called chose in random module.
# import random
# coin = ['Heads', 'Tails']
# correct, wrong = 0,0
# while True:
#     landed = random.choice(coin)
#     play = input("Do you want to play?")
#     if play == "Y":
#         user_input = input("Which side the coid landed on?")
#         if user_input == landed:
#             print("You win")
#             correct += 1
#         else:
#             print("You lost")
#             wrong +=1
#
#     elif play == "done":
#         print("Game over!")
#         print("Number of correct guesses {}".format(correct))
#         print("Number of incorrect guesses {}".format(wrong))
#         break
#     else:
#         print("Wrong input")
#
# x = 10, '+', 20
# output = ('{} + {} = {}'.format(10, 20, 10 + 20))
# print(output)

# Dict = {'a': 'apple','b': 'book', 'c': 'coconut'}
# # print(Dict)
# # print(Dict['a'])
# # print(Dict['b'])
# # print(Dict['c'])
# # print(Dict.get('a'))
# # print(Dict.values())
# # Dict['b'] = 'boy' # update dictionary
# # # print(Dict)
# # for key in Dict:
# #     print(Dict[key])
#
# # for key, value in Dict.items():
# #     print(key, '-->', value)
#
# # for key in Dict:
# #     print(key,':',Dict[key])
# Dict.pop('c')
# Dict.update({'k': 'kiwi'})
# print(Dict)

# phone_book = {
#     'andrew': '316-226-3456',
#     'doug': '315-224-5569',
#     'John': '334-443-5566'
#
# }
#
# # print(phone_book)
# # print(phone_book['andrew'])
# # print(phone_book)
# Check out below example again, interesting for user_input
# user_input = input('Enter in a name')
# for key, value in phone_book.items():
#
#     if key == user_input:
#         print(key, '#', '=', value)
#         break

# music = {
#     'jazz': ['song1', 'song2', 'song3'],
#     'electronic': ['song1', 'song2', ['edm1', 'edm2', 'edm3']]
# }
# # # print(music)
# # # print(music['jazz'][2])
# #
# # # for key,value in music.items():
# # #     print(value)
# #
# # print(music['electronic'][2][2])
#
# # music.update({'pop':'Music'})
# # print(music)
# # or to extend two dictionaries together, we can use updte function too.
#
# fruits1 = {'a': 'apple'}
# fruits2 = {'a': 'apple','c':'coconut'}
#
# fruits1.update(fruits2)
# print(fruits1)
"""
# Create a dictionary called shopping_cart,
# the dictionary will contain mappings of items from an online store
the items will have a name as the key, and then corresponding and piece as value

"""
