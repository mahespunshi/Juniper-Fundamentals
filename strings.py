poem = """this is a poem 
         python programming. And 
\        I am using tripple quotes
"""
path = r'c:\Neon\Example' # if you want to ignore \ char use r
print(poem.count('p'))
print(poem.upper())
print(poem.lower())
print(poem.find('p'))
print(poem.capitalize())
print(poem.capitalize().upper())
print(poem.isnumeric())

# Strings are immutable objects in memory
char = 'a'
char += 'b'
char += 'c'
print(char)
# So, in python we can effiencity do that as below.
print(' '.join(char))
hash('a') # hash tells the memory address
text= 'this is a simple text'
x = [x for x in text]
print(x)

import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

'a' in string.ascii_letters
#['a', 'b'] in string.ascii_letters # can't do list like this.
# user_input = input("Enter in a char")
# for x in string.ascii_letters:
#     if x == user_input:
#         print("yes")
#     else:
#         print("No")

print(string.ascii_lowercase in string.ascii_letters)

if 'a' or 'b' in string.ascii_letters:
    print("Yep")

# https://www.geeksforgeeks.org/python-string-ljust-rjust-center/
# https://github.com/purcellconsult/code-cool-stuff-with-python-video-course/blob/master/projects/random_person_project.md

