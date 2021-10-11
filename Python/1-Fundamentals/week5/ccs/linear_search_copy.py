my_dict = {"red": 5, "blue": 3, "yellow": 12, "green": 7}


# def linear_search_dictionary(dict, value):
#     for value in dict.items():
#         for tuple in enumerate(dict.items()):
#             if value == value:
#                 print(f'Found at key {dict}')
#             elif value != value:
#                 print("Target is not in the dictionary")

# def linear_search_dictionary(dict, value):
#     lst_tuples = list(dict.items())
#     for k, v in lst_tuples:
#         if value == v:
#             print(f'Found at key {k}')
#             return
#         else:
#             print("Target is not in the dictionary")
#             break

# def linear_search_dictionary(dict, value):
#     for k, v in dict.items():
#         if value == v:
#             print(f'Found at key {k}')
#             return
#         else:
#             print("Target is not in the dictionary")
#             break

def linear_search_dictionary(dict, value):
    for k in dict.keys():
        if dict[k] == value:
            print(f'Found at key {k}')
            return
    print("Target is not in the dictionary")


linear_search_dictionary(my_dict, 5)
linear_search_dictionary(my_dict, 3)
linear_search_dictionary(my_dict, 8)
