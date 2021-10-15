class Character:
    def __init__(self):
        pass

    def attack(self, attk_char):
        print(f'The {self.name} has attacked the {attk_char.name}!')
        attk_char.hp = attk_char.hp - self.dmg_pts
        print(
            f'The {attk_char.name}\'s health is now: {attk_char.hp} points!')

    def defend(self, defend_char):
        print(f'The {self.name} has defended the {defend_char.name}! ')
        defend_char.hp = defend_char.hp + (self.dmg_pts / 2)
        self.hp = self.hp_max - (self.dmg_pts / 2)
        print(
            f'The {defend_char.name}\'s health has risen by {(self.dmg_pts /2)} points!')
        print(
            f'The {self.name} has sacrificed its own health by {(self.dmg_pts /2)} points to defend!')
        print(f'The {self.name}\'s health is now: {self.hp} points\nThe {defend_char.name}\'s health is now: {defend_char.hp} points')


class Warlock(Character):
    def __init__(self):
        self.name = "Warlock"
        self.hp_max = 1_000
        self.hp = 1_000
        self.dmg_pts = 65


class Witch(Character):
    def __init__(self):
        self.name = "Witch"
        self.hp_max = 1_200
        self.hp = 1_200
        self.dmg_pts = 55


class Spellcaster(Character):
    def __init__(self, name):
        super().__init__(name, 0, 0)
        self.heal_pts = 0

    def heal(self, heal_char):
        if heal_char.hp < heal_char.hp_max:
            heal_char.hp = heal_char.hp_max
            print(
                f'The {self.name} has healed the {heal_char.name} by {self.heal_pts} points\nThe {heal_char.name}\'s health has been restored to {heal_char.hp} points')
            print(
                f'{heal_char.name}\'s Attack: {heal_char.dmg_pts}\n{heal_char.name}\'s Health {heal_char.hp}')


class Wizard(Spellcaster):
    def __init__(self):
        self.name = "Wizard"
        self.hp_max = 500
        self.hp = 500
        self.dmg_pts = 35
        self.heal_pts = 65


class Sidekick(Spellcaster):
    def __init__(self, name):
        super().__init__(name)
        self.boost = 0

    def assist(self, ass_char):
        ass_char.dmg_pts = ass_char.dmg_pts + self.boost
        print(f'The {self.name} has assisted the {ass_char.name}, boosting {ass_char.name}\'s Attack by {self.boost} points')
        print(
            f'{ass_char.name}\'s Attack: {ass_char.dmg_pts}\n{ass_char.name}\'s Health {ass_char.hp}')


class Minion(Sidekick):
    def __init__(self):
        self.name = "Minion"
        self.hp_max = 1_00
        self.hp = 1_00
        self.dmg_pts = 20
        self.heal_pts = 40
        self.boost = 75


class Titan(Character):
    def __init__(self, name, hp_max, dmg_pts):
        self.name = name
        self.hp_max = int(hp_max)
        self.hp = int(hp_max)
        self.dmg_pts = dmg_pts
        # TODO: special enemy ability?


class Gorilla(Titan):
    def __init__(self):
        self.name = "Gorilla Titan"
        self.hp_max = 10_000
        self.hp = 10_000
        self.dmg_pts = 50
