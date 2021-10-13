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


print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(name, "has been registered with a starting balance of $" + str(balance))

while True:
    print("          === Automated Teller Machine ===          \nLOGIN")
    name_to_validate_raw = input("Enter name to register: ")
    name_len = len(name_to_validate_raw)
    if name_len not in range(1, 10):
        print("The maximum name length is 10 characters")
        continue
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate_raw == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)
        print("Current Balance: $" + str(show_balance(balance)))
    elif option == "3":
        balance = withdraw(balance)
        print("Current Balance: $" + str(show_balance(balance)))
    elif option == "4":
        logout(name)
        break
    else:
        print("Invalid option")
