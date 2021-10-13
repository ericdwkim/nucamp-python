from my_pkgs.fns import char_menu

"""
Every `Character` has a name, hp, dmg_pts

"""


class Character:
    def __init__(self, name, hp, dmg_pts, ):
        self.name = str(name)
        self.hp = int(hp)
        self.dmg_pts = int(dmg_pts)
        pass
    # TODO: attack function; finish implementation

    def attack(self, attk_char):
        print(f'The {self.name} has attacked the {attk_char.name}!')
        attk_char.hp = attk_char.hp - self.dmg_pts
        # wizard.hp_new (445) = wizard.hp (500) - warlock.dmg (55)
        print(f'The {attk_char.name}\'s health is now: {attk_char.hp}!')


"""
Every Spellcaster consumes `Character` w/
extension of `heal_pts`

hp and dmg_pts initalized to 0
"""


class Spellcaster(Character):
    def __init__(self, name):
        super().__init__(name, 0, 0)
        # self.hp = 200
        # self.dmg_pts = 100
        self.heal_pts = 0  # initialize heal_pts

    # TODO: heal function


class Sidekick(Spellcaster):
    def __init__(self, name):
        super().__init__(name)
        pass
    # TODO: kill fn?


"""
Enemy consumes `Character`

"""


class Enemy(Character):
    def __init__(self, name, hp, dmg_pts):
        self.name = name
        self.hp = hp
        self.dmg_pts = dmg_pts
    # TODO: special enemy ability?


"""
Character instances

"""
warlock = Character("Warlock", 1_000, 55)

wizard = Spellcaster("Wizard")
wizard.hp = 500
wizard.dmg_pts = 100
wizard.heal_pts = 50

minion = Sidekick("Minion")

g_titan = Enemy("Gorilla Titan", 5_000, 40)

"""
attack() testing

"""

warlock.attack(wizard)
# TODO more testing


# char_option = input(
#     "1) Warlock\n2) Witch\n3) Minion\n4) Spellcaster\n5) Escape\n" "Choose your character: ").lower()

# TODO: minion; escape fixes

# while True:
#     char_menu(char_option)
#     if char_option == "warlock" or char_option == "1":
#         character = warlock
#         char_name = warlock.name
#         my_hp = warlock.hp
#         my_dmg = warlock.dmg_pts
#         print(
#             f'You have chosen the character: {char_name}\nHealth: {my_hp}\nAttack:{my_dmg}')
#         break
#     elif char_option == "wizard" or char_option == "2":
#         character = wizard
#         char_name = wizard.name
#         my_hp = wizard.hp
#         my_dmg = wizard.dmg_pts
#         my_heal = wizard.heal_pts
#         print(
#             f'You have chosen the character: {char_name}\nHealth: {my_hp}\nAttack:{my_dmg}\nHeal: {my_heal}')
#         break
# elif char_option == "minion" or char_option == "3":
#     character = minion
#     my_hp = minion_hp
#     my_dmg = minion_dmg
#     my_heal = minion_heal
#     print("You have chosen the character: ", character, "\nHealth: ",
#           my_hp, "\nAttack: ", my_dmg, "\nHeal: ", my_heal)
#     break
# elif char_option == "escape" or char_option == "5":
#     print("You have safely fled the battle!")
#     quit()
# else:
#     print("Unknown character!")
#     break

# while True:
#     gorilla_titan_hp = gorilla_titan_hp - my_dmg
#     print("\nThe", character, "damaged the Gorilla Titan!")
#     print("The Gorilla Titan's hitpoints are now:", gorilla_titan_hp, "\n")
#     if gorilla_titan_hp <= 0:
#         print("The Gorilla Titan has lost the batle")
#         break
#     my_hp = my_hp - gorilla_titan_dmg
#     print("The Gorilla Titan strikes back at", character)
#     print("The", character + "'s hitpoints are now:", my_hp)
#     if my_hp <= 0:
#         print("\nThe", character, "has lost the battle.")
#         break


############################################################################################
"""
NOTE: Character instance unit test

"""

# warlock = Character("Warlock", 1_000, 55)
# warlock.hp = 50
# warlock.dmg_pts = 19
# print(warlock.hp, warlock.dmg_pts, warlock.name)

"""
NOTE: Spellcaster instance unit test

"""
# wizard = Spellcaster("wizard")
# wizard.hp = 250
# wizard.dmg_pts = 40
# print(wizard.hp, wizard.dmg_pts, wizard.name)

"""
NOTE: Enemy instance unit test

"""
# gorilla_titan = Enemy("Gorilla Titan", 0, 0)
# gorilla_titan.hp = 5_000
# gorilla_titan.dmg_pts = 40
# print(gorilla_titan.hp, gorilla_titan.dmg_pts)

############################################################################################