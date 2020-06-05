# Create a dictionary called shopping_cart
shopping_cart = {'Airpods': [10, 234], 'Mouse': [5, 5], 'Keyboard': [20, 8], 'Pen': [200, 1], 'Belt': [20, 6], 'Jeans': [20, 10]}
print(shopping_cart)
# 1. Display all Keys
print(shopping_cart.keys())

# 2. Display all values in the dictionary
print(shopping_cart.values())

# 3. Iterate over Dictionary and display Key, Value pair.
for key, value in shopping_cart.items():
    print("{}:".format(key), "Quantity: {}".format(value[0]),"and Price: ${}".format(value[1]))

# 4. Create a new dictionary called sale and only add items from the sopping_cart dictionary that are <= $10.
# If there's no items that's less than $10, then update the dictionary with two items that are <= $10

sale = {}
for key, value in shopping_cart.items():
    if value[1] <= 10:
        sale.update({key:value})

print(sale)
