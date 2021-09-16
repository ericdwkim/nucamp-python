while True:
    print("1")
    print("2")
    print("3")
    option = input("pick an option")
    if option == "1":
        print("wrong choice!")
    elif option == "2":
        print("wrong choice again!")
    elif option == "3":
        print("right choice!")
        break
    else:
        print("not an option")
print("You have left the loop.")
