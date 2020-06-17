a = 2
b = 5
# c = b
# d = a
# a =c
# b = d
# print(a); print(b)

# above works fine, this is more concise 
a, b = b, a
print(a)
print(b)

# 2.
c = 510
d = 9
if c > d:
    print("greater is c")
else:
    print("greater is d")

# 3.
c = 'abb'
d = 'b'
if len(c) > len(d):
    print("greater is c")
else:
    print("greater is d")

# #4  Write for loop that prints even numbers from 1-100
for i in range(101):
    if i % 2 ==0:
        print("the number is even --->", i)

# 5 Rewrite #4 using while loop.

i = 0
while i <= 100:
    if i %2 ==0:
        print("the number is even", i)
    i += 1

# 6 Write a nested loop that print *

for i in range(3):
    print("*", end='')
    for j in range(2):
        print('*', end='')
    print("\n")
