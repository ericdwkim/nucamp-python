from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""

if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print("Logged in as:", authorized_user)

while True:
    show_homepage()
    option = input("Choose an option: ")
    if option == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    if option == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
    if option == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation = donate(username)
            donations.append(donation)
    if option == "4":
        show_donations(donations)
    if option == "5":
        print("Leaving DonateMe....")