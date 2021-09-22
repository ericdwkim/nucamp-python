my_string = "Set in GLOBAL scope"


def main():
    # the keyword `global` tells the interpreter that we are referencing the global my_string var
    global my_string
    my_string = "Set in LOCAL scope"


main()
print(my_string)
