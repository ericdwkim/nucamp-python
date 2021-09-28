state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacramento"}
# print(len(state_capitals))
# print(state_capitals["Washington"])

# mutating a value in a dictionary
state_capitals["Washington"] = "Aberdeen"
# appending a key/value pair to a dictionary
state_capitals["Texas"] = "Austin"
print(state_capitals)

# removing a key/value pair from a dictinary; NO returning value
"""
(1) using `del` keyword
"""
# del state_capitals["California"]

"""
(2) using `pop()`
"""
# state_capitals.pop("California")
# print(state_capitals)

"""
(3) creating an object of the returning value from the key/value pair
that has been deleted by the `pop()` method
"""
removed_cap = state_capitals.pop("California")
# "California" key/value pair removed from `state_capitals`
print(state_capitals)
# the removed value has been added to the `removed_cap` object
print("this is it", removed_cap)
