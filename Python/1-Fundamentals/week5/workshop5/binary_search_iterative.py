array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]


def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step = step+1
        mid = (start + end) // 2
        print(f'mid is {mid}')
        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# element = 7
# print("Searching for {} in {}".format(element, array))
# print("Index of {}: {}".format(element, binary_search_iterative(array, element)))

binary_search_iterative(array, 13)
