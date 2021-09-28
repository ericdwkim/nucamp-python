# table 5 ordered BBQ
orders = {5: "bbq", 2: "tacos", 9: "pizza"}

# table 9 changes their order to tacos
orders[9] = "tacos"

# changed "pizza" value to "tacos"
print(orders[9])
# change reflected in dictionary
print(orders)


"""
NOTE: having duplicate keys with different values WILL be overridden! 

orders = {5: "bbq", 2: "tacos", 2: "pizza"}
print(orders)

>> {5: "bbq", 2: "pizza"}

"""
