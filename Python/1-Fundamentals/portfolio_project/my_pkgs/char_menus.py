def char_main_menu():
    print("")
    print("             ==== CHOOSE YOUR MAIN CHARACTER ===              ")
    print("-------------------------------------")
    print("| 1.   Warlock       | 2.   Witch    |")
    print("--------------------------------------------")
    print("|              3.   Escape                  |")
    print("------------------------------------------")
    return input("Choose your main character: ").lower()


# TODO: preview hp, dmg_pts, and heal_pts for both char_menu & char_support_menu


def char_support_menu():
    print("")
    print("             ==== CHOOSE YOUR SUPPORT CHARACTER ===              ")
    print("-------------------------------------")
    print("| 1.   Minion       | 2.   Wizard    |")
    print("--------------------------------------------")
    print("|              3.   Escape                  |")
    print("------------------------------------------")
    return input("Choose your support character: ").lower()
