import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    option = input("Press enter to pick a card, or Q + enter to quit\n")
    if option == "":
        dia_random = random.choice(diamonds)
        diamonds.remove(dia_random)
        hand.append(dia_random)
        print(hand[-1], "has been randomly chosen and added to your hand\n")
        print("Remaining cards", diamonds)
        print("Your hand", hand)
    if option == "Q":
        break
if not diamonds:
    print("There are no more cards to pick.")
