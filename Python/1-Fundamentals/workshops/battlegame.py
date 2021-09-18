"""
# Task 1 - game variables
"""

wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_dmg = 150
elf_dmg = 100
human_dmg = 20

dragon_hp = 300
dragon_dmg = 50

"""
# Task 2 - prompt player

char_choice = input("1) Wizard\n2) Elf\n3) Human\n" "Choose your character: ")
"""

"""
# Task 3 - set up infinite while loop & wrap input() from task 2 inside
        asdf = print("You have chosen the ", character,
                     ":\nHealth: ", my_hp, "\nDamage: ", my_dmg)

"""
while True:
    char_choice = input(
        "1) Wizard\n2) Elf\n3) Human\n" "Choose your character: ")
    if char_choice == '1':
        character = wizard
        my_hp = wizard_hp
        my_dmg = wizard_dmg
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nDamage: ", my_dmg)
        break
    if char_choice == '2':
        character = elf
        my_hp = elf_hp
        my_dmg = elf_dmg
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nDamage: ", my_dmg)
        break
    if char_choice == '3':
        character = human
        my_hp = human_hp
        my_dmg = human_dmg
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nDamage: ", my_dmg)
        break
    else:
        print("Unknown character!")

# Task 4 - Battle w/ the Dragon!

while True:
    dragon_hp = dragon_hp - my_dmg
    print("\nThe", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    print("\n")
    if dragon_hp <= 0:
        print("The Dragon has lost the batle")
        break
    my_hp = my_hp - dragon_dmg
    print("The Dragon strikes back at", character)
    print("The", character, "'s hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("\nThe", character, "has lost the battle.")
        break
