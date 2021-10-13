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


def register(register_name, register_pin, register_bal):
    register_name_raw = input("Enter name to register: ")
    register_pin_raw = input("Enter PIN to register: ")
    balance = 0
    name_len = len(register_name_raw)
    pin_len = len(register_pin_raw)
    raw_balance = float(register_bal)
    while True:
        if name_len not in range(1, 10):
            print("The maximum name length is 10 characters")
            continue
        if (pin_len < 4) or (pin_len > 4):
            print("PIN must contain 4 numbers")
        elif (name_len in range(1, 10)) and (pin_len == 4):
            print(
                f'{register_name} has been registered with a starting balance of ${raw_balance}.')
            break
# def validate_login(name_to_validate, pin_to_valiate):
#     # do something
