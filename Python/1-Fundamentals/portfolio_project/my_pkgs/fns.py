def char_main_menu(char_main_option):
    print("")
    print("             ==== CHOOSE YOUR MAIN CHARACTER ===              ")
    print("Character: " + char_main_option)
    print("-------------------------------------")
    print("| 1.   Warlock       | 2.   Witch    |")
    print("--------------------------------------------")
    print("|              3.   Escape                  |")
    print("------------------------------------------")
    char_main_option = input("Choose your main character: ").lower()

# TODO: preview hp, dmg_pts, and heal_pts for both char_menu & char_support_menu


def char_support_menu(char_support_option):
    print("")
    print("             ==== CHOOSE YOUR SUPPORT CHARACTER ===              ")
    print("Character: " + char_support_option)
    print("-------------------------------------")
    print("| 1.   Minion       | 2.   Wizard    |")
    print("--------------------------------------------")
    print("|              3.   Escape                  |")
    print("------------------------------------------")
