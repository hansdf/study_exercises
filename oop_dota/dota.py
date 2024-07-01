class Midlaner:
    def __init__(self, hero, dmg, control_skill, farm_prio):
        self.hero = hero
        self.dmg = dmg
        self.control_skill = control_skill
        self.farm_prio = farm_prio

    def roam(self):
        print("ganked botlane")

    def take_rune(self):
        print("bottled haste rune")


class Hardcarry:
    def __init__(self, hero, dmg, control_skill, farm_prio):
        self.hero = hero
        self.dmg = dmg
        self.control_skill = control_skill
        self.farm_prio = farm_prio

    def farm(self):
        print("hit creepssss")

