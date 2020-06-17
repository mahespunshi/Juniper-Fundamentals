import os

DIR = f'search'
for x in os.listdir('.'):
    if os.path.isdir(x) and x == DIR:
        print(x)
