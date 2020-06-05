# implement the power functionality using **

# implement the mod functionality %

# import the math module, and implement ANY one functionality

# Create a GitHub account

# for x in range(1, 10):
#     for y in range(1,10):
#         print(f"set family inet address 10.{x}.{y}.1")
# Text based calculator as home work.

# for loop : for x in range(1, 11):
# print(x)
#while loop: i = 0; while < 10 ; print(i); i +=1
# try / except is similar to if else statement: try x = 10; except ValueError: ; print('Error!'),
# finally: if you always want to exceute something despite what happens in try and except.

while True:
    try:
        x = int(input("Enter a num"))
        y = int(input("Enter a den"))
        z = x/y
        print(z)
        break

    except ZeroDivisionError as zero:
        print("Can't divide by 0!")
        print(zero.args)
