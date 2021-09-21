wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
exit = "Exit"

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 9000

wizard_dmg = 150
elf_dmg = 100
human_dmg = 20
orc_dmg = 175

dragon_hp = 300
dragon_dmg = 50

while True:
    # char_choice is class `str`
    char_choice = input(
        "1) Wizard\n2) Elf\n3) Human\n4) Orc\n" "Choose your character: ").lower()
    if char_choice == 'wizard' or char_choice == '1':
        character = wizard
        my_hp = wizard_hp
        my_dmg = wizard_dmg
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nDamage: ", my_dmg)
        break
    if char_choice == 'elf' or char_choice == '2':
        character = elf
        my_hp = elf_hp
        my_dmg = elf_dmg
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nDamage: ", my_dmg)
        break
    if char_choice == 'human' or char_choice == '3':
        character = human
        my_hp = human_hp
        my_dmg = human_dmg
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nDamage: ", my_dmg)
        break
    if char_choice == 'orc' or char_choice == '4':
        character = orc
        my_hp = orc_hp
        my_dmg = orc_dmg
        print("You have chosen the character: ", character, "\nHealth: ",
              my_hp, "\nDamage: ", my_dmg)
        break
    else:
        print("Unknown character!")

# Task 4 - Battle w/ the Dragon!

while True:
    dragon_hp = dragon_hp - my_dmg
    print("\nThe", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp, "\n")
    if dragon_hp <= 0:
        print("The Dragon has lost the batle")
        break
    my_hp = my_hp - dragon_dmg
    print("The Dragon strikes back at", character)
    print("The", character + "'s hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("\nThe", character, "has lost the battle.")
        break
