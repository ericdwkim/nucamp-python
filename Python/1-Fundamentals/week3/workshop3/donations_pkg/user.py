def login(database, username, password):
    if username in database:
        if database[username] == password:
            print("Welcome admin ")
            return username
        else:
            print("Incorrect password ")
            return ""
    else:
        print("User was not found. Please register.")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered ")
        return ""
    else:
        print("Username has been registered ", username)
