def binary_search(the_list, target):
    # defines L/U bounds of elements' indices
    # not the # of elements in the list
    lower_bound = 0
    # deriving the highest index of the passed-in list
    upper_bound = len(the_list) - 1
    # while 0 <= 9
    while lower_bound <= upper_bound:
        # pivot = (0 + 9) // 2 = 4.5
        # pivot = 4.5 --> 5 (floor division rounds up)
        pivot = (lower_bound + upper_bound) // 2
        # var value of element at pivot index
        pivot_val = the_list[pivot]
        # if pivot value (at pivot index) is same as target value, return pivot index
        # having this check first makes following conditionals simplier
        if pivot_val == target:
            return pivot
        # if pivot value is greater than target value
        if pivot_val > target:
            # adjust Ubound to kill right-side subarray
            upper_bound = pivot - 1
        # if pivot_val < target
        else:
            # adjust Lbound to kill left-side subarray
            lower_bound = pivot + 1
    return - 1


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# indexed [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
# print(binary_search(test_list, 10))
# print(binary_search(test_list, 4))
# print(binary_search(test_list, 33))

print(binary_search(test_list, 5))
# 5 == pivot; returns an index of 4 since that's the index `5` is located
