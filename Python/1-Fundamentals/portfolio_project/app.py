from my_pkgs.char_menus import char_main_menu, char_support_menu
from my_pkgs.char_moves import char_moves, sidekick_moves
from my_pkgs.char_classes import *


while True:
    char_main_option = char_main_menu()
    if char_main_option == "warlock" or char_main_option == "1":
        character = Warlock()
        break
    elif char_main_option == "witch" or char_main_option == "2":
        character = Witch()
        break
    elif char_main_option == "escape" or char_main_option == "3":
        print("You have safely fled the battle!")
        quit()
    else:
        print("Unknown main character!")
    char_move_option = char_moves()

print(
    f'You have chosen the character: {character.name}\nHealth: {character.hp_max}\nAttack: {character.dmg_pts}')

while True:
    char_support_option = char_support_menu()
    if char_support_option == "minion" or char_support_option == "1":
        character = Minion()
        break
    if char_support_option == "wizard" or char_support_option == "2":
        character = Wizard()
        break
    elif char_main_option == "escape" or char_main_option == "3":
        print("You have safely fled the battle!")
        quit()
    else:
        print("Unknown support character!")
    sk_move_option = sidekick_moves()
print(
    f'You have chosen the character: {character.name}\nHealth: {character.hp_max}\nAttack: {character.dmg_pts}\nHeal: {character.heal_pts}')


while True:
    # TODO: actual game mechanics...
    # gorilla_titan_hp = gorilla_titan_hp - my_dmg
    # print("\nThe", character, "damaged the Gorilla Titan!")
    # print("The Gorilla Titan's hitpoints are now:", gorilla_titan_hp, "\n")
    # if gorilla_titan_hp <= 0:
    #     print("The Gorilla Titan has lost the batle")
    #     break
    # my_hp = my_hp - gorilla_titan_dmg
    # print("The Gorilla Titan strikes back at", character)
    # print("The", character + "'s hitpoints are now:", my_hp)
    # if my_hp <= 0:
    #     print("\nThe", character, "has lost the battle.")
    #     break
