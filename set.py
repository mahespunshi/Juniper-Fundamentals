y= {1, 1, 1, 1, 2, 5, 1, 10, 5, 10, 0}
y = {1, 1, 1, 1, 2, 5, 10}
# You can convert list into tuple, set and vice versa etc.
# if you have list of items and you want to remove duplicate, so convert it into constructor and then back to list.
#

x = {'a': 'apple', 'p': 'plum', 'c': 'Cherry'}
print(x['a'])
print(x.get('a'))
print(x.get('a').upper())
for key, value in x.items():
    print(key, "---->", value)

x['o'] = 'orange'
x.update({'l': 'lemon'})
fruit = {'l': 'lime'}
x.update(fruit)
print(x)

def f(*args):
    for x in args:
        print(x, end=' ')
f(10, 20, 30)

# Keyword argument v/s positional argument in functions.
# keyword is when you defined the default values  def f(x=5, y=6).

def f(**kwargs):
    for key, value in kwargs.items():
        print(key, '---->', value)

print(f(a=10))
print(f(a=10, b=100))

