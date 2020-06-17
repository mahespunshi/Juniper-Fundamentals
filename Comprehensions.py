# List comprehension example below. notes [] parenthesis. Comprehensions can't be used for tuple.
x =[x for x in range(10)]
print(x)
# create comprehension and it can creates for us, but in dict we need to create it first and then modify it.
# so, we can't create auto-dict, we can just modify dict, unlike list.

# Dictionary comprehension is implement after list comprehension
# Keys should be unique in dict, guess keys are tuples ()
dict1 = {'a': 5, 'b': 10, 'c': 15}
triple = {k:v**3 for (k,v) in dict1.items()}
print(triple)
triple = {k:v**3 for (k,v) in {'a': 3, 'b': 6}.items()}
print(triple)

# in dict, keys should be any immutable type tuple,set, so number or letters both are fine.
# read cha 1,

# Use enumerate in list or string when you want to store index values instead of using while loop with i counter

city = 'Boston'
for index, char in enumerate(city):
    print(index, char)

# or using while loop instead of enumerate
i = 0
while i < len(city):
    print(i, city[i])
    i = i + 1

