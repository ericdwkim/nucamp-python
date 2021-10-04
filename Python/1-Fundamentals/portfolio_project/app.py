"""
//battlegame.py -esq

turn-based final fantasy esq? 
    - team vs a "boss"
    - w/ healers!
"""
from my_pkgs.fns import char_menu
# Characters

warlock = "Warlock"
witch = "Witch"
minion = "Minion"
spellcaster = "Spellcaster"

# Character health points

warlock_hp = 1000
witch_hp = 1150
minion_hp = 450
spellcaster_hp = 750

# Character damage points

warlock_dmg = 55
witch_dmg = 45
minion_dmg = 15
spellcaster_dmg = 5

# Character healing points

warlock_heal = 35
witch_heal = 25
minion_heal = 75
spellcaster_heal = 120

# Enemy character stats

gorilla_titan_hp = 7000
gorilla_titan_dmg = 50

# character choice menu fn


# def char_menu(char_option):
#     print("")
#     print("             ==== CHOOSE YOUR CHARACTER ===              ")
#     print("Character: " + char_option)
#     print("-------------------------------------")
#     print("| 1.   Warlock       | 2.   Witch    |")
#     print("---------------------------------------")
#     print("| 3.   Minion      | 4.   Spellcaster  |")
#     print("--------------------------------------------")
#     print("|              5.   Escape                  |")
#     print("------------------------------------------")

# infinite while loop for character stats

char_option = input(
    "1) Warlock\n2) Witch\n3) Minion\n4) Spellcaster\n5) Escape\n" "Choose your character: ").lower()

while True:
    char_menu(char_option)
    # char_option = input(
    #     "1) Warlock\n2) Witch\n3) Minion\n4) Spellcaster\n5) Escape\n" "Choose your character: ").lower()
    if char_option == "warlock" or char_option == "1":
        character = warlock
        my_hp = warlock_hp
        my_dmg = warlock_dmg
        my_heal = warlock_heal
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nAttack: ", my_dmg, "\nHeal: ", my_heal)
        break
    elif char_option == "witch" or char_option == "2":
        character = witch
        my_hp = witch_hp
        my_dmg = witch_dmg
        my_heal = witch_heal
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nAttack: ", my_dmg, "\nHeal: ", my_heal)
        break
    elif char_option == "minion" or char_option == "3":
        character = minion
        my_hp = minion_hp
        my_dmg = minion_dmg
        my_heal = minion_heal
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nAttack: ", my_dmg, "\nHeal: ", my_heal)
        break
    elif char_option == "spellcaster" or char_option == "4":
        character = spellcaster
        my_hp = spellcaster_hp
        my_dmg = spellcaster_dmg
        my_heal = spellcaster_heal
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nAttack: ", my_dmg, "\nHeal: ", my_heal)
        break
    elif char_option == "escape" or char_option == "5":
        print("You have safely fled the battle!")
        quit()
    else:
        print("Unknown character!")
        break

while True:
    gorilla_titan_hp = gorilla_titan_hp - my_dmg
    print("\nThe", character, "damaged the Gorilla Titan!")
    print("The Gorilla Titan's hitpoints are now:", gorilla_titan_hp, "\n")
    if gorilla_titan_hp <= 0:
        print("The Gorilla Titan has lost the batle")
        break
    my_hp = my_hp - gorilla_titan_dmg
    print("The Gorilla Titan strikes back at", character)
    print("The", character + "'s hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("\nThe", character, "has lost the battle.")
        break


"""
TODO: 
1. play again option 
2. healing functionality
3. tag team battle, so (2) characters vs gorilla titan? 
4. ??
5. check for project requirements (if any)


"""
