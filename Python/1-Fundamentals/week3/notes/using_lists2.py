states = ["Washington", "Oregon", "California"]

'''for state in states:
    state = state.lower()
    print(state)

print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)
'''

"""
slicing notation for lists
"""
states2 = ["Arizona", "Ohio", "Louisiana"]
best_states = states + states2
print(best_states)
# from 1st index up to but not including the 3rd index of `best_states`
print(best_states[1:3])
# up to but not including the 2nd index
print(best_states[:2])
# starting from and including the 4th index to the end of the list
print(best_states[4:])
