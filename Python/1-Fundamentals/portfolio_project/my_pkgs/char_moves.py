from time import sleep


def char_moves():
    print("")
    print("                 ==== SELECT A MOVE ====           ")
    print("    --------------------------------------------")
    print("    | 1.   Attack         | 2.   Defend         |")
    print("    --------------------------------------------")
    print("    |              3.   Escape                  |")
    print("    --------------------------------------------")
    sleep(1)
    return input("Select a move: ").lower()


def spellcaster_moves():
    print("")
    print("             ==== SELECT A MOVE ===              ")
    print("     -------------------------------------")
    print("     | 1.   Attack       | 2.   Defend    |")
    print("     -------------------------------------")
    print("     | 3.   Heal         | 4.   Escape    |")
    print("     -------------------------------------")
    sleep(1)
    return input("Select a move: ").lower()


def sidekick_moves():
    print("")
    print("             ==== SELECT A MOVE ===              ")
    print("     -------------------------------------")
    print("     | 1.   Attack       | 2.   Defend    |")
    print("     -------------------------------------")
    print("     | 3.   Heal         | 4.   Assist    |")
    print("     -------------------------------------")
    print("     |           5.   Escape              |")
    print("     -------------------------------------")
    sleep(1)
    return input("Select a move: ").lower()
