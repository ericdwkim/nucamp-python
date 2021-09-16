
x = 0

while x != 10:
    x = x + 1
    # if x > 1: # kill to prevent exiting loop when x > 1
    #     break
    if x < 5:
        print(x)
    # needs to be above second elif to simply print `6`
    elif x == 6:
        print(x)  # print when x = 6
        # break # kill to prevent exiting the loop when x == 6
        continue
    # should remain nested to include both conditionals using logical `and`
    elif x >= 5 and x <= 8:
        print("x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)
    # should remain nested for conditions of x = 8 or 9
    else:
        print("x is bigger than 8. It is:", x)
