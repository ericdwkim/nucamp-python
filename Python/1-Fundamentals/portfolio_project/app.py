from my_pkgs.char_menus import char_main_menu, char_support_menu
# from my_pkgs.char_select import char_m_selected, char_s_selected
from my_pkgs.char_moves import char_moves, sidekick_moves, spellcaster_moves
from my_pkgs.char_classes import *
from time import sleep

while True:
    char_main_option = char_main_menu()
    if char_main_option == "warlock" or char_main_option == "1":
        character_m = Warlock()
        break
    elif char_main_option == "witch" or char_main_option == "2":
        character_m = Witch()
        break
    elif char_main_option == "escape" or char_main_option == "3":
        print("You have safely fled the battle!")
        quit()
    else:
        print("Unknown main character!")

# char_m_selected()
print(
    f'You have chosen the character: {character_m.name}\nHealth: {character_m.hp_max}\nAttack: {character_m.dmg_pts}')


while True:
    char_support_option = char_support_menu()
    if char_support_option == "minion" or char_support_option == "1":
        character_s = Minion()
        break
    if char_support_option == "wizard" or char_support_option == "2":
        character_s = Wizard()
        break
    elif char_support_option == "escape" or char_support_option == "3":
        print("You have safely fled the battle!")
        quit()
    else:
        print("Unknown support character!")

# char_s_selected()
print(
    f'You have chosen the character: {character_s.name}\nHealth: {character_s.hp_max}\nAttack: {character_s.dmg_pts}\nHeal: {character_s.heal_pts}\n')


while True:
    if character_s.name == "Minion":
        gorilla = Gorilla()
        sleep(2)
        gorilla.attack(character_m)
        if character_m.hp <= 0:
            print(f'{character_m.name} has fainted!')
        print(f'What does {character_s.name} want to do?')
        sk_move_option = sidekick_moves()
        if sk_move_option == "attack" or sk_move_option == "1":
            character_s.attack(gorilla)
        elif sk_move_option == "defend" or sk_move_option == "2":
            character_s.defend(character_m)
        elif sk_move_option == "Heal" or sk_move_option == "3":
            character_s.heal(character_m)
        elif sk_move_option == "Assist" or sk_move_option == "4":
            character_s.assist(character_m)
        elif sk_move_option == "Escape" or sk_move_option == "5":
            print("You have fled the battle!")
            quit()
        else:
            print("Not a move!")
            continue
        break
    elif character_s.name == "Wizard":
        gorilla = Gorilla()
        sleep(2)
        gorilla.attack(character_m)
        if character_m.hp <= 0:
            print(f'{character_m.name} has fainted!')
        print(f'What does {character_s.name} want to do?')
        sc_move_option = spellcaster_moves()
        if sc_move_option == "attack" or sc_move_option == "1":
            character_s.attack(gorilla)
        elif sc_move_option == "defend" or sc_move_option == "2":
            character_s.defend(character_m)
        elif sc_move_option == "Heal" or sc_move_option == "3":
            character_s.heal(character_m)
        elif sc_move_option == "Escape" or sc_move_option == "4":
            print("You have fled the battle!")
            quit()
        else:
            print("Not a move!")
            continue
        break

while True:
    if character_m.name == "Warlock":
        gorilla = Gorilla()
        sleep(2)
        gorilla.attack(character_s)
        if character_s.hp <= 0:
            print(f'{character_s.name} has fainted!')
        print(f'What does {character_m.name} want to do?')
        char_move_option = char_moves()
        if char_move_option == "attack" or char_move_option == "1":
            character_m.attack(gorilla)
        elif char_move_option == "defend" or char_move_option == "2":
            character_m.defend(character_s)
        elif char_move_option == "escape" or char_move_option == "3":
            print("You have fled the battle!")
            quit()
        else:
            print("Not a move!")
            continue
        break
    elif character_m.name == "Witch":
        gorilla = Gorilla()
        sleep(2)
        gorilla.attack(character_s)
        if character_s.hp <= 0:
            print(f'{character_s.name} has fainted!')
        print(f'What does {character_m.name} want to do?')
        char_move_option = char_moves()
        if char_move_option == "attack" or char_move_option == "1":
            character_m.attack(gorilla)
        elif char_move_option == "defend" or char_move_option == "2":
            character_m.defend(character_s)
        elif char_move_option == "escape" or char_move_option == "3":
            print("You have fled the battle!")
            quit()
        else:
            print("Not a move!")
            continue
        break
