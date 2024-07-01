from dota import *

# __init__(self, hero, dmg, control_skill, farm_prio):

ember = Midlaner("ember", "high dmg", "root skill", "prio 2")


print(f"{ember.hero} has", end =" ")
ember.take_rune()

print(f"{ember.hero} has", end =" ")
ember.roam()


gyro = Hardcarry("gyro", "high dmg", "delayed stun on rocket", "prio 1 = max")

print(f"{gyro.hero} has {gyro.farm_prio} and therefore needs to", end = " ")
gyro.farm()

