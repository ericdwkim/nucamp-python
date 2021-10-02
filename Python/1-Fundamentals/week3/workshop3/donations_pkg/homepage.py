def show_homepage():
    print("\n       === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.   Login       | 2.   Register        |")
    print("------------------------------------------")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("------------------------------------------")
    print("|              5.   Exit                  |")
    print("------------------------------------------")


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation = username + " donated " + str(donation_amt)
    print("Thank you", username)
    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        # for donation in range(len(donations)):
        #     print(donations[donation])
        for donation in donations:
            print(donation)
