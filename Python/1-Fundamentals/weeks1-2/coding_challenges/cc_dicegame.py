import random


def dice_game():
    high_score = 0
    while True:
        option = input("Current High Score: " + str(high_score) +
                       "\n1) Roll Dice\n2) Leave Game\nEnter your choice: ").lower()
        if option == '1' or option == 'roll dice':
            dice_roll = random.randint(1, 6)
            dice_roll2 = random.randint(1, 6)
            print("\nYou roll a...", str(dice_roll))
            print("You roll a...", str(dice_roll2))
            sum_roll = dice_roll + dice_roll2
            print("\nYou have rolled a total of:", sum_roll)
            if sum_roll > high_score:
                high_score = sum_roll
                print("New high score!\n")
                user_initials = input("Enter your initials: ")
                print(user_initials + " is in 1st place!\n")
            continue
        if option == '2' or option == 'leave game' or option == 'leave':
            print("\nYou have left the arcade!")
            print("Please insert (2) quarters")
            # quit()
            break


dice_game()
