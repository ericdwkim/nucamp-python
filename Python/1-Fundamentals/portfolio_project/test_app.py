from app2 import *

warlock.attack(wizard)
wizard.attack(g_titan)
g_titan.attack(warlock)

print(warlock.hp_max)

wizard.heal(warlock)
