my_dict = {"red": 5, "blue": 3, "yellow": 12, "green": 7}


# def linear_search_dictionary(key, value):
#     for key, value in my_dict.items():
#         if value == value:
#             print(f'Found at key {key}')
#         elif value != value:
#             print("Target is not in the dictionary")


"""
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)

"""
# linear_search_dictionary(my_dict, 5)
# linear_search_dictionary(my_dict, 3)
# linear_search_dictionary(my_dict, 8)

# print(type(my_dict.items()))

"""
linear_search_dictionary() returns list of tuple pairs as follows:

dict_items([('red', 5), ('blue', 3), ('yellow', 12), ('green', 7)])


TODO: unpack list of tuple pairs using `enumerate(list_of_tuples)
"""
list_of_tuples = my_dict.items()
enum_lst_tuples = enumerate(list_of_tuples)
print(type(enum_lst_tuples))

# for index, tuple in enumerate(list_of_tuples):
#     element_1 = tuple[0]
#     element_2 = tuple[1]
#     print(element_1, element_2)
