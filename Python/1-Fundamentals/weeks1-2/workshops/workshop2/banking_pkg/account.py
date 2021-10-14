def show_balance(balance):
    print(float(balance))
    # return balance


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return float(amount) + balance


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    return balance - float(amount)


def logout(name):
    print(f"Goodbye " + name + "!")


def validate_login(name_to_validate, pin_to_validate, balance_init):
    name = input("Enter name to register: ")
    pin = input("Enter PIN to register: ")
    balance = 0
    name_len = len(name_to_validate)
    pin_len = len(pin_to_validate)
    raw_balance = float(balance_init)
    while True:
        if name_len not in range(1, 10):
            print("The maximum name length is 10 characters")
            return True
        if (pin_len < 4) or (pin_len > 4):
            print("PIN must contain 4 numbers")
            return True
        elif (name_len in range(1, 10)) and (pin_len == 4):
            print(
                f'{name_to_validate} has been registered with a starting balance of ${raw_balance}.')
            break
