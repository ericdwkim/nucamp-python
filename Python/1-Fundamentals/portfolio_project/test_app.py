# from app import *
from my_pkgs.char_classes import Warlock, Witch, Minion, Gorilla


warlock = Warlock()
print(warlock.hp_max, warlock.dmg_pts, warlock.name)

witch = Witch()
print(witch.hp_max, witch.dmg_pts, witch.name)

minion = Minion()
print(minion.hp_max, minion.dmg_pts, minion.heal_pts, minion.name)

gorilla = Gorilla()
print(gorilla.name, gorilla.hp_max, gorilla.dmg_pts)
