from time import sleep


def char_main_menu():
    print("")
    print("             ==== CHOOSE YOUR MAIN CHARACTER ===              ")
    print("         -------------------------------------------")
    print("         | 1.   Warlock | Health: 1000 | Attack: 65 |")
    print("         -------------------------------------------")
    print("         | 2.   Witch   | Health: 1200 | Attack: 55 |")
    print("         -------------------------------------------")
    print("         |              3.   Escape                 |")
    print("         -------------------------------------------")
    sleep(1)
    return input("Choose your main character: ").lower()


# TODO: preview hp, dmg_pts, and heal_pts for both char_menu & char_support_menu

def char_support_menu():
    print("")
    print("             ==== CHOOSE YOUR SUPPORT CHARACTER ===              ")
    print("      ----------------------------------------------------")
    print("      | 1.   Minion | Health: 100 | Attack: 20 | Heal: 40 |")
    print("      ----------------------------------------------------")
    print("      | 2.   Wizard | Health: 500 | Attack: 35 | Heal: 65 |")
    print("      ----------------------------------------------------")
    print("         |              3.   Escape                 |")
    print("         --------------------------------------------")
    sleep(1)
    return input("Choose your support character: ").lower()


# def char_support_menu():
#     print("")
#     print("             ==== CHOOSE YOUR SUPPORT CHARACTER ===              ")
#     print("-------------------------------------")
#     print("| 1.   Minion       | 2.   Wizard    |")
#     print("--------------------------------------------")
#     print("|              3.   Escape                  |")
#     print("------------------------------------------")
#     return input("Choose your support character: ").lower()
