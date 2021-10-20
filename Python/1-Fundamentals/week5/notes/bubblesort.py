unsorted_list = [101, 49, 3, 12, 56]

# test = ((len(unsorted_list) - 1))
# print(test) >> 4
# print(range(test)) >> range(0, 4)


def bubblesort(the_list):
    # deriving the highest index of the passed-in list
    high_idx = len(the_list) - 1
    # range(0, 4) for i; for a total of 4 iterations
    for i in range(high_idx):
        print("this is i", i)
        # range(0, 4) for j; for a total of 4 iterations
        for j in range(high_idx):
            print("this is j", j)
            item = the_list[j]
            next = the_list[j + 1]
            if item > next:
                the_list[j] = next
                the_list[j + 1] = item
            print(the_list, i, j)


bubblesort(unsorted_list)


"""
for i in range(0, 4):
    for j in range(0, 4):
        do stuff
"""
