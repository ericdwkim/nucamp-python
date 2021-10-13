from banking_pkg.account import *


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# register_name_raw = input("Enter name to register: ")
# register_pin_raw = input("Enter PIN to register: ")
# balance = 0

while True:
    if name_len not in range(1, 10):
        print("The maximum name length is 10 characters")
        return True
    if (pin_len < 4) or (pin_len > 4):
        print("PIN must contain 4 numbers")
        return True
    elif (name_len in range(1, 10)) and (pin_len == 4):
        print(
            f'{register_name} has been registered with a starting balance of ${raw_balance}.')
        break

# def register(register_name, register_pin, register_bal):
#     raw_name = register_name
#     name_len = len(register_name)
#     pin_len = len(register_pin)
#     raw_balance = float(register_bal)
#     while True:
#         if name_len not in range(1, 10):
#             print("The maximum name length is 10 characters")
#             return
#         if (pin_len < 4) or (pin_len > 4):
#             print("PIN must contain 4 numbers")
#             return
#         else:
#             print(
#                 f'{register_name} has been registered with a starting balance of ${raw_balance}.')
#             raw_name = register_name_raw
#             raw_
#             break

name_raw = name
register()

# while True:
#     print("          === Automated Teller Machine ===          \nLOGIN")
#     name_to_validate_raw = input("Enter name to register: ")
#     name_len = len(name_to_validate_raw)
#     # if name_len not in range(1, 10):
#     #     print("The maximum name length is 10 characters")
#     #     continue
#     pin_to_validate = input("Enter PIN: ")
#     # pin_len = len(pin_to_validate)
#     # if pin_len not in range(1, 4):
#     #     print("PIN must contain 4 numbers")
#     if name_to_validate_raw == name and pin_to_validate == pin:
#         print("Login successful!")
#         break
#     else:
#         print("Invalid credentials!")

# while True:
#     atm_menu(name)
#     option = input("Choose an option: ")
#     if option == "1":
#         show_balance(balance)
#     elif option == "2":
#         balance = deposit(balance)
#         print("Current Balance: $" + str(show_balance(balance)))
#     elif option == "3":
#         balance = withdraw(balance)
#         print("Current Balance: $" + str(show_balance(balance)))
#     elif option == "4":
#         logout(name)
#         break
#     else:
#         print("Invalid option")
