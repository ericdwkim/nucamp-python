def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print(f'Found at index, {x}')
            return x  # returns the index of item, not the value
    print("Target is not in the list")
    return -1


my_list = [6, 3, 4, 2, 5, 7]

len(my_list)  # >> 6 (elements)

"""
array --> [6, 3, 4, 2, 5, 7]
indexed-> [0 ,1, 2, 3, 4, 5]
"""

# asdf = len(my_list) - 1
# print(asdf)

linear_search(my_list, 5)
linear_search(my_list, 3)
linear_search(my_list, 8)
