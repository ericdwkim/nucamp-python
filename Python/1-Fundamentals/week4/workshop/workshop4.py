class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f'{self.name} has an account balance of: ${self.balance}')

    def withdraw(self, balance):
        self.balance -= balance

    def deposit(self, balance):
        self.balance += balance

    def transfer_money(self, pin, tAmount, tUser):
        print(f'\nYou are transferring ${tAmount} to {tUser.name}')
        print("Authentication required")
        print(f'Enter your PIN: {self.pin}')
        if pin == self.pin:
            print("Transfer authorized")
            print(f'Transferring ${tAmount} to {tUser.name}')
            self.balance -= int(tAmount)
            tUser.balance += int(tAmount)
            return True
        else:
            return False

    def request_money(self, pin, password, tAmount, tUser):
        print(f'\nYou are requesting ${tAmount} from {tUser.name}')
        print("User authentication is required...")
        print(f'Enter {tUser.name}\'s PIN: {tUser.pin}')
        print(f'Enter your password: {self.password}')
        if pin == self.pin:
            if password == self.password:
                print("Request authorized")
                print(f'{tUser.name} sent ${tAmount}')
                tUser.balance -= int(tAmount)
                self.balance += int(tAmount)
            else:
                return False
        else:
            return False


""" Driver Code for Task 1 """

# user1 = User("Bob", "1234", "password")

# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """

# user1.change_name("pancake")
# user1.change_pin("4321")
# user1.change_password("potato")

# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 3 """

# bankUser1 = BankUser("Henry", "1001", "wayCoolerPassword")

# print(bankUser1.name, bankUser1.pin, bankUser1.password)

""" Driver Code for Task 4 """

# bankUser1 = BankUser("Joe", "1111", "coolPass")

# bankUser1.show_balance()

# bankUser1.deposit(50)
# bankUser1.show_balance()

# bankUser1.withdraw(20)
# bankUser1.show_balance()

""" Driver Code for Task 5a - transfer_money() """

# bankUser1 = BankUser("Joe", "1111", "coolPass")
# bankUser2 = BankUser("Sally", "1000", "whatever")
# bankUser2.show_balance()

# bankUser1.deposit(50)
# bankUser1.show_balance()

# bankUser1.transfer_money("1111", "10", bankUser2)
# bankUser1.show_balance()

""" Driver Code for Task 5b - request_money() """

bankUser1 = BankUser("Joe", "1111", "coolPass")
bankUser2 = BankUser("Sally", "1000", "whatever")

bankUser2.deposit(5000)
bankUser2.show_balance()
bankUser1.show_balance()

bankUser2.transfer_money("1000", 500, bankUser1)
bankUser2.show_balance()
bankUser1.show_balance()

bankUser2.request_money("1000", "whatever", 250, bankUser1)
bankUser2.show_balance()
bankUser1.show_balance()
